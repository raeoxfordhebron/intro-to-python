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