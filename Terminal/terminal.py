#====================================================================================

from time import sleep, asctime
from datetime import datetime
import json
import sys, os
#====================================================================================
PATH = os.getcwd()+'\\Terminal\\disk'
P = ''
REGISTERED_WORD = ['list', 'update', 'help', 'exit', 'disk', 'terminal', 'create']
#====================================================================================

def log(text):
    #print('{}'.format(datetime.strftime(datetime.now(), "[%H:%M:%S]: "))+str(text))
    print(text)
def cls():
    os.system('cls')
def checkInOldDisk(c, l):
    check = False
    for i in l:
        if i == c:
            check = True
            break
    return check
def returnDisk(path):
    if path.count('/') > 1:
        path = path.split('/')[0]
    return path

#====================================================================================
file = open('Terminal/settings.json')
jsons = file.read()
jsons = json.loads(jsons)
file.close()

if checkInOldDisk(jsons['directory'], os.listdir(os.path.join(PATH))):
    P = jsons['directory']
else:
    P = ''
if jsons['lang'] == 'ru':
    from Terminal.localization import ru as lang
else:
    from Terminal.localization import en as lang
#====================================================================================
cls()
log(lang.started_terminal[0])
log(lang.started_terminal[1].format(jsons['version']))

if P == '':
    while True:
        log(lang.not_directory)
        command = input('>>> ')
        if command == '1':
            cls()
            while True:
                log(lang.enter_name_disk)
                command = input('>>> ')
                cls()
                if command == 'exit()':
                    break
                if command == '':
                    log(lang.not_name_disk)
                    continue
                if command == 'disk':
                    log(lang.rezerve_word)
                    continue
                list_dir = os.listdir(PATH)
                if checkInOldDisk(command, list_dir):
                    log(lang.disk_exist)
                    continue
                os.mkdir(os.path.join(PATH, command))
                file = open(os.path.join(PATH, command, '.cfg'), 'w')
                file.write(json.dumps({
                    "created": asctime(),
                    "terminal_version": jsons['version'],
                    "update": asctime()
                }))
                file.close()
                log(lang.disk_created.format(command))
                break

        elif command == '2':
            list_dir = os.listdir(PATH)
            if list_dir == []:
                cls()
                print('\n===============\n')
                log(lang.list_empty)
                print('\n===============\n')
            else:
                score = 1
                cls()
                print('\n===============\n')
                for i in list_dir:
                    dir_size = 0
                    for path, sdir, files in os.walk(os.path.join(PATH, i)):
                        for file in files:
                            dir_size += os.path.getsize(os.path.join(path, file))
                    print('{}. {} | Размер (КБ): {}'.format(score, i, round(dir_size/1024, 1)))
                    score += 1
                print('\n===============\n')
        elif command == '3':
            cls()
            while True:
                log(lang.enter_name_disk)
                command = input('>>> ')
                cls()
                if command == 'exit':
                    break
                    exit
                list_dir = os.listdir(PATH)
                check = False
                for i in list_dir:
                    if i == command:
                        check = True
                        break
                if check == False:
                    cls()
                    log(lang.noexist_disk)
                else:
                    P = command
                    file = open('Terminal/settings.json', 'w')
                    file.write(json.dumps({
                        "directory": P,
                        "version": jsons['version'],
                        "lang": jsons['lang'],
                        "created": jsons['created']
                    }))
                    file.close()
                    jsons['directory'] = command
                    break
            break
        elif command == 'exit' or command == 'exit()':
            exit()
        else:
            log(lang.not_directory_error_number)
            #break
# ====================================================================================
cls()
while True:
    log('[Путь: {}]'.format(P))
    print('=========================\n')
    list_dir = os.listdir(os.path.join(PATH, P))
    if list_dir == []:
        print('Список пуст')
    else:
        score = 1
        print('[Папки]')
        if list_dir == []:
            print('Список пуст')
        for i in list_dir:
            if i[0] == '.':
                continue
            if os.path.isdir(os.path.join(PATH, P, i)) == False:
                continue
            log('{}. {}'.format(score, i))
            score += 1
        score = 1
        print('\n[Файлы]')
        for i in list_dir:
            if i[0] == '.':
                continue
            if os.path.isfile(os.path.join(PATH, P, i)) == False:
                continue
            log('{}. {}'.format(score, i))
            score += 1

    print('\n=========================')
    command = input('>>> ')
    cls()
    if command.count(' ') > 0:
        split = command.split(' ')
        if split[0] == 'create':
            if command.count(' ') != 2:
                log('create {dir/file} [Name]')
                continue
            if split[1] == 'dir':
                if checkInOldDisk(split[2], os.listdir(os.path.join(PATH, P))):
                    log(lang.disk_exist)
                    continue
                os.mkdir(os.path.join(PATH, P, split[2]))
                log('Папка {} создана'.format(split[2]))
            elif split[1] == 'file':
                check = False
                for path, sdir, files in os.walk(os.path.join(PATH, P)):
                    for file in files:
                        if file == split[2]:
                            check = True
                            break
                if check:
                    log(lang.file_exist)
                    continue
                file = open(os.path.join(PATH, P, split[2]), 'w')
                file.write('')
                file.close()
                continue

    else:
        if command == 'exit':
            break
            exit
        elif command == '':
            continue
        elif command == 'update':
            pass
        elif command == 'help':
            log(lang.disk_help)
        elif command == ' ':
            pass
        elif command == 'create':
            log('create {dir/file} [Name]')
        elif command == '..':
            if returnDisk(P) == jsons['directory']:
                continue
            if command == returnDisk(P):
                pass
            splits = P.split('\\')
            del splits[len(splits)-1]
            P = ''
            for i in splits:
                P = os.path.join(P, i)
        else:
            if checkInOldDisk(command, os.listdir(os.path.join(PATH,P))):
                P = os.path.join(P, command)
