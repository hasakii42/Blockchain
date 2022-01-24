# making blocking chain in python
'''
Theory
Coin(ck)
t1: M send B 2 ck
t2:T send C 2 ck
t3:B send D 2 ck
#SHA256 Secure Hash Algorithm 256bit
B1('Start',t1,t2,t3)-> 76fd89
B2('7689b9',t4,t5,t6)->8923ff
B3('8923ff',t7)
Coinhash()
'''
import hashlib


class CoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Harsh sends 10C to Vikas"
t2 = "Vikas sends 2.5C to Jay"
t3 = "Jeet sends 3C to Vikas"
t4 = "Hitesh sends 4C to Harsh"
t5 = "Mani sends 10C to Naveen"
t6 = "Harsh sends 6C to Mani"

initial_block = CoinBlock("Initial String", [t1, t2])

print("\n", initial_block.block_data, "\n")
print("\n", initial_block.block_hash, "\n")

second_block = CoinBlock(initial_block.block_hash, [t3, t4])
print("\n", second_block.block_data, "\n")
print("\n", second_block.block_hash, "\n")

third_block = CoinBlock(second_block.block_hash, [t5, t6])
print("\n", third_block.block_data, "\n")
print("\n", third_block.block_hash, "\n")
