number=int(input())

for i in range(number):
    space = (number-1) - 1 * i
    print(("1"*space)+("*"*((i+1)+(1*i))))
