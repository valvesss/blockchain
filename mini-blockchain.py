# Importando bibliotecas
import json
import hashlib
import datetime

from pprint import pprint

# Blockchain
class Blockchain:

    def __init__(self):
        self.cadeia = []

    def criar_bloco(self, conteudo='teste'):
        bloco = {'indice': len(self.cadeia) + 1,
                 'data_hora': str(datetime.datetime.now()),
                 'conteudo': str(conteudo),
                 'hash_anterior': self.obter_hash_bloco_anterior()}
        bloco['hash_atual'] = self.hash_bloco(bloco)
        self.cadeia.append(bloco)

    def hash_bloco(self, bloco):
        bloco_codificado = json.dumps(bloco, sort_keys = True).encode()
        return hashlib.sha256(bloco_codificado).hexdigest()

    def obter_hash_bloco_anterior(self):
        if self.cadeia:
            return self.cadeia[-1]['hash_atual']
        else:
            return 'Bloco Genesis'

blockchain = Blockchain()
blockchain.criar_bloco()
blockchain.criar_bloco('Sucesso!')
pprint(blockchain.cadeia)
