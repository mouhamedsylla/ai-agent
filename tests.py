from functions import get_files_info as functions  # importe ta fonction

# def run_tests():
#     print(functions.get_files_info("calculator", "."))
#     print()
#     print(functions.get_files_info("calculator", "pkg"))
#     print()
#     print(functions.get_files_info("calculator", "/bin"))
#     print()
#     print(functions.get_files_info("calculator", "../"))


# def run_tests():
#     print(functions.get_file_content("calculator", "main.py"))
#     print()
#     print(functions.get_file_content("calculator", "pkg/calculator.py"))
#     print()
#     print(functions.get_file_content("calculator", "/bin/cat"))
#     print()
#     print(functions.get_file_content("calculator", "pkg/does_not_exist.py"))


def run_tests():
    print(functions.write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print()
    print(functions.write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print()
    print(functions.write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

if __name__ == "__main__":
    run_tests()
