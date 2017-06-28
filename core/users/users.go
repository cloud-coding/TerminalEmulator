package users

/*
users.go - файл, где происходит вся работа над пользователем
*/

import (
	"os"
	"bufio"
	"strings"
)

//Users — структура данных пользователя
//
//Переменные структуры Users скрыты против обхода разных защит
type User struct {
	//login - логин пользователя
	//password - пароль пользователя
	login    string
	password string
}

//NewUser создает нового пользователя
func NewUser(Login string, Password string) *User {
	return &User{
		login:    Login,
		password: Password,
	}
}

//SearchUser ищет пользователя в базе данных
func (u *User) SearchUser() bool {
	file, err := os.Open("disk/system/users/" + u.login)
	if err != nil {
		return false
	}
	defer file.Close()
	return true
}

//LoadUser загружает информацию о пользователе
func (u *User) LoadUser() User {
	file, _ := os.Open("disk/system/users/" + u.login)
    f := bufio.NewReader(file)
	user := User{}
    for {
    	read_line, err := f.ReadString('\n')
		if err != nil { break }
		tag := strings.Split(read_line, "|")
    	switch tag[0] {
			case "login": user.login = tag[1]
		}
    }
    defer file.Close()
	return user
}

//GetLogin возвращает имя пользователя
func (u *User) GetLogin() string {
	return u.login
}

//SetLogin используется для изменения имени пользователя
func (u *User) SetLogin(login string) bool {
	u.login = login
	return true
}

//GetPassword возвращает пароль пользователя
func (u *User) GetPassword() string {
	return u.password
}

//SetPassword используется для изменения пароля пользователя
func (u *User) SetPassword(password string) bool {
	u.password = password
	return true
}
