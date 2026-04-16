# The Collatz Sequence

# if number is even => //2
# if odd => 3 * num + 1
# ends when it reaches to 1

def collatz(num) :                                                         # decleration of collatz function
        if num % 2 == 0:            # even
            res = num // 2
        else :                      # odd
            res = 3 * num + 1   

        print(res)
        return res

try:                                                                       # try block to avoid string errors
    userInput = int(input("Enter a number: "))
    
    while userInput!=1:                                                    # we use while cause we have a condition 
        userInput = collatz(userInput)                                     # calling collatz function

except ValueError:                                                         # prints error on invalid input
    print("please enter a valid integer")

