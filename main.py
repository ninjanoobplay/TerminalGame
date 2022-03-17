from random import random,randrange
from time import time


class Heroes:
    name = "LuarHero"
    damage = 5
    life = 650
    level = 1
    atack = False
    def PersonAtackOn(self):
        self.atack=True
    def PersonAtackOff(self):
        self.atack=False

jogador = Heroes()
inimigo = Heroes()

def Start():
    response = input("Você Quer Ler o Tutorial do jogo ?\nDigite S para Sim e N para Não: ")
    if response == "S" or response == "s":
        print("O Jogo Se Passa Com 2 Personagens Onde Estão em uma luta longa para vencer!\nOnde os 2 Possuem Os Mesmos Atributos,Para Vencer Temos um Numero da Sorte,\nSe o numero for Maior ou Igual a 5\n Seu Personagem Vai Executar a Ação,Se for menor que 5,Seu personagem vai errar o ataque ou não vai receber Defesa naquela rodada\nSe a vida de seu Personagem Zerar Com os Ataques do Inimigo Você Perde!\nSe a vida do Personagem Inimigo Zerar Com Seus Ataques Você Ganha!")
        jogador.name = str(input("Escolha o Nome do seu Personagem: "))
        print("Seu Personagem Foi Gerado Ele Possui Os Atributos Abaixo:")
        print(F"Nome do Personagem: {jogador.name}")
        print(F"Dano do Personagem: {jogador.damage}")
        print(F"Vida do Personagem: {jogador.life}")
        print(F"Nivel do Personagem: {jogador.level}")
        
    else:
        print("Iniciando o Jogo...")
        input("Pressione Enter para continuar.")

Start()

while True:
    print("1 = Atacar")
    print("2 = Defender")
    action = int(input("Escolha uma ação: "))
    luckyNumber = randrange(1,11)
    enemyNumber = randrange(1,3)
    if action == 1 and luckyNumber>=5:
        jogador.PersonAtackOn()
        while jogador.atack:
            print(f"Seu Numero da Sorte Foi: {luckyNumber}")
            print("A Vida do Inimigo Abaixou de ",inimigo.life)
            inimigo.life = (inimigo.life-jogador.damage)
            print("Para: ",inimigo.life)
            jogador.PersonAtackOff()
    elif action == 2 and luckyNumber >=5:
        print("Defesa com Sucesso!")
    elif action == 3:
        print("-"*15)
        print("-"*15)
        print("Seu Personagem:")
        print(F"Nome do Personagem: {jogador.name}")
        print(F"Dano do Personagem: {jogador.damage}")
        print(F"Vida do Personagem: {jogador.life}")
        print(F"Nivel do Personagem: {jogador.level}")
        print("-"*15)
        print("-"*15)
        print("Personagem Inimigo:")
        print(F"Nome do Personagem: {inimigo.name}")
        print(F"Dano do Personagem: {inimigo.damage}")
        print(F"Vida do Personagem: {inimigo.life}")
        print(F"Nivel do Personagem: {inimigo.level}")
        print("-"*15)
        print("-"*15)
    else:
        print(f"Seu Numero da Sorte Foi: {luckyNumber}")
        print("Você Errou o ataque")
        print(f"Vida Atual do Inimigo = {inimigo.life}")
