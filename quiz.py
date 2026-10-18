
class QuizManagementSystem:
    def __init__(self):
        self.questions = [
            {
                "question": "1. Which language is used for AI?",
                "options": [
                    "A. HTML",
                    "B. Python",
                    "C. CSS",
                    "D. XML"
                ],
                "answer": "B"
            },
            {
                "question": "2. Which keyword defines a function in Python?",
                "options": [
                    "A. function",
                    "B. define",
                    "C. def",
                    "D. fun"
                ],
                "answer": "C"
            },
            {
                "question": "3. Which data type stores True or False?",
                "options": [
                    "A. int",
                    "B. str",
                    "C. list",
                    "D. bool"
                ],
                "answer": "D"
            },
            {
                "question": "4. Which symbol is used for comments?",
                "options": [
                    "A. //",
                    "B. #",
                    "C. <!--",
                    "D. **"
                ],
                "answer": "B"
            },
            {
                "question": "5. Which function displays output?",
                "options": [
                    "A. input()",
                    "B. scan()",
                    "C. print()",
                    "D. display()"
                ],
                "answer": "C"
            }
        ]

        self.results = []

    def show_instructions(self):
        print("\n--- QUIZ INSTRUCTIONS ---")
        print("1. The quiz contains 5 questions.")
        print("2. Each correct answer carries 1 mark.")
        print("3. There is no negative marking.")
        print("4. Enter A, B, C, or D to answer.")
        print("5. Your final score will be displayed.")

    def start_quiz(self):
        score = 0
        correct = 0
        incorrect = 0

        print("\n--- STARTING QUIZ ---")

        for item in self.questions:
            print("\n" + item["question"])

            for option in item["options"]:
                print(option)

            while True:
                answer = input("Enter your answer (A/B/C/D): ")
                answer = answer.strip().upper()

                if answer in ["A", "B", "C", "D"]:
                    break

                print("Invalid answer! Please enter A, B, C, or D.")

            if answer == item["answer"]:
                print("Correct Answer!")
                score += 1
                correct += 1
            else:
                print("Incorrect Answer!")
                print("Correct answer:", item["answer"])
                incorrect += 1

        percentage = (score / len(self.questions)) * 100

        if percentage >= 80:
            performance = "Excellent Performance!"
        elif percentage >= 50:
            performance = "Good Performance!"
        else:
            performance = "Keep Practicing!"

        result = {
            "score": score,
            "correct": correct,
            "incorrect": incorrect,
            "percentage": percentage
        }

        self.results.append(result)

        print("\n===== QUIZ RESULT =====")
        print("Total Questions:", len(self.questions))
        print("Correct Answers:", correct)
        print("Incorrect Answers:", incorrect)
        print("Final Score:", score, "/", len(self.questions))
        print(f"Percentage: {percentage:.2f}%")
        print("Performance:", performance)

    def show_previous_results(self):
        print("\n--- PREVIOUS QUIZ RESULTS ---")

        if not self.results:
            print("No previous results available.")
            return

        for i, result in enumerate(self.results, start=1):
            print(f"\nQuiz {i}")
            print("Score:", result["score"], "/", len(self.questions))
            print("Correct:", result["correct"])
            print("Incorrect:", result["incorrect"])
            print(f"Percentage: {result['percentage']:.2f}%")

    def run(self):
        print("================================")
        print("  QUIZ MANAGEMENT SYSTEM")
        print("================================")

        while True:
            print("\n1. Start Quiz")
            print("2. View Instructions")
            print("3. View Previous Results")
            print("0. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.start_quiz()
            elif choice == "2":
                self.show_instructions()
            elif choice == "3":
                self.show_previous_results()
            elif choice == "0":
                print("\nThank you for using the Quiz Management System!")
                print("Exiting the system...")
                break
            else:
                print("Invalid Option! Please try again.")


# Main Program
if __name__ == "__main__":
    quiz = QuizManagementSystem()
    quiz.run()
