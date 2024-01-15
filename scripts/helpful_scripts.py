from brownie import accounts, network, config, MockV3Aggregator

DECIMALS = 8
INITAL_VALUE = 200000000

FORKED_LOCAL = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN = ["development", "ganache-local"]

def get_account():
    if network.show_active not in LOCAL_BLOCKCHAIN or network.show_active in FORKED_LOCAL:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    
def deploy_mocks():
    account = get_account()
    print(f"Current network is {network.show_active}")
    print("Deploying Mocks.....")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, INITAL_VALUE, {"from": account})
    print("Mock deployed.")