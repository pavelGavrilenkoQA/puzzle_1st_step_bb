import os
from global_auto_agr import AUTO_SETUP_ARG

def run_logger(method):
    try:
        method()
        with open(f'{AUTO_SETUP_ARG.get("project_root")}/passed.txt', 'a+') as f:
            f.write(f'{method.__name__} пройден успешно\n')
    except Exception as e:
        with open(f'{AUTO_SETUP_ARG.get("project_root")}/failed.txt', 'a+') as f:
            f.write(f'{method.__name__} провален, подробности: {e}\n')


def remove_txt_result_file():
    try:
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'passed.txt'))
    except Exception as e:
        print('Не удалось удалить прошлый файл пройденных тестов')
    try:
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'failed.txt'))
    except Exception as e:
        print('Не удалось удалить прошлый файл упавших тестов')

