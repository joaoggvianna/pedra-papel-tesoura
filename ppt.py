import random #para ter coisas randomicas

def menu():
    print('**SEJA BEM VINDO AO PEDRA-PAPEL-TESOURA**')

def opcoes():
    print('1. JOGAR')
    print('2. REGRAS')
    print('3. SOBRE O AUTOR')
    print('4. SAIR')

def jogar():
    opcoes = {'1': 'pedra','2': 'papel','3': 'tesoura'} #dicionario: atribui valor(1) a uma chave (pedra)
    pts_jogador = 0
    pts_maquina = 0
    print('*MELHOR DE 3*')
    
    while pts_jogador < 2 and pts_maquina < 2: #ganha quem chegar em 2 primeiro
        print('1. PEDRA')
        print('2. PAPEL')
        print('3. TESOURA')
        mao = input('O que você vai jogar desta vez? ')
        jogador = opcoes.get(mao) #Obtém a jogada do jogador com base na entrada (número), retornando None se inválida.
        if jogador is None:
            print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE!')
            continue

        pc = random.choice(list(opcoes.values())) #dentro dos valores das opções, a máquina escolhe um aleatoriamente

        if jogador == pc:
            print('EMPATE')
        elif (jogador == 'pedra' and pc == 'tesoura') or (jogador == 'papel' and pc == 'pedra') or (jogador == 'tesoura' and pc == 'papel'):
            print('VITRÓRIA DO JOGADOR!')
            pts_jogador += 1
        else:
            print('VITÓRIA DA MÁQUINA!')
            pts_maquina += 1
        print(f'Jogador {pts_jogador} x {pts_maquina} PC')

    if pts_jogador == 2:
        print('Parabéns! Você ganhou!')
    else:
        print('A máquina ganhou, tente na próxima!')
    voltar_menu()

def sair():
    print('Saindo...')

def regras():
    print("Regras:")
    print("- Pedra vence Tesoura")
    print("- Tesoura vence Papel")
    print("- Papel vence Pedra")
    print("Digite sua escolha como: pedra, papel ou tesoura")
    print("Boa sorte!\n")
    voltar_menu()


def autor():
    print('Jogo feito por: João Gabriel Guedes Vianna')
    print('Aluno da PUC-SP cursando Ciência da Computação')
    print('Atualmente no terceiro semestre')
    voltar_menu()
    
def escolher_opcao():
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        return jogar()
    elif opcao == '2':
        return regras()
    elif opcao == '3':
        return autor()
    elif opcao == '4':
        return sair()
    else:
        print('OPÇÃO INVÁLIDA!')
        escolher_opcao()
        
def voltar_menu():
    input('Digite qualquer tecla para voltar ao menu: ')
    main()

def main():
    menu()
    opcoes()
    escolher_opcao()

main()
