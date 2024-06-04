import re
import string
import copy

class Table:
    def __init__(self):
        self.token = []
        self.lexema = []
        self.tipo = []
        self.valor = []
    
    def add_info(self, token, lexema, tipo, valor):
        self.token.append(token)
        self.lexema.append(lexema)
        self.tipo.append(tipo)
        self.valor.append(valor)
    
    def search_variable(self, var):
        for i in range(len(self.lexema)):
            if var == self.lexema[i]:
                return True, i
        return False, -2

    def __str__(self):
        return f'Table(token={self.token}, lexema={self.lexema}, tipo={self.tipo}, valor={self.valor})'

def ler_arquivo(file_path):
    with open(file_path, 'r') as file:
        conteudo = file.read()
        
    # Expressão regular para encontrar palavras e strings entre aspas
    pattern = re.compile(r'\".*?\"|\S+')
    
    # Encontrar todas as correspondências
    matches = pattern.findall(conteudo)
    
    return matches

def automata(code):
    i = 0
    state = "Q0"
    stack = []
    table = Table()

    while i < len(code):
        if state == "Q0":
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
                    print(f"Variavel {code[i]} não declarada.")
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
                    print(f"Não é possivel redeclarar variavel {code[i]}.")
                    if code[i + 1] == ",":
                        state = "Q9"
                        i += 1
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
                    print(f"Não é possivel redeclarar variavel {code[i]}")
                    if code[i + 1] == ",":
                        state = "Q9"
                        i +=1
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
                    print(f"Não é possivel redeclarar variavel {code[i]}.")
                    if code[i + 1] == ",":
                        state = "Q14"
                        i += 1
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
                    print(f"Não é possivel redeclarar variavel {code[i]}")
                    if code[i + 1] == ",":
                        state = "Q14"
                        i +=1
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
                    print(f"Variavel {code[i]} não declarada.")
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
                print(f"Variavel {code[i]} não declarada.")
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
                if search_stack_table(stack, code[i]) != -2:
                    state = "Q22"
                    i += 1
                else:
                    print(f"Variavel {code[i]} não declarada.")
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
                print(f"Erro: Tipo da variavel '{stack[x].lexema[y]}' não é compativel com {code[i - 1]}.")
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
                print(f"Erro: Tipo da variavel '{stack[x].lexema[y]}' não é compativel com {code[i - 1]}.")
                if code[i] == ",":
                    state = "Q20"
                    i += 1
                else:
                    state = "Q0"
        #elif state == "Q22":


def search_stack_table(stack, code):
    var = 0
    for i in range(len(stack) - 1, -1, -1):
        x = stack[i]
        tf, pos = x.search_variable(code)
        if tf:
            var = stack[i].valor[pos]
            return i, pos
    return -2, -2

def is_tk_block(code):
    if code[0] == "_":
        return True
    else:
        False

def is_identifier(code):
    characters = string.ascii_lowercase

    if code[0] in characters:
        return True
    else:
        return False

def is_string(code):
    if code[0] == "\"":
        return True
    else:
        return False

def is_number(code):
    if is_string(code[0]):
        return False
    else:
        return True

code = ler_arquivo("hello.cic")
#print(code)
automata(code)

# stack = []
# table = Table()
# table.add_info("a", "b", "c", "d")
# stack.append(copy.deepcopy(table))
# print(stack[0])
# table.lexema = []
# table.token = []
# table.tipo = []
# table.valor = []
# print(stack[0])
# stack[0].lexema[0] = "Bruno"
# print(stack[0])