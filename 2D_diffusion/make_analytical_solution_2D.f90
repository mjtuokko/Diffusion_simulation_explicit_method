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
	


	!make analytical results to comparing
	call make_analytical_sol_besselj0_compare(matrix,n,k)


contains
!Subroutines

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


!subroutine to write single point to file, not used in main program
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

!subroutine to make analytical solution data to the compare
subroutine make_analytical_sol_besselj0_compare(matrix,n,k)
implicit none
integer,intent(in) :: n,k
integer, parameter :: k1=selected_real_kind(20,100)
integer :: i,j,a
real(kind=rk) :: r,r2,T
real(kind=rk):: besselZero=2.404825557695773_8
real(kind=rk), INTENT(INOUT) :: matrix(n,n)
	call chdir("Analytical_sol_data")
	do a=0,k !do loop for every time step
	if(mod(a,every_nth_save).eq.0) then !only every nth is calculated
	T=a*DT
			!iterate x
		do i=1,n
			!iterate y

			do j=1,n
			    !calculate the radius of each element		
				r2=((i-51))**2+((j-51))**2
				r=sqrt(r2)/100 !normalize
				!!the element is get from analytical solution
				matrix(i,j)=1-exp(-4*T*besselZero**2)*bessel_j0(2*besselZero*r)
			end do	
		end do
		call write_2d_matrix_to_file(matrix,n,a)
	!	call write_single_point2d_matrix_to_file(matrix,n,a,41,41)
	end if 	
	end do

end subroutine
end program Two_dimensional_diffusion_simulation
