# -*- coding: UTF-8 -*-

from ttk import *
from Tkinter import *
from ObjTRPG.PersoTRPG import *
from ObjTRPG.RacaTRPG import *
import tkMessageBox

class MontyPython :
    def __init__(self, janela):
        self.personagem=Personagem()

        #==========================Configurações=============================#
        
        self.janela=janela        
        self.janela.title("Persocon - Tormenta RPG")

        #========================Frames Principais===========================#
        caixa=Frame(self.janela,borderwidth=3, relief=GROOVE)
        caixa.pack(fill=X, pady= 5 , padx= 5, side=LEFT)
        ficha=Frame(self.janela)
        ficha.pack(fill=X, pady= 5 , padx= 5)
        baner=Frame(caixa,borderwidth=3, relief=RAISED)
        baner.pack(fill=X, pady= 5 , padx= 5)
        
        self.abas = Notebook(caixa)
        aba_habilidades=Frame(self.abas,borderwidth=3, relief=RAISED)
        aba_habilidades.pack()
        aba_racas=Frame(self.abas,borderwidth=3, relief=RAISED)
        aba_racas.pack()
        aba_classes=Frame(self.abas,borderwidth=3, relief=RAISED)
        aba_classes.pack()
        aba_pericias=Frame(self.abas,borderwidth=3, relief=RAISED)
        aba_pericias.pack()
        aba_talentos=Frame(self.abas,borderwidth=3, relief=RAISED)
        aba_talentos.pack()
        aba_equipamentos=Frame(self.abas,borderwidth=3, relief=RAISED)
        aba_equipamentos.pack()
        aba_magias=Frame(self.abas,borderwidth=3, relief=RAISED)
        aba_magias.pack()
        aba_miscelanias=Frame(self.abas,borderwidth=3, relief=RAISED)
        aba_miscelanias.pack()        
        

        #========================Adicionando Abas============================#
        self.abas.add(aba_habilidades,text='Habilidades')
        self.abas.add(aba_racas,text='Raças', state='disabled')
        self.abas.add(aba_classes,text='Classes', state='disabled')
        self.abas.add(aba_pericias,text='Pericias', state='disabled')
        self.abas.add(aba_talentos,text='Talentos', state='disabled')
        self.abas.add(aba_equipamentos,text='Equipamentos', state='disabled')
        self.abas.add(aba_magias,text='Magias', state='disabled')
        self.abas.add(aba_miscelanias,text='Miscelanias', state='disabled')
        self.abas.pack()

        #=============================Banner=================================#
        """logo=PhotoImage(file='img/logo.gif')
        self.logo=Label(baner, image = logo)
        self.logo.image=logo
        self.logo.pack()"""
        
        #=============================Ficha=================================#
        self.ficha_nomep=Label(ficha, text='Nome do Personagem:',  width=48, anchor='w',borderwidth=3, relief=GROOVE)
        self.ficha_nomep.grid(row=1, column=1, columnspan=3)
        self.ficha_nomej=Label(ficha, text='Nome do Jogador:', width=30, anchor='w',borderwidth=3, relief=GROOVE)
        self.ficha_nomej.grid(row=1, column=4, columnspan=2)
        self.ficha_raca=Label(ficha, text='Raça:', anchor='w',  width=20,borderwidth=3, relief=GROOVE)
        self.ficha_raca.grid(row=2, column=1)
        self.ficha_classe=Label(ficha, text='Classe:', anchor='w', width=27,borderwidth=3, relief=GROOVE)
        self.ficha_classe.grid(row=2, column=2, columnspan=2)
        self.ficha_nivel=Label(ficha, text='Nivel:', anchor='w', width=14,borderwidth=3, relief=GROOVE)
        self.ficha_nivel.grid(row=2, column=4, sticky=W)
        self.ficha_tendencia=Label(ficha, text='Tendência:', width=15, anchor='w',borderwidth=3, relief=GROOVE)
        self.ficha_tendencia.grid(row=2, column=5, sticky=W)
        self.ficha_sexo=Label(ficha, text='Sexo:', width=20, anchor='w',borderwidth=3, relief=GROOVE)
        self.ficha_sexo.grid(row=3, column=1, sticky=W)
        self.ficha_idade=Label(ficha, text='Idade:', width=9, anchor='w',borderwidth=3, relief=GROOVE)
        self.ficha_idade.grid(row=3, column=2, sticky=W)
        self.ficha_divindade=Label(ficha, text='Divindade:', width=17, anchor='w',borderwidth=3, relief=GROOVE)
        self.ficha_divindade.grid(row=3, column=3, sticky=W)
        self.ficha_tamanho=Label(ficha, text='Tamanho:', width=14, anchor='w',borderwidth=3, relief=GROOVE)
        self.ficha_tamanho.grid(row=3, column=4, sticky=W)
        self.ficha_deslocamento=Label(ficha, text='Deslocamento:', width=15, anchor='w',borderwidth=3, relief=GROOVE)
        self.ficha_deslocamento.grid(row=3, column=5, sticky=W)
        
        self.ficha_for=Frame(ficha,  width=20,borderwidth=3, relief=GROOVE)
        self.ficha_for.grid(row=4, column=1, sticky=W)
        self.ficha_forh=Label(self.ficha_for, text='FOR:', anchor='w',  width=6,borderwidth=3, relief=GROOVE)
        self.ficha_forh.pack(side=LEFT)
        self.ficha_forv=Label(self.ficha_for, text='', anchor='w',  width=6,borderwidth=3, relief=GROOVE)
        self.ficha_forv.pack(side=LEFT)
        self.ficha_formh=Label(self.ficha_for, text='', anchor='w',  width=5,borderwidth=3, relief=GROOVE)
        self.ficha_formh.pack(side=LEFT)

        self.ficha_des=Frame(ficha,  width=20,borderwidth=3, relief=GROOVE)
        self.ficha_des.grid(row=5, column=1, sticky=W)
        self.ficha_desh=Label(self.ficha_des, text='DES:', anchor='w',  width=6,borderwidth=3, relief=GROOVE)
        self.ficha_desh.pack(side=LEFT)
        self.ficha_desv=Label(self.ficha_des, text='', anchor='w',  width=6,borderwidth=3, relief=GROOVE)
        self.ficha_desv.pack(side=LEFT)
        self.ficha_desmh=Label(self.ficha_des, text='', anchor='w',  width=5,borderwidth=3, relief=GROOVE)
        self.ficha_desmh.pack(side=LEFT)

        self.ficha_con=Frame(ficha,  width=20,borderwidth=3, relief=GROOVE)
        self.ficha_con.grid(row=6, column=1, sticky=W)
        self.ficha_conh=Label(self.ficha_con, text='CON:', anchor='w',  width=6,borderwidth=3, relief=GROOVE)
        self.ficha_conh.pack(side=LEFT)
        self.ficha_conv=Label(self.ficha_con, text='', anchor='w',  width=6,borderwidth=3, relief=GROOVE)
        self.ficha_conv.pack(side=LEFT)
        self.ficha_conmh=Label(self.ficha_con, text='', anchor='w',  width=5,borderwidth=3, relief=GROOVE)
        self.ficha_conmh.pack(side=LEFT)

        self.ficha_int=Frame(ficha,  width=20,borderwidth=3, relief=GROOVE)
        self.ficha_int.grid(row=7, column=1, sticky=W)
        self.ficha_inth=Label(self.ficha_int, text='INT:', anchor='w',  width=6,borderwidth=3, relief=GROOVE)
        self.ficha_inth.pack(side=LEFT)
        self.ficha_intv=Label(self.ficha_int, text='', anchor='w',  width=6,borderwidth=3, relief=GROOVE)
        self.ficha_intv.pack(side=LEFT)
        self.ficha_intmh=Label(self.ficha_int, text='', anchor='w',  width=5,borderwidth=3, relief=GROOVE)
        self.ficha_intmh.pack(side=LEFT)

        self.ficha_sab=Frame(ficha,  width=20,borderwidth=3, relief=GROOVE)
        self.ficha_sab.grid(row=8, column=1, sticky=W)
        self.ficha_sabh=Label(self.ficha_sab, text='SAB:', anchor='w',  width=6,borderwidth=3, relief=GROOVE)
        self.ficha_sabh.pack(side=LEFT)
        self.ficha_sabv=Label(self.ficha_sab, text='', anchor='w',  width=6,borderwidth=3, relief=GROOVE)
        self.ficha_sabv.pack(side=LEFT)
        self.ficha_sabmh=Label(self.ficha_sab, text='', anchor='w',  width=5,borderwidth=3, relief=GROOVE)
        self.ficha_sabmh.pack(side=LEFT)

        self.ficha_car=Frame(ficha,  width=20,borderwidth=3, relief=GROOVE)
        self.ficha_car.grid(row=9, column=1, sticky=W)
        self.ficha_carh=Label(self.ficha_car, text='CAR:', anchor='w',  width=6,borderwidth=3, relief=GROOVE)
        self.ficha_carh.pack(side=LEFT)
        self.ficha_carv=Label(self.ficha_car, text='', anchor='w',  width=6,borderwidth=3, relief=GROOVE)
        self.ficha_carv.pack(side=LEFT)
        self.ficha_carmh=Label(self.ficha_car, text='', anchor='w',  width=5,borderwidth=3, relief=GROOVE)
        self.ficha_carmh.pack(side=LEFT)

        self.ficha_pv=Label(ficha, text='PV:', width=9, anchor='w',borderwidth=3, relief=GROOVE)
        self.ficha_pv.grid(row=4, column=2, sticky=W)
        self.ficha_ca=Label(ficha, text='CA:', width=17, anchor='w',borderwidth=3, relief=GROOVE)
        self.ficha_ca.grid(row=4, column=3, sticky=W)
        self.ficha_rd=Label(ficha, text='RD:', width=14, anchor='w',borderwidth=3, relief=GROOVE)
        self.ficha_rd.grid(row=4, column=4, sticky=W)
        self.ficha_pacao=Label(ficha, text='Pontos de Ação:', width=15, anchor='w',borderwidth=3, relief=GROOVE)
        self.ficha_pacao.grid(row=4, column=5, sticky=W)

        self.ficha_fort=Label(ficha, text='FORT:', anchor='w',  width=9,borderwidth=3, relief=GROOVE)
        self.ficha_fort.grid(row=5, column=2, sticky=W)
        self.ficha_ref=Label(ficha, text='REF:', anchor='w',  width=9,borderwidth=3, relief=GROOVE)
        self.ficha_ref.grid(row=6, column=2, sticky=W)
        self.ficha_von=Label(ficha, text='VON:', anchor='w',  width=9,borderwidth=3, relief=GROOVE)
        self.ficha_von.grid(row=7, column=2, sticky=W)
        
        #=============================Aba Habilidade=================================#
        habilidade_frame_esquerda=Frame(aba_habilidades,borderwidth=3, relief=RAISED)
        habilidade_frame_esquerda.pack(side=LEFT, pady= 1 , padx= 1)
        habilidade_frame_direita=Frame(aba_habilidades,borderwidth=3, relief=RAISED)
        habilidade_frame_direita.pack(pady= 1 , padx= 1)
        habilidade_frame_botoes=Frame(aba_habilidades)
        habilidade_frame_botoes.pack(pady= 1 , padx= 1)
        
        Label(habilidade_frame_esquerda, text='FOR').grid(row=1, column=1, pady=3)
        Label(habilidade_frame_esquerda, text='DES').grid(row=2, column=1, pady=3)
        Label(habilidade_frame_esquerda, text='CON').grid(row=3, column=1, pady=3)
        Label(habilidade_frame_esquerda, text='INT').grid(row=4, column=1, pady=3)
        Label(habilidade_frame_esquerda, text='SAB').grid(row=5, column=1,  pady=3)
        Label(habilidade_frame_esquerda, text='CAR').grid(row=6, column=1, pady=3)
        self.for_entry=Entry(habilidade_frame_esquerda,  width=5)
        self.for_entry.grid(row=1, column=2, sticky=W, pady=3)
        self.des_entry=Entry(habilidade_frame_esquerda,  width=5)
        self.des_entry.grid(row=2, column=2, sticky=W, pady=3)
        self.con_entry=Entry(habilidade_frame_esquerda,  width=5)
        self.con_entry.grid(row=3, column=2, sticky=W, pady=3)
        self.int_entry=Entry(habilidade_frame_esquerda,  width=5)
        self.int_entry.grid(row=4, column=2, sticky=W, pady=3)
        self.sab_entry=Entry(habilidade_frame_esquerda,  width=5)
        self.sab_entry.grid(row=5, column=2, sticky=W, pady=3)
        self.car_entry=Entry(habilidade_frame_esquerda,  width=5)
        self.car_entry.grid(row=6, column=2, sticky=W, pady=3)

        l=[self.for_entry,self.des_entry,self.con_entry,
           self.int_entry, self.sab_entry,self.car_entry]
        for i in l: i.insert(0, '10')

        #quebra galho
        Label(habilidade_frame_esquerda,  width=6, height=2).grid(row=7, column=2, sticky=W)
        
        
        Label(habilidade_frame_direita, text='Nome do Personagem').grid(row=1, column=1, sticky=W, columnspan=3)
        self.nome_entry=Entry(habilidade_frame_direita,  width=25)
        self.nome_entry.grid(row=2, column=1, pady=3, padx=3, columnspan=3, sticky=W)
        Label(habilidade_frame_direita, text='Nome do Jogador').grid(row=3, column=1, sticky=W, columnspan=3)
        self.nomej_entry=Entry(habilidade_frame_direita,  width=25)
        self.nomej_entry.grid(row=4, column=1, pady=3, padx=3, columnspan=3, sticky=W)
        Label(habilidade_frame_direita, text='Sexo').grid(row=5, column=1, sticky=W)
        self.sexo_entry=Entry(habilidade_frame_direita,  width=5)
        self.sexo_entry.grid(row=6, column=1, sticky=W, pady=3, padx=3)
        Label(habilidade_frame_direita, text='idade').grid(row=5, column=2, sticky=W)
        self.idade_entry=Entry(habilidade_frame_direita,  width=5)
        self.idade_entry.grid(row=6, column=2, sticky=W, pady=3, padx=3)
        Label(habilidade_frame_direita, text='Divindade').grid(row=5, column=3, sticky=W)
        self.divindade_entry=Entry(habilidade_frame_direita,  width=10)
        self.divindade_entry.grid(row=6, column=3, sticky=W, pady=3, padx=3)
        Label(habilidade_frame_direita, text='Nivel').grid(row=1, column=5, sticky=W)
        self.nivel_spinner=Spinbox(habilidade_frame_direita, from_=1, to=10, width=5)
        self.nivel_spinner.grid(row=2, column=5, sticky=W)

        #quebra galho                                       
        Label(habilidade_frame_direita,  width=21).grid(row=7, column=4, sticky=W)
        
        self.aceitar_habilidade=Button(habilidade_frame_botoes, command=self.aprovar_habilidades, text="Aprovar Habilidades").grid(row=1, column=1, sticky=W, pady=3, padx=3)
        Label(habilidade_frame_botoes,  width=15).grid(row=1, column=2, sticky=W)
        self.rezet_habilidade=Button(habilidade_frame_botoes,  width=17, command=self.limpar_habilidade, text="Limpar").grid(row=1, column=3, sticky=E, pady=3, padx=3)
     
        #=============================Aba Raça=================================#
        
        self.raca_frame_esquerda=Frame(aba_racas,borderwidth=3, relief=RAISED)
        #self.raca_frame_esquerda.pack(side=LEFT, pady= 1 , padx= 1)
        self.raca_frame_esquerda.grid(row=1, column=1, sticky=W) 
        self.raca_frame_direita=Frame(aba_racas,borderwidth=3, relief=RAISED)
        #self.raca_frame_direita.pack(pady= 1 , padx= 1)
        self.raca_frame_direita.grid(row=1, column=2, sticky=W)
        
        #raca_frame_botoes=Frame(self.raca_frame_esquerda)        
        #raca_frame_botoes.pack(side=BOTTOM, pady= 1 , padx= 1)

        raca_label=Label(self.raca_frame_esquerda, text='Raças')
        #raca_label.pack()
        raca_label.grid(row=1, column=1, sticky=W)
 
        l=('Escolha','Anao','Elfo')
        
        self.raca_spinner=Spinbox(self.raca_frame_esquerda, values=l)
        self.raca_spinner.pack()
        #self.raca_spinner.grid(row=2, column=1, sticky=W)
        
        self.current = None
        self.poll()
        
        self.desc_label=Label(self.raca_frame_esquerda)
        self.desc_label.pack()
        #self.desc_label.grid(row=3, column=1, sticky=W, columnspan=3)
       
        #self.aceitar_raca=Button(raca_frame_botoes, command=self.aprovar_habilidades, text="Aprovar Raça").grid(row=1, column=1, sticky=W, pady=3, padx=3)
        
    def poll(self):
        now = self.raca_spinner.get()
        if now != self.current:
            self.list_has_changed(now)
            self.current = now
        self.raca_frame_direita.after(250, self.poll)
    
    def list_has_changed(self, selection):
        if selection == 'Escolha':
            try:
                self.img_raca.destroy()
                self.desc_label['text']=''
            except:
                pass
        elif selection == 'Anao':
            try:
                self.img_raca.destroy()
            except:
                pass
            img_raca=PhotoImage(file=Anao().imagem)
            self.img_raca=Label(self.raca_frame_direita, image = img_raca)
            self.img_raca.image=img_raca
            self.img_raca.pack()
            self.desc_label['text']=Anao().tr
        elif selection == 'Elfo':
            try:
                self.img_raca.destroy()
            except:
                pass
            img_raca=PhotoImage(file=Elfo().imagem)
            self.img_raca=Label(self.raca_frame_direita, image = img_raca)
            self.img_raca.image=img_raca
            self.img_raca.pack()
            self.desc_label['text']=Elfo().tr
    
    def aprovar_habilidades(self):
        try:         
            nivel = int(self.nivel_spinner.get())
            ah=nivel/2
            if ah > 0:
                a=str(nivel)
                b=str(ah)
                tkMessageBox.showinfo("Pontos de Habilidade por nivel", "O Nivel %s da direito a %s pontos de habilidades.\nVocê já dividiu esses pontos?" %(a,b))

            self.personagem.nome=self.nome_entry.get().lower().title()
            self.personagem.jogador=self.nomej_entry.get().lower().title()
            self.personagem.sexo=self.sexo_entry.get().lower().title()
            self.personagem.divindade=self.divindade_entry.get().lower().title()
            self.personagem.idade=int(self.idade_entry.get())
            self.personagem.nivel=int(nivel)
            self.personagem.forca=int(self.for_entry.get())
            self.personagem.destreza=int(self.des_entry.get())
            self.personagem.constituicao=int(self.con_entry.get())
            self.personagem.inteligencia=int(self.int_entry.get())
            self.personagem.sabedoria=int(self.sab_entry.get())
            self.personagem.carisma=int(self.car_entry.get())

            self.ficha_forv['text']=str(self.personagem.forca)
            self.ficha_desv['text']=str(self.personagem.destreza)
            self.ficha_conv['text']=str(self.personagem.constituicao)
            self.ficha_intv['text']=str(self.personagem.inteligencia)
            self.ficha_sabv['text']=str(self.personagem.sabedoria)
            self.ficha_carv['text']=str(self.personagem.carisma)
            
            self.ficha_formh['text']=str((self.personagem.forca/2)-5)
            self.ficha_desmh['text']=str((self.personagem.destreza/2)-5)
            self.ficha_conmh['text']=str((self.personagem.constituicao/2)-5)
            self.ficha_intmh['text']=str((self.personagem.inteligencia/2)-5)
            self.ficha_sabmh['text']=str((self.personagem.sabedoria/2)-5)
            self.ficha_carmh['text']=str((self.personagem.carisma/2)-5)
            
            self.ficha_nomep['text']='Nome do Personagem: '+self.personagem.nome
            self.ficha_nomej['text']='Nome do Jogador: '+self.personagem.jogador
            self.ficha_sexo['text']='Sexo: '+self.personagem.sexo
            self.ficha_idade['text']='Idade: '+str(self.personagem.idade)
            self.ficha_divindade['text']='Divindade: '+self.personagem.divindade
            self.ficha_nivel['text']='Nivel: '+str(self.personagem.nivel)          
            self.abas.tab(self.abas.tabs()[1], state='normal')
            self.abas.select(self.abas.tabs()[1])


            
        except ValueError:
            tkMessageBox.showerror("Erro de Preenchimento", "Preencha todos os campos")
        
    def limpar_habilidade(self):
        l=[self.for_entry,self.des_entry,self.con_entry,
           self.int_entry, self.sab_entry,self.car_entry]
        for i in l:
            i.delete(0, END)
            i.insert(0, '10')
        
        self.nome_entry.delete(0, END)
        self.nomej_entry.delete(0, END)
        self.sexo_entry.delete(0, END)
        self.idade_entry.delete(0, END)
        self.divindade_entry.delete(0, END)
        
swallow=Tk()
MontyPython(swallow)
swallow.mainloop()

