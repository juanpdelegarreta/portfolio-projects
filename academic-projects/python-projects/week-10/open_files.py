#I iterated through multiple nested for loops and while loops to try and strip the \n character, then thought that perhaps
#the strip method for strings would work, and it did!

with open('data.txt') as f:
    imported_nums = [int(line.strip()) for line in f.readlines()]
print(f.closed)
print(sum(imported_nums))
print(sum(imported_nums)/len(imported_nums))