# Import para as bibliotecas usadas no programa
import re
import string
import copy

########## IMPORTANTE ##########
# Para o código se lido corretamente precisamos saber de algumas coisas
# Todos os comandos do seu programa devem estar separados por um espaço em branco
# Por exemplo: NUMERO x = 10 , y = 20
# Temos que separar os comandos com espaços para o algoritmo consseguir ler corretamente
# Toda atribuição ou virgula deve estar separada por pelo menos um espaço em branco

# Classe para a tabela onde guardaremos as informações das variaveis
class Table:
    def __init__(self):
        self.token = []
        self.lexema = []
        self.tipo = []
        self.valor = []

    # Adiciona uma linha na tabela
    def add_info(self, token, lexema, tipo, valor):
        self.token.append(token)
        self.lexema.append(lexema)
        self.tipo.append(tipo)
        self.valor.append(valor)

    # Procura uma variavel pelo seu nome em uma tabela especifica
    def search_variable(self, var):
        for i in range(len(self.lexema)):
            if var == self.lexema[i]:
                return True, i
        return False, -2

    # Retorna uma string com as informações do objeto
    def __str__(self):
        return f'Table(token={self.token}, lexema={self.lexema}, tipo={self.tipo}, valor={self.valor})'
# Fim Classe Table

# Metodo para ler o arquivo de entrada com o código fonte
# Nele foi usado uma expressão regular do Python para ser possivel ler uma string
# Pois usei o split para os espaços em branco
def ler_arquivo(file_path):
    with open(file_path, 'r') as file:
        conteudo = file.read()
        
    # Expressão regular para não separar uma CADEIA pelos espaços
    pattern = re.compile(r'\".*?\"|\S+')
    
    # Encontra as conrrespondências para a expressão regular
    matches = pattern.findall(conteudo)
    
    return matches
# Fim ler_arquivo

# Metodo para um automato
# Esse automato foi feito para reconhecer palavras inteiras da linguagem
# Importante falar que não consgui fazer a contagem das linhas corretamente
# Então as mensagens de erro são mostradas com a menssagem correta, porém não com a linha correta onde ele está
def automata(code):
    i = 0 # Contador
    state = "Q0" # Estado inicial
    stack = [] # Pilha
    table = Table() # Tabela
    line = 0 # Contador para as linhas

    # Loop para iterar pelo automato
    # Para cada iteração a variavel state recebe uma string para o proximo estado que deve entrar
    # Cada if trata de uma palavra que no caso é code[i] onde estão os comandos da linguagem
    while i < len(code):
        if state == "Q0":
            line += 1
            if code[i] == "BLOCO":
                state = "Q1"
            elif code[i] == "FIM":
                state = "Q3"
            elif code[i] == "CADEIA":
                state = "Q5"
            elif code[i] == "NUMERO":
                state = "Q10"
            elif code[i] == "PRINT":
                state = "Q15"
            elif is_identifier(code[i]):
                x = search_stack_table(stack, code[i])
                if x[0] != -2:
                    state = "Q17"
                else:
                    print(f"Erro na linha {line}: Variavel '{code[i]}' não declarada.")
            i += 1
        elif state == "Q1":
            if is_tk_block(code[i]):
                stack.append(copy.deepcopy(table))
                table.token = []
                table.lexema = []
                table.tipo = []
                table.valor = []
                state = "Q0"
                i += 1
        elif state == "Q3":
            if is_tk_block(code[i]):
                state = "Q0"
                i += 1
                stack.pop()
        elif state == "Q5":
            if is_identifier(code[i]):
                x = stack[-1].search_variable(code[i])
                if x[0]:
                    print(f"Erro na linha {line}: Não é possivel redeclarar variavel '{code[i]}'.")
                    if code[i + 1] == ",":
                        state = "Q9"
                        i += 1
                    elif code[i + 1] == "=":
                        if code[i + 3] == ",":
                            state = "Q9"
                            i += 4
                        else:
                            state = "Q0"
                            i += 3
                    else:
                        state = "Q0"
                        i += 1
                else:
                    state = "Q6"
                    i += 1
        elif state == "Q6":
            if code[i] == "=":
                state = "Q7"
                i += 1
            elif code[i] == ",":
                stack[-1].add_info("tk_identificador", code[i - 1], "CADEIA", "")
                state = "Q9"
                i += 1
            else:
                state = "Q0"
                stack[-1].add_info("tk_identificador", code[i - 1], "CADEIA", "")
        elif state == "Q9":
            if is_identifier(code[i]):
                x = stack[-1].search_variable(code[i])
                if x[0]:
                    print(f"Erro na linha {line}: Não é possivel redeclarar variavel '{code[i]}'.")
                    if code[i + 1] == ",":
                        state = "Q9"
                        i += 2
                    elif code[i + 1] == "=":
                        if code[i + 3] == ",":
                            state = "Q9"
                            i += 4
                        else:
                            state = "Q0"
                            i += 3
                    else:
                        state = "Q0"
                        i += 1
                else:
                    state = "Q6"
                    i += 1
        elif state == "Q7":
            if is_string(code[i]):
                state = "Q8"
                i += 1
            else:
                print(f"Erro na linha {line}: Tipo da variavel '{code[i - 2]}' não é compativel com tipo '{code[i]}'")
                if code[i + 1] == ",":
                    state = "Q9"
                    i += 2
                else:
                    state = "Q0"
                    i += 1
        elif state == "Q8":
            stack[-1].add_info("tk_identificador", code[i - 3], "CADEIA", code[i - 1])
            if code[i] == ",":
                state = "Q9"
                i += 1
            else:
                state = "Q0"
        elif state == "Q10":
            if is_identifier(code[i]):
                x = stack[-1].search_variable(code[i])
                if x[0]:
                    print(f"Erro na linha {line}: Não é possivel redeclarar variavel '{code[i]}'.")
                    if code[i + 1] == ",":
                        state = "Q14"
                        i += 1
                    elif code[i + 1] == "=":
                        if code[i + 3] == ",":
                            state = "Q14"
                            i += 4
                        else:
                            state = "Q0"
                            i += 3
                    else:
                        state = "Q0"
                        i += 1
                else:
                    state = "Q11"
                    i += 1
        elif state == "Q11":
            if code[i] == "=":
                state = "Q12"
                i += 1
            elif code[i] == ",":
                stack[-1].add_info("tk_identificador", code[i - 1], "NUMERO", "0")
                state = "Q14"
                i += 1
            else:
                state = "Q0"
                stack[-1].add_info("tk_identificador", code[i - 1], "NUMERO", "0")
        elif state == "Q14":
            if is_identifier(code[i]):
                x = stack[-1].search_variable(code[i])
                if x[0]:
                    print(f"Erro na linha {line}: Não é possivel redeclarar variavel '{code[i]}'.")
                    if code[i + 1] == ",":
                        state = "Q14"
                        i += 2
                    elif code[i + 1] == "=":
                        if code[i + 3] == ",":
                            state = "Q14"
                            i += 4
                        else:
                            state = "Q0"
                            i += 3
                    else:
                        state = "Q0"
                        i += 1
                else:
                    state = "Q11"
                    i += 1
        elif state == "Q12":
            if is_number(code[i]):
                state = "Q13"
                i += 1
            else:
                print(f"Erro na linha {line}: Tipo da variavel '{code[i - 2]}' não é compativel com tipo '{code[i]}'.")
                if code[i + 1] == ",":
                    state = "Q14"
                    i += 2
                else:
                    state = "Q0"
                    i += 1
        elif state == "Q13":
            stack[-1].add_info("tk_identificador", code[i - 3], "NUMERO", code[i - 1])
            if code[i] == ",":
                state = "Q14"
                i += 1
            else:
                state = "Q0"
        elif state == "Q15":
            if is_identifier(code[i]):
                x, y = search_stack_table(stack, code[i])
                if x != -2:
                    print(stack[x].valor[y])
                    i += 1
                    state = "Q0"
                else:
                    print(f"Erro na linha {line}: Variavel '{code[i]}' não declarada.")
                    i += 1
                    state = "Q0"
        elif state == "Q17":
            if code[i] == ",":
                state = "Q20"
                i += 1
            elif code[i] == "=":
                state = "Q18"
                i += 1
            else:
                state = "Q0"
        elif state == "Q20":
            if is_identifier(code[i]) and search_stack_table(stack, code[i]) != -2:
                state = "Q17"
                i += 1
            else:
                print(f"Erro na linha {line}: Variavel '{code[i]}' não declarada.")
                if code[i + 1] == ",":
                    state = "Q20"
                    i += 1
                else:
                    state = "Q0"
        elif state == "Q18":
            if is_number(code[i]):
                state = "Q19"
                i += 1
            elif is_string(code[i]):
                state = "Q21"
                i += 1
            elif is_identifier(code[i]):
                v = search_stack_table(stack, code[i])
                if v[0] != -2 or v[0] != -2:
                    state = "Q22"
                    i += 1
                else:
                    print(f"Erro na linha {line}: Variavel '{code[i]}' não declarada.")
                    if code[i + 1] == ",":
                        state = "Q20"
                        i += 2
                    else:
                        state = "Q0"
                        i += 1
        elif state == "Q19":
            x, y = search_stack_table(stack, code[i - 3])
            if stack[x].tipo[y] == "NUMERO":
                stack[x].valor[y] = code[i - 1]
                if code[i] == ",":
                    state = "Q20"
                    i += 1
                else:
                    state = "Q0"
            else:
                print(f"Erro na linha {line}: Tipo da variavel '{stack[x].lexema[y]}' não é compativel com tipo '{code[i - 1]}'.")
                if code[i] == ",":
                    state = "Q20"
                    i += 1
                else:
                    state = "Q0"
        elif state == "Q21":
            x, y = search_stack_table(stack, code[i - 3])
            if stack[x].tipo[y] == "CADEIA":
                stack[x].valor[y] = code[i - 1]
                if code[i] == ",":
                    state = "Q20"
                    i += 1
                else:
                    state = "Q0"
            else:
                print(f"Erro na linha {line}: Tipo da variavel '{stack[x].lexema[y]}' não é compativel com tipo '{code[i - 1]}'.")
                if code[i] == ",":
                    state = "Q20"
                    i += 1
                else:
                    state = "Q0"
        elif state == "Q22":
            x, y = search_stack_table(stack, code[i - 3])
            z, w = search_stack_table(stack, code[i - 1])

            if stack[x].tipo[y] == stack[z].tipo[w]:
                stack[x].valor[y] = stack[z].valor[w]
                if code[i] == ",":
                    state = "Q20"
                    i += 1
                else:
                    state = "Q0"
            else:
                print(f"Erro na linha {line}: Variavel '{stack[x].lexema[y]}' não é do mesmo tipo '{stack[z].lexema[w]}'.")
                if code[i] == ",":
                    state = "Q20"
                    i += 1
                else:
                    state = "Q0"
# Fim automato

# Metodo para procurar uma variavel da tabela dentro da pilha
def search_stack_table(stack, code):
    var = 0
    for i in range(len(stack) - 1, -1, -1):
        x = stack[i]
        tf, pos = x.search_variable(code)
        if tf:
            var = stack[i].valor[pos]
            return i, pos
    return -2, -2
# Fim search_stack_table

# Metodo para verificar se code é uma palavra valida para um bloco
def is_tk_block(code):
    if code[0] == "_":
        return True
    else:
        False
# Fim is_tk_block

# Metodo para verificar se code é uma palavra valida para um identificador
def is_identifier(code):
    characters = string.ascii_lowercase

    if (code[0] in characters) and (code[0] != "\""):
        return True
    else:
        return False
# Fim is_identifier

# Metodo para verificar se code é uma string/CADEIA
def is_string(code):
    if code[0] == "\"":
        return True
    else:
        return False
# Fima is_string

# Metodo para verificar se code é um NUMBER
def is_number(code):
    characters = string.ascii_lowercase

    if (code[0] in characters) or code[0] == "\"":
        return False
    else:
        return True
# Fim is_number

# Chama a função que vai fazer a leitura do arquivo do código fonte
code = ler_arquivo("hello.cic")

# Chama a função que vai vai rodar o codigo fonte no automato
automata(code)