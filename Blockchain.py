# making blocking chain in python
"""
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
"""
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
t6 = "Harsh sends 7C to Mani"
t7 = "Harsh sends 10C to Vikas"
t8 = "Vikas sends 2.5C to Jay"
t9 = "Jeet sends 3C to Vikas"
t10 = "Hitesh sends 4C to Harsh"
t11 = "Mani sends 10C to Naveen"
t12 = "Harsh sends 7C to Mani"
t13 = "Harsh sends 10C to Vikas"
t14 = "Vikas sends 2.5C to Jay"
t15 = "Jeet sends 3C to Vikas"
t16 = "Hitesh sends 4C to Harsh"
t17 = "Mani sends 10C to Naveen"
t18 = "Harsh sends 7C to Mani"
t19 = "Harsh sends 10C to Vikas"
t20 = "Vikas sends 2.5C to Jay"
t21 = "Jeet sends 3C to Vikas"
t22 = "Hitesh sends 4C to Harsh"
t23 = "Mani sends 10C to Naveen"
t24 = "Harsh sends 7C to Mani"
t25 = "Mani sends 10C to Naveen"
t26 = "Harsh sends 7C to Mani"
t27 = "Harsh sends 10C to Vikas"
t28 = "Vikas sends 2.5C to Jay"
t29 = "Jeet sends 3C to Vikas"
t30 = "Hitesh sends 4C to Harsh"
t31 = "Mani sends 10C to Naveen"
t32 = "Harsh sends 7C to Mani"
t33 = "Harsh sends 10C to Vikas"
t34 = "Vikas sends 2.5C to Jay"
t35 = "Jeet sends 3C to Vikas"
t36 = "Hitesh sends 4C to Harsh"
t37 = "Mani sends 10C to Naveen"
t38 = "Harsh sends 7C to Mani****"
t39 = "Mani sent 10C to Raj"
t40 = "Raj got 10C from Mani"
t41 = "Karan sent 40C to Pathak"
t42 = "Pathak got 40C  from Karan"

initial_block = CoinBlock("Initial String", [t1, t2])

print("\n", initial_block.block_data, "\n")
print("\n", initial_block.block_hash, "\n")

second_block = CoinBlock(initial_block.block_hash, [t3, t4])
print("\n", second_block.block_data, "\n")
print("\n", second_block.block_hash, "\n")

third_block = CoinBlock(second_block.block_hash, [t5, t6])
print("\n", third_block.block_data, "\n")
print("\n", third_block.block_hash, "\n")

fourth_block = CoinBlock(third_block.block_hash, [t7, t8])
print("\n", fourth_block.block_data, "\n")
print("\n ", fourth_block.block_hash, "\n")

fivth_block = CoinBlock(fourth_block.block_hash, [t9, t10])
print("\n", fivth_block.block_data, "\n")
print("\n", fivth_block.block_hash, "\n")

sixth_block = CoinBlock(fivth_block.block_hash, [t11, t12])
print("\n", sixth_block.block_data, "\n")
print("\n", sixth_block.block_hash, "\n")

seventh_block = CoinBlock(sixth_block.block_hash, [t13, t14])
print("\n", seventh_block.block_data, "\n")
print("\n", seventh_block.block_hash, "\n")

eighth_block = CoinBlock(seventh_block.block_hash, [t15, t16])
print("\n", eighth_block.block_data, "\n")
print("\n", eighth_block.block_hash, "\n")

ninth_block = CoinBlock(eighth_block.block_hash, [t17, t19])
print("\n", ninth_block.block_data, "\n")
print("\n", ninth_block.block_hash, "\n")

tenth_block = CoinBlock(ninth_block.block_hash, [t20, t21])
print("\n", tenth_block.block_data, "\n")
print("\n", tenth_block.block_hash, "\n")

eleventh_block = CoinBlock(tenth_block.block_hash, [t22, t24])
print("\n", eleventh_block.block_data, "\n")
print("\n", eleventh_block.block_hash, "\n")

twelfth_block = CoinBlock(eleventh_block.block_hash, [t25, t26])
print("\n", twelfth_block.block_data, "\n")
print("\n", twelfth_block.block_hash, "\n")

thirteenth_block = CoinBlock(twelfth_block.block_hash, [t27, t28])
print("\n", thirteenth_block.block_data, "\n")
print("\n", thirteenth_block.block_hash, "\n")

fourteenth_block = CoinBlock(thirteenth_block.block_hash, [t29, t30])
print("\n", fourteenth_block.block_data, "\n")
print("\n", fourteenth_block.block_hash, "\n")

fifteenth_block = CoinBlock(fourteenth_block.block_hash, [t31, t32])
print("\n", fifteenth_block.block_data, "\n")
print("\n", fifteenth_block.block_hash, "\n")

sixteenth_block = CoinBlock(fifteenth_block.block_hash, [t33, t34])
print("\n", sixteenth_block.block_data, "\n")
print("\n", sixteenth_block.block_hash, "\n")

seventeenth_block = CoinBlock(sixteenth_block.block_hash, [t35, t36])
print("\n", seventeenth_block.block_data, "\n")
print("\n", seventeenth_block.block_hash, "\n")

eighteenth_block = CoinBlock(seventeenth_block.block_hash, [t37, t38])
print("\n", eighteenth_block.block_data, "\n")
print("\n", eighteenth_block.block_hash, "\n")

ninthteenth_block = CoinBlock(eighteenth_block.block_hash, [t39, t40])
print("\n", ninthteenth_block.block_data, "\n")
print("\n", ninthteenth_block.block_hash, "\n")
