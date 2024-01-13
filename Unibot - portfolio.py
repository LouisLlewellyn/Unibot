# Simple chat bot for new students

subjects = {"science" : "The Science faculty is great at this university!", 
            "maths" : "This university has a good reputation for Maths!", 
            "computing" : "Computing! You'll love it here!", 
            "history" : "You'll learn a lot at LL uni studying History", 
            "sports" : "There's a great sports facility here!"
            }

colours = {"blue" : "Blue - great colour, same as the sports team here!",
           "green" : "That's my favourite.",
           "red" : "Strong colour!",
           "yellow" : "I hate that colour! But we're all different.",
           "pink" : "Lovely!",
           "purple" : "What of the best"
            }

questions_list = ["1 - Where is the fees office?",
             "2 - Who can help me with my curriculum form?", 
             "3 - Where can i find out more about student accommodation?", 
             "4 - What clubs does the university offer?",
             "5 - Which courses should i take?", 
             "6 - Who is my student mentor?" 
                ]

answers_list = ["The fees office is located in the Blue building on Camp Lane",
                "You can talk to your course advisor",
                "The SRC can help you with that",
                "See the notice board for whats on",
                "You can talk to an Orientation Leader",
                "Report to room 501 to find out"]

print("=================================================================================")
print("                                      UNIBOT")
print("=================================================================================")

print("Hi! My name is Unibot and I am here to help you through your university induction.")
print("---------------------------------------------------------------------------------\n")
print("I'm going to ask a few questions so I can get to know you a bit better...\n")

# Name input
while True:
    stu_name = input("What's your name: ")

    if len(stu_name) >= 0:
        break
    if stu_name.isnumeric:
        print("\nThats not a name!?")

name = ' '.join(word[0].upper() + word[1:] for word in stu_name.split())

print("---------------------------------------------------------------------------------")
print(f"               Hello " + name + " and welcome to LL's University")
print("---------------------------------------------------------------------------------\n")
# Age input
while True:
    age = input("What's your age: ")

    try:
        age_num = int(age)
        break
    except ValueError:
        print("Need a number for your age!\n")

if age_num <= 16:
    print("Mensa is that way!")
elif age_num <= 18:
    print("Wow! You must be super smart to start uni so young.")
elif age_num <= 20:
    print("That's when I started.")
elif age_num > 20:
    print("Never too late to start studying!")

# Subject input
while True:
    faculty = input(f"\n{name}, what faculty do you belong to: ")

    if faculty.lower() in subjects:
        print("---------------------------------------------------------------------------------")
        print(f"                   {subjects[faculty.lower()]}")
        print("---------------------------------------------------------------------------------")
        break
    else:
        print("We don't have that faculty here!?")

print("\nOne last thing... ")

# Colour input
while True:
    fav_colour = input("What is your favourite colour: ").lower()

    if fav_colour in colours:
        if fav_colour.isalpha() and len(fav_colour) > 2:
            break
        elif fav_colour != fav_colour.isalpha():
            print("That's not a colour!")
    else:
        print("I'm still learning and I don't recognise that colour!?\n")
            
print(f"{colours[fav_colour].capitalize()}")

print(f"\nThanks for telling me all about yourself! It's nice to meet you {name}.")
print(f"The {faculty.capitalize()} faculty is lucky to have you!")
input("\nIf you'd like to know anything, I've got some questions you can ask. Press enter if you'd like to see questions...")
[print(i) for i in questions_list]
print("\nWhen you're done asking questions, you can just say 'Bye'.\n")

# Questions
done = False
while not done:
    question = input("Do you have a question for me (1 - 6): ")

    if question.lower() == "bye":
        done = True
        print("\n-----------------------------------------------------------------------------------------")
        print(f"Thanks for chatting with me {name}! I hope you enjoy the rest of your time at LL university.")
        print("-----------------------------------------------------------------------------------------")

        break
    else:
        try:
            question_num = int(question)

            if 1 <= question_num <= len(questions_list):
                print(answers_list[question_num - 1],"\n")     

            else:
                print("I don't understand that. Please try again\n")

        except ValueError:
            print("I don't understand that. Please try again\n")


            


        
