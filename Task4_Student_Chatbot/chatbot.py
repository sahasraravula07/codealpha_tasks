from datetime import datetime

def show_menu():
    print("\n========== AVAILABLE COMMANDS ==========")
    print("hello")
    print("how are you")
    print("date")
    print("time")
    print("career")
    print("skills")
    print("python")
    print("ai")
    print("github")
    print("linkedin")
    print("internship")
    print("motivation")
    print("help")
    print("bye")
    print("========================================")

def chatbot():

    print("=" * 55)
    print("         STUDENT ASSISTANT CHATBOT")
    print("=" * 55)
    print("Welcome! I am your career and learning assistant.")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit.\n")

    while True:

        user = input("You: ").lower().strip()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm doing great. Thanks for asking!")

        elif user == "date":
            current_date = datetime.now().strftime("%d-%m-%Y")
            print(f"Bot: Today's date is {current_date}")

        elif user == "time":
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Bot: Current time is {current_time}")

        elif user == "career":
            print("Bot: Focus on Python, SQL, AI/ML, Data Analytics, and Web Development.")

        elif user == "skills":
            print("Bot: Important skills are Python, Git, SQL, HTML, CSS, Communication, and Problem Solving.")

        elif user == "python":
            print("Bot: Python is a powerful programming language used in AI, Data Science, Automation, and Web Development.")

        elif user == "ai":
            print("Bot: Artificial Intelligence helps machines perform tasks that normally require human intelligence.")

        elif user == "github":
            print("Bot: GitHub is a platform used to store, manage, and showcase coding projects.")

        elif user == "linkedin":
            print("Bot: LinkedIn helps you build a professional profile and connect with recruiters.")

        elif user == "internship":
            print("Bot: Build projects, maintain GitHub, improve coding skills, and stay active on LinkedIn.")

        elif user == "motivation":
            print("Bot: Success is the result of consistent effort and continuous learning.")

        elif user == "help":
            show_menu()

        elif user == "bye":
            print("Bot: Thank you for chatting. Goodbye and best wishes for your career!")
            break

        else:
            print("Bot: Sorry, I don't understand that command.")
            print("Bot: Type 'help' to see available commands.")

chatbot()