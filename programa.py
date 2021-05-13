from time import sleep
import json
import os

while True: # um menu fixo em um loop
    menu = print(
        '''
------------------------------------------
[1] - criar personagem
[2] - personagens criados
[3] - fechar o programa
------------------------------------------
        ''')
    
    resposta= int(input('Escolha sua opção: '))
    os.system('cls')

# Opção 1  
    
    if resposta == 1: # essa primeira parte é para pegar as informações
        N = input('Nome: ')
        L = int(input('Level: '))
        Cl = input('Classe: ')
        F = int(input('Força: '))
        C = int(input('Constituição: '))
        A = int(input('Agilidade: '))
        I = int(input('Inteligencia: '))
        Sa = int(input('Sabedoria: '))
        Ca = int(input('Carisma: '))

        os.system('cls')
        sleep(0.8)
        print('\n')
        print('--------------------------')
        print('nome: {}'.format(N))
        print('level: {}'.format(L))
        print('classe: {}'.format(Cl))
        print('força: {}'.format(F))
        print('constituição: {}'.format(C))
        print('agilidade: {}'.format(A))
        print('inteligencia: {}'.format(I))
        print('sabedoria: {}'.format(Sa))
        print('carisma: {}'.format(Ca))
        print('--------------------------')
        print('\n')
        
        sleep(0.8)
        save = input('Você quer salvar o personagem? ')
        
        sim = 'sim'
        não = 'não'
        
        if save == sim:
            ss = input('Nome da ficha do seu personagem: ')
            # Formato em que vai ser salvo no arquivo as informações
            p1 ={
                'Personagem':{
                    'Nome': '{}'.format(N),
                    'Level': L,
                    'Classe': '{}'.format(Cl),
                    'Forca': F,
                    'Constituicao': C,
                    'Agilidade': A,
                    'Inteligencia': I,
                    'Sabedoria': Sa,
                    'Carisma': Ca,
                },
            }
            
            p1_json = json.dumps(p1, indent=True)
            
            try: # criando o arquivo o arquivo em json salvando as informações
                with open('{}.json'.format(ss), 'x+') as file:
                    file.write(p1_json)
                sleep(1.6)
                os.system('cls')
                print('PERSONAGEM SALVO!!!')
                sleep(1.9)
            
            except: # caso tente criar o arquivo com mesmo nome
                print('\n')
                print('-----------------------------------------')
                print('Essa ficha já existe crie outra!!')
                print('-----------------------------------------')
                sleep(2)
        
        os.system('cls')

# Opção 2
    
    elif resposta == 2: 
        os.system('cls')
        y = input('Qual o nome da sua ficha? ')
        
        try: # lendo o arquivo solicitado no input acima
            with open('{}.json'.format(y), 'r') as pagina:
                s = pagina.read()
                print(s)
        except: # caso não exista o arquivo solicitado
            print('Error!')
        sleep(2)
        input('Aperte enter para voltar ao menu!!')
        sleep(0.8)
        os.system('cls')

# Opção 3

    elif resposta == 3: # opção para a quebra do loop assim acabando o script
        os.system('cls')
        print('Fechando o Programa...!!!')
        sleep(1.3)
        break
    
    else: # caso nenhum das opções possiveis for solicitada
        os.system('cls')
        print('ERRO! Digite uma opção Valida...')
        sleep(1.6)
        os.system('cls')