#====================================================================================

from time import sleep, asctime
from datetime import datetime
import json
import sys, os
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
#====================================================================================
file = open('Terminal/settings.json')
jsons = file.read()
jsons = json.loads(jsons)
file.close()

if jsons['lang'] == 'ru':
    from Terminal.localization import ru as lang
else:
    from Terminal.localization import en as lang
#====================================================================================
cls()
log(lang.started_terminal[0])
log(lang.started_terminal[1].format(jsons['version']))
PATH = os.getcwd()+'\\Terminal\\disk'
P = ''
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
                    P = 'nikita'
                    break
            break
        elif command == 'exit' or command == 'exit()':
            exit()
        else:
            log(lang.not_directory_error_number)
            #break
# ====================================================================================
while True:
    cls()
    log('[{}]'.format(P))
    break
    sleep(1)