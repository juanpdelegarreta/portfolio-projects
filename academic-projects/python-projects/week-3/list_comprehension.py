numbers = [x for x in range (1,101)]
print(numbers)
str_to_list = [x for x in ("scripting")]
print(str_to_list)
threes_power = [3**x for x in range (1,11)]
print(threes_power)
new_yorker_23_books = ["the bee sting","biography of x","birnam wood","the country of the blind","a day in the life of abed salama","fear is just a word"]
book_titles = [x.title() for x in new_yorker_23_books]
print(book_titles)