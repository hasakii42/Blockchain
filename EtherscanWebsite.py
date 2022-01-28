from web3 import Web3

# ReBuilding Ether scan website with python reading blockchain
infu_url = 'https://mainnet.infura.io/v3/67b9b926dce740418db637c475d4e685'
web3 = Web3(Web3.HTTPProvider(infu_url))

# print(web3.isConnected()) // to test connection


'''*********************************'''
# code to read get 10 blocks
new = web3.eth.blockNumber
print(new)
print(web3.eth.getBlock(new))

for i in range(0, 10):
    print(">>>", i, ")", web3.eth.getBlock(new - i), "\n", "**")
'''*********************************'''
# code to read specific block
hash = "0x57ebe95538eeff16ffc275c24d84bc84dc179d581d469dba62a44c9040de6f38"

print(web3.eth.getTransactionByBlock(hash, 2))  # to read specific block transaction
