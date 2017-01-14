start_terminal = 'Запуск терминала...'
login_in_system = 'Вход в систему'
auth_user = 'Авторизация пользователя...'
user_login_in_guest = 'Пользователь вошел как \"Гость\"'
user_login = '{} вошел как \"{}\"'
wrong_password = 'Пароль неверный'
account_not_exists = 'Данного аккаунта не существует. Пользователь вошел как \"Гость\"'
account_not_exists2 = 'Данного акаунта не существует'
press_enter = 'Нажмите Enter...'
disk_name_future = 'Введите будущее название диска'
name_reserved = 'Данное имя зарезервировано системой'
creating_disk = 'Создание диска'
disk_create = 'Диск {} создан'
disk_exists = 'Данный диск уже существует'
disk_not_exists_next_menucreate = 'Диска не существует. Вы переключитесь на меню создание диска'
available_disks = 'Доступные диски'
disks = 'Диски'
enter_name_disk_on_connect = 'Введите название диска для подключения'
connecting_disk = 'Подключение к диску {}'
connect_successfully = 'Вы успешно подключились!'
disk_name_not_exists = 'Диска {} не существует'
list_empty = 'Список пуст'
list_folders = '[Список папок]'
list_files = '[Список файлов]'
list_plugins = '[Список плагинов]'
folder_creation = 'mkdir {name} {...} - создание папок'
dir_not_exists = 'Данной директории не существует'
file_not_exists = 'Данного файла не существует'
word_rez_system = 'Слово {} зарезервировано системой'
dir_exists = 'Папка {} уже существует'
dir_created = 'Папка {} успешно создана'
command_not_exist = 'Данной команды не существует'
loading_plugins = 'Загрузка плагинов'
plugin_exists = 'Данный плагин уже существует'
name_exists_numbers = 'Название содержит запрещенные символы, либо имя начинается с цифры'
plugin_install_ok = 'Плагин успешно установлен'
plugin_uninstall = 'Плагин деинсталлирован'
project_created = 'Проект успешно создан'
use_illegal_char = 'Используется запрещенный символ (\".\")'
plugin_not_exists = 'Данного плагина не существует'
plugin_delete = 'Плагин успешно удален'
file_not_found = 'Файл не существует'
file_delete = 'Файл удален'
dir_delete = 'Папка удалена'
commands_plugin_name = '[Команды плагина \'{}\']'
current_version_terminal = 'Текущая версия терминала - {}'
not_permissions = 'Недостаточно прав'
user_exists = 'Данный пользователь существует'
user_created = 'Пользователь создан!\nДанные:\n\tЛогин: {}\n\tПароль: {}\n\tПривилегия: {}'
account_deleted = 'Аккаунт {} удален'
login = 'Логин'
group = 'Группа'
path = 'Путь'
print_help = [
    'q - выйти из терминала',
    'help - показать помощь по командам. Доступно два способа: help или help {команда}',
    'terminal - показать помощь по командам терминала',
    'apt - показать помощь по командам модуля apt',
    'cd {путь} - переместиться в каталог {путь}',
    'ls - отобразить доступные папки и файлы в текущей директории',
    'mkdir {name} {...} - создать папку(-и). mkdir 1 2 - создаст одновременно папки \"1\" и \"2\"',
    'rm {name} - удаление файла',
    'rmdir {name} - удалить папку',
    'file {name} - отобразить содержимое файла',
    'user - показать помощь по командам модуля user (Управление аккаунтами)',
]
print_apt = [
    'apt list - показать список загруженных плагинов',
    'apt create {name} - создать файл плагина в текущей директории',
    'apt install {name} - установить плагин в систему',
    'apt delete {name} - удалить установленный плагин'
]
print_terminal = [
    '[Terminal Helper]',
    'terminal version - показать текущую версию терминала',
    'terminal settings {options} - показать меню настроек терминала',
]
print_terminal_settings = [
    '[Terminal Settings]',
    'lang {lang} - Смена языка',
]
print_user = [
    '[User Helper]',
    'user create {name} {password} {group} - создать пользователя',
    'user delete {name} - удалить аккаунт',
    'user select {name} {password} - перейти на другую учетную запись',
]