# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action=user_action.strip()
    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos= functions.get_todos()

        todos.append(todo)

        # file = open('todos.txt','w')
        # file.writelines(todos)
        # file.close()
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos= functions.get_todos()

        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # new_todos=[item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5])
            number = number-1
            todos= functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Enter a valid command")
            continue

    elif user_action.startswith('complete'):
        try:

            todos= functions.get_todos()
            number = int(user_action[9])
            removed_todo = todos[number-1].strip('\n')
            todos.pop(number-1)

            functions.write_todos(todos)

            message = f"Todo number {number} i.e {removed_todo} was completed"
            print(message)
        except IndexError:
            print("NO item there")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid command")

