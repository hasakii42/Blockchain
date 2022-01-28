import json
from web3 import Web3

# tutorial to send transaction on smart contract
gan_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(gan_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":['
                 '],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],'
                 '"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view",'
                 '"type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"",'
                 '"type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],'
                 '"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')

add = web3.toChecksumAddress("0xc30c892E27923307Fe083fEb7EA059Ca53960090")

contract = web3.eth.contract(address=add, abi=abi)

print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('Noice').transact()

web3.eth.waitForTransactionReceipt(tx_hash)
print('updated greeting: {}'.format
      (contract.functions.greet().call()))
