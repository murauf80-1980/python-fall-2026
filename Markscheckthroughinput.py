name = input("Enter your name: ")
age = int(input("Enter your age: "))
MathMarks = int(input("Enter your math marks: "))
ScienceMarks = int(input("Enter your science marks: "))
EnglishMarks = int(input("Enter your english marks: "))

marks = [MathMarks, ScienceMarks,EnglishMarks]
total = sum(marks)
average = total / len(marks)
age_after_5_years = age + 5

print("Total marks:", total)
print("Student name:", name)
print("Age:", age)
print("Average marks:", round(average, 2))
print("Age after 5 years:", age_after_5_years)
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of average:", type(average))

