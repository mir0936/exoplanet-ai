program generate_data
    implicit none
    integer, parameter :: num_samples = 10000, num_steps = 100
    integer :: i, j, has_planet, dip_center, dip_width
    real :: flux(num_steps), noise, dip_depth
    real :: rand_val
    open(unit=10, file='lightcurves.csv', status='replace')

    call random_seed()
    
    do i = 1, num_samples
        call random_number(rand_val)
        if (rand_val > 0.5) then
            has_planet = 1
        else
            has_planet = 0
        end if
        
        call random_number(rand_val)
        dip_center = 30 + int(rand_val * 40)
        dip_width = 5 + int(rand_val * 10)
        dip_depth = 0.02 + (rand_val * 0.05)
        
        write(10, '(I2,$)') has_planet
        
        do j = 1, num_steps
            call random_number(rand_val)
            noise = (rand_val - 0.5) * 0.02
            flux(j) = 1.0 + noise
            
            if (has_planet == 1 .and. abs(j - dip_center) < dip_width) then
                flux(j) = flux(j) - dip_depth
            end if
            write(10, '(A,F8.4,$)') ',', flux(j)
        end do
        write(10, *)
    end do
    
    close(10)
    print *, "Data generated: lightcurves.csv"
end program generate_data
