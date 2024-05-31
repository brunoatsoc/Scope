#include <stdio.h>
#include <stdlib.h>
#include "stack/stack.h"

typedef struct PERSON{
    int age;
    char name[20];
}PERSON;

void automata(char* code);

/*
    Para executar use: gcc -o main main.c stack/stack.c
*/

int main(void){
    // Abre o arquivo onde está o codigo de teste, o nome do arquivo de teste é hello.cic
    FILE* file = fopen("hello.cic", "r");

    //Se o arquivo não existir retorna um erro
    if(file == NULL){
        printf("Error opening file!!!\n");
        return 1;
    }

    // Calcula o tamanho do arquivo
    fseek(file, 0, SEEK_END);
    int size = ftell(file);
    fseek(file, 0, SEEK_SET);

    // Vetor onde o conteudo do arquivo será guardado
    char* contentfile = (char*)malloc(size + 1);

    // Se não puder alocar memória retorna um erro
    if(contentfile == NULL){
        printf("Error to allocate memory!!!\n");
        return 1;
    }

    // Faz  leitura do arquivo e guarda no array contentfile
    fread(contentfile, 1, size, file);
    contentfile[size] = '\0';

    // Fecha o arquivo
    fclose(file);

    automata(contentfile);

    return 0;
}

void automata(char* code){
    int i = 0;

    Q0:
        if(code[i] == ' '){i++; goto Q0;}
        if(code[i] == '\n'){i++; goto Q0;}
        else if(code[i] == 'B'){i++; goto Q1;}
        else if(code[i] >= 'a' && code[i] <= 'z'){i++; goto Q8;}
        else if(code[i] == 'P'){i++; goto Q19;}
        else if(code[i] == 'N'){i++; goto Q26;}
        else if(code[i] == 'F'){i++; goto Q44;}
        else if(code[i] == '\0'){printf("Fim programa"); return;}
    Q1:
        if(code[i] == 'L'){i++; goto Q2;}
    Q2:
        if(code[i] == 'O'){i++; goto Q3;}
    Q3:
        if(code[i] == 'C'){i++; goto Q4;}
    Q4:
        if(code[i] == 'O'){i++; goto Q5;}
    Q5:
        if(code[i] == ' '){i++; goto Q5;}
        else if(code[i] == '_'){i++; goto Q6;}
    Q6:
        if(code[i] >= 'a' && code[i] <= 'z'){i++; goto Q7;}
    Q7:
        if((code[i] >= 'a' && code[i] <= 'z') || (code[i] >= '0' && code[i] <= '9')){i++; goto Q7;}
        else if(code[i] == '_'){i++; goto Q17;}
    Q17:
        // Reconhece abertura de bloco
        printf("Aqui   %c   ", code[i]);
        i++;
        goto Q0;
    Q8:
        if((code[i] >= 'a' && code[i] <= 'z') || (code[i] > '0' && code[i] <= 'z') || (code[i] == '_')){i++; goto Q9;}
    Q9:
        if((code[i] >= 'a' && code[i] <= 'z') || (code[i] > '0' && code[i] <= 'z') || (code[i] == '_')){i++; goto Q9;}
        else if(code[i] == '='){i++; goto Q10;}
        else{goto Q0;}
    Q10:
        if(code[i] >= 'a' && code[i] <= 'z'){i++; goto Q8;}
        else if(code[i] == '-'){i++; goto Q50;}
        else if(code[i] >= '0' && code[i] <= '9'){i++; goto Q11;}
        else if(code[i] == '"'){i++; goto Q14;}
    Q50:
        if(code[i] >= '0' && code[i] <= '9'){i++; goto Q11;}
    Q11:
        if(code[i] >= '0' && code[i] <= '9'){i++; goto Q11;}
        else if(code[i] == '.'){i++; goto Q12;}
        else{goto Q0;}
    Q12:
        if(code[i] >= '0' && code[i] <= '9'){i++; goto Q13;}
    Q13:
        if(code[i] >= '0' && code[i] <= '9'){i++; goto Q13;}
        else if(code[i] == ','){i++; goto Q18;}
        else{goto Q0;}
    Q18:
        if(code[i] >= 'a' && code[i] <= 'z'){i++; goto Q8;}
    Q14:
        if(((code[i] >= ' ' && code[i] <= '~') || code[i] == 9) && code[i] != '"'){i++; goto Q15;}
    Q15:
        if(((code[i] >= ' ' && code[i] <= '~') || code[i] == 9) && code[i] != '"'){i++; goto Q15;}
        else if(code[i] == '"'){i++; goto Q16;}
    Q16:
        if(code[i] == ','){i++; goto Q18;}
        else{goto Q0;}
    Q19:
        if(code[i] == 'R'){i++; goto Q20;}
    Q20:
        if(code[i] == 'I'){i++; goto Q21;}
    Q21:
        if(code[i] == 'N'){i++; goto Q22;}
    Q22:
        if(code[i] == 'T'){i++; goto Q23;}
    Q23:
        if(code[i] >= 'a' && code[i] <= 'z'){i++; goto Q24;}
    Q24:
        if((code[i] >= 'a' && code[i] <= 'z') || (code[i] >= '0' && code[i] <= '9') || (code[i] == '_')){i++; goto Q25;}
    Q25:
        if((code[i] >= 'a' && code[i] <= 'z') || (code[i] >= '0' && code[i] <= '9') || (code[i] == '_')){i++; goto Q25;}
        else{goto Q0;}

    Q26:
        if(code[i] == 'U'){i++; goto Q27;}
    Q27:
        if(code[i] == 'M'){i++; goto Q28;}
    Q28:
        if(code[i] == 'E'){i++; goto Q29;}
    Q29:
        if(code[i] == 'R'){i++; goto Q30;}
    Q30:
        if(code[i] == 'O'){i++; goto Q31;}
    Q31:
        if(code[i] >= 'a' && code[i] <= 'z'){i++; goto Q32;}
    Q32:
        if((code[i] >= 'a' && code[i] <= 'z') || (code[i] >= '0' && code[i] <= '9') || (code[i] == '_')){i++; goto Q33;}
        else if(code[i] == ','){i++; goto Q43;}
        else{goto Q0;}
    Q33:
        if((code[i] >= 'a' && code[i] <= 'z') || (code[i] >= '0' && code[i] <= '9') || (code[i] == '_')){i++; goto Q33;}
        else if(code[i] == '='){i++; goto Q34;}
        else if(code[i] == ','){i++; goto Q43;}
        else{goto Q0;}
    Q34:
        if(code[i] >= 'a' && code[i] <= 'z'){i++; goto Q41;}
        else if(code[i] == '"'){i++; goto Q38;}
        else if(code[i] >= '0' && code[i] <= '9'){i++; goto Q35;}
        else if(code[i] == '-'){i++; goto Q51;}
    Q41:
        if((code[i] >= 'a' && code[i] <= 'z') || (code[i] >= '0' && code[i] <= '9') || (code[i] == '_')){i++; goto Q42;}
    Q42:
        if((code[i] >= 'a' && code[i] <= 'z') || (code[i] >= '0' && code[i] <= '9') || (code[i] == '_')){i++; goto Q42;}
        else if(code[i] == ','){i++; goto Q43;}
        else{goto Q0;}
    Q43:
        if(code[i] >= 'a' && code[i] <= 'z'){i++; goto Q32;}
    Q38:
        if(((code[i] >= ' ' && code[i] <= '~') || code[i] == 9) && code[i] != '"'){i++; goto Q39;}
    Q39:
        if(((code[i] >= ' ' && code[i] <= '~') || code[i] == 9) && code[i] != '"'){i++; goto Q39;}
        else if(code[i] == '"'){i++; goto Q40;}
    Q40:
        if(code[i] == ','){i++; goto Q43;}
        else{goto Q0;}
    Q35:
        if(code[i] >= '0' && code[i] <= '9'){i++; goto Q35;}
        else if(code[i] == '.'){i++; goto Q36;}
        else{goto Q0;}
    Q36:
        if(code[i] >= '0' &&  code[i] <= '9'){i++; goto Q37;}
    Q37:
        if(code[i] >= '0' &&  code[i] <= '9'){i++; goto Q37;}
        else if(code[i] == ','){i++; goto Q43;}
        else{goto Q0;}
    Q51:
        if(code[i] >= '0' && code[i] <= '9'){i++; goto Q35;}
    Q44:
        if(code[i] == 'I'){i++; goto Q45;}
    Q45:
        if(code[i] == 'M'){i++; goto Q46;}
    Q46:
        if(code[i] == '_'){i++; goto Q47;}
    Q47:
        if(code[i] >= 'a' && code[i] <= 'z'){i++; goto Q48;}
    Q48:
        if((code[i] >= 'a' && code[i] <= 'z') || (code[i] >= '0' && code[i] <= '9')){i++; goto Q48;}
        else if(code[i] == '_'){i++; goto Q49;}
    Q49:
        // Fim bloco
        i++;
        goto Q0;
}