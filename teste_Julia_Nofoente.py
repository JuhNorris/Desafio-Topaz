#Transformação do arquivo .txt em um vetor de string
f=open('C:/Users/julia/OneDrive/Área de Trabalho/input.txt')
f = [s.rstrip() for s in f]

#Transformação do conteúdo do vetor f de string para inteiro 
numeros = []
for s in f:
    numeros.append(int(s))

#Inicialização das constantes e lista de usuarios
ttmax = numeros[0]
umax = numeros[1]
usuarios = numeros[2:]

#Verificação das condições de umax e ttmax
if (ttmax >10) or (umax>10) or (ttmax <0) or (umax<0) :
    print("Valores de ttmax e umax não podem ultrapassar 10 e não podem ser negativos!")
else:

    #Criação dos contadores dos servidores, usuarios instantâneos e ticks
    servidor = 0
    conta_usuarios = 0
    tick=0

    #Variável que indica o valor máximo de ticks de acordo com o tamanho do vetor usuário e do intervalo ttmax
    tamanho = len(usuarios) + ttmax + 1

    #Variável booleana para interrupção do looping dos servidores
    verdade = True



    #Ínicio do sistema de servidores e usuários
    while (verdade):

        for tick in range (0,tamanho):
            print("Tick",(tick +1))

            #Verificação da adição de usuários e/ou servidores através do input
            if(tick<len(usuarios)):
                conta_usuarios += usuarios[tick]

                if (usuarios[tick] !=0):
                    servidor +=1

                #Verificação da subtração de usuários e/ou servidores a partir do número ttmax
                if (tick>=ttmax):
                    conta_usuarios -= usuarios[tick-ttmax]
                    if(conta_usuarios % umax == 0):
                        servidor -=1 
                print("Usuarios ativos",conta_usuarios)
                print("Servidores ativos", servidor)

            else:

            #Após o término do vetor usuários, somente decréscimo de usuários e/ou servidores de acordo com o término das tarefas
                if conta_usuarios == 0:
                    servidor = 0
                    verdade = False
                else:
                    conta_usuarios -= usuarios[tick-ttmax]
                    if(conta_usuarios % umax == 0):
                        servidor -=1
                    print("Usuarios ativos",conta_usuarios)
                    print("Servidores ativos", servidor)


    #teste_Julia_Nofoente.py > output.txt 