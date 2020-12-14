import os, shutil


class File_Manger:
    def extract_files(self, path):
        if not os.path.isdir(path):
            print("Invalid Path Try again!")
            return False
        for (path, dirs, files) in os.walk(path):
            for file in files:
                if '.' in file:
                    extension = file.split('.')[1]
                    print(extension)


if __name__ == '__main__':
    FM = File_Manger()
    directory = input("Enter your path: ")
    FM.extract_files(directory)
