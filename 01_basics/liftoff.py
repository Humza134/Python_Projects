# def coutdown():
#     for i in range(11):
#         print(i, end=" ")
#         if i == 10:
#             print("liftOff")

# coutdown()

def coutdown():
    for i in range(10, 0, -1):
        print(i, end=" ")
    print("liftOff")

coutdown()

number:list[int] = [10,9,8,7,6,5,4,3,2,1]
def liftOff():
    for x in number:
        print(x, end=" ")
    print("LiftOff")

liftOff()