import time
import random
from utils import load_questions

def calculate_score(score, total, incorrect, skipped):
    print()
    print("Summary:")
    print("Total Correct:", score)
    print("Total Incorrect:", len(incorrect))
    print("Total Skipped:", skipped)

    if total != 0:
        percentage = (score / total) * 100
    else:
        percentage = 0

    if percentage >= 90:
        print("Your percentage is: ", percentage, "%", "Excellent")
    elif percentage >= 70:
        print("Your percentage is: ", percentage, "%", "Very good")
    elif percentage >= 50:
        print("Your percentage is: ", percentage, "%", "Fair")
    else:
        print("Your percentage is: ", percentage, "%", "Needs improvement")

    if incorrect:
        print()
        print("Incorrect Questions & Correct Answers:")
        for q in incorrect:
            print("Q:", q["question"])
            print("Correct Answer:", q["correct_answer"])
            print()

def take_quiz():
    score = 0
    questions = load_questions()
    random.shuffle(questions)
    time_limit = 10
    incorrect_questions = []
    skipped = 0
    skipped_questions = []

    for q in questions:
        print()
        print(q["question"])
        print("A)", q["options"][0])
        print("B)", q["options"][1])
        print("C)", q["options"][2])
        print("D)", q["options"][3])
        print(f"You have {time_limit} seconds to answer this question.")

        start_time = time.time()
        answer = input("Enter your answer (A/B/C/D), or press Enter to skip: ").upper()
        end_time = time.time()
        taken_time = end_time - start_time

        if answer == "":
            print("Question skipped")
            skipped_questions.append(q)
            skipped += 1
            print()
            continue
        if taken_time > time_limit:
            print("Time is up, Your answer was not counted.")
            skipped += 1
        elif answer == q["correct_answer"]:
            print("Correct")
            score += 1
        else:
            print("Wrong answer")
            incorrect_questions.append(q)
        print()

    return score, incorrect_questions, skipped_questions
