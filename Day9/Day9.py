from art import logo
from replit import clear

print(logo)

print("Welcome to the secret auction program.")

dic_bid = {}
more_bidders = True
while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    dic_bid[name] = bid

    more = input("Are there any other bidders? Type 'yes' or 'no' ")
    if more == 'no':
        more_bidders = False
    elif more == 'yes':
        clear()

max_bidder = max(dic_bid, key=dic_bid.get)
all_values = dic_bid.values()
max_bid = max(all_values)
print(f"The winner is {max_bidder} with a bid of ${max_bid}")
