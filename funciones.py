#Funciones
#Def name_fuction():
# code


#Funcion sin parametros
#Funcion sin retorno

def saluda():
    print("Hola prros")
    
saluda()

#parametros sin retornos

def duplica(number):
    print(number*2)

duplica(23)

def suma(num1, num2):
    print(num1+num2)

suma(12,15)

#parametros opcionales
def lista_drinks(d1="Beer", d2="water"):
    print(d1)
    print(d2)

lista_drinks("Tequila")
lista_drinks()
lista_drinks("Tequila", "Juice")