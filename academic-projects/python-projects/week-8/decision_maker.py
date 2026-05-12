import random
things = {
        "get_dinner":["Maggiano's","Quatman Cafe","El Rancho Grande","Blue Ash Chili","Copper Blue","Little Miami Brewing Company"], 
        "go_out":["walk in the park","bowling","thrifting","antiquing","go to an FC Cincinnati match","go to a concert","watch a musical"],
        "stay_in":["watch Avatar: The Last Airbender","play Animal Crossing","play a board game","craft a seasonal decoration","marathon the Lord of the Rings"]
        }

user_input = ""

while True:
    print("What would you like to do tonight(get dinner, go out, stay in, or 'quit' to exit):\n")
    
    user_input = input().lower()
    
    if user_input in ["get dinner", "go out", "stay in", "quit"]:
        if user_input == "get dinner":
            options = things["get_dinner"]
            activity = random.choice(options)
            print(f"\nMay I suggest the following restaurant: {activity}\n")
        elif user_input == "go out":
            options = things["go_out"]
            activity = random.choice(options)
            print(f"\nMay I suggest the following activity: {activity}\n")
        elif user_input == "stay in":
            options = things["stay_in"]
            activity = random.choice(options)
            print(f"\nMay I suggest the following activity: {activity}\n")
        elif user_input == "quit":
            break
    else:
        print("\nInvalid input. Please select one of the following: get dinner, go out, stay in, quit.\n")
print("\nHope you have fun tonight!\n")