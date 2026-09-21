# [How well do you know your black history? Law Edition!]
# Author: [Jorden Lee]
# A quiz/questionnaire program built for CS 104 Project 1

# TODO: Define your variables here.
points = 5
startig_score = 0
score = startig_score
# TODO: Print a welcome message introducing your program.
print("Welcome, today you will be taking a quiz to see how well you know your black history, but not just any black history, Black legal history!\n There are 6 questions, you can earn up to a total of 30 points. When you finish the last question, you will automatically recieve your quiz grade back.\n\n")
# TODO: Write your questions and conditional logic here.
# Question 1
print("1. Which 1896 Supreme Court decision famously established the 'separate but equal' doctrine, providing legal justification for Jim Crow laws for over half a century? \n1.Plessy V. Ferguson\n2.Dred Scott V. Sandford\n3.Cumming V. Richmond County Board of Education\n4.Civil Rights Cases of 1883\n")

answer = input("Enter your answer:")

if answer == "1":
    print("Correct!")
    score = score + points
else:
    print("Incorrect. Next question.\n")
# Question 2
print("2. In  the landmark 1954 decision Brown v. Board of Education, the Supreme Court ruled that racial segregation in public schools violated which part of the U.S. Constitution? \n1.The Equal Protection Clause of the Fourteenth Amendment\n2.The Due Process Clause of the Fifth Amendment \n3.The Commerce Clause of the Fifth Amendment \n4.The Privileges and Immunities Clause of Article IV\n")

answer = input("Enter your answer:")

if answer == "1":
    print("Correct!")
    score = score + points
else:
    print("Incorrect. Next question.\n")
# Qustion 3
print("3.Before his appointment to the Supreme Court, Thurgood Marshall famously served as the chief legal counsel for which civil rights organization? \n1.Southern Christian Leadership Conference(SCLC)\n2.Congress of Racial Equality(CORE)\n3.NAACP Legal Defense and Educational Fund\n4.Urban League\n")

answer = input("Enter your answer:")

if answer == "3":
    print("Correct!")
    score = score + points
else:
    print("Incorrect. Next question.\n")
# Question 4
print("4.The 1967 Supreme Court case Loving v. Virginia unanimously struck down state anti-miscegenation laws, which criminalized what practice? \n1.Interstate travel by interracial couples\n2.Integrated public housing\n3.Voter suppression targeting minorities\n4.Interracial marriage\n")

answer = input("Enter your answer:")

if answer == "4":
    print("Correct!")
    score = score + points
else:
    print("Incorrect. Next question.\n")
# Question 5
print("5.As chief counsel for the NAACP Legal Defense Fund, Thurgood Marshall successfully spearheaded the litigation and oral arguments for which landmark 1954 Supreme Court case? \n1.Brown V. Board of Education\n2.Sweatt v. Painter\n3.Briggs v. Elliot\n4.Bolling v. Sharpe\n")

answer = input("Enter your answer:")

if answer == "1":
    print("Correct!")
    score = score + points
else:
    print("Incorrect. Next question.\n")
# Question 6
print("6.What did the 13th Amendment to the U.S. Constitution accomplish? \n1.It guaranteed equal voting rights regardless of race.\n2.It granted citizenship to all people born in the United States.\n3.It granted women the right to vote.\n4.It abolished slavery and involuntary servitude, except as punishment for a crime.\n")

answer = input("Enter your answer:")

if answer == "4":
    print("Correct!")
    score = score + points
else:
    print("Incorrect. Next question.\n")
# Follow the outline you planned in your README.

# TODO: Display the final results to the user.
# Final score

if score == 30:
    print("You got every question right and an A!")
elif score >= 20:
    print("Good job! You earned an A!")
elif score >= 10:
    print("Nice try! You earned a B!")
else: 
    print("Nice try! You earned a C.")

print("You have compleated the quiz!")
print(f"Your final score is: {score} out of 30 points.")
