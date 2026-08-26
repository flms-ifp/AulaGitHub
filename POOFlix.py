class Usuario:
    def __init__(self,id,nome,senha,plano):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.plano = plano
        pass

class Filmes:
    def __init__(self,genero,duracao,elenco,produtora):
        self.genero = genero
        self.duracao = duracao
        self.elenco = elenco
        self.produtora = produtora
        pass

class Serie:
    def __init__(self,temporadas,genero,elenco,produtora):
        self.temporadas = temporadas
        self.genero = genero
        self.elenco = elenco
        self.produtor = produtora
        pass
