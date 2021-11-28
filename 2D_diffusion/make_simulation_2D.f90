program Two_dimensional_diffusion_simulation
implicit none
!Define variables
integer :: n=11 !n is the size of the matrix used
integer, parameter :: rk = selected_real_kind(8)
integer :: k !k is the number of iterations.
real(kind=rk), dimension(:,:), allocatable :: matrix !matrix for the function of the diffusion equation 
integer :: i,j !iteration parameters
real(kind=rk) :: DX, DT !Approximation of differentials of functions
character(len=80) :: arg, arg1, arg2, arg4, Path
integer :: every_nth_save


!DX is used DT and k overwritten later

	DT=0.0000125_8
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
	allocate ( matrix(n,n) )

	call chdir(Path)

!write used parameters to filename
	open(1, file = "parameters.txt", status='new')
	write(1,*) DX
	write(1,*) DT
	write(1,*) n
	write(1,*) k
	write(1,*) every_nth_save
	write(1,*) "^ Meaning" !because this file is automatically readed sometimes, only parameter is written in each file
	write(1,*) "DX"
	write(1,*) "DT"
	write(1,*) "n"
	write(1,*) "k"
	write(1,*) "every_nth_save"
	!Close the file parameters is written
	close(1)
	


!	call chdir("2D_single_point_data")			   
	!Initialize matrix c in the form of besselfunction												   
	call make_2d_init_c_besslej0(matrix,n)
!	call make_extremely_init_c(matrix,n)
	!Make iteration k times.												  
	call make_2d_simulation(matrix,n,k)




contains
!Subroutines

!subroutine to iteration
subroutine make_2d_simulation(matrix,n,k)
	implicit none
	!define variables
	real(kind=rk), INTENT(INOUT) :: matrix(n,n)
	integer, INTENT(IN) :: n,k
	real(kind=rk) :: matrix_new(n,n) !new matrix for the iteration
	integer :: i,j,a !a is an iteration parameter for every iteration
		! i and j are iteration parameter for each element 
		!make iteration k times
	real(kind=rk) :: r,r2	!radius and radius^2 parameters
	

	do a=1,k 
		!make a new matrix for 
		matrix_new=0
		!make changes to each element		
		!iterate every row (x-index)
		do i=1,n
		  !iterate every element in a row (y-index)
		  do j=1,n
		    !calculate the radius of each element
			r2=((i-(n+1)/2))**2+((j-(n+1)/2))**2
			r=sqrt(r2)/(n-1) !normalize
			!boundary condition 
		  	if(r.ge.0.50) then
		  		matrix_new(i,j)=1
		  	else
			!else element is get from previous elements
		  	matrix_new(i,j)=(1-4*DT/DX**2)*matrix(i,j)+DT/DX**2*(matrix(i+1,j)+matrix(i-1,j)+matrix(i,j+1)+matrix(i,j-1))
			end if
		  end do
		end do					
		!set the new matrix to the previous matrix
		matrix=matrix_new	
		!write to file every 50th iteration
		if (mod(a,every_nth_save).eq.0) then !if every timestep is not worth to save
			
		call write_2d_matrix_to_file(matrix,n,a)  
	!	call write_single_point2d_matrix_to_file(matrix,n,a,41,41)
		end if	
	!	close(1) 
	end do

end subroutine

subroutine make_2d_init_c_besslej0(matrix,n)
implicit none
!Analytical solution to compare this function: 1 - np.exp(-4*T*BesselJZero**2)*besselj(0,2*BesselJZero*np.sqrt((-0.5 + x)**2 + (-0.5 + y)**2))
integer,intent(in) :: n
integer, parameter :: k1=selected_real_kind(20,100)
integer :: i,j
real(kind=rk) :: r,r2
real(kind=rk) :: besselZero=2.404825557695773_8
real(kind=rk), INTENT(INOUT) :: matrix(n,n)
	matrix=0

		!iterate x

	do i=1,n
		!iterate y

		do j=1,n
		    !calculate the radius of each element		
			r2=((i-(n+1)/2))**2+((j-(n+1)/2))**2
			r=sqrt(r2)/(n-1) !normalize
			
			!boundary condition 
			if (r.ge.0.50) then
		  		matrix(i,j)=1
			else	
			!!the element is get from known function, when t=0
				matrix(i,j)=1-bessel_j0(2*besselZero*r)
			end if
		end do	
	end do
	call write_2d_matrix_to_file(matrix,n,0)
!	call write_single_point2d_matrix_to_file(matrix,n,0,41,41)
end subroutine

subroutine make_extremely_init_c(matrix,n)
implicit none
integer,intent(in) :: n
integer, parameter :: k1=selected_real_kind(20,100)
integer :: i,j
real(kind=rk) :: r,r2
real(kind=rk) :: besselZero=2.404825557695773_8
real(kind=rk), INTENT(INOUT) :: matrix(n,n)
	matrix=0

		!iterate x

	do i=1,n
		!iterate y

		do j=1,n
			matrix(i,j)=(sin(i*0.12+j*0.30))
		    
		end do	
	end do
	call write_2d_matrix_to_file(matrix,n,0)
!	call write_single_point2d_matrix_to_file(matrix,n,0,41,41)
end subroutine


!subroutine to make write matrix to file
subroutine write_2d_matrix_to_file(matrix,n,a)
implicit none
integer,intent(in) :: n,a !the size of the array and number of the iteration
real(kind=rk), INTENT(IN) :: matrix(n,n) !matrix, wanted to write to the file
integer :: row !parameter to iterate each row
character(len=80) :: filename
	write(filename,'(A, i0,A)') "2D_data_", a, ".txt"
	!Open the file where the results will be written. 
	open(1, file = filename, status='new')
	do row =1,n
		write(1,*) matrix(row,:) !every row of the matrix is wrote to the new row, 
	end do
	!Close the file where the results has been written.
	close(1)
end subroutine		
!subroutine to write single point to file
subroutine write_single_point2d_matrix_to_file(matrix,n,a,x,y)
implicit none
integer,intent(in) :: n,a,x,y !the size of the array and number of the iteration and position of elem
real(kind=rk), INTENT(IN) :: matrix(n,n) !matrix, wanted to write to the file
real(kind=rk) :: T
integer :: row !parameter to iterate each row
character(len=80) :: filename
	
	T=a*DT
	write(filename,'(A, i0,A)') "2D_data_", a, ".txt"
	!Open the file where the results will be written. 
	open(1, file = filename, status='new')
		write(1,*) matrix(x,y), DX, DT, T !write value of element, DX, DT and T value
	!Close the file where the results has been written.
	close(1)

end subroutine	

end program Two_dimensional_diffusion_simulation
