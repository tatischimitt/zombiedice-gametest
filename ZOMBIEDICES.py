'''Aluna: Tatiane Schimitt Munhoz
Curso: Tecnólogo em Análise e Desenvolvimento de Sistemas.
Matéria: Raciocínio Computacional (11100010563_20221_01)'''

print('ZOMBIE DICE')
from random import shuffle
import emoji

#definindo os jogadores
class Jogador(object):
    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos

    def rodada(self):
        print(f'Vez do jogador: {self.nome}')
        self.pont_temp = {'Cérebros': 0, 'Tiros': 0}
        self.dados_na_mesa = []
        self.dados = criar_dados()

        while True:
            print('\n' * 2)

#verificar quantidade de dados na mão:
            while len(self.dados_na_mesa) <3:
                self.dados_na_mesa.append(self.dados.pop())

#embaralha as faces dos dados e mostra pro jogador:
            for i in range(2, -1, -1):
                shuffle(self.dados_na_mesa[i].lados)
                self.face_para_cima = self.dados_na_mesa[i].lados[-1]
                print(f'Dado {self.dados_na_mesa[i].cor}, face: {self.face_para_cima}')

                if self.face_para_cima == 'tiro':
                    self.pont_temp['Tiros'] += 1
                    self.dados.append(self.dados_na_mesa.pop(i))
                elif self.face_para_cima == 'cerebro':
                    self.pont_temp['Cérebros'] += 1
                    self.dados.append(self.dados_na_mesa.pop(i))

            print(self.pont_temp)

#verificando tiros tomados e se o jogador deseja permanecer na rodada
            if self.pont_temp['Tiros'] < 3:
                continuar = input('Deseja continuar jogando? (s/n)')
                if continuar != 's':
                    self.pontos += self.pont_temp['Cérebros']
                    print(f'Fim da rodada do jogador {self.nome}. Você possui {self.pontos} cérebros.')
                    break
            else:
                print(f'Você levou 3 tiros ou mais e morreu nesta rodada, perdendo {self.pont_temp} . ')
                break

#definindo os dados
class Dado(object):
    def __init__(self, cor, lados):
        self.cor = cor
        self.lados = lados

def criar_dados():
    vermelho = Dado('Vermelho', ['tiro', 'tiro', 'tiro', 'cerebro', 'passo', 'passo'])
    amarelo = Dado('Amarelo', ['passo', 'passo', 'tiro', 'tiro', 'cerebro', 'cerebro'])
    verde = Dado('Verde', ['tiro', 'cerebro', 'cerebro', 'cerebro', 'passo', 'passo'])
    dados = [vermelho, vermelho, vermelho, amarelo, amarelo, amarelo, amarelo, verde, verde, verde, verde, verde, verde]
    shuffle(dados)
    return dados

#criar jogadores
def criar_jogadores():
    jogadores = []
    while True:
        try:
            total_jogadores = int(input('Informe o número de jogadores:'))
            if total_jogadores > 1:
                break
            else:
                print('Você não pode jogar sozinho!')
        except ValueError:
            print('O número de jogadores tem que ser um número inteiro!')

    for i in range(0, total_jogadores):
        nome = input(f'Digite o nome do jogador {i+1}:')
        este_jogador = Jogador(nome, 0)
        jogadores.append(este_jogador)
    shuffle(jogadores)

    print('A ordem aleatória para jogar é:')
    for cada_jogador in jogadores:
        print(f'Jogador {cada_jogador.nome}')

    return jogadores

if __name__ == '__main__':
#criar jogadores usando a função e armazenando na variável
    jogadores = criar_jogadores()
    game_over = False

#verificar se algum jogador já possui 13 cérebros:
    while game_over == False:
        for cada_jogador in jogadores:
            Jogador.rodada(cada_jogador)
            if cada_jogador.pontos >= 13:
                game_over = True
            jogador_vencedor = cada_jogador.nome

    print('Fim da rodada, Pontuação:')

#mostra pontuação final do jogo
    print('Fim de jogo. Pontuação final:')
    for cada_jogador in jogadores:
        print(f'Jogador {cada_jogador.nome}: {cada_jogador.pontos} pontos.')
        print(f'O jogador vencedor é: {jogador_vencedor}. Parabéns!!!!')