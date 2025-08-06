# 1****
 # 22***
 # 333**
 # 4444*
 # 55555

n=int(input("enter number"))
for i in range(1,n+1):
    print(str(i)*i+"*"*(n-i))

 # 1****
 # 12***
 # 123**
 # 1234*
 # 12345

n=int(input("Enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("*"*(n-i))

 # 55555
 # 4444*
 # 333**
 # 22***
 # 1****

n=int(input("Enter a number"))
for i in range(n,0,-1):
    print(str(i)*i+"*"*(n-i))

 # 12345
 # 1234*
 # 123**
 # 12***
 # 1****

n=int(input("Entr number :"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("* "*(n-i))

 # ****1
 # ***22
 # **333
 # *4444
 # 55555

n=int(input("Enter a number"))
for i in range(1,n+1):
    print("*"*(n-i)+str(i)*i)


 # ****1
 # ***21
 # **321
 # *4321
 # 54321

n=int(input("Enter a number"))
for i in range(1,n+1):
    print("*"*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()

# ****1
# ***12
# **123
# *1234
# 12345

n=int(input("Enter a number"))
for i in range(1,n+1):
    print("*"*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    print()


 # 55555
 # *4444
 # **333
 # ***22
 # ****1

n=int(input("enter number"))
for i in range(n,0,-1):
    print("*"*(n-i)+str(i)*i)


 # 54321
 # *4321
 # **321
 # ***21
 # ****1

n=int(input("enter a number"))
for i in range(n,0,-1):
    print("*"*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()