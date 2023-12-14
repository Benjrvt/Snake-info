import pyxel

print("hello world")

def f(n):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
    
print(f(4))