# -*- coding: UTF-8 -*-

class Personagem:
    """
    Classe para Criação de Personagens para Tormenta RPG
    """
    def __init__(self):
        self.nome=str()
        self.jogador=str()
        self.raca=str()
        self.classe=dict()
        self.nivel=int()
        self.tendencia=str()
        self.sexo=str()
        self.idade=int()
        self.mutiplicadoridade=1
        self.divindade=str()
        self.tamanho=str()
        self.deslocamento=int()
        self.forca=0
        self.mforca=int()
        self.destreza=0
        self.mdestreza=int()
        self.constituicao=0
        self.mconstituicao=int()
        self.inteligencia=0
        self.minteligencia=int()
        self.sabedoria=0
        self.msabedoria=int()
        self.carisma=0
        self.mcarisma=int()
        self.pvtotal=int()
        self.pvatual=int()
        self.pacao=int()
        self.ca=int()
        self.redano=int()
        self.fortitude=int()
        self.reflexos=int()
        self.vontade=int()
        self.bba=0
        self.bbacac=0
        self.bbaadi=0
        self.armas={'ARMA':{'BBA':0,'DANO':0,'CRITICO':'Dado critico','DISTANCIA':0,'TIPO':'Tipo de dano','PESO':0.0}}      
        self.armadura={'ARMADURA':{'BONUS NA CA':0,'BONUS MAXIMO DE DESTREZA':0,'PENALIDADE DE ARMADURA':0,'PESO':0.0}}
        self.escudo={'ESCUDO':{'BONUS NA CA':0,'BONUS MAXIMO DE DESTREZA':0,'PENALIDADE DE ARMADURA':0,'PESO':0.0}}
        self.itemequipado={'ITEM':{'EFEITO':'Descrição do Efeito','PESO':0.0}}
        #a lista das pericias é [total,treinada,habilidade,penalidade]
        self.pericias={"PERICIA":[0,0,0,0],"ACROBACIA":[0,0,2,0],"ADESTRAR ANIMAIS":[0,0,6,0],"ATLETISMO":[0,0,1,0],
                       "ATUACAO DRAMATURGIA":[0,0,6,0],"ATUACAO DANCA":[0,0,6,0],"ATUACAO MUSICA":[0,0,6,0],
                       "ATUACAO ORATORIA":[0,0,6,0],"CAVALGAR":[0,0,2,0],"CONHECIMENTO ARCANO":[0,0,4,0],
                       "CONHECIMENTO ENGENHARIA":[0,0,4,0],"CONHECIMENTO GEOGRAFIA":[0,0,4,0],"CONHECIMENTO HISTORIA":[0,0,4,0],
                       "CONHECIMENTO NATUREZA":[0,0,4,0],"CONHECIMENTO NOBREZA":[0,0,4,0], "CONHECIMENTO RELIGIAO":[0,0,4,0],
                       "CURA":[0,0,5,0],"DIPLOMACIA":[0,0,6,0],"ENGANACAO":[0,0,6,0],"FURTIVIDADE":[0,0,2,0],"IDENTIFICAR MAGIA":[0,0,4,0],
                       "INICIATIVA":[0,0,2,0],"INTIMIDACAO":[0,0,6,0],"INTUICAO":[0,0,5,0],"LADINAGEM":[0,0,2,0],"OBTER INFORMACAO":[0,0,6,0],
                       "OFICIO ALQUIMIA":[0,0,4,0], "OFICIO ALVENARIA":[0,0,4,0], "OFICIO CARPINTARIA":[0,0,4,0],"OFICIO JOALHERIA":[0,0,4,0],
                       "OFICIO METALURGIA":[0,0,4,0],"OFICIO ARTE":[0,0,4,0], "OFICIO PROFISSAO":[0,0,4,0],"PERCEPCAO":[0,0,5,0],"SOBREVIVENCIA":[0,0,5,0],                       
                       }
        self.habilidaderaca={'HABILIDADE':'EFEITO'}
        self.habilidadeclasse={'HABILIDADE':'EFEITO'}
        self.equipamento={'Item':'Peso'}
        self.qnttalentos=int()
        self.talentos={'HABILIDADE':'EFEITO'}
        self.magias={'MAGIA':'EFEITO'}
        self.idiomas=list()
        self.pmtotal=int()
        self.pmatual=int()
        self.xpatual=int()
        self.xpproxnivel=int()
        self.historia=str()
        self.personalidade=str()
        self.aparencia=str()
        self.informacoes={"campanha":'',"mestre":'',"outros jogadores":''}
        self.peso=float()
        self.cargan=float()
        self.cargam=float()
        self.aumhabili=int()
        self.gradpericiast=int()
        self.gradpericiasnt=int()
        self.espaco=float()
        self.alcance=float()
        self.modificadordetamanho=int()
        self.modificadordetamanhop=int()
    def Gerar(self):
        """
        Faz todos os calculos e gera o Personagem
        """
        #Calculo da Idade        
        if self.idade/self.mutiplicadoridade >=35 and self.idade/self.mutiplicadoridade < 50:
            self.forca+=-1
            self.destreza+=-1
            self.constituicao+=-1
            self.inteligencia+=1
            self.sabedoria+=1
            self.carisma+=1
        elif self.idade/self.mutiplicadoridade >= 50 and self.idade/self.mutiplicadoridade <70:
            self.forca+=-3
            self.destreza+=-3
            self.constituicao+=-3
            self.inteligencia+=2
            self.sabedoria+=2
            self.carisma+=2
        elif self.idade/self.mutiplicadoridade >= 70:
            self.forca+=-6
            self.destreza+=-6
            self.constituicao+=-6
            self.inteligencia+=3
            self.sabedoria+=3
            self.carisma+=3
        #Calculo do tamanho do personagem
        """
            Define o Tamanho do Personagem dependendo da String informada.
            Escolha a sigla correspondente ao tamanho do Personagem:
            "IN" - Infimo
            "DI" - Diminuto
            "MI" - Minimo
            "PE" - Pequeno
            "ME" - Médio
            "GRA" - Grande (alto)
            "GRC" - Grande (comprido)
            "ENA" - Enorme (alto)
            "ENC" - Enorme (comprido)
            "DEA" - Descomunal (alto)
            "DEC" - Descomunal (comprido)
            "COA" - Colossal (alto)
            "COC" - Colossal (comprido)
        """
        self.tamanho=self.tamanho.upper()
        if self.tamanho == "IN":
            self.espaco=0.15
            self.alcance=1.5
            self.modificadordetamanho=8
            self.modificadordetamanhop=16
        elif self.tamanho == "DI":
            self.espaco=0.30
            self.alcance=1.5
            self.modificadordetamanho=4
            self.modificadordetamanhop=12
        elif self.tamanho == "MI":
            self.espaco=0.75
            self.alcance=1.5
            self.modificadordetamanho=2
            sself.modificadordetamanhop=8
        elif self.tamanho == "PE":
            self.espaco=1.5
            self.alcance=1.5
            self.modificadordetamanho=1
            self.modificadordetamanhop=4
        elif self.tamanho == "ME":
            self.espaco=1.5
            self.alcance=1.5
            self.modificadordetamanho=0
            self.modificadordetamanhop=0
        elif self.tamanho == "GRA":
            self.espaco=3.0
            self.alcance=3.0
            self.forca+=4
            self.modificadordetamanho=-1
            self.modificadordetamanhop=-4
        elif self.tamanho == "GRC":
            self.espaco=3.0
            self.alcance=1.5
            self.forca+=4
            self.modificadordetamanho=-1
            self.modificadordetamanhop=-4
        elif self.tamanho == "ENA":
            self.espaco=4.5
            self.alcance=4.5
            self.forca+=8
            self.modificadordetamanho=-2
            self.modificadordetamanhop=-8
        elif self.tamanho == "ENC":
            self.espaco=4.5
            self.alcance=3.0
            self.forca+=8
            self.modificadordetamanho=-2
            self.modificadordetamanhop=-8
        elif self.tamanho == "DEA":
            self.espaco=6.0
            self.alcance=6.0
            self.forca+=12
            self.modificadordetamanho=-4
            self.modificadordetamanhop=-12
        elif self.tamanho == "DEC":
            self.espaco=6.0
            self.alcance=4.5
            self.forca+=12
            self.modificadordetamanho=-4
            self.modificadordetamanhop=-12
        elif self.tamanho == "COA":
            self.espaco=9.0
            self.alcance=9.0
            self.forca+=16
            self.modificadordetamanho=-8
            self.modificadordetamanhop=-16
        elif self.tamanho == "COC":
            self.espaco=9.0
            self.alcance=6.0
            self.forca+=16
            self.modificadordetamanho=-8
            self.modificadordetamanhop=-16
            
        #Calculo de modificadores de Atributo
        self.mforca=(self.forca/2)-5
        self.mdestreza=(self.destreza/2)-5
        self.mconstituicao=(self.constituicao/2)-5
        self.minteligencia=(self.inteligencia/2)-5
        self.msabedoria=(self.sabedoria/2)-5
        self.mcarisma=(self.carisma/2)-5

        #Calculo de Carga
        self.cargan= self.forca*3
        self.cargam= self.forca*10

        #Calculo Classe de Armadura

        chavesa=self.armadura.keys()
        chavese=self.escudo.keys()
        for i in chavesa:
            if i <> "ARMADURA":
                for x in chavese:
                    if x <> "ESCUDO":
                        if self.mdestreza <= self.armadura[i]['BONUS MAXIMO DE DESTREZA']:
                            self.ca=10+(self.nivel/2)+self.mdestreza+self.armadura[i]['BONUS NA CA']+self.escudo[x]['BONUS NA CA']+self.modificadordetamanho
                        elif self.mdestreza > self.armadura[1][2]:
                            self.ca=10+(self.nivel/2)+self.armadura[i]['BONUS NA CA']+self.armadura[i]['BONUS MAXIMO DE DESTREZA']+self.escudoself.escudo[x]['BONUS NA CA']+self.modificadordetamanho
                              
        #Calculo das Resistencias
        self.fortitude=self.mconstituicao+(self.nivel/2)   
        self.reflexos=self.mdestreza+(self.nivel/2)    
        self.vontade=self.msabedoria+(self.nivel/2)

        #Calculo Bonus Base de Ataque
        self.bbacac=self.bba+self.mforca+self.modificadordetamanho
        self.bbaadi=self.bba+self.mdestreza+self.modificadordetamanho
                            
        #Revisar

        #Calculo de Pericias
        self.gradpericiast=self.nivel+3
        self.gradpericiasnt=self.nivel/2
        chaves = self.pericias.keys()
        for x in chaves:
            if self.pericias[x][1]==1:
                    if self.pericias[x][2]==1:
                        self.pericias[x][0]=self.gradpericiast+self.mforca+self.pericias[x][3]
                    elif self.pericias[x][2]==2:
                        self.pericias[x][0]=self.gradpericiast+self.mdestreza+self.pericias[x][3]
                    elif self.pericias[x][2]==3:
                        self.pericias[x][0]=self.gradpericiast+self.mconstituicao+self.pericias[x][3]
                    elif self.pericias[x][2]==4:
                        self.pericias[x][0]=self.gradpericiast+self.minteligencia+self.pericias[x][3]
                    elif self.pericias[x][2]==5:
                        self.pericias[x][0]=self.gradpericiast+self.msabedoria+self.pericias[x][3]
                    elif self.pericias[x][2]==6:
                        self.pericias[x][0]=self.gradpericiast+self.mcarisma+self.pericias[x][3]
            elif self.pericias[x][1]==0:
                    if self.pericias[x][2]==1:
                        self.pericias[x][0]=self.gradpericiasnt+self.mforca+self.pericias[x][3]
                    elif self.pericias[x][2]==2:
                        self.pericias[x][0]=self.gradpericiasnt+self.mdestreza+self.pericias[x][3]
                    elif self.pericias[x][2]==3:
                        self.pericias[x][0]=self.gradpericiasnt+self.mconstituicao+self.pericias[x][3]
                    elif self.pericias[x][2]==4:
                        self.pericias[x][0]=self.gradpericiasnt+self.minteligencia+self.pericias[x][3]
                    elif self.pericias[x][2]==5:
                        self.pericias[x][0]=self.gradpericiasnt+self.msabedoria+self.pericias[x][3]
                    elif self.pericias[x][2]==6:
                        self.pericias[x][0]=self.gradpericiasnt+self.mcarisma+self.pericias[x][3]

        
