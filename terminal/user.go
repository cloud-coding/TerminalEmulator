package terminal

// В данном файле содержатся функции для управления пользователем

import (
	"path/filepath"
	"errors"
	"encoding/json"
	"os"
	"io/ioutil"
)

// User - структура, в которой находятся данные о юзере
type User struct {
	login string
	password string
}

// NewUser создает нового пользователя, возвращая адрес структуры User
func NewUser(login string, password string) *User {
	return &User{		
		login:login,
		password:password,
	}
}

// GetLogin возвращает строку, в которой содержится логин User`а. Данный способ используется для того, чтобы нельзя было изменить логин без ведомости
func (u *User) GetLogin() string {
	return u.login
}

// GetPassword возвращает пароль
func (u *User) GetPassword() string {
	return u.password
}

// UpdateInfo сохраняет данные пользователя в файл
func (u *User) UpdateInfo() error {
	path, _ := filepath.Abs(PathUsers + "/" + u.login)
	if Exists(path) {
		data := make(map[string]interface{})
		data["login"] = u.login
		data["password"] = u.password
		//data["disk"] = u.disk.name
		bytes, err := json.Marshal(&data)
		if err != nil {
			return err
		}
		ioutil.WriteFile(path, bytes, os.ModePerm)
		return nil
	}
	return errors.New("Ошибка: не найден файл-сохранения в пути " + path)
}