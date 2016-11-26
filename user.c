#include "user.h"

#include <stdio.h>
#include <stdlib.h>

void addUser(User **user, char login[30], char password[50]) {
	User *tmp = (User*) malloc(sizeof(User));
	tmp->login = login;
	tmp->password = password;
	tmp->nextUser = (*user);
	(*user) = tmp;
}

void printAllUsers(User *users) {
	int i = 0;
	while(users) {
		i++;
		printf("%i. %s\n", i, users->login);
		users = users->nextUser;
	}
}