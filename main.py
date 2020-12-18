import os
import shutil


def path_exist(path):
    return os.path.exists(path) is True


def check_dir(di):
    if os.path.isdir(di) is False:
        return False
    else:
        return True


class FileManager:
    def __init__(self):
        self.root = ""
        self.no_files = 0
        self.destination_dir = ""

    def menu(self):
        pass

    def prep_new_dir(self, new_dir):
        parent = self.root.split('/')
        parent.pop(-1)
        created_root = '/'.join(parent) + '/'
        created_root += new_dir
        self.destination_dir = created_root
        return created_root

    def create_dir(self, new_dir):
        if path_exist(new_dir) is True:
            return False
        else:
            os.mkdir(new_dir)
            return True

    def init_root(self, root):
        if check_dir(root):
            print("Path added successfully!")
            self.root = root
            self.no_files = 0
            return True
        else:
            print("Invalid Path Try again!")
            return False

    def organize_by_extensions(self, new_dir):
        # Prepare a destination directory path
        self.prep_new_dir(new_dir)

        # Create a destination directory
        if (self.create_dir(self.destination_dir)) is False:  # if the destination is already exists
            print(f"[OK] Destination file founded successfully at {self.destination_dir} ..")
        else:
            print(f"[OK] {new_dir} is created successfully at {self.destination_dir} ..")

        # Move all files from root folder with a certain (ext) to our new root folder under a folder named -> ("ext") #
        for (path, dirs, files) in os.walk(self.root):
            for file in files:
                if '.' in file:
                    extension = file.split('.')[-1]
                    destination = os.path.join(self.destination_dir, extension)
                    source = os.path.join(path, file)

                    # Make a new Directory if it's not exist
                    if (self.create_dir(destination)) is True:
                        print(f"[OK] Successfully created the directory {destination} ..")

                    # if the file is already in destination
                    if path_exist(destination + '/' + file):
                        print(f'[Skipped] File : {file} , is in a suitable place ..')
                    else:
                        shutil.move(source, destination)
                        self.no_files += 1
                        print(f"[OK] File {source} Moved to {destination} successfully ..")

        print(f"[Done] {self.no_files} File successfully sorted by extension in Folder named {new_dir},"
              f"which located at {self.destination_dir} ..")


if __name__ == '__main__':
    FM = FileManager()
    cont, valid_path = True, False
    while cont is True:
        valid_path = False
        while valid_path is False:
            directory = input("Enter your path:")
            valid_path = FM.init_root(directory)
        new_root = input("Enter new 'Directory' name: ")
        FM.organize_by_extensions(new_root)
        cont = False if input("[Q] Do you want to try again (Y/N) ? :") in 'nN' else True
