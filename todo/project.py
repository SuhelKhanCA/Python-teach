"""
This is basic TODO list CLI based project. With the help of this s/w, you can
add, delete and mark complete/incomplete your todos. Go enjoy!!
"""

# create
def create_todo():
    todo = input("Enter a todo: ")  # todo = "create yt videos"
   
    # todo = "create yt videos(Incomplete)"
    todo = todo + "(Incomplete)"
    # save in file
    with open("todo.txt", 'a') as f:
        f.write("\n" + todo)

    print(todo)

# read

def read_todos():
    with open("todo.txt", "r") as f:
        todos = f.read()
    print(todos)

# update

def update_todo():
    
    with open("todo.txt", "r") as f:
        todo_list = f.readlines()

    for i in range(0, len(todo_list)):

        print(f"{i}. {todo_list[i]}")    
    
    pos = int(input("Enter a todo list number to update:"))

    todo = todo_list[pos]
    todo = todo.replace("Incomplete", "Complete")
    todo_list[pos] = todo

    for i in range(0, len(todo_list)):

        print(f"{i}. {todo_list[i]}") 

    with open("todo.txt", "w") as f1:
        f1.writelines(todo_list)

# delete

def delete_todo():

    with open("todo.txt", "r") as f:
        todo_list = f.readlines()

    for i in range(0, len(todo_list)):

        print(f"{i}. {todo_list[i]}")    
    
    pos = int(input("Enter a todo list number to delete:"))

    todo_list.remove(todo_list[pos])

    for i in range(0, len(todo_list)):

        print(f"{i}. {todo_list[i]}") 

    with open("todo.txt", "w") as f1:
        f1.writelines(todo_list)


# main
def main():

    try:
        while True:
            cmd = input("Enter commmand: ")
            if cmd == "add":
                create_todo()

            if cmd == "read":
                read_todos()

            if cmd == "update":
                update_todo()

            if cmd == "delete":
                delete_todo()


            if cmd == "exit":
                break
    except Exception as e:

        print(str(e))

# __main__ # dunder
if __name__ == "__main__":
    main()