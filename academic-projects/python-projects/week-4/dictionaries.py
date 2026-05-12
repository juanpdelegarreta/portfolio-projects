person = {"name":"Juan Pablo de Legarreta",
          "age":31,
          "city":"Cincinnati",
          "hobbies":["board games","movies","video games","puzzles","playing music","programming"], 
          "pets":{"dogs":["millie","linda"],"cats":["squirt","smudge","tuxedo"],"fish":["buddy","nemo"]}, 
          "placeholder":""
          }
#Question 1 - I decided to insert a blank line between the different prompts for readability. Cheers!
print(person)
print("\n")
print(person.items())
print("\n")
print(person.keys())
print(person.values())
print("\n")
print(person["hobbies"])
print(person.get("name"))
print(person.get("family","no family recorded yet"))
print("\n")

#Question 2
print(type(person))
print(type(person.get("hobbies")))
print("\n")
person.get("hobbies").append("painting")
#Hey, can I just say how stinkin' neat THIS ^^^ was?? Combining the get method with the lists' append method?? VERY COOL!
person.update({"dream job":"SOC Operations Manager"})
person["age"] = 32
person["fake data"] = {"foo":"bar"}
person["fake data"].pop("foo")
person.popitem()
#Since the popitem method deletes on a 'last in, first out' basis, it will be deleting the "fake data" key,
#which is convenient since it doesn't have an associated value
del person["placeholder"]

#Question 3
people = {"person1":dict(person),"person2":dict(person),"person3":dict(person)}
print(people.get("person1").get("name"))
print(people.get("person2").get("hobbies"))
print((people.get("person2").get("pets").get("dogs"))[0])
#Adding an extra set of parentheses was was finally made this work. Interesting how that worked while .get("dogs"[0]) returned "None"
people.get("person3").get("hobbies").append("woodworking")
people.get("person2").update({"city":"Rivendell"})
#Love the LOTR reference here!
del people["person3"]["pets"]
print(people.get("person2").keys())
print(sorted(people.get("person1").keys()))
print(sorted(people.get("person1").keys(),reverse=True))













