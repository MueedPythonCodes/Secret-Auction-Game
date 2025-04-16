import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
bidders={}

def storage(bidder_name,bidder_amount):
    bidders[bidder_name]=bidder_amount    


result=True
winner_amount=0
winner_name=""
while result:
    name=input("What's your name: ")
    bid=int(input("What's your bid: $"))
    storage(name,bid)
    type=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    os.system('cls')
    if type=="no":
        result=False
        for key in bidders:
            if winner_amount<bidders[key]:
                winner_amount=bidders[key]
                winner_name=""
                winner_name += key
    
        print(f"The winner is {winner_name} with a bid ${winner_amount}")
