def decimal_to_base(number, base):
    if number == 0:
        return '0'
    
    digits = "0123456789ABCDEF"
    result = ''
    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number //= base
    return result

def base_to_decimal(number, base):
    digits = "0123456789ABCDEF"
    result = 0
    power = 0
    for digit in reversed(number):
        result += digits.index(digit) * (base ** power)
        power += 1
    return result

def convert_between_bases(number, source_base, target_base):
    if source_base == 10:
        return decimal_to_base(int(number), target_base)
    else:
        decimal_number = base_to_decimal(number, source_base)
        return decimal_to_base(decimal_number, target_base)

def main():
    while True:
        print("\nBase Converter")
        print("Select bases:")
        print("1. Binary (2)")
        print("2. Octal (8)")
        print("3. Decimal (10)")
        print("4. Hexadecimal (16)")
        print("5. Exit")

        source_base = int(input("\nEnter source base (1-4), Exit (5): "))
        if source_base == 5:
            print("Exiting the program.")
            break

        target_base = int(input("\nEnter target base (1-4): "))
        number = input("\nEnter the number in the source base: ")

        if source_base == 1:
            source_base = 2
        elif source_base == 2:
            source_base = 8
        elif source_base == 3:
            source_base = 10
        elif source_base == 4:
            source_base = 16

        if target_base == 1:
            target_base = 2
        elif target_base == 2:
            target_base = 8
        elif target_base == 3:
            target_base = 10
        elif target_base == 4:
            target_base = 16

        converted_number = convert_between_bases(number, source_base, target_base)
        print(f"Converted number: {converted_number}")

if __name__ == "__main__":
    main()
