package terminal

// Данный пакет является главным. Он - пульт управления всем терминалом

import (
	// Стандартные библиотеки
	"os"
	"io/ioutil"
	"path/filepath"
	"errors"
	"encoding/json"
	"bufio"
	"fmt"

	// Библиотеки с сайта github.com
	"github.com/yanzay/cfg"
)

// Terminal - главня структура, от которой происходит вся работа над программой
type Terminal struct {
	*User
}

// Константы, которые используются для правильной работы терминала
const (
	// Системные пути для работы терминала
	PathDisk = "disk" 							// Путь к диску, где содержатся все данные	
	PathSystem = PathDisk + "/system"			// Путь к системной папке
	PathUsers = PathSystem + "/users" 			// Путь к папке с данными о пользователях
	PathInfo = PathSystem + "/terminal.info" 	// Путь к файлу, содержащего данные терминала

	// ForbiddenWord - слово, которое нельзя использовать, как логин
	ForbiddenWord = "unknown"

	// CONFIG - Конфигурация файла terminal.info
	CONFIG = "USER=" + ForbiddenWord

)

// NewTerminal - функция, с помощью которой мы получаем адрес struct Terminal. Данная операция используется для того, чтобы мы могли работать с функциями, присущие данной структуре.
func NewTerminal() *Terminal {
	return &Terminal {
		nil,
	}
}

// UpdateStatus используется, как проверка всех необходимых системных файлов
func (t *Terminal) UpdateStatus() {
	os.Mkdir("disk", os.ModePerm)
	path, _ := filepath.Abs(PathSystem)
	os.Mkdir(path, os.ModePerm)
	path, _ = filepath.Abs(PathUsers)
	os.Mkdir(path, os.ModePerm)
	path, _ = filepath.Abs(PathInfo)
	if !Exists(path) {
		//Если системного файла terminal.info нет, то мы создаем новый и записываем данные из константы CONFIG
		file, _ := os.Create(path)
		ioutil.WriteFile(path, []byte(CONFIG), os.ModePerm)
		file.Close()
	}
}

// Run запускает терминал
func (t *Terminal) Run() error {
	path, err := filepath.Abs(PathInfo)
	if err != nil {
		return err
	}
	settings := make(map[string]string)
	if err = cfg.Load(path, settings); err != nil {
		return err
	}
	if _, ok := settings["user"]; !ok {
		return errors.New(`Не найден ключ "USER" в ` + PathInfo + "\nПересоздайте данные: для этого запустите терминал с тегом -reinfo")
	}
	user, err := login(settings)
	if err != nil {
		return err
	}
	err = user.UpdateInfo()
	if err != nil {
		return err
	}
	return nil
}

func login(settings map[string]string) (*User, error) {
	path, _ := filepath.Abs(PathUsers + "/" + settings["user"])
	if Exists(path) && settings["user"] != ForbiddenWord {
		var user map[string]interface{}
		data, _ := ioutil.ReadFile(path) 
		err := json.Unmarshal(data, &user)
		if err != nil {
			return nil, err
		}
		return NewUser(user["login"].(string), user["password"].(string)), nil
	}
	var (
		loginString string
		loginPassword string
	)
	for {
		fmt.Print("Введите будущий логин: ")
		loginString, _ = Scan()
		if len(loginString) == 0 {
			continue
		}
		if loginString == ForbiddenWord {
			continue
		}
		path, _ := filepath.Abs(PathUsers + "/" + loginString)
		if Exists(path) {
			fmt.Println("Данный логин занят. Попробуйте другой.")
			continue
		}
	
		fmt.Print("Введите будущий пароль: ")
		loginPassword, _ = Scan()

		break
	}
	path, _ = filepath.Abs(PathUsers + "/" + loginString)
	file, err := os.Create(path)
	if err != nil {
		return nil, err
	}
	file.Close()
	return NewUser(loginString, loginPassword), nil	
}

//Scan считывает данные с консоли
func Scan() (string, error) {
	in := bufio.NewScanner(os.Stdin)
	in.Scan()
	if err := in.Err(); err != nil {
		return "", err
	}
	return in.Text(), nil
}

//Scanln считывает данные с консоли с переходом на новую строку
func Scanln() (string, error) {
	in := bufio.NewReader(os.Stdin)
	str, err := in.ReadString('\n')
	return str, err
}


// Exists проверяет: существует ли файл/папка в данной директории
func Exists(path string) bool {
    _, err := os.Stat(path)
    if err == nil { return true }
    if os.IsNotExist(err) { return false }
    return true
}