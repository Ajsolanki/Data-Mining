def test():

    n = input("enter the unit of electricity: ")
    cost = 0
    if n<=100:
        cost = cost + n*5
        print(cost)
    elif (n>100 and n<=200):
        cost = cost + 100*5 + (n-100)*10
        print(cost)
    elif n>200:
            cost = cost + 100*5 + 100*10 + (n-200)*15
            print(cost)
    else:
        print("Enter the correct value")

            
test()