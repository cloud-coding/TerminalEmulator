#ifndef user__H
#define user__H

typedef struct User {
	char *login;
	char *password;
	struct User *nextUser;
} User;

void addUser(User **user, char login[30], char password[50]);
void printAllUsers(User *user);

#endif