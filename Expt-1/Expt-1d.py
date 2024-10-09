# Write a function that takes a dictionary where keys are student names and
# values are their scores. The function should return list of student names who have highest score.
# if multiple students have highest scores reurn all names

student_scores = {"Muskan": 88, "tur tur":75, "Moin":88, "Alice": 93, "Eve":93, "Akay":93}
highest_score = max(student_scores.values())
toppers = [name for name, score in student_scores.items() if score == highest_score]
print("By Rafat Muskan!!!")
print('Students with highest score:')
print(f'Highest Score : {highest_score}')
print(f'Student Names : {toppers}')
