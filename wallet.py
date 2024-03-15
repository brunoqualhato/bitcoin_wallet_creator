from mnemonic import Mnemonic
from bitcoinlib.wallets import Wallet
import requests
import json


mnemo = Mnemonic("english")
words = mnemo.generate(strength=256)
print('-------------------')
print(words)

#entropy
print('-------------------')
entropy = mnemo.to_entropy(words)
print(entropy)
print('-------------------')

#gera uma nova seed
seed = mnemo.to_seed(words)
print(seed)
print('-------------------')

#nome aleatorio
name = str(entropy)

#gera uma carteira
wallet = Wallet.create(name=name, witness_type='segwit', keys=seed, network='bitcoin')
print(wallet)

#gera um endereço
address = wallet.get_key().address
print(address)


#consulta saldo bitcoin
url = 'https://blockchain.info/rawaddr/'+address
response = requests.get(url)
data = json.loads(response.text)
print(data['final_balance'])

print('-------------------')
