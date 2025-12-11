import hashlib
import random
import time


class Block:
    def __init__(self, index, prevBlock, timestamp, transactions, validation):
        self.index = index
        self.prevBlock = prevBlock
        self.timestamp = timestamp
        self.transactions = transactions
        self.validation = validation

        blockHash = (str(index) + str(prevBlock) + str(timestamp) + str(transactions), str(validation))

        self.hash = hashlib.sha256(blockHash.encode()).hexdigest()

def Ouroboros(validators=10, blocks=50):
    stakeshares = {f"Validator {i}": random.randint(1, 100) for i in range(validators)}
    totalShareStakes = sum(stakeshares.values())

    blockSpent = []
    TP = []

    prevHash = "GENESIS"

    for block in range(blocks):
        start = time.time()

        randy = random.uniform(0, totalShareStakes)
        cumulative = 0

        for val, sta in stakeshares:
            cumulative += sta
            if cumulative >= randy:
                leader = val
                break

        tran = random.randint(200, 1000)

        time.sleep(0.005)

