import json
import hashlib
import os

BlockChain = []
BlockNumber = 1
PrevHash = ''
Nonce = 0

Ledger_location = "Ledgers"
Math_location = "Math_Problems"
Ledger = ''
problem = ''


def readfromjson(fname):
    return json.load(open(fname,))


addr = os.path.join("GenesisBlock", "GenesisBlock.json")
data_j = readfromjson(addr)
data = json.dumps(data_j)
sha = hashlib.sha256()
sha.update(data.encode())
Hash = sha.hexdigest()
block = {
    'Block number': BlockNumber,
    'Block hash': Hash,
    'Prev hash': PrevHash,
    'Nonce value': ''
}
BlockChain.append(block)
print(block)
PrevHash = Hash
BlockNumber += 1

##


# reading ledger
for BlockNumber in range(2, 12):
    Ledger_location2 = "Ledger_Number" + str(BlockNumber) + ".json"
    l_file = os.path.join(Ledger_location, Ledger_location2)
    data_j = readfromjson(l_file)
    data = json.dumps(data_j)
    Math_location2 = "Math_Problem_Number" + str(BlockNumber) + ".json"
    m_file = os.path.join(Math_location, Math_location2)
    math_data = readfromjson(m_file)
    Math_prob = math_data["mathProblem"]
    # print(Math_prob)
    while True:
        temp = data + PrevHash + str(Nonce)
        sha = hashlib.sha256()
        sha.update(temp.encode())
        Hash = sha.hexdigest()
        # print("Nounce: " +str(Nonce))

        if (Hash[-(len(str(Math_prob))):] == str(Math_prob)):
            # problem solved
            block = {
                'Block number': BlockNumber,
                'Block hash': Hash,
                'Prev hash': PrevHash,
                'Nonce value': Nonce
            }
            PrevHash = Hash
            Nonce = 0
            print(block)
            BlockChain.append(block)
            break
        else:
            Nonce += 1

