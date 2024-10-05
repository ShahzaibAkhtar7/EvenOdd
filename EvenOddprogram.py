# Python program to check if a number is even or odd

def check_even_odd(number):
    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break  # Exit the loop

    try:
        number = int(user_input)  
        check_even_odd(number)    
    except ValueError:
        print("Please enter a valid number or 'exit' to quit.")
