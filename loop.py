
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("\nPrime numbers between", start, "and", end, "are:")

for num in range(max(2, start), end + 1):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

print()
