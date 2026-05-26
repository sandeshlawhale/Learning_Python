# string literals

# print('Tha is Alice's cat')             # this will give an error cause the string prints to the alice and the rest is invalid input in py

# we can sort this by two ways
print("this is alice's cat")            # by double quote
print('this is alice\'s cat')           # or by escapre characters

# escape characters in py 
# \'          single quote
# \"          double quote
# \t          tab
# \n          new line 
# \\          back slash


print("\nHello there! \nHow are you doint? \nI'm doing fine.\n")


# multiline string with triple quote
print('''Dear Alice,
      
Your cat was so good, I wish to see her again soon.
your lovely,
Bob
      ''')


"""just like the miltiline string output in print
we can do the same with comments
that is multi line comment with triple double quotes"""




# indexing and slicing
spam  = "hello! world"
print(spam[0])
print(spam[5])
print(spam[:6])
print(spam[6:])
print(spam[:])
print(spam[1:8])
print()


#  in and not in  operators in string
print("hello" in spam)
print("hello" not in spam)
print("!" in spam)
print("Hello" in spam)
print("Hello" not in spam)
print()


# methods on string
print(spam.upper())                                                 # converts everything into uppercase
print(spam.lower())                                                 # converts everything into lowercase
print(spam.isupper())                                               # check if it is uppercase
print(spam.islower())
print(spam.upper().isupper())                                                   
print(spam.isalpha())                                               # checks for letters only
print(spam.isalnum())                                               # check for letter and numbers only
print(spam.isdecimal())                                             # checks for decimal only
print(spam.isspace())                                               # check for spaces only and not empty
print(spam.istitle())                                               # checks for title case, First Letter Upper In Every Word
print()

# join and split
eggs = spam.split("! ")                                     # splits with the given characters if none then splits for every space
print(eggs)
print('---'.join(eggs))                                     # joins with given char

eggs = spam.split()
print(eggs)
print(''.join(eggs))                                     
print()


# justifying text with ljust(), rjust(), and center()
print("hello".rjust(10))
print("hello".ljust(10))
print("hello".center(10))

print("hello".rjust(11, "*"))
print("hello".ljust(11, "-"))
print("hello".center(11, "="))
print()


# removing white spaces with strip(), rstrip(), lstrip()
spam = "              Hello!                 "
print(spam)
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

