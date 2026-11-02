class FileManager:

    def create_file(self, fname):
        with open(fname, "w") as file:
            pass
        print("File Created Successfully!")

    def write_file(self, fname):
        data = input("Enter Data: ")

        with open(fname, "a") as file:
            file.write(data + "\n")

        print("Data Written Successfully!")

    def read_file(self, fname):
        try:
            with open(fname, "r") as file:
                print("\nFile Contents:")
                print(file.read())

        except FileNotFoundError:
            print("File Not Found!")

    def search_file(self, fname):
        word = input("Enter Word to Search: ")

        try:
            found = False

            with open(fname, "r") as file:
                for line in file:
                    if word.lower() in line.lower():
                        print("Found:", line.strip())
                        found = True

            if not found:
                print("Word Not Found!")

        except FileNotFoundError:
            print("File Not Found!")

    def update_file(self, fname):
        old = input("Enter Old Word: ")
        new = input("Enter New Word: ")

        try:
            with open(fname, "r") as file:
                data = file.read()

            data = data.replace(old, new)

            with open(fname, "w") as file:
                file.write(data)

            print("Updated Successfully!")

        except FileNotFoundError:
            print("File Not Found!")

    def delete_file(self, fname):
        word = input("Enter Word to Delete: ")

        try:
            with open(fname, "r") as file:
                data = file.read()

            data = data.replace(word, "")

            with open(fname, "w") as file:
                file.write(data)

            print("Deleted Successfully!")

        except FileNotFoundError:
            print("File Not Found!")


obj = FileManager()

while True:
    print("\n===== FILE MANAGEMENT SYSTEM =====")
    print("1. Create File")
    print("2. Write Data")
    print("3. Read Data")
    print("4. Search Data")
    print("5. Update Data")
    print("6. Delete Data")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        fname = input("Enter File Name: ")
        obj.create_file(fname)

    elif choice == "2":
        fname = input("Enter File Name: ")
        obj.write_file(fname)

    elif choice == "3":
        fname = input("Enter File Name: ")
        obj.read_file(fname)

    elif choice == "4":
        fname = input("Enter File Name: ")
        obj.search_file(fname)

    elif choice == "5":
        fname = input("Enter File Name: ")
        obj.update_file(fname)

    elif choice == "6":
        fname = input("Enter File Name: ")
        obj.delete_file(fname)

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")