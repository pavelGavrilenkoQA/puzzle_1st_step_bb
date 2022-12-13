import os

# Set this dir as global project root
project_dir = os.getcwd()

### Global set for feature
AUTO_SETUP_ARG = {
    'path': os.getcwd(),
    'logdir': True,
    # 'logdir': './log',
    'devices': 'android://127.0.0.1:5037/08111JEC214267?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH', ### Pixel
    'project_root': project_dir
}

if __name__ == "__main__":
    print('go')
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'log')
    print(path)
