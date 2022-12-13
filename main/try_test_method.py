import os
import shutil
from global_auto_agr import AUTO_SETUP_ARG

def run_logger(method):
    '''Выполняется тестовый метод, при удачном выполнении пишет в пройденные'''
    '''при падении пишет в падения вместе с исключением'''
    try:
        method()
        with open(f'{AUTO_SETUP_ARG.get("project_root")}/passed.txt', 'a+') as f:
            f.write(f'{method.__name__} --- is passed\n')
    except Exception as e:
        with open(f'{AUTO_SETUP_ARG.get("project_root")}/failed.txt', 'a+') as f:
            f.write(f'{method.__name__} --- is failed, detail: {e}\n')


def remove_txt_result_file():
    '''Удаляет предыдущий список пройденных и упавших тестов'''
    try:
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'passed.txt'))
    except Exception as e:
        print('Не удалось удалить прошлый файл пройденных тестов')
    try:
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'failed.txt'))
    except Exception as e:
        print('Не удалось удалить прошлый файл упавших тестов')


def remove_log_dir(feature_dir):
    '''Чистит внутрению папку лога перед запуском фичи'''
    '''Передать str название папки фичи'''
    try:
        shutil.rmtree(f'{AUTO_SETUP_ARG.get("project_root")}\{feature_dir}\log')
    except Exception as e:
        print(f'проблема с удаление лог дира {feature_dir} подробности {e}')
