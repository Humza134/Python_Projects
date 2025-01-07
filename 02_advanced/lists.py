# fruits = ['apple', 'banana', 'orange', 'grape', 'pineapple']

# def list_fruits():
#     print(fruits)
#     fruits.append("mango")
#     return fruits
    

# updated_fruits = list_fruits()
# print(updated_fruits)

def access_list(list, index):
    try:
        return list[index]
    except IndexError:
        return "index is out of range"
    
def modify_list(list, index, value):
    try:
        list[index] = value
        return list
    except IndexError:
        return "index is out of range"
    
def slicing_list(list, start, end):
    try:
        return list[start:end]
    except IndexError:
        return "index is out of range"
    
def index_game():
    list = [1,2,3,4,5]
    print("Current list: ", list)
    print("Chosse an operation: access, modify, slicing")
    operation = input("Enter operation: ")
    if operation == "access":
        index = int(input("Enter index: "))
        print(access_list(list, index))
    elif operation == "modify":
        index = int(input("Enter index: "))
        value = int(input("Enter value: "))
        print(modify_list(list, index, value))
    elif operation == "slicing":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index"))
        print(slicing_list(list, start, end))
    else:
        print("Invalid operation")

index_game()