# Define a list of questions , ech with question, options and correct answer

questions = [
    {
        "question": "What is the capita city of Nepal?",
        "options": ["Kathmandu", "Lalitpur", "Bhaktapur","Pokhara"],
        "correct": 0
    },

    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Saturn", "Jupiter", "Uranus"],
        "correct": 2
    },

   {
        "question": "Which country has won the most World Cups?",
        "options": ["Brazil", "Germany", "Argentina", "France"],
        "correct": 0
    },

    {
        "question": "What is the smallest unit of matter? ",
        "options": ["Proton", "Neutron", "Atom"],
        "correct": 2
    },
    
]

# Initialize score to zero
score = 0
# Loop through each question
for question in questions:
    # Print the question
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}.{option}") # Print the options with numbers

    # Get user's answer
    user_answer = int(input("Choose the option number: ")) -1 # Get user's answer and subtract 1 to match list index

    #Check if user answer is correct
    if user_answer == question["correct"]:
        print("Correct answer!")
        score += 1
    else:
        print(f"Incorrect answer. The correct answer is {question['options'][question['correct']]}.")

    #Print a blank line to seperate questions
    print()

# Print final score
print(f"Your final score is {score} out of {len(questions)}")
                                                                             
      
