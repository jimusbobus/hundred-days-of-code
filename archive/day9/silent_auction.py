from art import logo


def clear_screen():
    print("\n" * 100)


bids = {}

while True:
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bids[name] = bid

    add_another_bid = input("Do you wish to add another bid? (y to add again.): ")
    if add_another_bid != "y":
        break
    else:
        clear_screen()

# An initial low bid to start the comparisons.
highest_bid = -1
highest_bidder = ""

for bid in bids:
    if bids[bid] > highest_bid:
        highest_bidder = bid
        highest_bid = bids[bid]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
