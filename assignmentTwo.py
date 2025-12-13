import hashlib
import random
import time
import matplotlib.pyplot as plt

#This is where each of the blocks in a blockchain gets generated and hashed.
#Metadata is stored here too.
class Block:
    def __init__(self, index, prevBlock, singleBlock, top, transactions):
        self.index = index
        self.prevBlock = prevBlock
        self.singleBlock = singleBlock
        self.top = top
        self.transactions = transactions
        self.timestamp = time.time()

        blockHash = (str(index) + str(prevBlock) + str(singleBlock) + str(transactions) + str(self.timestamp))

        self.hash = hashlib.sha256(blockHash.encode()).hexdigest()

#validators selected along with their stake
#higher stake increases chances of being slected
def Ouroboros(validators=10, blocks=50):
    stakeshares = {f"Validator {i}": random.randint(1, 100) for i in range(validators)}
    totalShareStakes = sum(stakeshares.values())

    blockSpent = []
    TP = []

    prevHash = "GENESIS"

    for singleBlock in range(blocks):
        start = time.time()

        randy = random.uniform(0, totalShareStakes)
        cumulative = 0

        for val, sta in stakeshares.items():
            cumulative += sta
            if cumulative >= randy:
                top = val
                break

        tran = random.randint(50, 200)

        time.sleep(0.05)

        block = Block(index=singleBlock, prevBlock=prevHash, singleBlock=singleBlock, top=top, transactions=tran)

        end = time.time()

        miningTimeTotal = end - start
        blockSpent.append(miningTimeTotal)
        TP.append(tran / miningTimeTotal)

        prevHash = block.hash

    return blockSpent, TP

#random committee is selected each time
#one validator is randomly selected
def Algorand(validators=10, blocks=50):
    AllValidators = [f"Validator {i}" for i in range(validators)]
    blockSpent = []
    TP = []

    prevHash = "GENESIS"

    for singleBlock in range(blocks):
        start = time.time()

        commit = max(1, validators // 3)
        commit = random.sample(AllValidators, commit)

        top = random.choice(commit)

        tran = random.randint(50, 200)
        time.sleep(random.uniform(0.005, 0.02))

        block = Block(index=singleBlock, prevBlock=prevHash, singleBlock=singleBlock, top=top, transactions=tran)

        end = time.time()

        miningTimeTotal = end - start
        blockSpent.append(miningTimeTotal)
        TP.append(tran / miningTimeTotal)

        prevHash = block.hash

    return blockSpent, TP

#validators propose blocks each round
#delays are caused by voting
def Tendermint(validators=10, blocks=50):
    AllValidators = [f"Validator {i}" for i in range(validators)]
    blockSpent = []
    TP = []

    prevHash = "GENESIS"
    index = 0

    for singleBlock in range(blocks):
        start = time.time()
        top = AllValidators[index]
        index = (index + 1) % validators

        time.sleep(random.uniform(0.01, 0.03))
        time.sleep(random.uniform(0.01, 0.03))

        tran = random.randint(100, 300)
        block = Block(index=singleBlock, prevBlock=prevHash, singleBlock=singleBlock, top=top, transactions=tran)

        end = time.time()

        miningTimeTotal = end - start
        blockSpent.append(miningTimeTotal)
        TP.append(tran / miningTimeTotal)

        prevHash = block.hash

    return blockSpent, TP



if __name__ == "__main__":
    spent, tp = Ouroboros()
    spentA, tpA = Algorand()
    spentT, tpT = Tendermint()

    print("====Ouroboros\n")

    print("Mining time: ", sum(spent) / len(spent))
    print("\nAvg throughput: ", sum(tp) / len(tp))

    print("\n====Algorand\n")

    print("Mining time: ", sum(spentA) / len(spentA))
    print("\nAvg throughput: ", sum(tpA) / len(tpA))

    print("\n====Tendermint\n")

    print("Mining time: ", sum(spentT) / len(spentT))
    print("\nAvg throughput: ", sum(tpT) / len(tpT))

    avgMining = [sum(spent) / len(spent), sum(spentA) / len(spentA), sum(spentT) / len(spentT)]

    algs = ["Ouroboros", "Algorand", "Tendermint"]

    plt.figure()
    plt.bar(algs, avgMining)
    plt.xlabel("(Algorithms)")
    plt.ylabel("Avg Mining time (sec)")
    plt.title("Avg mining time comparison")
    plt.show()

    avgThroughput = [sum(tp) / len(tp), sum(tpA) / len(tpA), sum(tpT) / len(tpT)]

    plt.figure()
    plt.bar(algs, avgThroughput)
    plt.xlabel("(Algorithms)")
    plt.ylabel("Avg Throughput (sec)")
    plt.title("Avg Throughput comparison")
    plt.show()











