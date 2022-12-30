# Created by Emma Hodor on 12/30/2022
# import replit

print('Welcome to the auction house!')
bidders = {}

while True:
    name = input('What is your name?\n')
    if name in bidders.keys():
        bid = int(input('What is your new bid?\n'))
    else:
        bid = int(input('How much are you bidding?\n'))
    bidders[name] = bid
    # replit.clear()
    others = input('Are there any other bidders? Type "yes" or "no".\n')
    if others == "no":
        redo = input('Would any current bidder like to update their bid? Type "yes" or "no".\n')
        if redo == "no":
            break
    # replit.clear()

winner = ""
winning_bid = 0
for name in bidders:
    if bidders[name] > winning_bid:
        winning_bid = bidders[name]
        winner = name

print(f'Congratulation! {winner} has won the auction with a bid of ${winning_bid}!')