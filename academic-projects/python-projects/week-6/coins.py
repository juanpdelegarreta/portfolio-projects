def count_money(**kwargs):
    global purse
    #A for loop to iterate through all of the kwargs
    for x in kwargs:
        #This holder is assigned the value in each key/value pair
        holder = kwargs[x]
        #The if/elif loops check to see if the key matches one of the purse dictionary keys
        if x == "penny":
            #If the keys match, the corresponding value in the purse dictionary is increased by the argument's key 
            purse["penny"] += holder
        elif x == "nickel":
            purse["nickel"] += holder
        elif x == "dime":
            purse["dime"] += holder
        elif x == "quarter":
            purse["quarter"] += holder
        elif x == "half_dollar":
            purse["half_dollar"] += holder
        elif x == "dollar":
            purse["dollar"] += holder
        else:
            print(f"Sorry, we do not accept {x}, we only accept {list(purse.keys())}") 

def printer(dictionary):
    #this function takes a dictionary as a parameter and prints it. It also returns the sum of all the values in the dictionary
    print(list(dictionary.items()))
    sum_coin = sum(dictionary.values())
    return sum_coin


purse = {"penny":0, "nickel":0, "dime":0, "quarter":0, "half_dollar":0, "dollar":0}

count_money(penny=3, quarter=5)
count_money(penny=5, quarter=6, half_dollar=2, dollar=10)
count_money(nickel=8, three_dollar=2)
count_money(dime=17, quarter=2, nickel=3, penny=30, half_cent=9)
count_money(dollar=27, dime=10, quarter_cent=9)

#To store the return value, the variable total_coins is assigned the function with the purse dictionary as an argument
total_coins = printer(purse)
print(f"You currently have {total_coins} coins!")