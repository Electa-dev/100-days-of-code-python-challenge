import art_for_auction
print(art_for_auction.logo)
bidders = {}
ongoing_auction = False
while not ongoing_auction:
    name = input("What is your name:\n").lower()
    bid_price = int(input("How much are you bidding:\n$"))

    bidders[name] = bid_price

    continue_auction = input("Are there any other bidders? Type 'yes' if there are and 'no' if there are none:\n").lower()
  
    price = 0
    for name in bidders:
        highest_bid = bidders[name]
        if highest_bid > price:
            price = highest_bid
            highest_bidder = name
    if continue_auction == "yes":
        print("\n" * 100)
    elif continue_auction == "no":
        print(f"The winner is {highest_bidder.title()} with a bid of ${price}!")
        ongoing_auction = True
    else: 
        print("Enter the correct input!!")
        ongoing_auction = True
    
