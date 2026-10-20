# stdCode = 34551001
# stdName = 'Mohammed'
# stdLastname = 'Ali'
# stdMidterm = 80
# stdFinal = 98.5
# stdGPA = 3.7
# stdActive = True
# stdCourses = ['Python', 'Math', 'English']
# stdBirthDate = (2001, 5, 14)
# stdProfile = {'name': 'Mohammed', 'city': 'Alexandria'}
# stdSkills = {'typing', 'Excel', 'typing'}
# stdAdvisor = None

# 1. Use type() to print the data type of stdCode, stdName and stdFinal.
stdCode = 34551001
stdName = 'Mohammed'
stdFinal = 98.5

print("type of stdCode is ", type(stdCode))
print("type of stdName is ", type(stdName))
print("type of stdFinal is ", type(stdFinal))

# 2. Print the data type of stdActive and stdAdvisor.
stdActive = True
stdAdvisor = None

print("type of stdActive is ", type(stdActive))
print("type of stdAdvisor is ", type(stdAdvisor))

# 3. Print the data type of stdCourses, stdBirthDate, stdProfile and stdSkills.
stdCourses = ['Python', 'Math', 'English']
stdBirthDate = (2001, 5, 14)
stdProfile = {'name': 'Mohammed', 'city': 'Alexandria'}
stdSkills = {'typing', 'Excel', 'typing'}

print("type of stdCourses is ", type(stdCourses))
print("type of stdBirthDate is ", type(stdBirthDate))
print("type of stdProfile is ", type(stdProfile))
print("type of stdSkills is ", type(stdSkills))

# 4. PREDICT: How many items will print(stdSkills) show? Why?   
#    My guess: 2 items (since sets in Python only store unique elements, the duplicate 'typing' will be removed)    
print(stdSkills)

# 5. Create a variable x = 5j and print its data type.  
x = 5j
print("type of x is ", type(x)) 

# 6. Create a variable r = range(5). Print its data type,
#    then print list(r) to see the numbers inside it.
r = range(5)
print("type of r is ", type(r))
print("list(r) is ", list(r))   

# 7. Convert stdMidterm to a float using float(). Print the new value and its type.
stdMidterm = 80
stdMidterm = float(stdMidterm)
print("new value of stdMidterm is ", stdMidterm)
print("type of stdMidterm is ", type(stdMidterm))   

# 8. PREDICT: What will print(int(stdFinal)) show? Does it round up?
#    My guess: 98 (it will truncate the decimal part, not round up) 
print("int(stdFinal) is ", int(stdFinal))   

# 9. Convert stdCode to a string and print how many characters it has using len().  
stdCode = 34551001
stdCode = str(stdCode)
print("stdCode as a string has ", len(stdCode), " characters")  


# 10. Create a frozenset from stdCourses and print its data type.
stdCourses = ['Python', 'Math', 'English']
frozen_courses = frozenset(stdCourses)
print("type of frozen_courses is ", type(frozen_courses))   

# 11. Create a variable msg = b"Hello" and print its data type.
msg = b"Hello"
print("type of msg is ", type(msg))

# 12. PREDICT the data type of each value below, then check with type():
#     10    10.0    "10"    [10]    (10,)    {10}    {'a': 10}    True
#     My guesses: Give all the diffrent types of each value
print("type of 10 is ", type(10))
print("type of 10.0 is ", type(10.0))
print("type of '10' is ", type("10"))
print("type of [10] is ", type([10]))
print("type of (10,) is ", type((10,)))
print("type of {10} is ", type({10}))
print("type of {'a': 10} is ", type({'a': 10}))
print("type of True is ", type(True))   

# 13. PREDICT: What is the data type of stdMidterm + stdFinal?
#     My guess: float (since stdMidterm is converted to a float and stdFinal is a float, their sum will be a float)
print("type of stdMidterm + stdFinal is ", type(stdMidterm + stdFinal)) 

# 14. PREDICT: What is the data type of stdMidterm / 2 ?  (Hint: 80 / 2 = 40 ... or is it?)
#     My guess: float (since division in Python always returns a float)
print("type of stdMidterm / 2 is ", type(stdMidterm / 2))      

 # 15. Fill in the blank so the output is <class 'tuple'>
#     print(type(_))                        
print(type((10,)))                        

# BONUS: Why does print(type((1))) show <class 'int'> and not <class 'tuple'>?
#        Answer in a comment.
#        Answer: Because a single value in parentheses is interpreted as an expression, not a tuple. To create a tuple with one element, you need to include a comma after the element: (1,).           
        