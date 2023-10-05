# A
# Take a look at the example:
record = ('Nhut', 'IntroPython', 30)
student_name, course_name, grade = record
print(student_name, course_name, grade)

# Now add a new element: the ID of student, to get a tuple like this
# ('ID', 'Name', 'Course', 'Grade')
record = list(record)
record.insert(0, '12345') # add ID
record = tuple(record)

# You cannot modify a tuple, but there are a few ways to accomplish the requirement. -> convert it into mutable list
# If you cannot figure out, just create a new tuple with 4 elements

# Then unpack the new tuple above into 4 variables
student_id, student_name, course_name, grade = record
print(student_id, student_name, course_name, grade)

################################################

# B
tuple_1 = (1, 2, 3, 4)
tuple_2 = ([1, 2], [3, 4])
tuple_3 = ((1, 2), (3, 4))
print(len(tuple_1), len(tuple_2), len(tuple_3)) # 4 2 2, a nested element is counted as 1 element only

tuple_1[0] = 1 # TypeError: 'tuple' object does not support item assignment
tuple_2[0][0] = 1 # yes it can modify the first list
tuple_3[0][0] = 1 # TypeError: 'tuple' object does not support item assignment
# Tuple does not contain the actual values, it contains the
# references (e.g. what cell in the computer memory) to objects.
# See more at https://stackoverflow.com/questions/9755990/why-can-tuples-contain-mutable-items
