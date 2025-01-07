# def main():
#     ## input as a integer
#     curr_val = int(input("Enter a number: "))
#     while curr_val < 200:
#         curr_val = curr_val*2
#         print(curr_val)

# main()

# a:list = []

# def main(curr_val):
#     a:list = []
#     while curr_val < 100:
#         curr_val = curr_val*2
#         # print(curr_val, end=" ")
#         a.append(curr_val)
#         print(a)
        

# main(2)
# print(a)

def main():
    try:
        # Input as an integer
        curr_val = int(input("Enter a number: "))
        
        # Check if the input is 0
        if curr_val == 0:
            print("Input should not be 0. Please enter a non-zero number.")
            return  # Exit the function if 0 is entered
        
        # Run the loop if curr_val is not 0
        while curr_val < 200:
            curr_val = curr_val * 2
            print(curr_val)
    
    except ValueError:
        print("Invalid input. Please enter an integer.")

main()
