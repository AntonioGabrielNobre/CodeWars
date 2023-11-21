
import os

#FUNÇÃO QUE COLETA OS DADOS NECESSARIO PARA O CACULO DOS PONTOS

def value (bem, mal, controlador = 0):


      # FOI UTILIZADO ARRAYS DEVIDO A FLEXBILIDADE DE ADICIONAR MAIS CAMPOS, RAÇAS E VALORES

        nivel_bem = 0
        nivel_mal = 0


      # LAÇO DE REPETIÇÃO PARA COLETAR OS DADOS DO BEM 
      # ----- AINDA SEM TRATAMENTO DE ERROS OU VALORE INFORMADOS INCORRETAMENTE -------

        racas_bem= [
              "Hobbits", "Homens", "Elfos", "Anões", "Águias", "Magos"
        ]
        racas_mal =[
              "Orcs", "Homens", "Wargs", "Goblins", "Trolls", "Magos"
        ]
        nivel_bem = 0
        nivel_mal = 0

        power_bem = [
              1, 2, 3, 3, 4, 10
        ]
        power_mal = [
              1, 2, 2, 2, 3, 5, 10
        ]


        while controlador < 6:

            bem[controlador] = input("Digite um valor para a raça " + str(racas_bem[controlador]) + ": ")
            controlador += 1

            if controlador == 6:
                  controlador = 0
                  break
            
        os.system('cls')    # LIMPEZA DO CONSOLE DEVIDO A GRANDE CONTIDADE DE DADOS


      # LAÇO DE REPETIÇÃO PARA COLETAR OS DADOS DO MAL 
      # ----- AINDA SEM TRATAMENTO DE ERROS OU VALORE INFORMADOS INCORRETAMENTE -------
 
        while controlador < 6:
              
              mal[controlador] = input("Digite um valor para a raça " + str(racas_mal[controlador]) + ": ")
              controlador += 1

              if controlador == 6:
                    controlador = 0
                    break


        os.system('cls')


      # LAÇOS DE REPETIÇÃO QUE IMPRIME TODOS OS VALORE INFORMADOS PEGANDO 
      # INFORMAÇÕES DAS VARIAVEIS CRIADAS NO INICIO A FUNÇÃO QUE ARMAZENA OS NOMES DAS RAÇAS TANTO DO BEM QUANTO DO MAL

        print("\n\n A equipe do bem ficou da seguinte forma: \n")
        while nivel_bem != 6:
              print(str(racas_bem[nivel_bem]) + " : " + str(bem[nivel_bem]) + " unidades")
              nivel_bem += 1
              if nivel_bem == 14:
                    break
              
        print("\n\n A equipe do mal ficou da seguinte forma: \n")
        while nivel_mal != 6:
              print(str(racas_mal[nivel_mal]) + " : " + str(mal[nivel_mal]) + " unidades")
              nivel_mal += 1
              if nivel_mal == 14:
                    break

# FUNÇÃO PARA CALCULAR O VALOR DO PODER DE CADA RAÇA

def calculos() :

        nivel_bem = 0
        nivel_mal = 0


        nivel_bem = 0
        nivel_mal = 0


        while nivel_bem != 6:
              power_bem[nivel_bem] = int(bem[nivel_bem]) * int(power_bem[nivel_bem])
              power_mal[nivel_mal] = int(mal[nivel_mal]) * int(power_mal[nivel_mal])
              nivel_bem += 1
              nivel_mal += 1


      # VARIAVEIS ZERADAS PARA SEREM USADAS COMO CONTROLADORES NOVAMENTE EM OUTRO LOOP LOGO EM SEGUIDA

        nivel_bem = 0
        nivel_mal = 0

        while nivel_bem != 6:
              print(str(racas_bem[nivel_bem]) + ": " + str(power_bem[nivel_bem]))
              nivel_bem += 1

        while nivel_mal != 6:
              print(str(racas_mal[nivel_mal]) + ": " +  str(power_mal[nivel_mal]))
              nivel_mal += 1

        result = ''
        result = input("\nVoce gostaria de saber a somatoria de todos os poderes das raças ? \n [S / n]")
        if result == 's':
            nivel_bem = 0
            nivel_mal = 0

            total_bem = power_bem[0] + power_bem[1] + power_bem[2] + power_bem[3] + power_bem[4] + power_bem[5]
            total_mal = power_mal[0] + power_mal[1] + power_mal[2] + power_mal[3] + power_mal[4] + power_mal[5]

            print("\n Total de poder do time do bem é: " + str(total_bem))
            print("\n Total de poder do time do mal é: " + str(total_mal))

# FUNÇÃO QUE IRA REALIZR  O CALCULO DOS DADOS COLETADOS DAS FUNÇÕES ANTERIORES

def result():
        print("O nivel de poder do time do bem ficou com o seguinte valor: \n")
        print(power_bem)
        print("\n=O nivel de poder do time do mal ficou com o seguinte valor: \n")
        print(power_mal)



# DEFINIÇÕES DAS VARIAVEIS GLOBAIS DAS FUNÇÕES E OS CHAMADOS DAS MESMAS. 


bem = [0, 0, 0, 0, 0, 0]
mal = [0, 0, 0, 0, 0, 0]

power_bem = [
      1, 2, 3, 3, 4, 10
  ]
power_mal = [
      1, 2, 2, 3, 5, 10
  ]

racas_bem = [
      "Hobbits", "Homens", "Elfos", "Anões", "Águias", "Magos"
  ]
racas_mal = [
      "Orcs", "Homens", "Wargs", "Goblins", "Trolls", "Magos"
  ]

value(bem, mal)

afirmation = input("\n\nDeseja verificar os reultados de poder de cada raça ? \n [S, N]")

if afirmation == 's':
      os.system('cls')
      calculos()
else:
      result()
