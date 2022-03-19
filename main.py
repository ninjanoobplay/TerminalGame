from random import random,randrange
import os


class Heroes:
    name = "Dark Wizard"
    damage = 35
    life = 560
    level = 1
    atack = False
    def PersonAttackOn(self):
        self.attack=True
    def PersonAttackOff(self):
        self.attack=False

FirstPlayer = Heroes()
EnemyPlayer = Heroes()

def main():
    Start()
    action = None
    EnemyAction = None
    luckyNumber = None
    while True:
        CheckVitoryAndDefeat()
        print("1 = Atacar")
        print("2 = Defender")
        print("3 = Status atual")
        action = int(input("Escolha uma ação: "))
        luckyNumber = randomNumber()
        AttackEnemy(luckyNumber,action)
        FirstPlayerDefense(luckyNumber,action)
        PlayerAndEnemyStatus(action)
        EnemyAction = EnemyRandomAction()
        EnemyAttack(EnemyAction)
        EnemyDefense(EnemyAction)
        input("Se Você Ja leu as Informações Acima, Pressione Enter Para Continuar...")
        clear()
    
def Start():
    clear()
    print("-----------------------SEJA BEM VINDO-----------------------")
    print("|                                                          |")
    print("|                                                          |")
    print("|                      TERMINAL GAME                       |")
    print("|                                                          |")
    print("|                                                          |")
    print("------------------------------------------------------------")
    userResponse = input("Você Quer Ler o Tutorial do jogo ?\nDigite S para Sim e N para Não: ")
    if userResponse == "S" or userResponse == "s":
        print("O Jogo Se Passa Com 2 Personagens Onde Estão em uma luta longa para vencer!\nOnde os 2 Possuem Os Mesmos Atributos,Para Vencer Temos um Numero da Sorte,\nSe o numero for Maior ou Igual a 5\nSeu Personagem Vai Executar a Ação,Se for menor que 5,Seu personagem vai errar o ataque ou não vai receber Defesa naquela rodada alem de perder 10 de vida!\nSe a vida de seu Personagem Zerar Com os Ataques do Inimigo Você Perde!\nSe a vida do Personagem Inimigo Zerar Com Seus Ataques Você Ganha!")
        input("Pressione Enter para continuar.")
        clear()
        FirstPlayer.name = str(input("Escolha o Nome do seu Personagem: "))
        print("Seu Personagem Foi Gerado Ele Possui Os Atributos Abaixo:")
        print(F"Nome do Personagem: {FirstPlayer.name}")
        print(F"Dano do Personagem: {FirstPlayer.damage}")
        print(F"Vida do Personagem: {FirstPlayer.life}")
        print(F"Nivel do Personagem: {FirstPlayer.level}")
        print("")
        input("Pressione Enter para continuar.")
        clear()
    else:
        clear()
        print("Iniciando o Jogo...")
        FirstPlayer.name = str(input("Escolha o Nome do seu Personagem: "))
        print("Seu Personagem Foi Gerado Ele Possui Os Atributos Abaixo:")
        print(F"Nome do Personagem: {FirstPlayer.name}")
        print(F"Dano do Personagem: {FirstPlayer.damage}")
        print(F"Vida do Personagem: {FirstPlayer.life}")
        print(F"Nivel do Personagem: {FirstPlayer.level}")
        print("")
        input("Pressione Enter para continuar.")
        clear()

def randomNumber():
    luckyNumber = randrange(1,11)
    return luckyNumber

def AttackEnemy(luckyNumber,action):
    if (action == 1) and (luckyNumber>=5):
        FirstPlayer.PersonAttackOn()
        while FirstPlayer.attack:
            print(f"Seu Numero da Sorte Foi: {luckyNumber}")
            print("A Vida do Inimigo Abaixou de ",EnemyPlayer.life)
            EnemyPlayer.life = (EnemyPlayer.life-FirstPlayer.damage)
            print("Para: ",EnemyPlayer.life)
            print("")
            FirstPlayer.PersonAttackOff()
    elif (action == 1) and (luckyNumber < 5):
        print(f"Você tirou {luckyNumber} no numero da sorte, Por Isso Não Ira Efetivar o Ataque!")
        print("Mais Sorte na Proxima Vez")
        print("")
    else: 
        pass

def EnemyRandomAction():
    EnemyAction = randrange(1,3)
    return EnemyAction

def EnemyAttack(EnemyAction):
    enemyRandomNumber= None
    enemyRandomNumber = randomNumber()
    if (EnemyAction == 1) and (enemyRandomNumber >=5 ):
        EnemyPlayer.PersonAttackOn()
        while EnemyPlayer.attack:
            print(f"O Numero da Sorte Do Inimigo Foi: {enemyRandomNumber}")
            print("O Inimigo Acertou o Ataque em Você!")
            print(f"Sua vida caiu de {FirstPlayer.life}")
            FirstPlayer.life = FirstPlayer.life-EnemyPlayer.damage
            print(F"Para: {FirstPlayer.life}")
            print("")
            EnemyPlayer.PersonAttackOff()
        
    elif (EnemyAction == 1) and (enemyRandomNumber < 5 ):
        print(f"O Numero da Sorte do Inimigo Foi: {enemyRandomNumber}")
        print("O Inimigo Errou o Ataque!")
        print("")
        
    else:
        pass

def EnemyDefense(EnemyAction):
    enemyRandomNumber= None
    enemyRandomNumber = randomNumber()
    DefensiveHealing = 50
    DefensiveHealingFail = 10
    if (EnemyAction == 2) and (enemyRandomNumber >=5 ):
        EnemyPlayer.PersonAttackOff
        print("O Inimigo Se Defendeu Com Sucesso!")
        print(f"Vida Do Inimigo Antes Da Defesa: {EnemyPlayer.life}")
        EnemyPlayer.life = EnemyPlayer.life+DefensiveHealing
        print(f"Vida Do Inimigo Atual: {EnemyPlayer.life}")
    elif (EnemyAction == 2) and (enemyRandomNumber < 5):
        print("A Defesa Do Inimigo Falhou Ele Perdeu 10 De Vida!")
        FirstPlayer.life = FirstPlayer.life-DefensiveHealingFail

def FirstPlayerDefense(luckyNumber, action):
    DefensiveHealing = 50
    DefensiveHealingFail = 10
    if (action == 2) and (luckyNumber >=5):
        FirstPlayer.PersonAttackOff
        print("Você Se Defendeu Com Sucesso!")
        FirstPlayer.life = FirstPlayer.life+DefensiveHealing
    elif (action == 2) and (luckyNumber < 5):
        print("Sua Defesa Falhou Você Perdeu 10 De Vida!")
        FirstPlayer.life = FirstPlayer.life-DefensiveHealingFail
    else:
        pass
    return DefensiveHealing

def CheckVitoryAndDefeat():
    if (FirstPlayer.life <= 0 ):
        print("Sua Vida Chegou A Zero")
        print("Que Pena, Você Perdeuu!!!")
        input("Pressione Enter Para Continuar...")
        clear()
        exit()
    elif (EnemyPlayer.life <= 0 ):
        print("A Vida do Inimigo Chegou A Zero")
        print("Parabens, Você Ganhouu!!!")
        input("Pressione Enter Para Continuar...")
        clear()
        exit()
    else:
        pass

def PlayerAndEnemyStatus(action):
    if (action == 3):
        print("="*15)
        print("Seu Personagem:")
        print(F"Nome do Personagem: {FirstPlayer.name}")
        print(F"Dano do Personagem: {FirstPlayer.damage}")
        print(F"Vida do Personagem: {FirstPlayer.life}")
        print(F"Nivel do Personagem: {FirstPlayer.level}")
        print("="*15)
        print("Personagem Inimigo:")
        print(F"Nome do Personagem: {EnemyPlayer.name}")
        print(F"Dano do Personagem: {EnemyPlayer.damage}")
        print(F"Vida do Personagem: {EnemyPlayer.life}")
        print(F"Nivel do Personagem: {EnemyPlayer.level}")
    else:
        pass

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
main()