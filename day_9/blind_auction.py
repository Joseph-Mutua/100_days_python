
# Secret bid program
from art import logo
print(logo)

continue_bid = "yes"
bids = {}
while continue_bid == "yes":
    name = input("Please type your name\n")
    bid_price = int(input("Please type your bid price\n"))

    bids[name] = bid_price

    continue_bid = input(
        "Are there any other users who want to bid? Type 'yes' or 'no'\n").lower()

highest_bid = max(bids, key=bids.get)
print(f"The highest bid is {bids[highest_bid]} by {highest_bid}")

