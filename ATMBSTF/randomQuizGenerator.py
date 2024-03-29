#! python3
# randomQUizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# the quiz data. Keys are states and values are their capitals

capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
     'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
     'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
      'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 
      'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
       'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
        'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
         'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
         'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 
         'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
          'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
           'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

# Generate 35 quiz file

for quizNum in range(35):
    # TODO: Create the quiz and answer key files.
    # TODO: Write out the header for the quiz.
    # TODO: Shuffle the order of the states.
    # TODO: Loop through all 50 states, making a question for each.

    quizFile = open('capitalsquiz%s.txt' % (quizNum+1), 'w')
    answerkeyFile = open('capitalquiz_answer%s.txt' % (quizNum+1), 'w')

    # Write out the header for the quiz.

    quizFile.write('Name:\n\nDate:\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    #shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # get right and wrong answers.

    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

    # Write the question and the answer options to the quiz file
    quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
    for i in range(4):
        quizFile.write('   %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        #Write the answer key to a file.
        answerkeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerkeyFile.close()

