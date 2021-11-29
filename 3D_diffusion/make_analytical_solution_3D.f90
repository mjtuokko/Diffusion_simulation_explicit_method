program Three_dimensional_diffusion_simulation
implicit none
!Define variables
integer :: n=201 !n is the size of the matrix used
integer, parameter :: rk = selected_real_kind(8)
integer :: k !k is the number of iterations.
real(kind=rk), dimension(:,:,:), allocatable :: matrix !matrix for the function of the diffusion equation 
integer :: i,j !iteration parameters
real(kind=rk) :: DX, DT !Approximation of differentials of functions
character(len=80) :: arg, arg1, arg2, arg4, Path
integer :: every_nth_save = 1
real(kind=rk) :: singlepoint_x_y_z_coordinate=0.45_8 !coordinate (X,Y,Z) to save
integer :: singlepoint_x_y_z_index
!DX is used DT and k overwritten later

!	DT=0.0000125
	k=20000

!Read arguments

	call get_command_argument(1,arg)
	read(arg,*) n

	call get_command_argument(2,arg1)
	read(arg1,*) DT

	call get_command_argument(3,arg2)
	read(arg2,*) k

	call get_command_argument(4,arg4)
	read(arg4,*) every_nth_save

	call get_command_argument(5,Path)

	DX=1.0_8/(n-1)
	allocate ( matrix(n,n,n) )

	call chdir(Path)

	!calculate new differential and singlepoint coordinate
	singlepoint_x_y_z_index=idnint(singlepoint_x_y_z_coordinate*(n-1)+1)
	
!write used parameters to filename
	open(1, file = "parameters.txt", status='new')
	write(1,*) DX
	write(1,*) DT
	write(1,*) n
	write(1,*) k
	write(1,*) every_nth_save
	write(1,*) singlepoint_x_y_z_index
	!Close the file parameters is written
	close(1)
! write parameters meaning
	open(1, file = "parameters_meaning.txt", status='new')
	write(1,*) "^ Meaning" !because this file is automatically readed sometimes, only parameter is written in each file
	write(1,*) "DX"
	write(1,*) "DT"
	write(1,*) "n"
	write(1,*) "k"
	write(1,*) "every_nth_save"
	!Close the file parameters is written
	close(1)
	
	!make analytical results to comparing
	call make_analytical_sol_to_compare(matrix,n,k)
!	call make_analytical_sol_single_point_to_compare(k,singlepoint_x_y_z_index,singlepoint_x_y_z_index,singlepoint_x_y_z_index)	
contains
!ALIOHJELMAT


!aliohjelma, jolla voi tulostaa matriisin
subroutine write_3d_matrix_to_file(matrix,n,a)
implicit none
integer,intent(in) :: n,a !the size of the array and number of the iteration
real(kind=rk), INTENT(IN) :: matrix(n,n,n) !matrix, wanted to write to the file
integer :: row, column !parameters to iterate each row and column
character(len=80) :: filename
	write(filename,'(A, i0,A)') "3D_data_", a, ".txt"
	!Open the file where the results will be written. 
	open(1, file = filename, status='new')
	do row =1,n
		do column=1,n

			write(1,*) matrix(row,column,:)
		end do
	end do
	!Close the file where the results has been written.
	close(1)
end subroutine




subroutine make_analytical_sol_to_compare(matrix,n,k)
implicit none
integer,intent(in) :: n,k
integer :: a,i,j,z
real(kind=rk), INTENT(INOUT) :: matrix(n,n,n)
integer :: k1,n1=3 !for do loop to make init matrix
real(kind=rk) :: pi=4*atan(1.0_8),r,r2,T
	do a=0,k !do loop for every time step
	if (mod(a,every_nth_save).eq.0) then
	T=a*DT
	matrix=0
	do i=1,n
		do j=1,n
			do z=1,n
				!calculate the radius of each element		
				r2=((i-(n+1)/2))**2+((j-(n+1)/2))**2+((z-(n+1)/2))**2
				r=sqrt(r2)/(n-1) !normalize
				if (r.le.0.00000001) then
					r = 0.0000000000001_8
				end if
				!boundary condition 
				!if (r.ge.0.50) then
			  	!	matrix(i,j,z)=0
				!else	
				!!the element is get from known function, when t=0
				!let's calculate k element from sum and then sum those
				do k1=1,n1
					matrix(i,j,z)=matrix(i,j,z)+sin(2*k1**2*r*pi)/(2*k1**2*r*pi)*exp(-4*k1**4*pi**2*T)
				end do
				matrix(i,j,z)=matrix(i,j,z)/n1
				!end if

				!if r=0 there is a bug because fortran can't calculate limit
				
				if (isnan(matrix(i,j,z))) then
					matrix(i,j,z)=1.0_8
				end if
			end do
		end do	
	end do
	call write_3d_matrix_to_file(matrix,n,a)
!	call write_single_point3d_matrix_to_file(matrix,n,a,singlepoint_x_y_z_index,singlepoint_x_y_z_index,singlepoint_x_y_z_index)
	end if 	
	end do

end subroutine
subroutine make_analytical_sol_single_point_to_compare(k,i,j,z)
implicit none
integer,intent(in) :: k,i,j,z
integer :: a
real(kind=rk) :: value
integer :: k1,n1=3 !for do loop to make 3 terms to solution
real(kind=rk) :: pi=4*atan(1.0_8),r,r2,T
character(len=80) :: filename

!calculate the radius of each element		
	r2=((i-(n+1)/2))**2+((j-(n+1)/2))**2+((z-(n+1)/2))**2
	r=sqrt(r2)/(n-1) !normalize
	if (r.le.0.00000001) then
		r = 0.0000000000001_8
	end if

	do a=0,k !do loop for every time step
	if (mod(a,every_nth_save).eq.0) then

	T=a*DT
				

	value = 0

	!calculate solution
	do k1=1,n1
		value=value+sin(2*k1**2*r*pi)/(2*k1**2*r*pi)*exp(-4*k1**4*pi**2*T)
	end do
	value=value/n1


	write(filename,'(A, i0,A)') "3D_data_", a, ".txt"
	!Open the file where the results will be written. 
	open(1, file = filename, status='new')
	
	write(1,*) value
	
	close(1)
	end if
	end do

end subroutine

subroutine write_single_point3d_matrix_to_file(matrix,n,a,x,y,z)
implicit none
integer,intent(in) :: n,a,x,y,z !the size of the array and number of the iteration and position of elem
real(kind=rk), INTENT(IN) :: matrix(n,n,n) !matrix, wanted to write to the file
integer :: row !parameter to iterate each row
character(len=80) :: filename

	write(2,*) matrix(x,y,z)!write the value of element, DX, DT and T value


end subroutine	


end program Three_dimensional_diffusion_simulation
