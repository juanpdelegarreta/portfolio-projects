import random
names = ["Adam","Beverly","Carol","Dino","Edward","Fred","George","Hector","Isabel","Jimmy"]
customers = 0

for x in names:
    print(x)
    done = False
    while done != True:
        ready = 0
        ready = random.randrange(1,7)
        print(ready)
        if ready == 1 or ready == 5:
            done = True
        elif ready == 6:
            break
        else:
            continue
    print(f"Thank you {x} for coming, hope to see you again soon!")
print(f"Today has been a long day. We served {len(names)} guests. Hopefully tomorrow is just as busy!")
