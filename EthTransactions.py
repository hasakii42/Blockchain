from web3 import Web3

# tutorial to send transaction
gan_url = "HTTP://127.0.0.1:7545"  # use ganache or Ethereum url
web3 = Web3(Web3.HTTPProvider(gan_url))

print(web3.eth.blockNumber)

acc_1 = "0xbC3826a8E6b33E9AD0E406302c11f758ABBE3206"  # user1's account address

acc_2 = "0x886367E0498EF1Bef83354466d88a60A3061b13e"  # user2 's account address

pvt_key = "07090a50962f1d3d77d0a900e4a2cfd2f11ada15c44f4440a2778c696cd89c46"  # user1's Private key

# get the nonce
nonce = web3.eth.getTransactionCount(acc_1)

# build a transaction
tx = {
    'nonce': nonce,  # nonce prevents doing same transaction twice
    'to': acc_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),

}

# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, pvt_key)

# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
# get trans hash
