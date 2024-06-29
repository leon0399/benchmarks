program benchmark_primes
    implicit none
    integer, parameter :: NUMBER = 100000
    integer :: lastPrime
    real :: start_time, end_time, duration

    ! Get the starting time
    call cpu_time(start_time)

    ! Find the last prime number
    lastPrime = getLastPrime(NUMBER)
    print *, 'Last prime: ', lastPrime

    ! Get the ending time
    call cpu_time(end_time)

    ! Calculate the duration in milliseconds
    duration = (end_time - start_time) * 1000.0
    print '(A, F6.2, A)', 'Execution time: ', duration, 'ms'

contains

    function getLastPrime(count) result(lastPrime)
        integer, intent(in) :: count
        integer :: lastPrime
        integer :: i, j
        logical :: isPrime

        lastPrime = 0

        do i = 2, count
            isPrime = .true.

            do j = 2, i / 2
                if (mod(i, j) == 0) then
                    isPrime = .false.
                    exit
                end if
            end do

            if (isPrime) then
                lastPrime = i
            end if
        end do
    end function getLastPrime

end program benchmark_primes