# Create a dictionary with the key as a student name and the value as a grade of a course.
# Your dict should have at least 3 pairs of key-value.
student_grade = {'Andrea': 25, 'Chiara': 29.5, 'Paolo': 10}

# Choose one of the student, modify their grade.
student_grade['Paolo'] = 30
print(student_grade)

# Add a new pair of name-grade to the dictionary.
student_grade['Zoro'] = 28
print(student_grade)

# Remove a pair of name-grade from the dictionary.
del student_grade['Chiara']
print(student_grade)

# Print all the names of students.
print(student_grade.keys())

# What if for each student, we have a collection of 3 grades, instead of 1 grade? -> Use list to store grades
# Create a new dictionary that for each student there are 3 grades corresponding.
# Use the sum() function to print the total grade for each student.
student_grade_multi = {'Andrea': [25, 30, 1],
                       'Chiara': [29.5, 23, 14],
                       'Paolo': [10, 20, 31]}
print(sum(student_grade_multi['Andrea']), sum(student_grade_multi['Chiara']), sum(student_grade_multi['Paolo']))

