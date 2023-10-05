def decimal_to_binary(decimal):
    binary = ""

    if decimal == 0:
        binary = "0"
    else:
        while decimal > 0:
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal = decimal // 2

    return binary


print("Hello, this program converts a decimal number to binary.")
decimal_number = int(input("Enter a decimal number: "))

binary_representation = decimal_to_binary(decimal_number)
print(
    f"The binary representation of {decimal_number} is: {binary_representation}")
