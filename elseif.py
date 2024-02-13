marks=int(input("Enter marks:"))

if marks>=80 and marks<=100:
    print("You have an A")
elif marks>=60 and marks<=79:
    print("You have a B")
elif marks>=40 and marks<=59:
    print("You have a C")
elif marks>=0 and marks<=39:
    print("You have terribly failed")
else:
    print("Wrong Input")