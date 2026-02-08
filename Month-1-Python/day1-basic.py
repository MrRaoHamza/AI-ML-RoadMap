#Task 1 => Check Positive/Negative/Zero

Number = int(input("Enter a number:"))

if Number > 0:
    print("The Number is Positive.")
elif Number < 0:
    print("The Number is Negative.")
else:
    print("The Number is Zero.")


#Task 2 => Print table of a number

Number = int(input("Enter a number:"))
print("Table of", Number, "is:")

for i in range(1, 11):
    print(Number, "x", i, "=", Number * i)

#Task 3 => Find the largest of three numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    print("The largest number is:", num1)
elif num2 > num1 and num2 > num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)
