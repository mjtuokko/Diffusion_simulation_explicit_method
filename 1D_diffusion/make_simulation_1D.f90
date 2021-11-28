program One_dimensional_diffusion_simulation
implicit none
!Define variables
integer :: n=11 !n is the size of the matrix used
integer, parameter :: rk = selected_real_kind(8)
integer :: k !k is the number of iterations.
real(kind=rk), dimension(:), allocatable :: matrix !matrix for the function of the diffusion equation 
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
	allocate ( matrix(n) )

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
		
	!Initialize matrix c in the form of sine function
	call make_1d_init_c_sin(matrix,n)
	!Make iteration k times.
	call make_1d_simulation(matrix,n,k)
	!make analytical results to comparing
!	call make_analytical_sol_sin_compare(matrix,n,k)
	
!Subroutines
contains

subroutine make_1d_simulation(matrix,n,k)
	implicit none
	!define variables
	real(kind=rk), INTENT(INOUT) :: matrix(n)
	integer, INTENT(IN) :: n,k
	real(kind=rk) :: matrix_new(n) !new matrix for the iteration
	integer :: a,i !a is an iteration parameter for every iteration
	! i is iteration parameter for each element 
	!make iteration k times


	do a=1,k
		matrix_new=0
		!make changes to each element
		do i=1,n 
			matrix_new(i)=(1-2*DT/DX**2)*matrix(i)+DT/DX**2*(matrix(i+1)+matrix(i-1))
		end do
		!From boundary conditions, make boundary elements zero
		matrix_new(1)=(1-2*DT/DX**2)*matrix(1)+2*DT/DX**2*matrix(2)
		matrix_new(n)=(1-2*DT/DX**2)*matrix(n)+2*DT/DX**2*matrix(n-1)
		!make original matrix equal to the new matrix after time step
		matrix = matrix_new
		if (mod(a,every_nth_save).eq.0) then !if every timestep is not worth to save
			call write_1d_matrix_to_file(matrix,n,a)  
		end if	
	end do
	
end subroutine

!subroutine to initailize matrix
subroutine make_1d_init_c_sin(matrix,n)
implicit none
integer,intent(in) :: n !the size of the array
integer :: i !iteration parameter
real(kind=rk), INTENT(INOUT) :: matrix(n) !matrix, we want to initialize
real(kind=rk) :: pi=4*atan(1.0)

	matrix=0 !make each element zero for backup.
 	!make each element own value with sine function
	do i=1,n
			matrix(i)=0.5_8-0.5_8*cos(2*pi*(i-1)/(n-1)) !the first and the last is zero.
	end do
	!write matrix to the file
	call write_1d_matrix_to_file(matrix,n,0)

end subroutine

!subroutine to make write matrix to file
subroutine write_1d_matrix_to_file(matrix,n,a)
implicit none
integer,intent(in) :: n,a !n=the size of the array, a=iteration number
real(kind=rk), INTENT(IN) :: matrix(n) !matrix, wanted to write to the file
character(len=80) :: filename
	write(filename,'(A, i0,A)') "1D_data_", a, ".txt"
	!Open the file where the results will be written. 
	open(1, file = filename, status='new')
	write(1,*) matrix
	!Close the file where the results has been written.
	close(1)
end subroutine

!subroutine to make analytical solution data to the compare
subroutine make_analytical_sol_sin_compare(matrix,n,k)
implicit none
integer,intent(in) :: n,k !the size of the array, times of iterations
integer :: i,a !iteration parameters
real(kind=rk), INTENT(INOUT) :: matrix(n) !matrix, we want to initialize
real(kind=rk) :: pi=4*atan(1.0) , T
	do a=0,k !do loop for every time step
	if(mod(a,every_nth_save).eq.0) then !only every nth is calculated
	T=a*DT
			!iterate x
		do i=1,n
			matrix(i)=0.5_8-0.5_8*exp(-2**2*pi**2*T)*cos(2*pi*(i-1)/(n-1)) !analytical solution
		end do
		call write_1d_matrix_to_file(matrix,n,a)
	end if	
	end do

	

end subroutine
end program One_dimensional_diffusion_simulation
