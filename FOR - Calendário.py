#Importa o calendario
import calendar
#Escolher um ano
#tente
try:
    y = int(input("Digite o ano: "))
    #Condicional de erro
    if (1>y or y>9999):
        print ('Escolha outro ano.')
    #Impressão dos meses
    else:
        for i in range (12):
            print (calendar.month(y,i+1))

#Excessão a regra adicionada a condicional de erro
except:
    print ('Escolha outro ano do calendário')
    
