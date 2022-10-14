from art import SA_Logo
import os
print(SA_Logo)

name = ""
price = 0
bids = {}

def startOptions():
    name = input("What is your name?: ")
    price = int(input("What is your price?: $"))
    decision = input("Thank you for your bid!\nIs there another bidder? Y/N: ")
    bids[name] = price
    if decision.lower() == "y":
        clear()
        startOptions()
    elif decision.lower() == "n":
        clear()
        winner = findHighestBidder(bids)
        print("Bidding has ended.\nThe winner of the Blind Auction is: " + winner)
    else:
        startOptions()
        print("Please abide by the rules sir. You're being rowdy.")

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def findHighestBidder(bidding_record):
    highestBid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amt = bidding_record[bidder]
        if bid_amt > highestBid:
            highestBid = bid_amt
            winner = bidder

    return winner

startOptions()