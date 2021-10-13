MENU = "1. Print the list\n" \
       "2. Append into position\n" \
       "3. Delete the last element\n" \
       "4. Make tuple of even indexes of the list and print it\n" \
       "5. Print sum of the real elements of the list\n" \
       "6. Print the count of the words of the list, converted to string\n" \
       "7. Print the distraction between sets\n" \
       "8. Make the dictionary of the list with key = index and print all the elements with the key > 3\n" \
       "Q - quit\n" \
       ">>>"


def list_to_tuple(own_list):
    list_copy = list(own_list).copy()

    difference = 0

    for i in range(0, len(list_copy) - 1):
        if i % 2 != 0:
            del (list_copy[i - difference])
            difference += 1

    return tuple(list_copy)


def real_values_sum(own_list):
    sum = 0

    for i in list(own_list):
        try:
            sum += float(i)
        except Exception:
            continue

    return sum


def count_words_in_list_starting_with(letter, own_list):
    count = 0

    string = ""

    for i in list(own_list):
        string += str(i) + " "

    for i in range(len(string)):

        if string[i] == letter and (i == 0 or string[i - 1] == " "):
            count += 1

    return count


def input_new_set_and_return_distraction(own_list):
    own_set = set()

    choice = input("Enter the element to add, enter \\q to quit\n>")

    while choice != "\\q":
        own_set.add(choice)
        choice = input("Enter the element to add, enter \\q to quit\n>")

    return set(own_list) - own_set


def list_to_dictionary(own_list):
    # we're making a new list with the indexes of the previous one

    indexes = []

    for i in range(0, len(own_list)):
        indexes.append(i)

    return dict(zip(indexes, own_list))


def print_dict_with_keys_gt3(own_dict):
    for k, v in dict(own_dict).items():
        if k > 3:
            print(k, ":", v, "\n")


if __name__ == '__main__':

    a = []

    while True:
        try:
            choice = input(MENU)
            if choice == '1':
                print(a)
            elif choice == '2':
                a.append(input("Enter new element to append\n>"))
            elif choice == '3':
                a.remove(a[len(a) - 1])
            elif choice == '4':
                print(list_to_tuple(a))
            elif choice == '5':
                print(real_values_sum(a))
            elif choice == '6':
                print(count_words_in_list_starting_with(input("Enter the letter to count\n>"), a))
            elif choice == '7':
                print(input_new_set_and_return_distraction(a))
            elif choice == '8':
                print_dict_with_keys_gt3(list_to_dictionary(a))
            elif choice.lower() == 'q':
                exit(0)

        except Exception as e:
            print(e.args[0])
