s1 = "hello123world45"

digits = []

for char in s1:
    if char.isdigit():
        digits.append(int(char))

sum_digits = sum(digits)

average = sum_digits / len(digits)

print("Digits:", digits)
print("Sum:", sum_digits)
print("Average:", average)