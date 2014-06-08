# -*- coding: UTF-8 -*-

class Anao:
    def __init__(self):
        self.nome='Anão'        
        self.tamanho='ME'
        self.deslocamento=6
        self.imagem='img/anao.gif'
        self.tr="""+4 Constituição, +2 Sabedoria, –2 Destreza.
Outras Habilidades ver livro
Basico Tormenta RPG, pagina 32"""

    def Aplicar(self, personagem):
        personagem.constituicao+=4
        personagem.destreza+=2
        personagem.sabedoria-=2
        personagem.tamanho=self.tamanho
        personagem.deslocamento=self.deslocamento
        personagem.raca=self.nome

class Elfo:
    def __init__(self):
        self.nome='Elfo'        
        self.tamanho='ME'
        self.deslocamento=9
        self.imagem='img/elfo.gif'
        self.tr="""+4 Destreza, +2 Inteligência, –2 Constituição.
Outras Habilidades ver livro
Basico Tormenta RPG, pagina 33
Lembrete para o Programador!!!!"""
        
    def Aplicar(self, personagem):
        personagem.constituicao-=2
        personagem.destreza+=4
        personagem.inteligencia+=2
        personagem.tamanho=self.tamanho
        personagem.deslocamento=self.deslocamento
        personagem.raca=self.nome

