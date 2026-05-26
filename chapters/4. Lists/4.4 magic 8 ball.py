import random

messages = [
    "It is decidely so",
    "yes definitely",
    "reply hazy try again",
    "ask again later",
    "concentrate and ask again",
    "my reply is no",
    "outlook not so good",
    "very doubtful"
]

print("your fortune says",messages[random.randint(0, len(messages))])

# you can compare this with 3.1 how easy it looks with list