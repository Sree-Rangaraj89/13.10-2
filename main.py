def recur_factorial(n):
    if n ==1:
        return n
    else :
        return n*recur_factorial(n-1)
    
num = int(input("ENTER A NUMBER"))

if num < 0:
    print("SORRY, FOATORIAL DOES NOT EXISIT FOR NEGATIVE NUMBER")
elif num == 0:
    print("THE FACTORIAL OF 0 IS 1")
else:
    print("THE FACTORIAL OF", num, "is", recur_factorial(num))