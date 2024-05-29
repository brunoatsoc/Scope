#include <stdio.h>
#include "stack/stack.h"

typedef struct PERSON{
    int age;
    char name[20];
}PERSON;

/*
    Para executar use: gcc -o main main.c stack/stack.c
*/

int main(void){
    STACK s;
    int var = 10;
    int var1 = 20;
    int var2 = 30;
    int var3 = 40;
    int var4 = 50;

    initialize_stack(&s);

    push(&s, &var, sizeof(int));
    push(&s, &var1, sizeof(int));
    push(&s, &var2, sizeof(int));
    push(&s, &var3, sizeof(int));
    push(&s, &var4, sizeof(int));

    int popVar;
    pop(&s, &popVar, sizeof(int));
    printf("%d\n", popVar);

    int popVar1;
    pop(&s, &popVar1, sizeof(int));
    printf("%d\n", popVar1);

    int popVar2;
    pop(&s, &popVar2, sizeof(int));
    printf("%d\n", popVar2);

    int popVar3;
    pop(&s, &popVar3, sizeof(int));
    printf("%d\n", popVar3);

    int popVar4;
    pop(&s, &popVar4, sizeof(int));
    printf("%d\n", popVar4);

    free_stack(&s);

    PERSON p = {24, "Bruno"};
    PERSON p2 = {22, "Flavia"};
    PERSON p3 = {20, "Coito"};
    PERSON p4 = {20, "Kakau"};
    PERSON p5 = {24, "Guga"};
    PERSON p6 = {69, "Predo"};
    PERSON p7 = {24, "Valter"};
    PERSON p8 = {22, "Fotana"};
    PERSON p9 = {24, "Luiz"};
    STACK s2;

    initialize_stack(&s2);

    push(&s2, &p, sizeof(PERSON));
    push(&s2, &p2, sizeof(PERSON));
    push(&s2, &p3, sizeof(PERSON));
    push(&s2, &p4, sizeof(PERSON));
    push(&s2, &p5, sizeof(PERSON));
    push(&s2, &p6, sizeof(PERSON));
    push(&s2, &p7, sizeof(PERSON));
    push(&s2, &p8, sizeof(PERSON));
    push(&s2, &p9, sizeof(PERSON));

    pop(&s2, &p9, sizeof(PERSON));
    pop(&s2, &p9, sizeof(PERSON));
    pop(&s2, &p9, sizeof(PERSON));
    pop(&s2, &p9, sizeof(PERSON));
    pop(&s2, &p9, sizeof(PERSON));
    pop(&s2, &p9, sizeof(PERSON));
    pop(&s2, &p9, sizeof(PERSON));
    pop(&s2, &p9, sizeof(PERSON));

    PERSON topPerson;
    stack_top(&s2, &topPerson, sizeof(PERSON));
    printf("%s\n", topPerson.name);

    free_stack(&s2);

    return 0;
}