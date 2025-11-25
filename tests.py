from functions.run_python_file import run_python_file


def test():
    result = run_python_file("calculator", "main.py")
    print("Result of trying to run main.py:")
    print(result)
    print("")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result of trying to run main.py 3 + 5:")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print("Result of trying to run tests.py:")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print("Result of trying to run ../main.py:")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print("Result of trying to run nonexistent.py:")
    print(result)

    result = run_python_file("calculator", "lorem.txt")
    print("Result of trying to run lorem.txt:")
    print(result)




if __name__ == "__main__":
    test()