#Question-1
q1="1.Which planet has the longest day in our solar system?"
o1=[ 
"A. Earth",
"B. Mars",
"C. Venus",
"D. Jupiter",
]
a1="C"
print(q1)
print("(Select an option)")
for option in o1:
    print(option)
s1=input("Enter Your Answer:").upper().strip()

#Question-2
q2="2.What invention connects people globally but was never meant for social media?"
c2="(Answer in a single word)"
print(q2)
print(c2)
a2="INTERNET"
s2=input("Enter Your Answer:").upper().strip()

#Question-3
q3="3.What is the only letter not used in the periodic table symbols?"
c3="(Answer in a single letter)"
print(q3)
print(c3)
a3="J"
s3=input("Enter Your Answer:").upper().strip()

#Question-4    
q4="4.Which animal can survive the longest without water?"
c4="(Answer in two words)"
print(q4)
print(c4)
a4="kangaroo rat"
s4=input("Enter Your Answer:").lower().strip()

#Question-5
q5="5.In python, print(2**3)"
c5="(Answer with a single digit)"
print(q5)
print(c5)
a5=8
s5=int(input("Enter Your Answer:"))

#Answers
print("*****************************************************")
score=0 
i=0
i+=1
print("Answers:")
if s1==a1:
    print("1.Correct!")
    score+=1
else:
    print("1.Wrong!")
print("Your Answer:",s1)
print("Correct Answer: C")


if s2==a2:
    print("2.Correct!")
    score+=1
else:
    print("2.Wrong!")
print("Your Answer:",s2)
print("Correct Answer: Internet")


if s3==a3:
    print("3.Correct!")
    score+=1
else:
    print("3.Wrong!")
print("Your Answer:",s3)
print("Correct Answer: J")


if s4==a4:
    print("4.Correct!")
    score+=1
else:
    print("4.Wrong!")
print("Your Answer:",s4)
print("Correct Answer: Kangaroo Rat")


if s5==a5:
    print("5.Correct!")
    score+=1
else:
    print("5.Wrong!")
print("Your Answer:",s5)
print("Correct Answer: 8")

#Final Score
print("******************************************************")
print("Your Final Score:",score)
print("******************************************************")