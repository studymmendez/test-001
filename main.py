# ======================
# ====== NIM 1.01 ======
# == Guilherme Campos ==
# === Matheus Mendes ===
# ======================

#Observação: o jogo pode ficar meio lento, então quando não aparecer os prints(caixa pra digitar), sugerimos que recomeçe denovo.

import random  # Biblioteca usada para gerar escolhas aleatórias (usada pelo bot)
import os  # Biblioteca para interagir com o sistema operacional (limpar terminal)

global IS_NOTEBOOK
try:
  from IPython.display import clear_output  # Função usada para limpar saída no Jupyter Notebook
  IS_NOTEBOOK = True
except:
  IS_NOTEBOOK = False

# Função responsável por limpar a tela (Notebook ou terminal)
def limpar():
  if (IS_NOTEBOOK):
    clear_output()
  else:
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_estado(pilha, historico):  # Mostra o estado atual do jogo (pilhas + o histórico de jogadas)
  limpar()
  print("Historico:")
  for i in range(len(historico)):
    print(historico[i])
  print("=====================")
  for i in pilha:
    print(i * "*")
  print("=====================")

def bot(pilha):  # Lógica do bot: escolhe aleatoriamente uma pilha e uma quantidade para remover
  while True:
      num_pilha = random.randint(0, len(pilha) - 1)
      if pilha[num_pilha] > 0:
        quant_subtrair = random.randint(1, pilha[num_pilha])
        pilha[num_pilha] = pilha[num_pilha] - quant_subtrair
        return pilha, "Bot removeu " + str(quant_subtrair) + " da coluna " + str(num_pilha + 1)

def verifica_jogo(pilha):  # Verifica se o jogo terminou (todas as pilhas zeradas)
  for x in range(len(pilha)):
    if pilha[x] > 0:
      return False
  return True

def user(pilha, name):  # Controla a jogada do usuário (entrada, validação e atualização da pilha)
  while True:
    try:
      num_pilha = int(input(name +" escolha uma pilha (1 a " + str(len(pilha)) + "): "))
      if num_pilha > len(pilha) or num_pilha < 1:
        print("Escolha uma pilha válida")
      else:
        quant_subtrair = int(input("Escolha uma quantidade pra remover (1 a " + str(pilha[num_pilha-1]) + "): "))
        if quant_subtrair > pilha[num_pilha - 1] or quant_subtrair < 1:
          print("Escolha uma quantidade válida")
        else:
          pilha[num_pilha - 1] = pilha[num_pilha - 1] - quant_subtrair
          return pilha, name + " removeu " + str(quant_subtrair) + " da coluna " + str(num_pilha)
    except ValueError:
      print("Entrada inválida. Por favor, digite um número.")

def singlePlay(): #Função que determina o modo de jogo(que é o individual)
  pilha = [3, 5, 6, 9]
  historico = []
  while True:
    imprimir_estado(pilha, historico)
    pilha, user_action = user(pilha, "Jogador")  # Jogada do usuário
    historico.append(user_action)
    pilha = [x for x in pilha if x != 0] # Remove as pilhas vazias
    if(verifica_jogo(pilha)):  # Verifica se o jogo acabou, vendo se as pilhas acabaram, se acabou ele atualiza o estado do jogo e dai vem o return que interrompe o codigo, pra finalizar a partida, com base na ultima jogada, se for no caso do Jogador
      imprimir_estado(pilha, historico)
      return "Jogador venceu"

    pilha, bot_action = bot(pilha) # Jogada do bot
    historico.append(bot_action)
    pilha = [x for x in pilha if x != 0] # Remove as pilhas vazias
    if(verifica_jogo(pilha)):   # O mesmo do comentario mais a cima so que se tratando do bot
      imprimir_estado(pilha, historico)
      return "Sistema venceu"

def onlyPlayers():  # Modo PvP: apenas com 2 jogadores humanos alternando em cada turno
  pilha = [3, 5, 6, 9]
  historico = []
  while True:
    for jogador in ["Jogador01", "Jogador02"]: # Alterna entre os dois jogadores
      imprimir_estado(pilha, historico)
      pilha, user_action = user(pilha, jogador)
      historico.append(user_action)
      pilha = [x for x in pilha if x != 0] # Remove pilhas zeradas
      if verifica_jogo(pilha): # Checa se alguém venceu
        imprimir_estado(pilha, historico)
        return f"{jogador} venceu"

sair = False
while sair == False: # Loop principal (roda até o usuário decidir sair)
  limpar()
  modo = input("Digite qual modo de jogo você quer jogar (solo/pvp), ou digite 'help' para saber mais: ").lower()
  while True:
    if modo == "solo":
      limpar()
      res = singlePlay() # Executa o modo solo
      print(res)
      break
    elif modo == "help":
      limpar()
      print("Jogo:\n • Existem várias pilhas de objetos (*).\n • Em cada turno, escolha uma pilha e remova quantos quiser (mínimo 1).\n • Os jogadores se alternam nas jogadas.\n • Pilhas vazias são removidas automaticamente.\n • Objetivo: ser quem remove o último objeto e vence o jogo.\nModos de jogo:\n • Solo: você joga contra o sistema (bot), que faz jogadas automáticas.\n • PvP: dois jogadores humanos se alternam a cada turno.\n")
      break
    elif modo == "pvp":
      limpar()
      res = onlyPlayers() # Executa o modo somente jogadores(pvp)
      print(res)
      break
    else:
      modo = input("Digite uma opção válida (solo/pvp): ").lower()

  saida = input("Digite 'j' para jogar mais uma vez ou 's' para sair: ").lower()
  while True:
    if saida == "j":
      print("Novo jogo") # Reinicia o jogo
      break
    elif saida == "s":
      limpar()
      print("Até a proxima")
      sair = True # Encerra o loop principal
      break
    else:
       saida = input("Digite uma opção válida (j/s): ").lower()