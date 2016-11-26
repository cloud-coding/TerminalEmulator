#include <stdio.h>
#include <stdlib.h>

typedef struct ArrayInt {
	int value;
	struct ArrayInt *next;
} ArrayInt;

void push(ArrayInt **head, int value) {
	ArrayInt *tmp = (ArrayInt*) malloc(sizeof(ArrayInt));
	tmp->value = value;
	tmp->next = (*head);
	(*head) = tmp;
}

void printArrayInt(ArrayInt *head) {
	while(head) {
		printf("%d", head->value);
		head = head->next;
	}
}

int main()
{
	ArrayInt* list = NULL;
	push(&list, 1);
	printArrayInt(list);

	getch();
}