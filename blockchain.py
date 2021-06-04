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



def sha256digest(fname):
    return hashlib.sha256(open(fname, 'rb').read()).hexdigest()


Hash = sha256digest('GenesisBlock\GenesisBlock.json')
chain = {
    'Block number': BlockNumber,
    'Block hash': Hash,
    'Prev hash': PrevHash,
    'Nonce value': str(Nonce)
}
BlockChain.append(chain)
PrevHash = Hash
BlockNumber +=1

for BlockNumber in range(11):
    # creating new Ledger
    pass
