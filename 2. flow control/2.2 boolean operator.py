# There are three boolean operators are used to compare boolean values
# and, or & not

# and Truth Table
# Expression              Evaluates to
# True and True           True
# True and False          False
# False and True          False
# False and False         False


# or Truth Table
# Expression              Evaluates to
# True and True           True
# True and False          True
# False and True          True
# False and False         False

# not Truth Table
# Expression              Evaluates to
# not True                  False
# not False                 True


print("True and True: ", True and True)
print("True or False: ", True or False)
print("True and False: ", True and False)
print("not True: ", not True)
print("not not False: ", not not False)

# combination of comparison and boolean operators
print("( 4 < 5 ) and ( 5 < 6 ): ", ( 4 < 5 ) and ( 5 < 6 ))
print("( 4 < 5 ) and ( 9 < 6 ): ", ( 4 < 5 ) and ( 9 < 6 ))
print("( 1 == 2 ) or ( 2 == 2 ): ", ( 1 == 2 ) or ( 2 == 2 ))