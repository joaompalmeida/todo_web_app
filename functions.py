FILEPATH = 'data.txt'


def load_todo_data(data_file=FILEPATH):
    """Loads the persistent data file and returns a list.
    """
    with open(data_file, "r") as df:
        my_list = df.readlines()
    return my_list


def write_todo_data(item, data_file=FILEPATH):
    """Writes a new entry on the data file.
    """
    with open(data_file, "w") as wdf:
        wdf.writelines(item)


def add_todo(user_input, data_file=FILEPATH):
    # if user_input == 'add' or user_input == 'new':
    #     item = input("Add a todos: ").capitalize() + "\n"
    # else:
    #     item = user_input[4:].strip().capitalize() + "\n"
    # print("")

    my_list = load_todo_data(data_file)
    my_list.append(user_input + "\n")
    write_todo_data(my_list)


def show_list(data_file=FILEPATH):
    with open(data_file, "r") as rdf:
        for index, item in enumerate(rdf.readlines()):
            number = index + 1
            task = item.strip('\n')
            print(f"{number} - {task}")
        print("")


def edit_todo(data_file=FILEPATH):
    show_list(data_file)

    my_list = load_todo_data(data_file)

    valid_option = True
    while valid_option:
        item_to_edit = input("Which item do you want to edit? ")
        print("")
        try:
            number = int(item_to_edit)
        except ValueError:
            print("That is not a valid number.\n")
        else:
            if int(item_to_edit) > len(my_list):
                print("That is not a valid option. Input a valid number from the list.\n")
            else:
                new_todo = input(f"Edit todo number {number}: ").capitalize() + "\n"
                print("")
                my_list[number - 1] = new_todo
                print(f"New item\n"
                      f"{number} - {new_todo}\n")
                valid_option = False

    write_todo_data(my_list)


def complete_todo(input, data_file=FILEPATH):

    my_list = load_todo_data(data_file)
    my_list.pop(input)
    write_todo_data(my_list)

# def complete_todo(data_file=FILEPATH):
#     show_list(data_file)
#
#     my_list = load_todo_data(data_file)
#
#     valid_option = True
#     while valid_option:
#         item_to_edit = input("Which item do you want to complete? ")
#         try:
#             number = int(item_to_edit)
#         except ValueError:
#             print("That is not a valid number.\n")
#         else:
#             if int(item_to_edit) > len(my_list):
#                 print("That is not a valid option. Input a valid number from the list.\n")
#             else:
#                 task = my_list[number - 1].strip('\n')
#                 print(f"Item '{number} - {task}' completed.\n"
#                       f"Removing from list.\n")
#                 my_list.pop(number - 1)
#                 valid_option = False
#
#     write_todo_data(my_list)
