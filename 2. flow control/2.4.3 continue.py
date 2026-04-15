# continue statement are used inside the loop as well but it shifts the execution to the start of the loop instead of the end like the break st.
#  using continue statement, the loop immidiately jumps back to start

while True: 
    print("who are you: ")
    name = input()
    if name != 'joe':
        continue
    print("hello, joe. what is password? (is it a fish?)")
    password = input()
    if password == 'swordfish':
        break
print("Access Granted")