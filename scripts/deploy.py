from brownie import accounts, config, FundMe, network, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN

def main():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        
        
    fundMe = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(fundMe.address)
    pass