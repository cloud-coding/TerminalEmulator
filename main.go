package main

import (
	"fmt"
	u "terminalemulator/core/users"
	"os"
	"strings"
)

func firststart() {
	os.Mkdir("disk", 0777)
	os.Mkdir("disk/system", 0777)
	os.Mkdir("disk/system/users", 0777)
	os.Mkdir("disk/users", 0777)
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

	newUser := u.NewUser(login, password)
	isUser := newUser.SearchUser()
	if !isUser {
		fmt.Print("Данного пользователя не существует")
		os.Exit(0)
	}
	user, err := newUser.LoadUser(password)
	if err != nil {
		fmt.Print(err)
		os.Exit(0)
	}

	diskUser := user.GetDisk()

	//user - переменная для работы с пользователем
	//diskUser - перменная для работы с диском

	fmt.Printf("Добро пожаловать, %s\n", user.GetLogin())
	
	if !diskUser.SearchDisk(diskUser.GetDiskName()) {
		fmt.Printf("Диск %s не найден. Желаете создать (y/n)? ", diskUser.GetDiskName())
		var slct string
		fmt.Scanln(&slct)
		if strings.Contains(strings.ToLower(slct), "y") {
			for 1 < 5 {
				fmt.Print("Введите название будущего диска: ")
				fmt.Scanln(&slct)
				if diskUser.CreateDisk(slct) {
					fmt.Printf("Вы успешно создали диск %s", slct)
					user.SetDisk(slct)
					break
				}
				fmt.Println("Попробуйте выбрать другое название")
			}
		} else { os.Exit(1)	}
	}
}	