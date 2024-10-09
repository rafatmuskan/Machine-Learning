#Write a function that takes a list of tuples, where each tuple contains a student's name and their score. The function should return a list of tuples sorted in descending order of scores. If two students have the same score, they should be sorted alphabetically by their names.
#Given: students = [("Moin ",88), ("Muskiii", 75), ("Sakhiii", 88), ("Sammy",93), ("Tur Tur", 75) ]
#Expected Output: Sorted students: [(“Sammy”, 93), (“Pollard”, 88), (“Moin”, 88), (“Hardik”, 75), (“Virat”, 75)]
#Function to sort a list of tuples by score in descending order, and by name alphabetically if scores are the same
def sorted_students_by_score_(students):
    # Sort the list of tuples using sorted()
    sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
    return sorted_students
students = [ 
    ("Moin",88),
    ("Muskiii", 75),
    ("Sakhiii", 88),
    ("Sammy", 93),
    ("Tur Tur", 75),
]
#Sorting the list of students
sorted_students = sorted_students_by_score_(students)
print("By Rafat Muskan!!!")
print("Students:", students)
print("Sorted Students:", sorted_students)
