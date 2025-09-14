from functions import get_files_info as functions  # importe ta fonction

def run_tests():
    print(functions.get_files_info("calculator", "."))
    print()
    print(functions.get_files_info("calculator", "pkg"))
    print()
    print(functions.get_files_info("calculator", "/bin"))
    print()
    print(functions.get_files_info("calculator", "../"))

if __name__ == "__main__":
    run_tests()
