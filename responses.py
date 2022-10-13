import requests
import random

correctAnswer = ''
points_scored = 0
total_questions = 0
correctLetter = ''
correctIndex = 0

def handle_response(message) -> str:
    l_message = message.lower()

    if l_message == '!q':

        x = requests.get('https://the-trivia-api.com/api/questions?limit=1&region=US&difficulty=medium')
        x_json = x.json()
        answers = [x_json[0]['correctAnswer'], x_json[0]['incorrectAnswers'][0], x_json[0]['incorrectAnswers'][1], x_json[0]['incorrectAnswers'][2]]
        random.shuffle(answers)
        question = str(x_json[0]['question']) + '\n\nA) ' + str(answers[0]) + '\nB) ' + str(answers[1]) + '\nC) ' + str(answers[2]) + '\nD) ' + str(answers[3])
        global correctAnswer, correctLetter, correctIndex
        correctAnswer =str(x_json[0]['correctAnswer'])
        correctIndex = answers.index(x_json[0]['correctAnswer'])
        if correctIndex == 0:
            correctLetter = 'a'
        elif correctIndex == 1:
            correctLetter = 'b'
        elif correctIndex == 2:
            correctLetter = 'c'
        else:
            correctLetter = 'd'


        return question

    elif l_message == '!help':
        return 'Rules \n\n !q - Receive a question \n $(answer) - Enter a dollar sign followed by your answer for the question \n #accuracy - Check your game accuracy. \n ^score - See your score for active game.'

def handle_response2(message) -> str:
    l_message = message.lower()
    if l_message[1:] == correctAnswer.lower() or l_message[1:] == correctLetter.lower():
        global points_scored, total_questions
        points_scored = points_scored + 1
        total_questions = total_questions + 1
        return 'Correct! You now have ' + str(points_scored) + ' points!'
    else:
        total_questions = total_questions +1
        return 'Incorrect. The correct answer is: \n' + correctLetter.upper() + ') '+ correctAnswer

def handle_response3(message) -> str:
    l_message = message.lower()

    if l_message[1:] == 'accuracy':
        return 'You have gotten ' + str(points_scored) + ' out of ' + str(total_questions) + ' correct. Your accuracy is ' + str(round(points_scored/total_questions*100, 2)) + '%.'
    else:
        return 'Sorry! I don\'t know that one.'

def handle_response4(message) -> str:
    l_message = message.lower()

    if l_message[1:] == 'score':
        return 'You have ' + str(points_scored) + ' points in this game!'
    else:
        return 'Sorry! I don\'t know that one. Enter !help to view commands'






