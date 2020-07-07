a = 0
b = 1
n = int(input("Enter number of terms in Fibbonacci series: "))
print(a)
print(b)
for i in range(0,n):
    c = a + b
    a = b
    b = c
    print(b)
