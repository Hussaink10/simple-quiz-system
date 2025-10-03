from quiz import take_quiz, calculate_score
from leaderboard import save_result, view_leaderboard
from admin import admin_menu

while True:
    print("Welcome to the Quiz System")
    print("1. Take Quiz")
    print("2. View Leaderboard")
    print("3. Admin Mode")
    print("4. Exit")
    choice=input("Enter your choice: ")

    if choice=="1":
        score,incorrect_questions, skipped_questions =take_quiz()
        name=input("Enter your name: ")
        save_result(name,score)
        calculate_score(score,len(incorrect_questions),incorrect_questions,len(skipped_questions))

    elif choice=="2":
        view_leaderboard()

    elif choice=="3":
        admin_menu()

    elif choice=="4":
        print("Goodbye")
        break
    else:
        print("Invalid choice. Try again.")