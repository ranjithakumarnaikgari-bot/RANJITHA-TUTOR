print("Welcome to the Mini Brain Quiz!")
score = 0

answer1 = input("1.Which planet is known as Red Planet?")
if answer1.lower() == "mars":
    print("Correct! + 1 point!")
    score = score + 1
else:
    print("Oops! The right answer is Mars.")
answer2 = input("2.What is 5 + 3 * 2? ")
if answer2 == "11":
    print("Awesome job! + 1 point")
    score = score + 1
else :
    print("Close! Multiply first: 5 + 6 =11.")
answer3 = input("3. Which language uses print() to show text on screen?")
if answer3.lower() == "python":
    print("Spot on! + 1 point")
    score = score + 1
else:
    print("It's Python")
print("Game over! Your final score is:",score,"out of 3")
