list_a = [160, 38, 97, 136, 53, 103, 194, 113, 180, 130, 154, 126, 162, 76, 93, 76, 154, 95, 162, 76, 55, 113, 144, 173, 124, 47, 148, 163, 74, 66, 14, 19, 81, 58, 151, 59, 10, 114, 96, 11, 143, 85, 103, 31, 91, 177, 83, 149, 47, 197]
list_b = [76, 67, 69, 120, 191, 12, 45, 112, 48, 11, 81, 144, 117, 141, 68, 10, 47, 30, 32, 107, 79, 166, 62, 2, 70, 22, 130, 192, 168, 115, 62, 53, 182, 56, 142, 64, 194, 162, 106, 186, 196, 123, 185, 106, 144, 12, 31, 71, 187, 110]
list_c = [184, 86, 65, 72, 84, 125, 122, 100, 107, 27, 47, 29, 1, 92, 35, 81, 163, 94, 84, 187, 87, 22, 147, 50, 77, 121, 135, 142, 111, 165, 92, 103, 38, 107, 116, 15, 132, 114, 181, 122, 120, 122, 198, 129, 121, 70, 144, 96, 15, 112]
stats = {"list_a":{"unsorted_list":list_a}, "list_b":{"unsorted_list":list_b}, "list_c":{"unsorted_list":list_c}}

def sorted_list(list):
    list_sort = sorted(list)
    list_min = min(list)
    list_max = max(list)
    list_mean = sum(list)/len(list)
    return list_sort, list_mean, list_max, list_min

#The way that made the most sense to me to get the returned values was to put them into a list instead of making 4 variables
values = list(sorted_list(list_a))
stats["list_a"]["sorted_list"] = values[0]
stats["list_a"]["mean"] = values[1]
stats["list_a"]["max"] = values[2]
stats["list_a"]["min"] = values[3]

values = list(sorted_list(list_b))
stats["list_b"]["sorted_list"] = values[0]
stats["list_b"]["mean"] = values[1]
stats["list_b"]["max"] = values[2]
stats["list_b"]["min"] = values[3]

values = list(sorted_list(list_c))
stats["list_c"]["sorted_list"] = values[0]
stats["list_c"]["mean"] = values[1]
stats["list_c"]["max"] = values[2]
stats["list_c"]["min"] = values[3]

#Simplicity for me was the name of the game with this nested loop:
for x in stats.keys():
    print(f"key: {x}")
    for y in stats[x].keys():
        print(f"{y}: " + str(stats[x][y]))
    print("\n")