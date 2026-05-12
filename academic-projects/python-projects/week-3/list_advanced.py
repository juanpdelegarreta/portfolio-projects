sports = ["Baseball","Soccer","Basketball","Football","Wrestling","Golf","Bowling","Boxing"]
print(sports)
print(len(sports))
print(sports[0:3])
print(sports[::2])
print(sports[3:])
more_sports = sports.copy()
more_sports.insert(1, "Cricket")
more_sports.append("Volleyball")
more_sports.insert(4, "Tennis")
del sports[3]
del sports[-1]
print(sports)
print(more_sports)