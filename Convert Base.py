def decimal_to_binary(n):
    return bin(n)[2:]

def decimal_to_octal(n):
    return oct(n)[2:]

def decimal_to_hexadecimal(n):
    return hex(n)[2:]

while True:
    print("")
    print("Number Conversion Menu:")
    print("1. Convert to binary (Base 2)")
    print("2. Convert to octal (Base 8)")
    print("3. Convert to decimal (Base 10)")
    print("4. Convert to hexadecimal (Base 16)")
    print("5. Exit")

    print("")
    choice = input("Enter your choice: ")

    if choice == "5":
        print("")
        print("Exiting the program...")
        print("")
        break

    try:
        print("")
        num = int(input("Enter the number to convert: "))
    except ValueError:
        print("")
        print("Invalid input. Please enter a valid number.")
        continue

    if choice == "1":
        result = decimal_to_binary(num)
        print("")
        print(f"The binary conversion of {num} is: {result}")
    elif choice == "2":
        result = decimal_to_octal(num)
        print("")
        print(f"The octal conversion of {num} is: {result}")
    elif choice == "3":
        print("")
        print(f"The decimal form of {num} is: {num}")
    elif choice == "4":
        result = decimal_to_hexadecimal(num)
        print("")
        print(f"The hexadecimal conversion of {num} is: {result}")
    else:
        print("")
        print("Invalid choice. Please enter a valid option.")