FibArray = [1,1] 
  
def fibonacci(n): 
    if n<=1:
        return n
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        FibArray.append(temp_fib) 
        return temp_fib 

n = int(input())
print(fibonacci(n))

