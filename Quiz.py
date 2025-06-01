#Quiz Application
quiz = [{"questions":"What is the capital of France?","options":"A) Paris\nB) London\nC) Berlin\nD) Madrid","answer":"A"},
        {"questions":"What is achieved after mixing yellow and red?","options":"A) Green\nB) Orange\nC) Purple\nD) Brown","answer":"B"},
        {"questions":"What is the largest planet in our solar system?","options":"A) Earth\nB) Jupiter\nC) Saturn\nD) Mars","answer":"B"}]
score = 0
for q in quiz:
    print("Question:" , q["questions"])
    print("\nOptions:\n",q["options"])
    user_answer = input("\n Enter your Answer:").upper()
    if user_answer == q["answer"]:
        print("Correct!")
        score +=1
    else:
        print("Incorrect! The correct answer is:", q["answer"])
print("\n Your final score is:",score)
print("Thank you for playing the quiz!")
# End of Quiz Application
