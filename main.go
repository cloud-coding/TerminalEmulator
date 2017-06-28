package main

import (
	"fmt"
	u "terminalemulator/core/users"
	"os"
)

func firststart() {
	os.Mkdir("disk", 0777)
	os.Mkdir("disk/system", 0777)
	os.Mkdir("disk/system/users", 0777)
}

func main() {
	firststart()
	var (
		login string
		password string
	)

	fmt.Println("\nДобро пожаловать в Terminal Emulator")
	fmt.Print("Введите логин: ")
	fmt.Scanln(&login)
	fmt.Print("Введите пароль: ")
	fmt.Scanln(&password)

	new_user := u.NewUser(login, password)
	isUser := new_user.SearchUser()
	if !isUser {
		fmt.Print("Данного пользователя не существует")
		os.Exit(0)
	}
	user := new_user.LoadUser()
	fmt.Printf("%s", user.GetLogin())
}	