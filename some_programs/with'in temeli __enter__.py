class my_file_reader():
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

    # Additional methods implemented below

# artık bu yapıyı kullanabilirsin:
# with my_file_reader('dog_breeds.txt') as reader:
    Perform custom class operations
    # pass