x = 7

for x in range(1,12):
    if x < 10:
        print("That makes sense")
        x = x + 1
        print("new value of x is " + str(x) + ".")
    else:
        print("This should not have happened")

print("Final value of x is %d") % (x)
print(type(x))