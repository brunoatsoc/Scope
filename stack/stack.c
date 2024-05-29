// Includ para as bibliotecas que serão usadas no código
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stack.h" // Aqui ficam as definições das funções, structs e enums que vão ser usados nas funções desse arquivo

/*
    Esse arquivo contem uma biblioteca de funções para a estrutura de dados pilha
    <void* data> significa que a função recebe um ponteiro vazio
    Isso faz com que a pilha seja genérica, ou seja ela pode receber qualquer tipo de dado primitivo
    da linguagem C, e também qualquer struct
*/

// Inicializa a pilha com NULL no topo dela
// Recebe o topo da pilha
void initialize_stack(STACK* stk){
    stk->top = NULL;
}// Fim initialize_stack

// Verifica se a pilha está vazia
// Recebe o topo da pilha
TRUE_FALSE is_empty(STACK* stk){
    if(stk->top == NULL){
        return TRUE;
    }
    return FALSE;
}// Fim is_empty

// Adiciona um elemento no topo da pilha
// Recebe um ponteiro para o topo da pilha, o dado como um ponteiro vazio e o tamanho do tipo de dado
// Os retornos dessa função são feitos pelos parâmetros passados por referência(será retornado pela variavel data)
void push(STACK* stk, void* data, size_t size){
    NODE* new_node = (NODE*)malloc(sizeof(NODE*));

    if(new_node == NULL){
        printf("Stack Overflow!!!");
        exit(-1);
    }

    new_node->data = malloc(size);
    memcpy(new_node->data, data, size);
    new_node->next = stk->top;
    stk->top = new_node;
}// Fim push

// Remove um elemento do topo da pilha
// Recebe um ponteiro para o topo da pilha, o dado como um ponteiro vazio e o tamanho do tipo de dado
// Os retornos dessa função são feitos pelos parâmetros passados por referência(será retornado pela variavel data)
void pop(STACK* stk, void* data, size_t size){
    if(is_empty(stk)){
        printf("Error, stack is empty!!!\n");
        exit(-1);
    }

    NODE* temp_stack = stk->top;
    memcpy(data, temp_stack->data, size);
    stk->top = stk->top->next;

    free(temp_stack->data);
    free(temp_stack);
}// Fim pop

// Remove todos os elementos da pilha e vai livberando memória de cada nó
// Recebe o topo da pilha
void free_stack(STACK* stk){
    NODE* current = stk->top;
    NODE* next_node;

    while(current != NULL){
        next_node = current->next;
        free(current->data);
        free(current);
        current = next_node;
    }
}// Fim free_stack

// Retorna o que tem no topo da pilha
// Recebe um ponteiro para o topo da pilha, o dado como um ponteiro vazio e o tamanho do tipo de dado
// Os retornos dessa função são feitos pelos parâmetros passados por referência(será retornado pela variavel data)
void stack_top(STACK* stk, void* data, size_t size){
    if(is_empty(stk)){
        printf("Error, stack is empty!!!\n");
        exit(-1);
    }

    pop(stk, data, size);
    push(stk, data, size);
}// Fim stack_top