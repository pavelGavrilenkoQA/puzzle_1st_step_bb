import os

# Set this dir as global project root
project_dir = os.getcwd()
PAGE_ROOT_TAISIA = f"{project_dir}/page_taisia/"
PAGE_ROOT_ALEX = f"{project_dir}/page_alex/"

# Global set for feature
AUTO_SETUP_ARG = {
    'path': os.getcwd(),
    'logdir': True,
    # 'logdir': './log',
    #'devices': 'ios:///http://127.0.0.1:8100', # ключ для iOS при запущеной проксе и подключенным WebDriverAgent
    'devices': 'android:///',# универсальный ключ для запуска на текущем подключенном устройстве
    #127.0.0.1:5037/08111JEC214267?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH' ### Pixel personal start
    'project_root': project_dir
}

if __name__ == "__main__":
    print('go')
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lol')
    print(path)

