import unittest
import json

class TestSistemaEstoque(unittest.TestCase):

    def setUp(self):
        self.dados_teste = [
            {"id": 1, "nome": "Item A", "quantidade": 10, "valor": 15.0},
            {"id": 3, "nome": "Item C", "quantidade": 5, "valor": 20.0}
        ]

    def test_geracao_id_sequencial_com_lacuna(self):
        ids_existentes = sorted([item['id'] for item in self.dados_teste])
        novo_id = 1
        for id_atual in ids_existentes:
            if id_atual == novo_id:
                novo_id += 1
            else:
                break
        
        self.assertEqual(novo_id, 2)

    def test_remover_item(self):
        id_para_remover = 1
        novos_dados = [item for item in self.dados_teste if item['id'] != id_para_remover]
        
        self.assertEqual(len(novos_dados), 1)
        self.assertEqual(novos_dados[0]['id'], 3)

if __name__ == '__main__':
    unittest.main()