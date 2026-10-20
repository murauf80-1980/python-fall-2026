stdCode = 34551001
stdName = 'Mohammed'
stdLastname = 'Ali'
stdMidterm = 80
stdFinal = 98.5
stdCity = '  Alexandria  '
stdEmail = 'mohammed.ali@school.edu'
stdPhone = '555-0142'
stdComment = ''

# 1. Create these three variables and print the type of each:
# a = 12      b = 12.0      c = 12 + 3j
a = 12
b = 12.0
c = 12 + 3j
print("a type is ",type(a))
print("b type is ",type(b))
print("c type is ",type(c))


# 2. PREDICT: What is the type of x = 35e3 ? What value will print(x) show?
#    My guess: Float

x = 35e3    
print("x type is ",type(x))

# 3. Import the random module and print a random number between 1 and 10.
#    (Hint: random.randrange(1, 11))   

import random

print(random.randrange(1, 11))

# 4. The number "75" below is a STRING. Cast it to an int, add it to stdMidterm,
#    and print the result.
number = "75"
print(int(number) + stdMidterm)

# 4. The number "75" below is a STRING. Cast it to an int, add it to stdMidterm,
#    and print the result.
bonusPoints = "75"

number = "75"
print(int(number) + stdMidterm)

# 5. PREDICT: What will each line print?
#    print(int(9.99))
#    print(float(7))
#    print(str(3.0))
#    My guess: 9, 7.0, and 3.0
print(int(9.99))
print(float(7))
print(str(3.0))

# 6. Fix this line so it runs without an error (use casting):
#    print('Student code: ' + stdCode)
print('Student code: ' + str(stdCode))

# 7. PREDICT: What happens when you run print(int('12.5')) ? Try it, then
#    write a line that correctly turns '12.5' into the int 12.
#    My guess: int('12.5') raises a ValueError because the string is not an integer literal.
try:
    print(int('12.5'))
except ValueError as error:
    print(type(error).__name__)

print(int(float('12.5')))


# 8. Print the first letter of stdName, and the LAST letter of stdName
#    (use a negative index for the last letter
print(stdName[0])
print(stdName[-1])

# 9. Use slicing to print only 'Moh' from stdName.
print(stdName[:3])

# 10. Print stdName in all UPPERCASE and stdLastname in all lowercase
print(stdName.upper())
print(stdLastname.lower())

# 11. stdCity has extra spaces. Print it with the spaces removed using strip().
#     Then print len() of stdCity before and after strip
print("Length before strip:", len(stdCity))
strippedCity = stdCity.strip()
print(strippedCity)
print("Length after strip:", len(strippedCity))

# 12. Use replace() to change the '-' in stdPhone to a space and print it.
print(stdPhone.replace('-', ' '))

# 13. Use split() to separate stdEmail at the '@' and print the result.
#     PREDICT: What data type does split() return?
#     My guess: split() returns a list.
emailParts = stdEmail.split('@')
print(emailParts)
print(type(emailParts))

# 14. Use an f-string to print exactly:
#     Mohammed Ali scored 98.5 on the final.
print(f"{stdName} {stdLastname} scored {stdFinal} on the final.")

# 15. Use an f-string with a format specifier to print the average of
#     stdMidterm and stdFinal with exactly 2 decimal places.
#     Expected output: Average: 89.25
average = (stdMidterm + stdFinal) / 2
print(f"Average: {average:.2f}")

# 16. Print this sentence using an escape character for the quotes:
#     The teacher said "Great job!" to Mohammed.
print("The teacher said \"Great job!\" to Mohammed.")

# 17. Use the in keyword to check if 'school' is in stdEmail. Print the result.
print('school' in stdEmail)

# 18. PREDICT True or False for each, then check with bool():
#     bool(0)   bool(15)   bool("")   bool("False")   bool([])   bool(None)
#     My guesses: False, True, False, True, False, False
print(bool(0))
print(bool(15))
print(bool(""))
print(bool("False"))
print(bool([]))
print(bool(None))



# 19. Print the result of bool(stdComment). Then explain in a comment
#     why it gives that answer.
print(bool(stdComment))
# An empty string is falsy in Python, so bool(stdComment) is False.


# 20. Use isinstance() to check if stdFinal is a float. Print the result.
print(isinstance(stdFinal, float))

# BONUS: Print stdName backwards ('demmahoM') using slicing.
#        Hint: [::-1]
print(stdName[::-1])