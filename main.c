#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <direct.h>

#include "user.h"

int main() {

	mkdir("Terminal");
	mkdir("Terminal\\disk");
	mkdir("Terminal\\disk\\system");
	mkdir("Terminal\\disk\\system\\users");
	mkdir("Terminal\\disk\\system\\cache");

	
	User* user = NULL;
	char login;

	printf("1. Registration\n2. Login\n\n>>> ");
	scanf("%c", &login);
	printf("%c", login);

	/*addUser(&user, "Test", "123456");
	addUser(&user, "Olegators", "74841f5r");
	addUser(&user, "Everxants", "fr4f4r4frfr4");
	printAllUsers(user);*/

	getch();
	return 0;
}