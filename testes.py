import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.inicializado, self.robo = inicializar()

    def testar_00_inicializado(self):
        self.assertTrue(self.inicializado)

    def testar_01_oi_ola(self):
        saudacoes = ["oi", "olá", "oi, tudo bem?"]

        for saudacao in saudacoes:
            print(f"testando a saudação: {saudacao}")

            resposta, confianca = get_resposta(self.robo, saudacao)
            self.assertGreaterEqual(confianca, CONFIANCA_MINIMA)
            self.assertIn("sou o ListaBot, assistente de atendimento da Lista de Compras", resposta)

    def testar_02_variabilidades(self):
        saudacoes = ["como vai?", "olá, como vai?", "olá, tudo bem?", "tudo bem?"]

        for saudacao in saudacoes:
            print(f"testando: {saudacao}")

            resposta, confianca = get_resposta(self.robo, saudacao)
            self.assertGreaterEqual(confianca, CONFIANCA_MINIMA)
            self.assertIn("sou o ListaBot, assistente de atendimento da Lista de Compras", resposta)

class TesteFuncionamentoGeral(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.inicializado, self.robo = inicializar()

    def testar_00_inicializado(self):
        self.assertTrue(self.inicializado)

    def testar_01_planilha_automatica(self):
        mensagens = [
            "os itens sao adicionados automaticamente a uma planilha?",
            "os itens vao para uma planilha?",
            "o sistema guarda os itens em uma planilha?"
        ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("gravado automaticamente em uma planilha", resposta.text.lower())

    def testar_02_confirmacao_item(self):
        mensagens = [
            "como saber se um item foi adicionado a lista?",
            "como sei que o item foi salvo?",
            "como verificar se o item entrou na lista?"
        ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)

    def testar_03_status_pendente(self):
        mensagens = [
            "o que e o status pendente?",
            "o que é o status pendente",
            "o que significa o status pendente?",
            "para que serve o campo status?"
        ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("status pendente", resposta.text.lower())

    def testar_04_informacoes_do_item(self):
        mensagens = [
            "quais informacoes cada item da lista possui?",
            "quais informações cada item da lista possui?",
            "quais dados tem cada item da lista?",
            "o que e registrado para cada item?"
        ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("id, produto, quantidade e status", resposta.text.lower())

class TesteGerenciamentoItens(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.inicializado, self.robo = inicializar()

    def testar_00_inicializado(self):
        self.assertTrue(self.inicializado)

    def testar_01_adicionar_item(self):
        mensagens = [
            "como adicionar um item na lista?",
            "como faco para adicionar um item?",
            "como inserir um produto na lista?"
        ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("status pendente", resposta.text.lower())

    def testar_02_remover_item(self):
        mensagens = [
            "como remover um item?",
            "como faco para remover um item da lista?",
            "como excluir um produto da lista?"
        ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("remove o item da lista", resposta.text.lower())

    def testar_03_exibir_itens(self):
        mensagens = [
            "como ver os itens cadastrados?",
            "como faco para ver a lista de compras?",
            "como exibir os itens da lista?"
        ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("id, produto, quantidade e status", resposta.text.lower())

    def testar_04_organizar_lista(self):
        mensagens = [
            "como organizar a lista?",
            "como faco para organizar a lista de compras?",
            "como ordenar os itens da lista?"
        ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("ordem alfabética", resposta.text.lower())


if __name__ == "__main__":
    unittest.main()