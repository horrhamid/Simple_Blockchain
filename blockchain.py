import json
import hashlib

BlockChain = []
BlockNumber = 1
PrevHash = ''
Hash = ''
Nonce = 0
chain = {
    'Block number': '',
    'Block hash': '',
    'Prev hash': '',
    'Nonce value': ''
}
Ledger_location = "Ledgers\Ledger_Number"
Math_location = "Math_Problems\Math_Problem_Number"
Ledger = ''
problem = ''


def sha256digest(fname):
    return hashlib.sha256(open(fname, 'rb').read())


Hash = sha256digest('GenesisBlock\GenesisBlock.json')
chain = {
    'Block number': BlockNumber,
    'Block hash': Hash.hexdigest(),
    'Prev hash': PrevHash,
    'Nonce value': str(Nonce)
}
print(Hash)
BlockChain.append(chain)
PrevHash = Hash
BlockNumber += 1

for BlockNumber in range(11):
    #reading ledger
    l_file = Ledger_location + str(BlockNumber) + ".json"
    temp = sha256digest(l_file)
    m_file = Math_location + str(BlockNumber) + ".json"
    file = open(m_file)
    math = json.load(file)
    number = math["mathProblem"]
    temp.update(PrevHash)
    T = temp
    while True:
        temp.update(str(Nonce).encode())
        tx = temp.hexdigest()
        
        Nonce += 1


