
num = int(input("Enter a number: "))

print("\nMultiplication Table of", num)
print("-------------------------")

for i in range(1, 11):
    if i >= 1:
        print(f"{num} x {i} = {num * i}")
