# 1. Reverse String
def reverse_string(str):
    return str [::-1]

print(reverse_string("Hello World"))
    
# 2. Fizz Buzz
def fizz_buzz(num):
    for i in num:
        result = ""
        if(i % 3 == 0):
            result = result + "fizz"
        
        if(i % 5 == 0):
            result = result + "buzz"
        
        print (f"{i} = ", result)

fizz_buzz([1, 2, 3, 4, 5, 6, 7, 83, 29, 50])   

# 3. Calculator 
def calculator(num1, num2, operation):
    if(operation == "+"):
        return num1 + num2
    if(operation == "-"):
        return num1 - num2 
    if(operation == "*"):
        return num1 * num2
    if(operation == "/"):
         return "Can't Divide By 0" if num2 == 0 else num1/num2
     
print(calculator(99, 11, "/"))

# 4. Random Number
def random_number(low, max):
    while(True):
        import random
        random_num = random.randint(low, max)
        if(random_num >= low & random_num <= max):
            return random_num
        
print(random_number(10, 20))

# 5. Map
def add(n):
    int(n)
    return n + 1 ## forgot the return and the list came back as a list of none
    
x = list(map(add, [1, 2, 3, 4])) 

print(x)
    
    
# 6. Filter

    
    