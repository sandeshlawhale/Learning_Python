#! python3
# randomQuizGenerator.py - creates the quizzes with question and answers in random order, along with the answer key

import random
from datetime import datetime

capitals = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}


# generate quiz and answer key file
currentDate = datetime.now()
formattedDate = currentDate.strftime("%d-%m-%Y_%H-%M-%S")
quizFile = open('8. read and write files\\sample\\quizFile_%s.txt' % (formattedDate), 'w')
answerFile = open('8. read and write files\\sample\\answerFile_%s.txt' % (formattedDate), 'w')

# write out the header of the quiz file
quizFile.write('Name:\nDate:\nPlace:\n\n')
quizFile.write((' '*20) + "Capitals Quiz Test - %s\n\n" % (formattedDate))

# Shuffle the order of the states
states = list(capitals.keys())
random.shuffle(states)

# loop through alll states making a question for each
for i in range(len(capitals)):
    currentState = states[i]

    correctAnswer = capitals[currentState]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)

    quizFile.write('%s. What is the capital of %s?\n' % (i + 1, currentState))
    for j in range(4):
        quizFile.write('%s. %s\t\t' % ('ABCD'[j], answerOptions[j]))
    quizFile.write('\n\n')

    answerFile.write('%s. %s\n' % (i+1, 'ABCD'[answerOptions.index(correctAnswer)]))

quizFile.close()
answerFile.close()
