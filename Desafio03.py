'''Descrição
Você está desenvolvendo um sistema de monitoramento de temperaturas para uma estação meteorológica. 
O seu script deve processar os dados brutos de temperaturas e converter esses dados de Celsius para Fahrenheit.

Para converter uma temperatura de Celsius para Fahrenheit, utiliza-se a fórmula matemática:

TF = (TC × 9/5) + 32

Onde:

TF representa a temperatura em graus Fahrenheit,
TC representa a temperatura em graus Celsius.

Entrada
A entrada deve receber uma string com valores numéricos separados por “,” (vírgula) 
representando as temperaturas em graus Celsius.

Saída
Deverá retornar uma lista de valores numéricos representando as temperaturas convertidas para Fahrenheit.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.0,10,20,30,40 '''

# Recebe a entrada do usuário como uma string e divide essa string nos caracteres ',' (vírgula),
temperaturas_celsius = ('0,10,20,30,40').split(',')

# função chamada converter_celsius_para_fahrenheit que recebe uma lista de strings
def converter_celsius_para_fahrenheit(temperaturas_celsius):
    temperaturas_fahrenheit = []
    temperaturas_celsius = [float(temp) for temp in temperaturas_celsius]
    # TODO: Calcule as temperaturas em Fahrenheit para cada temperatura em Celsius convertida para float
    for temp in temperaturas_celsius:
        conv = (temp*9/5)+32
        temperaturas_fahrenheit.append(conv)
    
    
    return temperaturas_fahrenheit

# Imprime o resultado das temperaturas convertidas para Fahrenheit.
print(converter_celsius_para_fahrenheit(temperaturas_celsius))