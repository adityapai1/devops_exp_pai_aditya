import os

def thala_check(string):
    if len(string) % 7 == 0:
        return "Thala for a reason"
    else:
        return "Thala for no reason"

if __name__ == "__main__":
    user_input = os.environ.get('THALA_INPUT', '')
    print(f"Input: {user_input}")
    print(f"Result: {thala_check(user_input)}")
    
    