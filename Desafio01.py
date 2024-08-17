"""Descrição
Os domínios de email são essenciais para categorizar e identificar a origem dos contatos, 
facilitando a segmentação e análise dos dados. Sabendo disso, sua função será receber uma string contendo múltiplos emails 
separados por ponto e vírgula e retornar uma lista contendo apenas os domínios de cada um desses emails.

Entrada
A entrada deve receber uma string contendo emails separados por ponto e vírgula: "email;email;email;...". Cada email é uma string.

Saída
Deverá retornar uma lista de strings com os domínios dos emails."""


# Recebe a entrada e armazena na variável "entrada"
entrada = 'ana@example.com;bob@test.com'

def extrair_dominios(emails):
    lista_emails = emails.split(';')
    dominios = []
    for emails in lista_emails:
        dominio = emails.split('@')[1]
        dominios.append(dominio)
    return dominios

print(extrair_dominios(entrada))