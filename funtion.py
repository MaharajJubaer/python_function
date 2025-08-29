#write a function to print the length of a list(list is the parameter)

list_data = ["tara","lavender","roohi","sweetheart"]
list_data1 = ["rakib","no_one"]

def length(list):
    a = len(list)
    print(a)
    return a

length(list_data)
length(list_data1)

#WAF to print the elements of a list in a single line(list is a parameter)

name = ["tara","lavender","roohi"]

def single_line(list):

    for i in list:
        print(i,end="  ")

single_line(name)

#WAF to find the factorial of n

def calc_factorial(n):

    i = 1
    factorial = 1
    while i<=n:
        factorial *= i
        i += 1
    print(factorial)
    return factorial

calc_factorial(5)
calc_factorial(10)

#WAF to convert USD to BDT

def convert(USD):

    doller_rate = 121
    BDT = doller_rate * USD
    print(BDT)
    return BDT

convert(5)
convert(10)
convert(15)

#writea recursive function to calculate the sum of first natural number

def calc_sum(n):
    if(n==0):
        return 0
    calc_sum(n-1)
    sum = calc_sum(n-1) + n
    return sum

print(calc_sum(5))





