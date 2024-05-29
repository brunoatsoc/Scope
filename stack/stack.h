#ifndef STACK_H

#define STACK_H

/*
    Aqui temos a definição de tudo que estamos usando no arquivo stack.c
*/

// Definição dos structs
// Struct para os nós da pilha
typedef struct NODE{
    void* data; // Ponteiro vazio para guardar qualquer tipo de dado
    struct NODE* next; // Ponteiro para o proximo nó
}NODE;

// Struct para a pilha
typedef struct STACK{
    NODE* top; // Ponteiro para o proximo nó
}STACK;
// Fim definição dos structs

// Definição do enum
// Enum para podermos usar FALSE e TRUE ao invés de 0 ou 1
typedef enum{
    FALSE, TRUE
}TRUE_FALSE;
// Fim definição do enum

// Definição das funções questão em stack.c
void initialize_stack(STACK* stk);
TRUE_FALSE is_empty(STACK* stk);
void push(STACK* stk, void* data, size_t size);
void pop(STACK* stk, void* out, size_t size);
void free_stack(STACK* stk);
void stack_top(STACK* stk, void* data, size_t size);
// Fim definições das funções

#endif