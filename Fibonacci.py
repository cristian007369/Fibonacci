# Fibonacci
print("-----------------------------------------")
print("----------------Fibonacci----------------")
print("-----------------------------------------")
a=1
b=1
n=int(input("Dígite hasta que término quieres llegar y hacer su respectiva suma: "))
x=2
y=0
# Processing 
while n>=x:
    print(str(a))
    print(str(b))
    y=a+b+y
    a=a+b
    b=a+b
    x=x+2
    
    
print("La suma hasta el término " + str(n)+" es: " + str(y))