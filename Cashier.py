# Create inventory containing items and prices
inventory = {"chips": 2, "soda": 1.50, "candy": 1, "coffee": 2.50, "canned soup": 1.25, "cereal": 3,
             "cigarettes": 7, "milk": 4, "canned beans": 1.75, "beer": 2.25}

cart = []
total = []

# Within a loop, ask customer for input, and include option to quit
def cashier():
    user_answer = input("Hello, sir!  What do you want to purchase today?").lower()
    while user_answer != "quit":
        if user_answer in inventory:
            cart.append(user_answer)
            user_answer = input("Perfect! I will add that to your cart! Anything else?"
                                "(Type 'quit' to end)").lower()
        else:
            user_answer = input("I am sorry, we do not have that item! Would you like anything else?")
            "(Type 'quit' to end)".lower()

cashier()

# Display customer's shopping cart and ask if they want to purchase anything else
print("Here are all the items in your cart: ", cart)

answer = input("Do you want to add anything else to your cart? (Type yes/no)")

if answer == "yes":
    cashier()
    print("Here are all the items you selected: ", cart)
    for items in cart:
        total.append(inventory[items])
    amount_due = sum(total)
else:
    for items in cart:
        total.append(inventory[items])
    amount_due = sum(total)

# Display the total amount due
print("Your total amount due is: ", amount_due)

