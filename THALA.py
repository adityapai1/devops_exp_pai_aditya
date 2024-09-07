def thala_check(string):
    if len(string) % 7 == 0:
        print("Thala for a reason")
    else:
        print("Thala for no reason")

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    thala_check(user_input)
