''' @file main Lab0_Fibonacci.py
There must be a docstring at the beginning of a Python source file
with an @file [filename] tag in it! '''

def fib (idx):
    ''' This method calculates a Fibonacci number corresponding to
    a specified index.
    @param idx An integer specifying the index of the desired
                Fibonacci number.'''

user_input = input('Would you like to find a Fibonacci Number? '
                   '(y)es or (n)o: ')

if __name__ == '__main__':
    while (True):
        if (user_input == 'y'):
            # User-Input            
            while(True):
                # This small section I found online and adjusted to fit what
                # I needed to do to complete this code. The try function will
                # complete the command that follows it. The except function
                # will give an alternative if the specified error occurs (in
                # this case, if the ValueError error in Spyder occurs).
                try:
                    idx = int(input('Please enter a positive index number to '
                                    'solve for the Fibonacci: '))
                except ValueError:
                    print('\nInvalid Input. Please enter a positive integer.')
                    continue
                    # This continue function will return the code to the top
                    # top of the current while loop
                # This next if function is to make sure that the input is a
                # positive integer
                if (idx < 0):
                    print('\nInvalid Input. Please enter a positive integer.')
                    continue
                else:
                    break
                    # This break function exits this current while loop

            # This isn't entirely necessary since in the printed answer, I 
            # include the number input by the user
            print ('Calculating Fibonacci number at '
                       'index n = {:}...'.format(idx))
            
            # Initials
            j = 0    
            n_previous1 = 0
            n_previous2 = 1
        
            while(True):
    
                # Calculating Fibonacci
                if (j < idx-1):
                # Need to j < idx-1 because j will increase by 1 every run
                # through the loop. This is similar to doing the for loop in 
                # MATLab which I will look up later if that same function 
                # exists in Python
                    if (idx == 0):
                        # If the index is 0, the Fibonacci value is zero
                        print('\nYour Fibonacci number is 0.')
                        break
                    elif (idx == 1):
                        # If the index is 1, the Fibonacci value is one
                        print('\nYour Fibonacci number is 1.')
                        break
                    else:
                        n = n_previous1 + n_previous2
                        # This is the equation to find the Fibonacci value at 
                        # any index above 1. It is the sum of the two 
                        # preceding Fibonacci values.
                        
                        n_previous1 = n_previous2
                        n_previous2 = n
                        # These are to take notes on the previous two 
                        # Fibonacci values. They change every loop through
                        # the code                        
                        
                        j = j + 1
                        # This is a placeholder for the loop. 
                else:
                    break
        elif (user_input == 'n'):
            print('\nMaybe some other time...')
            # If the user does not want to find a Fibonacci number, then this
            # message is displayed and the code ends
            break
        else:
            user_input = input('Invalid Input. Would you still like to '
                               'find a Fibonacci Number? (y)es or (n)o: ')
            # This will prompt the user if they want to try to enter a correct
            # indexing value
            continue
            
        print('\nThe Fibonacci Number at index {:} is {:}.'.format(idx,n))
        # This message displays the index the user entered and the Fibonacci 
        # value corresponding to that index.
    
        user_input = input('Would you like to find another Fibonacci Number? '
                   '(y)es or (n)o: ')