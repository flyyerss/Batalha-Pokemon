#imports

import os
from time import sleep
from random import randint
os.system("cls")

# Comandos

def continuar():
    continuar = input('Aperte qualquer botão para continuar: ')
def limpa_tela():
    os.system("cls")

#Personagens

class Personagens:
    def __init__(self, nome, vida, atk, cura):
        self.nome = nome
        self.vida = vida
        self.atk = atk
        self.cura = cura
    def recive_dmg (self,vida,dmg):
        self.vida = vida - dmg
    def heal(self,):
        self.vida += self.cura
    pass

Monstro = Personagens('Monstrengo' , 960, 135, 35)
Charmander = Personagens('Charmander' , 800, 160, 50)
Bulbasaur = Personagens('Bulbasaur' , 900, 140, 70)
Pikachu = Personagens('Pikachu' , 600, 200, 80)
Personagem = Personagens

vidamax = ''                    #guardando o valor de vida maxima para quando personagem 
monster_vidamax = Monstro.vida  #securar com a vida cheia não ultrapassar a vida maxima

#Start Play

print('''    
         Bem vindo a batalha pokemon
            Escolha seu pokemon!!
                [1]Charmander
                [2]Bulbasaur
                [3]Pikachu
                [4]Sair
                ''')
while True:
    escolha = input(str('Digite sua escolha: '))
    limpa_tela()
    if escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4":
        print('''    
                         escolha invalida
        Escolha Novamente e corretamente o seu pokemon!!
                            [1]Charmander
                            [2]Bulbasaur
                            [3]Pikachu
                            [4]Sair
            ''')
        while escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4":
            escolha = input(str('Digite sua opção novamente!'))
    if escolha == "1":
        Personagem = Charmander
        vidamax = Charmander.vida
    if escolha == "2":
        Personagem = Bulbasaur
        vidamax = Bulbasaur.vida
    if escolha == "3":
        Personagem = Pikachu
        vidamax = Pikachu.vida
    if escolha == '4':
        print('Você saiu do jogo')
        break
    if escolha == '1' or escolha == '2' or escolha == '3':
        limpa_tela()
        print(f"      você escolheu o {Personagem.nome}")
        print(f'''       Atributos do {Personagem.nome}
            vida {Personagem.vida}
            dano {Personagem.atk}
            cura {Personagem.cura} ''')
    continuar()
    limpa_tela()
    print(f"você lutará contra o monstro {Monstro.nome}!")
    print(f'''       Atributos do {Monstro.nome}
                vida {Monstro.vida}
                dano {Monstro.atk}
                cura {Monstro.cura}''')
    continuar()
    limpa_tela()
    break

#In game
while Personagem.vida >0:
    limpa_tela()
    print(f''' 
        Sua Vida = {Personagem.vida}   
        Oque você deseja fazer? {Monstro.nome} ainda tem {Monstro.vida} de vida!
            [1]Atacar
            [2]Curar
            [3]Passar o Turno
            [4]Sair do jogo
            ''')

    #Pessoa jogando

    escolha = input(str('Digite sua Ação: '))
    if escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4":
        limpa_tela()
        print('''    
                         escolha invalida
        Escolha Novamente e corretamente o seu pokemon!!
                            [1]Atacar
                            [2]Curar
                            [3]Passar o turno
            ''')
        while escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4":
            escolha = input(str('Digite sua opção novamente!'))
    if escolha == '1':
         Monstro.recive_dmg(Monstro.vida, Personagem.atk)
         limpa_tela()
         print(f'Você atacou o monstro! e deu {Personagem.atk} de dano')
         sleep(1)
    if escolha == '2':
        Personagem.heal()
        limpa_tela()
        print(f"você se curou em {Personagem.cura} de vida!")
        sleep(1)
    if escolha == '3':
        limpa_tela()
        print('você passou o turno')

        # LIMITE DE VIDA #
    if Personagem.vida > vidamax:
        Personagem.vida = vidamax

    if escolha =='4':
        break
    if Monstro.vida <0:
        break
    sleep(1)

    #Npc jogando

    npc_random = randint(1,3)
    if npc_random == 1:
         Personagem.recive_dmg(Personagem.vida, Monstro.atk)
         limpa_tela()
         print(f'O Monstro te atacou! e deu {Monstro.atk} de dano')
         sleep(2)
    if npc_random == 2:
        Monstro.heal()
        limpa_tela()
        print(f"O Monstro se curou em {Monstro.cura} de vida!")
        sleep(2)
    if npc_random == 3:
        limpa_tela()
        print('O Monstro passou o turno')
        sleep(2)
    if Monstro.vida > monster_vidamax:
        Monstro.vida = monster_vidamax
limpa_tela()

#Ganhou ou perdeu
if Monstro.vida <= 0:
    print(f'Você venceu!!! conseguiu matar o {Monstro.nome}!')
if escolha == '4':
    print(f'Você escolheu sair correndo do {Monstro.nome}!')
if Personagem.vida <=0:
    print(f'Você Morreu para o {Monstro.nome} derrota!! :c ')
print('Fim de jogo')
