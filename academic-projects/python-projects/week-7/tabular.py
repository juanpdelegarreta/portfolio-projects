from tabulate import tabulate

students = [
    ["Bob", 47, 35, 28, 18, 33, 42, 43, 17, 15, 50, 186],
    ["Trisha", 32, 33, 50, 22, 29, 43, 26, 24, 12, 16, 182],
    ["Sally", 26, 24, 34, 16, 23, 94, 21, 34, 12, 12, 163],
    ["Leo", 25, 23, 28, 26, 40, 63, 47, 24, 26, 36, 55],
    ["Fred", 28, 14, 41, 30, 43, 84, 26, 40, 40, 20, 143],
    ["Paul", 29, 36, 22, 14, 21, 57, 20, 11, 34, 44, 67],
    ["Katie", 47, 24, 39, 25, 30, 84, 29, 43, 39, 38, 186],
    ["Jacklyn", 47, 31, 10, 38, 39, 44, 45, 13, 21, 47, 68],
    ["Alfred", 11, 39, 15, 11, 25, 80, 19, 36, 49, 33, 76]
]

#I wonder if there's a way to make this loop more dynamic and less reliant on my knowing how many elements are in the list
for x in range(0,9):
    points = 0
    for y in range(1,12):
        points += students[x][y]
    grade = (points/600)*100
    students[x].append(grade)

#According to the lab, we were supposed to have 14 columns: the Student name, 10 labs, 1 midterm, 1 final, and the overall grade.
#However, we only had data for 11 total assignments, which means that there was either less than 10 labs or no midterm.
#My chart assumes that column 7 was the midterm and I removed 'lab 10' so the headers would align with the data.
print(tabulate(students, 
                headers=["Student","Lab 1","Lab 2","Lab 3","Lab 4","Lab 5","Midterm", 
                            "Lab 6","Lab 7","Lab 8","Lab 9","Final","Overall"], 
                tablefmt="fancy_grid")
    )
#I'll have to double check the proper etiquette for multi-line print statements like this one, but I wanted it to be more legible.