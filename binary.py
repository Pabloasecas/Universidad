
def pass_to_binary():
    global n
    binary = ""
    b = n % 2
    n = int(n / 2)
    binary = str(b) + binary
    if n == 0:
        print("The binary number is " + binary)
    else:
        while n > 0:
            binary = ""
            b = n % 2
            n = int(n // 2)
            binary = str(b) + binary
    return binary


print("Hello, the next code is maded to pass any decimal number to binary")
n = int(input("Enter any decimal number "))
pass_to_binary()
print(binary)