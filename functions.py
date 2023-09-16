file_path = r'C:\Projects\TodoList_app\todos.txt'


def get_todos(file_path=file_path):
    with open(file_path, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(arg, file_path):
    with open(file_path, 'w') as file:
        file.writelines(arg)
    return file


def greetings():
    print('Hello')


if __name__ == "__main__":
    greetings()

