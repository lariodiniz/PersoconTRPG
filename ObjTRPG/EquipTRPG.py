# -*- coding:UTF-8 -*-
"""
Módulo que cria os Objetos Arma, Armadura, Escudo e Equipamento para Tormenta RPG
"""

#Classe Armas

class Arma:
    def __init__(self):
        """
Forma de Ataque:
0=Simples leves
1=Simples uma mão
2=Simples duas maõs
4=Simples a distancia

10=Marciais leves
11=Marciais uma mão
12=Marciais duas maõs
14=Marciais a distancia

20=Exoticas leves
21=Exoticas uma mão
22=Exoticas duas maõs
24=Exoticas a distancia

"""
        self.nome=str()
        self.preco=float()
        self.dano=str()
        self.critico=str()
        self.distancia=int()
        self.peso=float()
        self.tipo=str()
        self.formadeataque=int()
        self.quantidade=int()
        self.dureza=int()
        self.pv=int()
        self.tamanho="ME"
        self.bba=0
    def Equipar(self, perso):
        """
Coloca as Informações da arma no Objeto Personagem.
"""
        perso.armas[self.nome]={'BBA':0,'DANO':self.dano+'+'+str(perso.mforca),'CRITICO':self.critico,
                                'DISTANCIA':str(self.distancia)+'m','TIPO':self.tipo,'PESO':self.peso}
        if str(self.formadeataque)[::-1][0]=='4':
            perso.armas[self.nome]['BBA']=perso.bbaadi+self.bba
        else:
            perso.armas[self.nome]['BBA']=perso.bbacac+self.bba
        perso.cargaatual+=self.peso
    def Tamanho(self,tamanho):
        """
Modifica o Dado de dano da arma de acordo com o tamanho.
"""
        self.tamanho=tamanho.upper()
        if self.tamanho == "IN":
            self.pv=self.pv/8
            self.peso=self.peso/8
            self.nome+= " Infi."
            if self.dano.upper() == '1D2':
                self.dano = "1"                
            elif self.dano.upper() == '1D3':
                self.dano = "1"
            elif self.dano.upper() == '1D4':
                self.dano = "1"
            elif self.dano.upper() == '1D6':
                self.dano = "1"
            elif self.dano.upper() == '2D4':
                self.dano = "1d2"
            elif self.dano.upper() == '1D8':
                self.dano = "1d2"
            elif self.dano.upper() == '1D10':
                self.dano = "1d3"
            elif self.dano.upper() == '2D6':
                self.dano = "1d4"
            elif self.dano.upper() == '1D12':
                self.dano = "1d4"
            elif self.dano.upper() == '2D8':
                self.dano = "1d6"
            elif self.dano.upper() == '3D6':
                self.dano = "1d8"            
            elif self.dano.upper() == '3D8':
                self.dano = "1d8"
            else:
                self.dano = "Não especificado"
        elif self.tamanho == "DI":
            self.pv=self.pv/6
            self.peso=self.peso/6
            self.nome+= " Dimin."
            if self.dano.upper() == '1D2':
                self.dano = "1"                
            elif self.dano.upper() == '1D3':
                self.dano = "1"
            elif self.dano.upper() == '1D4':
                self.dano = "1"
            elif self.dano.upper() == '1D6':
                self.dano = "1d2"
            elif self.dano.upper() == '2D4':
                self.dano = "1d3"
            elif self.dano.upper() == '1D8':
                self.dano = "1d3"
            elif self.dano.upper() == '1D10':
                self.dano = "1d4"
            elif self.dano.upper() == '2D6':
                self.dano = "1d6"
            elif self.dano.upper() == '1D12':
                self.dano = "1d8"
            elif self.dano.upper() == '2D8':
                self.dano = "1d8"
            elif self.dano.upper() == '3D6':
                self.dano = "1d8"            
            elif self.dano.upper() == '3D8':
                self.dano = "1d10"
            else:
                self.dano = "Não especificado"
            
        elif self.tamanho == "MI":
            self.pv=self.pv/4
            self.peso=self.peso/4
            self.nome+= " Mini."
            if self.dano.upper() == '1D2':
                self.dano = "1"                
            elif self.dano.upper() == '1D3':
                self.dano = "1"
            elif self.dano.upper() == '1D4':
                self.dano = "1d2"
            elif self.dano.upper() == '1D6':
                self.dano = "1d3"
            elif self.dano.upper() == '2D4':
                self.dano = "1d4"
            elif self.dano.upper() == '1D8':
                self.dano = "1d4"
            elif self.dano.upper() == '1D10':
                self.dano = "1d6"
            elif self.dano.upper() == '2D6':
                self.dano = "1d8"
            elif self.dano.upper() == '1D12':
                self.dano = "1d8"
            elif self.dano.upper() == '2D8':
                self.dano = "1d10"
            elif self.dano.upper() == '3D6':
                self.dano = "1d10"            
            elif self.dano.upper() == '3D8':
                self.dano = "2d6"
            else:
                self.dano = "Não especificado"            
            
        elif self.tamanho == "PE":
            self.pv=self.pv/2
            self.peso=self.peso/2
            self.nome+= " Pequen."
            if self.dano.upper() == '1D2':
                self.dano = "1"                
            elif self.dano.upper() == '1D3':
                self.dano = "1d2"
            elif self.dano.upper() == '1D4':
                self.dano = "13"
            elif self.dano.upper() == '1D6':
                self.dano = "1d4"
            elif self.dano.upper() == '2D4':
                self.dano = "1d6"
            elif self.dano.upper() == '1D8':
                self.dano = "1d6"
            elif self.dano.upper() == '1D10':
                self.dano = "1d8"
            elif self.dano.upper() == '2D6':
                self.dano = "1d10"
            elif self.dano.upper() == '1D12':
                self.dano = "1d10"
            elif self.dano.upper() == '2D8':
                self.dano = "2d6"
            elif self.dano.upper() == '3D6':
                self.dano = "2d6"            
            elif self.dano.upper() == '3D8':
                self.dano = "2d8"
            else:
                self.dano = "Não especificado"
            
        elif self.tamanho == "GRA" or self.tamanho == "GRC":
            self.pv=self.pv*2
            self.peso=self.peso*2
            self.nome+= " Grande"
            if self.dano.upper() == '1D2':
                self.dano = "1d3"                
            elif self.dano.upper() == '1D3':
                self.dano = "1d4"
            elif self.dano.upper() == '1D4':
                self.dano = "1d6"
            elif self.dano.upper() == '1D6':
                self.dano = "1d8"
            elif self.dano.upper() == '2D4':
                self.dano = "2d6"
            elif self.dano.upper() == '1D8':
                self.dano = "2d6"
            elif self.dano.upper() == '1D10':
                self.dano = "2d8"
            elif self.dano.upper() == '2D6':
                self.dano = "3d6"
            elif self.dano.upper() == '1D12':
                self.dano = "3d6"
            elif self.dano.upper() == '2D8':
                self.dano = "3d8"
            elif self.dano.upper() == '3D6':
                self.dano = "4d8"            
            elif self.dano.upper() == '3D8':
                self.dano = "4d8"
            else:
                self.dano = "Não especificado"
            
        elif self.tamanho == "ENA" or self.tamanho == "ENC":
            self.pv=self.pv*4
            self.peso=self.peso*4
            self.nome+= " Enorme"
            if self.dano.upper() == '1D2':
                self.dano = "1d4"
            elif self.dano.upper() == '1D3':
                self.dano = "1d6"
            elif self.dano.upper() == '1D4':
                self.dano = "1d8"
            elif self.dano.upper() == '1D6':
                self.dano = "2d6"
            elif self.dano.upper() == '2D4':
                self.dano = "3d6"
            elif self.dano.upper() == '1D8':
                self.dano = "2d8"
            elif self.dano.upper() == '1D10':
                self.dano = "3d6"
            elif self.dano.upper() == '2D6':
                self.dano = "3d8"
            elif self.dano.upper() == '1D12':
                self.dano = "4d6"
            elif self.dano.upper() == '2D8':
                self.dano = "4d8"
            elif self.dano.upper() == '3D6':
                self.dano = "5d6"
            elif self.dano.upper() == '3D8':
                self.dano = "5d8"       
             
        elif self.tamanho == "DEA" or self.tamanho == "DEC":
            self.pv=self.pv*6
            self.peso=self.peso*6
            self.nome+= " Descomunal"
            if self.dano.upper() == '1D2':
                self.dano = "1d6"                
            elif self.dano.upper() == '1D3':
                self.dano = "1d8"
            elif self.dano.upper() == '1D4':
                self.dano = "2d6"
            elif self.dano.upper() == '1D6':
                self.dano = "3d8"
            elif self.dano.upper() == '2D4':
                self.dano = "4d6"
            elif self.dano.upper() == '1D8':
                self.dano = "4d6"
            elif self.dano.upper() == '1D10':
                self.dano = "4d8"
            elif self.dano.upper() == '2D6':
                self.dano = "5d6"
            elif self.dano.upper() == '1D12':
                self.dano = "5d6"
            elif self.dano.upper() == '2D8':
                self.dano = "5d8"
            elif self.dano.upper() == '3D6':
                self.dano = "6d6"            
            elif self.dano.upper() == '3D8':
                self.dano = "6d8"
            else:
                self.dano = "Não especificado"            
                    
        elif self.tamanho == "COA" or self.tamanho == "COC":
            self.pv=self.pv*8
            self.peso=self.peso*8
            self.nome+= " Colossal"
            if self.dano.upper() == '1D2':
                self.dano = "1d8"                
            elif self.dano.upper() == '1D3':
                self.dano = "2d6"
            elif self.dano.upper() == '1D4':
                self.dano = "3d6"
            elif self.dano.upper() == '1D6':
                self.dano = "4d6"
            elif self.dano.upper() == '2D4':
                self.dano = "5d6"
            elif self.dano.upper() == '1D8':
                self.dano = "5d6"
            elif self.dano.upper() == '1D10':
                self.dano = "5d8"
            elif self.dano.upper() == '2D6':
                self.dano = "6d6"
            elif self.dano.upper() == '1D12':
                self.dano = "6d6"
            elif self.dano.upper() == '2D8':
                self.dano = "6d8"
            elif self.dano.upper() == '3D6':
                self.dano = "7d6"            
            elif self.dano.upper() == '3D8':
                self.dano = "7d8"
            else:
                self.dano = "Não especificado"            

    def ObraPrima(self, perso):
        self.nome=self.nome+" Obra Prima"
        self.bba = 1
        self.preco+=30000.0
    def Brutal(self):
        self.nome=self.nome+" Brutal"
        self.dano = self.dano+"+1"
        self.preco+=60000.0
    def Equilibrada(self):
        self.nome=self.nome+" Equilibrada"
        self.dano = self.dano+"(+2 manobras)"
        self.preco+=60000.0
    def Magistral(self):
        self.nome=self.nome+" Magistral"
        self.bba = 2
        self.preco+=90000.0
    def Precisa(self):
        self.nome=self.nome+" Precisa"
        self.preco+=150000.0
        if self.critico.upper()=="-":
            self.critico="-"
        elif self.critico.upper()=="19-20":
            self.critico="18-20"
        elif self.critico.upper()=="18-20":
            self.critico="17-20"
        elif self.critico.upper()=="=17-20":
            self.critico="16-20"
        elif self.critico.upper()=="16-20":
            self.critico="15-20"
        elif self.critico.upper()=="15-20":
            self.critico="14-20"
        else:
            self.critico=self.critico+"/19-20"
    def BanhadaOuro(self):
        self.nome=self.nome+" Banhada a Ouro(+2 Diplomacia)"
        self.preco+=100000.0
    def CravejadaJoias(self):
        self.nome=self.nome+" Cravejada de joias(+2 Enganação)"
        self.preco+=100000.0
    def Macabro(self):
        self.nome=self.nome+" Macabro(+2 Intimidar / -2 Diplomacia)"
        self.preco+=100000.0
    def Macica(self):
        self.nome=self.nome+" Maciça"
        self.preco+=300000.0
        if self.critico.upper()=="-":
            self.critico="-"
        elif self.critico.upper()=="X2":
            self.critico="x3"
        elif self.critico.upper()=="X3":
            self.critico="x4"
        elif self.critico.upper()=="X4":
            self.critico="x5"
        elif self.critico.upper()=="X5":
            self.critico="x6"
        elif self.critico[2].upper()=="/":
            if self.critico[:2].upper()=="X2":
                self.critico="x3/19-20"
            elif self.critico[:2].upper()=="X3":
                self.critico="x4/19-20"
            elif self.critico[:2].upper()=="X4":
                self.critico="x5/19-20"
            elif self.critico[:2].upper()=="X5":
                self.critico="x6/19-20"
        else:
            self.critico="x3"+self.critico
            
    def Material(self, material):
        self.nome=self.nome+" de "+str(material)
        nome=self.nome        
        if material.upper() == "AÇO RUBI":
            self.preco+=150000.0
            self.dano = self.dano+"+1"
        elif material.upper() == "ADAMANTE":
            self.preco+=100000.0
            self.dano = self.dano+"+1"
            self.tamanho=tamanho.upper()
            if self.tamanho == "IN":
                self.Tamanho('DI')            
            elif self.tamanho == "DI":
                self.Tamanho('MI')
            elif self.tamanho == "MI":
                self.Tamanho('PE')            
            elif self.tamanho == "PE":
                self.Tamanho('GRA')            
            elif self.tamanho == "GRA" or self.tamanho == "GRC":
                self.Tamanho('ENA')                
            elif self.tamanho == "ENA" or self.tamanho == "ENC":
                self.Tamanho('DEA')                         
            elif self.tamanho == "DEA" or self.tamanho == "DEC":
                 self.Tamanho('COA')       
            elif self.tamanho == "COA" or self.tamanho == "COC":
                self.Tamanho('COA')
            self.nome=nome
        elif material.upper() == "GELO ETERNO":
            self.preco+=100000.0
            self.dano = self.dano+"+1+1(frio)"
        elif material.upper() == "MADEIRA TOLLON":
            self.preco+=10000.0
            self.dano = self.dano+"+1"
        elif material.upper() == "MATERIA VERMELHA":
            self.preco+=100000.0
            self.dano = self.dano+"+1d4+1"
        elif material.upper() == "MITRAL":
            self.preco+=100000.0
            if self.critico.upper()=="-":
                self.critico="-"
            elif self.critico.upper()=="19-20":
                self.critico="18-20"
            elif self.critico.upper()=="18-20":
                self.critico="17-20"
            elif self.critico.upper()=="17-20":
                self.critico="16-20"
            elif self.critico.upper()=="16-20":
                self.critico="15-20"
            elif self.critico.upper()=="15-20":
                self.critico="14-20"
            else:
                self.critico=self.critico+"/19-20"
        elif material.upper() == "BASILISVO":
            self.preco+=20000.0
        elif material.upper() == "CÂO DO INFERNO":
            self.preco+=50000.0

#Classe Armaduras

class Armaduras:
    def __init__(self):
        self.nome=str()
        self.preco=float()
        self.bonus=int()
        self.destreza=int()
        self.penalidade=int()
        self.peso=float()
        self.tipo=int()
        self.dureza=int()
        self.pv=int()
    def Equipar(self, perso):
        perso.armadura[self.nome]={'BONUS NA CA':self.bonus,'BONUS MAXIMO DE DESTREZA':self.destreza,'PENALIDADE DE ARMADURA':self.penalidade,'PESO':self.peso}
        perso.cargaatual+=self.peso
        
#Classe Escudos

class Escudos:
    def __init__(self):
        self.nome=str()
        self.preco=float()
        self.bonus=int()
        self.destreza=int()
        self.penalidade=int()
        self.peso=float()
        self.tipo=int()
        self.dureza=int()
        self.pv=int()
    def Equipar(self, perso):
        perso.escudo[self.nome]={'BONUS NA CA':self.bonus,'BONUS MAXIMO DE DESTREZA':self.destreza,'PENALIDADE DE ARMADURA':self.penalidade,'PESO':self.peso}
        perso.cargaatual+=self.peso

#Classe Equipamento

class Equipamento:
    def __init__(self):
        self.nome=str()
        self.preco=float()
        self.peso=float()
        self.quantidade=int()
        self.dureza=int()
        self.pv=int()
    def Equipar(self, perso):
        perso.equipamento[self.nome]={self.peso}
        perso.cargaatual+=self.peso
"""            
#Armas
#Adaga        
Adaga=Arma()
Adaga.nome='Adaga'
Adaga.preco=200.0
Adaga.dano='1d4'
Adaga.critico='19-20'
Adaga.distancia=3
Adaga.formadeataque=0
Adaga.peso=0.5
Adaga.tipo='Perfuração'
Adaga.quantidade=1
Adaga.dureza=10
Adaga.pv=2

#Ataque Desarmado
AtaqueDesarmado=Arma()
AtaqueDesarmado.nome='Ataque Desarmado'
AtaqueDesarmado.preco=0.0
AtaqueDesarmado.dano='1d3'
AtaqueDesarmado.critico='x2'
AtaqueDesarmado.distancia=0
AtaqueDesarmado.formadeataque=0
AtaqueDesarmado.peso=0.0
AtaqueDesarmado.tipo='Esmagamento'
AtaqueDesarmado.quantidade=1
AtaqueDesarmado.dureza=0
AtaqueDesarmado.pv=0

#Espada Curta
EspadaCurta=Arma()
EspadaCurta.nome='Espada Curta'
EspadaCurta.preco=1000.0
EspadaCurta.dano='1d6'
EspadaCurta.critico='19-20'
EspadaCurta.distancia=0
EspadaCurta.formadeataque=0
EspadaCurta.peso=1.0
EspadaCurta.tipo='Perfuração'
EspadaCurta.quantidade=1
EspadaCurta.dureza=10
EspadaCurta.pv=2

#Manopla
Manopla=Arma()
Manopla.nome='Manopla'
Manopla.preco=500.0
Manopla.dano='1d4'
Manopla.critico='x2'
Manopla.distancia=0
Manopla.formadeataque=0
Manopla.peso=1.0
Manopla.tipo='Esmagamento'
Manopla.quantidade=1
Manopla.dureza=10
Manopla.pv=2

#Clava
Clava=Arma()
Clava.nome='Clava'
Clava.preco=0.0
Clava.dano='1d6'
Clava.critico='x2'
Clava.distancia=0
Clava.formadeataque=1
Clava.peso=1.5
Clava.tipo='Esmagamento'
Clava.quantidade=1
Clava.dureza=5
Clava.pv=5

#Lança
Lanca=Arma()
Lanca.nome='Lança'
Lanca.preco=200.0
Lanca.dano='1d6'
Lanca.critico='x2'
Lanca.distancia=6
Lanca.formadeataque=1
Lanca.peso=1.5
Lanca.tipo='Perfuração'
Lanca.quantidade=1
Lanca.dureza=10
Lanca.pv=5

#Maça
Maca=Arma()
Maca.nome='Maça'
Maca.preco=1200.0
Maca.dano='1d8'
Maca.critico='x2'
Maca.distancia=0
Maca.formadeataque=1
Maca.peso=6.0
Maca.tipo='Esmagamento'
Maca.quantidade=1
Maca.dureza=10
Maca.pv=5

#Bordão
Bordao=Arma()
Bordao.nome='Bordão'
Bordao.preco=0.0
Bordao.dano='1d6/1d6'
Bordao.critico='x2'
Bordao.distancia=0
Bordao.formadeataque=2
Bordao.peso=2.0
Bordao.tipo='Esmagamento'
Bordao.quantidade=1
Bordao.dureza=5
Bordao.pv=10

#Pique
Pique=Arma()
Pique.nome='Pique'
Pique.preco=200.0
Pique.dano='1d8'
Pique.critico='x2'
Pique.distancia=0
Pique.formadeataque=2
Pique.peso=5.0
Pique.tipo='Perfuração'
Pique.quantidade=1
Pique.dureza=10
Pique.pv=10

#Tacape
Tacape=Arma()
Tacape.nome='Tacape'
Tacape.preco=0.0
Tacape.dano='1d10'
Tacape.critico='x2'
Tacape.distancia=0
Tacape.formadeataque=2
Tacape.peso=4.0
Tacape.tipo='Esmagamento'
Tacape.quantidade=1
Tacape.dureza=5
Tacape.pv=10

#Ácido
Acido=Arma()
Acido.nome='Ácido'
Acido.preco=1000.0
Acido.dano='2d4'
Acido.critico='-'
Acido.distancia=3
Acido.formadeataque=3
Acido.peso=0.5
Acido.tipo='Ácido'
Acido.quantidade=1
Acido.dureza=0
Acido.pv=0

#Água Benta
AguaBenta=Arma()
AguaBenta.nome='Água Benta'
AguaBenta.preco=2500.0
AguaBenta.dano='2d6'
AguaBenta.critico='-'
AguaBenta.distancia=3
AguaBenta.formadeataque=3
AguaBenta.peso=0.5
AguaBenta.tipo='Especial'
AguaBenta.quantidade=1
AguaBenta.dureza=0
AguaBenta.pv=0

#Arco Curto
ArcoCurto=Arma()
ArcoCurto.nome='Arco Curto'
ArcoCurto.preco=3000.0
ArcoCurto.dano='1d6'
ArcoCurto.critico='x3'
ArcoCurto.distancia=12
ArcoCurto.formadeataque=3
ArcoCurto.peso=1.0
ArcoCurto.tipo='Perfuração'
ArcoCurto.quantidade=1
ArcoCurto.dureza=5
ArcoCurto.pv=5

#Azagaia
Azagaia=Arma()
Azagaia.nome='Azagaia'
Azagaia.preco=100.0
Azagaia.dano='1d6'
Azagaia.critico='x2'
Azagaia.distancia=9
Azagaia.formadeataque=3
Azagaia.peso=1.0
Azagaia.tipo='Perfuração'
Azagaia.quantidade=1
Azagaia.dureza=5
Azagaia.pv=2

#Besta Leve
BestaLeve=Arma()
BestaLeve.nome='Besta Leve'
BestaLeve.preco=3500.0
BestaLeve.dano='1d8'
BestaLeve.critico='19-20'
BestaLeve.distancia=18
BestaLeve.formadeataque=3
BestaLeve.peso=3.0
BestaLeve.tipo='Perfuração'
BestaLeve.quantidade=1
BestaLeve.dureza=5
BestaLeve.pv=5

#Fogo Alquimico
FogoAlquimico=Arma()
FogoAlquimico.nome='Fogo Alquimico'
FogoAlquimico.preco=1000.0
FogoAlquimico.dano='1d6'
FogoAlquimico.critico='-'
FogoAlquimico.distancia=3
FogoAlquimico.formadeataque=3
FogoAlquimico.peso=0.5
FogoAlquimico.tipo='Fogo'
FogoAlquimico.quantidade=1
FogoAlquimico.dureza=0
FogoAlquimico.pv=0

#Funda
Funda=Arma()
Funda.nome='Funda'
Funda.preco=0.0
Funda.dano='1d4'
Funda.critico='x2'
Funda.distancia=15
Funda.formadeataque=3
Funda.peso=0.250
Funda.tipo='Esmagamento'
Funda.quantidade=1
Funda.dureza=5
Funda.pv=2

#Granada
Granada=Arma()
Granada.nome='Granada'
Granada.preco=500.0
Granada.dano='4d6'
Granada.critico='-'
Granada.distancia=3
Granada.formadeataque=3
Granada.peso=0.5
Granada.tipo='Fogo'
Granada.quantidade=1
Granada.dureza=0
Granada.pv=0

#Escudo Leve        
EscudoLeve=Arma()
EscudoLeve.nome='Escudo Leve'
EscudoLeve.preco=500.0
EscudoLeve.dano='1d4'
EscudoLeve.critico='x2'
EscudoLeve.distancia=0
EscudoLeve.formadeataque=10
EscudoLeve.peso=3.0
EscudoLeve.tipo='Esmagaento'
EscudoLeve.quantidade=1
EscudoLeve.dureza=10#
EscudoLeve.pv=2#

#Machadinha
Machadinha=Arma()
Machadinha.nome='Machadinha'
Machadinha.preco=600.0
Machadinha.dano='1d6'
Machadinha.critico='x3'
Machadinha.distancia=3
Machadinha.formadeataque=10
Machadinha.peso=2.0
Machadinha.tipo='Corte'
Machadinha.quantidade=1
Machadinha.dureza=10#
Machadinha.pv=2#

#Martelo
Martelo=Arma()
Martelo.nome='Martelo'
Martelo.preco=100.0
Martelo.dano='1d6'
Martelo.critico='x2'
Martelo.distancia=6
Martelo.formadeataque=10
Martelo.peso=1.0
Martelo.tipo='Esmagamento'
Martelo.quantidade=1
Martelo.dureza=10#
Martelo.pv=2#

#Cimitarra
Cimitarra=Arma()
Cimitarra.nome='Cimitarra'
Cimitarra.preco=1500.0
Cimitarra.dano='1d6'
Cimitarra.critico='18-20'
Cimitarra.distancia=0
Cimitarra.formadeataque=11
Cimitarra.peso=2.0
Cimitarra.tipo='Corte'
Cimitarra.quantidade=1
Cimitarra.dureza=10#
Cimitarra.pv=2#

#Escudo Pesado
EscudoPesado=Arma()
EscudoPesado.nome='Escudo Pesado'
EscudoPesado.preco=1500.0
EscudoPesado.dano='1d6'
EscudoPesado.critico='x2'
EscudoPesado.distancia=0
EscudoPesado.formadeataque=11
EscudoPesado.peso=7.0
EscudoPesado.tipo='Esmagamento'
EscudoPesado.quantidade=1
EscudoPesado.dureza=10#
EscudoPesado.pv=2#

#Espada Longa
EspadaLonga=Arma()
EspadaLonga.nome='Espada Longa'
EspadaLonga.preco=1500.0
EspadaLonga.dano='1d8'
EspadaLonga.critico='19-20'
EspadaLonga.distancia=0
EspadaLonga.formadeataque=11
EspadaLonga.peso=2.0
EspadaLonga.tipo='Corte'
EspadaLonga.quantidade=1
EspadaLonga.dureza=10#
EspadaLonga.pv=2#

#Florete
Florete=Arma()
Florete.nome='Florete'
Florete.preco=2000.0
Florete.dano='1d6'
Florete.critico='18-20'
Florete.distancia=0
Florete.formadeataque=11
Florete.peso=1.0
Florete.tipo='Perfuração'
Florete.quantidade=1
Florete.dureza=10#
Florete.pv=2#

#Machado de Batalha
MachadodeBatalha=Arma()
MachadodeBatalha.nome='Machado de Batalha'
MachadodeBatalha.preco=1000.0
MachadodeBatalha.dano='1d8'
MachadodeBatalha.critico='x3'
MachadodeBatalha.distancia=0
MachadodeBatalha.formadeataque=11
MachadodeBatalha.peso=3.0
MachadodeBatalha.tipo='Corte'
MachadodeBatalha.quantidade=1
MachadodeBatalha.dureza=10#
MachadodeBatalha.pv=2#

#Mangual
Mangual=Arma()
Mangual.nome='Mangual'
Mangual.preco=800.0
Mangual.dano='1d8'
Mangual.critico='x2'
Mangual.distancia=0
Mangual.formadeataque=11
Mangual.peso=2.5
Mangual.tipo='Esmagamento'
Mangual.quantidade=1
Mangual.dureza=10#
Mangual.pv=2#

#Martelo de Guerra
MartelodeGuerra=Arma()
MartelodeGuerra.nome='Martelo de Guerra'
MartelodeGuerra.preco=1200.0
MartelodeGuerra.dano='1d8'
MartelodeGuerra.critico='x3'
MartelodeGuerra.distancia=0
MartelodeGuerra.formadeataque=11
MartelodeGuerra.peso=2.5
MartelodeGuerra.tipo='Esmagamento'
MartelodeGuerra.quantidade=1
MartelodeGuerra.dureza=10#
MartelodeGuerra.pv=2#

#Picareta
Picareta=Arma()
Picareta.nome='Picareta'
Picareta.preco=800.0
Picareta.dano='1d6'
Picareta.critico='x4'
Picareta.distancia=0
Picareta.formadeataque=11
Picareta.peso=3.0
Picareta.tipo='Perfuração'
Picareta.quantidade=1
Picareta.dureza=10#
Picareta.pv=2#

#Tridente
Tridente=Arma()
Tridente.nome='Tridente'
Tridente.preco=1500.0
Tridente.dano='1d8'
Tridente.critico='x2'
Tridente.distancia=0
Tridente.formadeataque=11
Tridente.peso=2.0
Tridente.tipo='Perfuração'
Tridente.quantidade=1
Tridente.dureza=10#
Tridente.pv=2#

#Alabarda
Alabarda=Arma()
Alabarda.nome='Alabarda'
Alabarda.preco=1000.0
Alabarda.dano='1d10'
Alabarda.critico='x3'
Alabarda.distancia=0
Alabarda.formadeataque=12
Alabarda.peso=6.0
Alabarda.tipo='Corte'
Alabarda.quantidade=1
Alabarda.dureza=10#
Alabarda.pv=2#

#Alfange
Alfange=Arma()
Alfange.nome='Alfange'
Alfange.preco=7500.0
Alfange.dano='2d4'
Alfange.critico='18-20'
Alfange.distancia=0
Alfange.formadeataque=12
Alfange.peso=4.0
Alfange.tipo='Corte'
Alfange.quantidade=1
Alfange.dureza=10#
Alfange.pv=2#

#Espada Grande
EspadaGrande=Arma()
EspadaGrande.nome='Espada Grande'
EspadaGrande.preco=5000.0
EspadaGrande.dano='2d6'
EspadaGrande.critico='19-20'
EspadaGrande.distancia=0
EspadaGrande.formadeataque=12
EspadaGrande.peso=4.0
EspadaGrande.tipo='Corte'
EspadaGrande.quantidade=1
EspadaGrande.dureza=10#
EspadaGrande.pv=2#

#Foice
Foice=Arma()
Foice.nome='Foice'
Foice.preco=1800.0
Foice.dano='2d4'
Foice.critico='x4'
Foice.distancia=0
Foice.formadeataque=12
Foice.peso=5.0
Foice.tipo='Corte'
Foice.quantidade=1
Foice.dureza=10#
Foice.pv=2#

#Lança Montada
LancaMontada=Arma()
LancaMontada.nome='Lança Montada'
LancaMontada.preco=1000.0
LancaMontada.dano='1d8'
LancaMontada.critico='x3'
LancaMontada.distancia=0
LancaMontada.formadeataque=12
LancaMontada.peso=5.0
LancaMontada.tipo='Perfuração'
LancaMontada.quantidade=1
LancaMontada.dureza=10#
LancaMontada.pv=2#

#Machado Grande
MachadoGrande=Arma()
MachadoGrande.nome='Machado Grande'
MachadoGrande.preco=2000.0
MachadoGrande.dano='1d12'
MachadoGrande.critico='x3'
MachadoGrande.distancia=0
MachadoGrande.formadeataque=12
MachadoGrande.peso=6.0
MachadoGrande.tipo='Corte'
MachadoGrande.quantidade=1
MachadoGrande.dureza=10#
MachadoGrande.pv=2#

#Arco Composto
ArcoComposto=Arma()
ArcoComposto.nome='Arco Composto'
ArcoComposto.preco=7500.0
ArcoComposto.dano='1d6'
ArcoComposto.critico='x3'
ArcoComposto.distancia=18
ArcoComposto.formadeataque=13
ArcoComposto.peso=1.0
ArcoComposto.tipo='Perfuração'
ArcoComposto.quantidade=1
ArcoComposto.dureza=10#
ArcoComposto.pv=2#

#Arco Longo
ArcoLongo=Arma()
ArcoLongo.nome='Arco Longo'
ArcoLongo.preco=10000.0
ArcoLongo.dano='1d8'
ArcoLongo.critico='x3'
ArcoLongo.distancia=24
ArcoLongo.formadeataque=13
ArcoLongo.peso=1.5
ArcoLongo.tipo='Perfuração'
ArcoLongo.quantidade=1
ArcoLongo.dureza=10#
ArcoLongo.pv=2#

#Besta Pesada
BestaPesada=Arma()
BestaPesada.nome='Besta Pesada'
BestaPesada.preco=5000.0
BestaPesada.dano='1d12'
BestaPesada.critico='19-20'
BestaPesada.distancia=27
BestaPesada.formadeataque=13
BestaPesada.peso=4.0
BestaPesada.tipo='Perfuração'
BestaPesada.quantidade=1
BestaPesada.dureza=10#
BestaPesada.pv=2#

#Nunchaku
Nunchaku=Arma()
Nunchaku.nome='Nunchaku'
Nunchaku.preco=200.0
Nunchaku.dano='1d6'
Nunchaku.critico='x3'
Nunchaku.distancia=0
Nunchaku.formadeataque=20
Nunchaku.peso=1.0
Nunchaku.tipo='Esmagamento'
Nunchaku.quantidade=1
Nunchaku.dureza=10#
Nunchaku.pv=2#

#Sai
Sai=Arma()
Sai.nome='Sai'
Sai.preco=500.0
Sai.dano='1d6'
Sai.critico='x2'
Sai.distancia=0
Sai.formadeataque=20
Sai.peso=0.5
Sai.tipo='Esmagamento'
Sai.quantidade=1
Sai.dureza=10#
Sai.pv=2#

#Wakizashi
Wakizashi=Arma()
Wakizashi.nome='Wakizashi'
Wakizashi.preco=31000.0
Wakizashi.dano='1d6'
Wakizashi.critico='19-20'
Wakizashi.distancia=0
Wakizashi.formadeataque=20
Wakizashi.peso=1.0
Wakizashi.tipo='Corte'
Wakizashi.quantidade=1
Wakizashi.dureza=10#
Wakizashi.pv=2#

#Chicote
Chicote=Arma()
Chicote.nome='Chicote'
Chicote.preco=100.0
Chicote.dano='1d3'
Chicote.critico='x2'
Chicote.distancia=0
Chicote.formadeataque=21
Chicote.peso=1.0
Chicote.tipo='Corte'
Chicote.quantidade=1
Chicote.dureza=10#
Chicote.pv=2#

#Espada Bastarda
EspadaBastarda=Arma()
EspadaBastarda.nome='Espada Bastarda'
EspadaBastarda.preco=3500.0
EspadaBastarda.dano='1d10'
EspadaBastarda.critico='19-20'
EspadaBastarda.distancia=0
EspadaBastarda.formadeataque=21
EspadaBastarda.peso=3.0
EspadaBastarda.tipo='Corte'
EspadaBastarda.quantidade=1
EspadaBastarda.dureza=10#
EspadaBastarda.pv=2#

#Katana
Katana=Arma()
Katana.nome='Katana'
Katana.preco=40000.0
Katana.dano='1d10'
Katana.critico='19-20'
Katana.distancia=0
Katana.formadeataque=21
Katana.peso=3.0
Katana.tipo='Corte'
Katana.quantidade=1
Katana.dureza=10#
Katana.pv=2#

#Machado Anão
MachadoAnao=Arma()
MachadoAnao.nome='Machado Anão'
MachadoAnao.preco=3000.0
MachadoAnao.dano='1d10'
MachadoAnao.critico='19-20'
MachadoAnao.distancia=0
MachadoAnao.formadeataque=21
MachadoAnao.peso=4.0
MachadoAnao.tipo='Corte'
MachadoAnao.quantidade=1
MachadoAnao.dureza=10#
MachadoAnao.pv=2#

#Sabre Serrilhado
SabreSerrilhado=Arma()
SabreSerrilhado.nome='Sabre Serrilhado'
SabreSerrilhado.preco=3000.0
SabreSerrilhado.dano='1d10'
SabreSerrilhado.critico='19-20'
SabreSerrilhado.distancia=0
SabreSerrilhado.formadeataque=21
SabreSerrilhado.peso=4.0
SabreSerrilhado.tipo='Corte'
SabreSerrilhado.quantidade=1
SabreSerrilhado.dureza=10#
SabreSerrilhado.pv=2#

#Equipamentos
#Flechas
Flechas=Equipamento()
Flechas.nome='Flechas'
Flechas.preco=100.0
Flechas.peso=1.5
Flechas.quantidade=20
Flechas.dureza=5
Flechas.pv=5
#Virotes
Virotes=Equipamento()
Virotes.nome='Virotes'
Virotes.preco=100.0
Virotes.peso=0.5
Virotes.quantidade=10
Virotes.dureza=5
Virotes.pv=5

#BalasFunda
BalasFunda=Equipamento()
BalasFunda.nome='Balas Funda'
BalasFunda.preco=10.0
BalasFunda.peso=2.0
BalasFunda.quantidade=10
BalasFunda.dureza=10
BalasFunda.pv=5

"""
