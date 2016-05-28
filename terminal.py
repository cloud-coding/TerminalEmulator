#====================================================================================

from time import sleep, asctime
from datetime import datetime
import json
import sys, os
#====================================================================================
PATH = os.getcwd()+'\\Terminal\\disk'
P = ''
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

P = jsons['directory']
if jsons['lang'] == 'ru':
    from Terminal.localization import ru as lang
else:
    from Terminal.localization import en as lang
#====================================================================================
cls()
log(lang.started_terminal[0])
log(lang.started_terminal[1].format(jsons['version']))

if jsons['directory'] == '':
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

    log('\n[Путь: {}]'.format(P))
    command = input('>>> ')
    cls()
    if command.count(' ') > 0:
        split = command.split(' ')
        if split[0] == 'create':
            if split[1] is None or split[2] is None:
                log('create {dir/file} [Name]')
            if split[1] == 'dir':
                print(os.path.join(PATH, P))
                if checkInOldDisk(split[2], os.listdir(os.path.join(PATH, P))):
                    log(lang.disk_exist)
                    continue

            elif split[1] == 'file':
                pass

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