import random

num1 = None
num2 = None
correct_answer = None
inputted_answer = None
score = None

def question():
    global num1
    global num2
    global correct_answer
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    correct_answer = str(num1 * num2)

def get_answer():
    global inputted_answer
    inputted_answer = str(input(f"What is {num1} times {num2}: "))

def question_and_answer():
    question()
    get_answer()

def check_answer(answer_given, answer_correct):
    return answer_correct == answer_given

def test(test_length):
    global score
    score = 0
    for i in range(test_length):
        question_and_answer()
        if check_answer(inputted_answer, correct_answer):
            score = score + 1
    result_percentage = int((score / test_length) * 100)
    result_fraction = str(f"{score} / {test_length}")
    print(f"You got {result_fraction} = {result_percentage}% well done! :)")

mode = str(input("Would you like to practice or test?: ")).upper()

if mode == "PRACTICE":

    while inputted_answer != "end":

        question_and_answer()

        if inputted_answer == "end":
            break
        elif check_answer(inputted_answer, correct_answer):
            print("Correct! Well done :)\n")
        else:
            while not check_answer(inputted_answer, correct_answer):
                print("Unlucky! Try again or ask for help\n")
                get_answer()
            print("Well done, you got there in the end! :)\n")

elif mode == "TEST":
    length = int(input("How many questions do you want to do?: "))
    test(length)
