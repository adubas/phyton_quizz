# coding: utf-8
from __future__ import print_function, unicode_literals

# NOTE: Esse quiz foi feito em python 3.

# NOTE: definição das perguntas e respostas de cada nível usando dic, que facilita o processo seguinte.

perguntas = {
    'a': {
        'frase': "O arquiteto _1_ é um dos principais arquitetos brasileiros, nascido na cidade de _2_ ele é conhecido por ter feito o _3_ em Brasília, cujo nome oficial é Palácio Nereu Ramos e que é um dos edifícios que fazem parte da _4_",
        'resposta': ['Oscar Niemeyer', 'Rio de Janeiro', 'Congresso Nacional', 'Praça dos três poderes']
    },
    'b': {
        'frase': "A arquiteta _1_ foi quem projeto o MASP. Antoni Gaudí levou 40 anos para projetar a _2_ e acabou falecendo sem tê-lo vista concluida. Na realidade foi _3_ quem projetou Brasília. Nascido em 28 de julho de 1951, _4_, foi quem projetou a Ponte da Mulher em Buenos Aires", 
        'resposta': ['Lina Bo Bardi', 'Sagrada Família', 'Lúcio Costa']
    },
    'c': {
        'frase': "_1_ é um conceituado arquiteto japonês que nunca se formou em arquitetura. As pirâmedes do Louvre foram feitas por _2_. O elemento arquitetonico _3_ era frequentemente usado por Gaudí em suas obras. _4_, foi um artística plástico brasileiro que ficou conhecido mundialmente por realizar projetos paisagistos", 
        'resposta': ['Tadao Ando', 'Ieoh Ming Pei', 'parabólico cantenário', 'Roberto Burle Marx']
    }
}


def grau_dificuldade(nome_jogador):
    """Funcao para escolha do grau de dificuldade. A resposta para pergunta de dificuldade está é validade pelo keys do dic pergunta. """
    print('Este é um quiz de arquitetura!')
    dificuldade = input('Escolha qual nível de dificuldade você quer jogar {}: '.format(', '.join(perguntas.keys()))).lower()
    if dificuldade in perguntas:
        print('Muito bem! {}. Você escolheu: {}'.format(nome_jogador, dificuldade))
        return dificuldade
    return grau_dificuldade(nome_jogador)


def resposta(grau_dificuldade_valor):
    """Funcao para receber resposta do jogador para o nivel de dificuldade escolhido."""
    frase = perguntas[grau_dificuldade_valor]['frase']
    respostas = perguntas[grau_dificuldade_valor]['resposta']
    print('Complete a frase: {}'.format(frase))
    n = 0
    for esperado in respostas:
        valor = input('Qual o valor para a lacuna _{}_: '.format(n + 1))
        if valor != esperado:
            print('Não é bem isso.')
            return False
        n += 1
    return True


def jogo():
    """Estruturacao do jogo. Onde todas as definições são atreladas para fazer o quiz funcionar.
    Aqui também está formatado o input de quantas chances o jogador quer, se ele digitar um valor 
    que não seja número terá apenas uma chance."""
    print('Bem Vindo ao meu Quiz')
    nome_jogador = input('Por favor digite seu nome: ')
    print('Então vamos começar {} !'.format(nome_jogador))
    rodar = input('Escolha o número de vezes que você quer tentar responder as questões: ')
    rodar = int(rodar) if rodar.isdigit() else 1
    grau_dificuldade_valor = grau_dificuldade(nome_jogador)
    while rodar:
        verificador = resposta(grau_dificuldade_valor)
        if verificador:
            print('Parabéns {}, você ganhou!'.format(nome_jogador))
            return
        else:
            print('Vai, mais uma chance!')
        rodar -= 1
    print('Acho melhor você estudar mais, {}.'.format(nome_jogador))


jogo()