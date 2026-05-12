def add_things(item_1, item_2):
    new_value = item_1 + item_2
    return new_value

def sub_things(item_1, item_2):
    return (item_1 - item_2)


def main():

    first_value = 5
    second_value = 2

    print(add_things(first_value, second_value))
    print(sub_things(first_value, second_value))

if __name__ == "__main__":
    main()