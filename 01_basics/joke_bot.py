PROMPT = "what do you want?"
JOKE = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY = "Sorry i tell only jokes"

def main():
    user_input = input(PROMPT)
    print(user_input)

    if user_input.lower() == "joke":
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()