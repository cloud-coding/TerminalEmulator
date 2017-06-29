package disk

import "os"

/*
disk.go - файл, где находится вся работа над диском
*/

const pathToDisk string = "disk/users/"

//Disk - структура диска
type Disk struct {
	nameDisk string
	activePath string
}

//NewDisk возвращает структуру Disk
func NewDisk(NameDisk string) *Disk {
	return &Disk{
		nameDisk: NameDisk,
		activePath: NameDisk,
	}
}

//GetDiskName возвращает имя диска
func (d *Disk) GetDiskName() string {
	return d.nameDisk
}

//GetDiskPath возвращает текущий путь по диску
func (d *Disk) GetDiskPath() string {
	return d.activePath
}

//SearchMyDisk ищет диск по заданному значению
func (d *Disk) SearchDisk(nameDisk string) bool {
	err := os.Mkdir(pathToDisk + nameDisk, 0777)
	if err != nil {
		return true
	}
	os.Remove(pathToDisk + nameDisk)
	return false
}

//CreateDisk создает новый диск для пользователя. Возвращает 1, если диск создан, 0 - не создан
func (d *Disk) CreateDisk(nameDisk string) bool {
	err := os.Mkdir(pathToDisk + nameDisk, 0777)
	if err != nil {
		return false
	}
	return true
}