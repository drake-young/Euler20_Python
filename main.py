from timeit import default_timer

# ===========================================================
# PROBLEM 20 -- Factorial Digit Sum
# ===========================================================
#
#  n! means n * (n-1) * ... * 3 * 2 * 1
#
#  For example, 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
#  = 3628800 and the sum of the digits of that number is
#  3+6+2+8+8+0+0 = 27
#
#  Find the sum of the digits in the number 100!
#
# ===========================================================
def problem_20( ):
    # Print Problem Context
    print( "Project Euler Problem 20 -- Factorial Digit Sum" )

    # Set Up Variables
    start_time  =  default_timer( )
    n           =  100
    factorial   =  n

    # Calculate n!
    for k in range( 1 , n ):
        factorial  *=  k

    # Compute Results
    result  =  sum( int(d) for d in str(factorial) )

    # Compute Execution Time
    end_time        =  default_timer( )
    execution_time  =  ( end_time - start_time ) * 1000

    # Display Results
    print( "   The sum of digits in 100!:   %d"      %  result )
    print( "   Computation Time:            %.3fms"  %  execution_time )
    return


if __name__ == '__main__':
    problem_20( )