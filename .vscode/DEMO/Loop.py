
####################### For Loop ########################

data = [10, 20, 30, 40, 50, 60]
for i in data:
    print(i)  # o/p --->  10, 20, 30, 40, 50, 60

print("***************************")

# Sum of first natural number 1+2+3+4+5 = 15
# range(i, j) ---> i to j-1
add = 0
for j in range(1, 6):
    add = add + j
print(add)  # o/p ---> 15

print("*******************")
for k in range(1, 10, 2):
    print(k)  # o/p ---> (1 3 5 7 9)

print("*******************")
for p in range(10):
    print(p)
print("*********************")

######################### while loop ################################

# while loop is used to check the conditions

a = 5
while a > 1:
    if a != 3:
        print(a)
        break
    a = a - 1
print("while loop excution is done")
