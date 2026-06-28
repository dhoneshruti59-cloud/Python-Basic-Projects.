question_bank = [
    ("Which keyword is used to define a function in Python?", "function", "define", "def", "fun", "C"),
    ("Which language is used for Python programming?", "Python", "Java", "C", "HTML", "A"),
    ("Which data type is mutable in Python?", "tuple", "string", "list", "integer", "C"),
    ("Which symbol is used to create dictionary?", "[]", "()", "{}", "<>", "C"),
    ("What is the output of bool(0)?", "True", "False", "0", "Error", "B")
]

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

score = 0
wrong_answers = []

for q in question_bank:
    print("\n" + q[0])
    print("A.", q[1])
    print("B.", q[2])
    print("C.", q[3])
    print("D.", q[4])

    answer = input("Enter Answer (A/B/C/D): ").upper()

    while answer not in ["A", "B", "C", "D"]:
        answer = input("Invalid! Enter A/B/C/D: ").upper()

    if answer == q[5]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")

        if q[5] == "A":
            print("Correct Answer is: A.", q[1])
        elif q[5] == "B":
            print("Correct Answer is: B.", q[2])
        elif q[5] == "C":
            print("Correct Answer is: C.", q[3])
        elif q[5] == "D":
            print("Correct Answer is: D.", q[4])

        wrong_answers.append(q[0])

total = len(question_bank)
percentage = (score / total) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

print("\n*** RESULT REPORT ***")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Score        :", score, "/", total)
print("Percentage   :", percentage, "%")
print("Grade        :", grade)

