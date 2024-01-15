from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    fundMe = FundMe[-1]
    account = get_account()
    entranceFee = fundMe.getEntranceFee()
    print(entranceFee)
    fundMe.fund({"from": account, "value": entranceFee})
    

def withdraw():
    fundMe = FundMe[-1]
    account = get_account()
    fundMe.withdraw({"from": account})    
    
def main():
    fund()
    withdraw()