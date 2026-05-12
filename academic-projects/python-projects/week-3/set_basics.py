numbers = [1,6,3,7,5,4,6,2,1,8,5,5,3,4,2,6,1,4,3,2]
print("The length of list numbers is "+ str(len(numbers)))
count = 0
for x in range(len(numbers)):
    if(numbers[x]==1):
        count = count + 1
print("The count of 1's is " + str(count))

second_count = 0 
for x in range(len(numbers)):
    if(numbers[x]==5):
        second_count = second_count + 1
print("The count of 5's is " + str(count))
numbers.sort()
print(f"The max value is " + str(numbers[-1]))
print(f"The min value is " + str(numbers[0]))

set_a = set(numbers)
print("The length of set_a is " + str(len(set_a)))
set_b = {1,3,5,8,12,16,45}
print("union: " + str(set_a | set_b))
print("intersection: " + str(set_a & set_b))
print("difference: " + str(set_a - set_b))
print("symmetric difference: " + str(set_a ^ set_b))
