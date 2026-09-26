money=int(input("enter the amount of the money you have: "))
if money >= 100:
    print("You can buy a new phone.")
elif money >= 50:
    print("You can buy a used phone.")
elif money >= 20:
    print("You can buy a new book.")
else:
    print("You cannot buy anything.")
