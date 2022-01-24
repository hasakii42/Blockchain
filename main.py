import json
from web3 import Web3

# tutorial 1 to read from blockchain smart contract and return value
infura_url = "https://mainnet.infura.io/v3/e9ea95d8232d499f9d1464be408f94b8"
web3 = Web3(Web3.HTTPProvider(infura_url))

# to check the connection (true if connected)
# print(web3.isConnected())

# copied from contract abi
abi = json.loads(
    '[{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,'
    '"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],'
    '"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},'
    '{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},'
    '{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,'
    '"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to",'
    '"type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,'
    '"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],'
    '"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[{"name":"",'
    '"type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},'
    '{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":false,'
    '"type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],'
    '"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],'
    '"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},'
    '{"constant":false,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":false,'
    '"type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],'
    '"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"",'
    '"type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{'
    '"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to",'
    '"type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,'
    '"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount",'
    '"type":"uint256"},{"name":"_releaseTime","type":"uint256"}],"name":"mintTimelocked","outputs":[{"name":"",'
    '"type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner",'
    '"type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining",'
    '"type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner",'
    '"type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},'
    '{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value",'
    '"type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[],"name":"MintFinished",'
    '"type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],'
    '"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},'
    '{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],'
    '"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},'
    '{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],'
    '"name":"Transfer","type":"event"}]')
# copied from contract
ad1 = "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07"

contract = web3.eth.contract(address=ad1, abi=abi)

totalSupply = contract.functions.totalSupply().call()

print(web3.fromWei(totalSupply, 'ether'))
print(contract.functions.name().call())
print(contract.functions.symbol().call())
address2 = Web3.toChecksumAddress('0x2551d2357c8da54b7d330917e0e769d33f1f5b93')  # copied from holders
balance = contract.functions.balanceOf(address2).call()
print(web3.fromWei(balance, 'ether'))
