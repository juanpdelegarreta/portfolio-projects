def welcome_message(first_name,age):
    print(f"Welcome to Cincinnati State, {first_name}! Let me tell you how lucky you are.")
    if age <= 18:
        print("You are super lucky!")
    elif age <=35:
        print("You are pretty darn lucky!")
    elif age <=65:
        print("You are overflowing with luck!")
    else:
        print("You are the most lucky!")
    #First we create the lucky_numbers list of integers:
    lucky_numbers = [int(i) for i in str(len(first_name)*age)]
    #Then we eliminate duplicates by making it a set and turning it back to a list
    lucky_numbers = list(set(lucky_numbers))
    print(f"{first_name}, your lucky numbers are: {lucky_numbers}") 
    #Finally, we return the following, adding the integers lucky_numbers to the all_lucky_nums list
    return all_lucky_nums.extend(lucky_numbers)

all_lucky_nums = []
welcome_message("Sally", 17)
welcome_message("Lacey", 39)
welcome_message("Billy", 9)
welcome_message("Frank", 73)
welcome_message("George", 53)

#Like before, we will make the list a set and then back to a list to make sure we eliminate the duplicates
all_lucky_nums = list(set(all_lucky_nums))

print("The number of lucky numbers is " + str(len(all_lucky_nums)) + " and they are:")
print(all_lucky_nums)