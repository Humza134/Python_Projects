import random
# Print 10 random numbers in the range 1 to 100.
# def main():
#     for i in range(10):
#         print(random.randint(1, 100), end=' ')


# main()   

MIN_NUMBER = 1
MAX_NUMBER = 100
N_RANDOM_NUMBER = 10

number_list:list = []

def main():
    for i in range(N_RANDOM_NUMBER):
        rand_numb = random.randint(MIN_NUMBER, MAX_NUMBER)
        number_list.append(rand_numb)
        # print(number_list)
main()
print(number_list, end=" ")