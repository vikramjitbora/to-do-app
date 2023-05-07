FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return a list of to do items
    """
    with open(filepath, 'r') as file:
        return file.readlines()


def write_todos(todo_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)
