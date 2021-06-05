import json
import hashlib
import os

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
Ledger_location = "Ledgers"
Math_location = "Math_Problems"
Ledger = ''
problem = ''


def sha256digest(fname):
    return hashlib.sha256(open(fname, 'rb').read())

addr = os.path.join("GenesisBlock", "GenesisBlock.json")
Hash = sha256digest(addr)
chain = {
    'Block number': BlockNumber,
    'Block hash': Hash.hexdigest(),
    'Prev hash': PrevHash,
    'Nonce value': str(Nonce)
}
print(Hash.hexdigest())
BlockChain.append(chain)
PrevHash = Hash
BlockNumber += 1

##


#reading ledger
Ledger_location2 = "Ledger_Number" + str(BlockNumber) + ".json"
l_file = os.path.join(Ledger_location, Ledger_location2)
temp = sha256digest(l_file)
print("Ledger" + temp.hexdigest())
print (temp)
Math_location2 = "Math_Problem_Number" + str(BlockNumber) + ".json"
m_file = os.path.join(Math_location, Math_location2)
file = open(m_file)
math = json.load(file)
number = math["mathProblem"]
print(number)
temp.update(PrevHash)
print(temp.hexdigest())
T = temp

temp.update(str(Nonce).encode())
print(temp.hexdigest())
# tx = temp.hexdigest()

Nonce += 1



#
# for BlockNumber in range(11):
#     #reading ledger
#     l_file = Ledger_location + str(BlockNumber) + ".json"
#     temp = sha256digest(l_file)
#     m_file = Math_location + str(BlockNumber) + ".json"
#     file = open(m_file)
#     math = json.load(file)
#     number = math["mathProblem"]
#     temp.update(PrevHash)
#     T = temp
#     while True:
#         temp.update(str(Nonce).encode())
#         tx = temp.hexdigest()
#
#         Nonce += 1
#

