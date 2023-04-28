__author__ = "QA PG"

from airtest.core.api import *
from airtest.report.report import simple_report
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir
from general_steps_alex import skip_system_pop



def test_press_setting_button():
    touch(Template(
        r"tpl1670921483290.png",
        record_pos=(-0.4, -0.866),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1670921510454.png",
        record_pos=(0.003, -0.65),
        resolution=(1080, 2340)),
        "Ожидаем плашки <Настройки>"
    )


def test_sound_off():
    touch(Template(
        r"tpl1670921961085.png",
        record_pos=(-0.139, -0.214),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1670921983142.png",
        record_pos=(-0.133, -0.213),
        resolution=(1080, 2340)),
        "Ожидаем отображение выключенного свичера звуков"
    )


def test_vibro_off():
    touch(Template(
        r"tpl1670921999824.png",
        record_pos=(0.137, -0.213),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1670922010445.png",
        record_pos=(0.151, -0.215),
        resolution=(1080, 2340)),
        "Ожидаем отображение выключенного свичера вибрации"
    )


def test_sound_and_vibro_on():
    touch(Template(
        r"tpl1670922609202.png",
        record_pos=(-0.131, -0.217),
        resolution=(1080, 2340))
    )
    touch(Template(
        r"tpl1670922621818.png",
        record_pos=(0.137, -0.208),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1670922636903.png",
        record_pos=(0.007, -0.21),
        resolution=(1080, 2340)),
        "Ожидаем отображение включенных свичеров вибро и звука"
    )


def test_language_list_get():
    touch(Template(
        r"tpl1670922039986.png",
        record_pos=(0.007, -0.013),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1670922057836.png",
        record_pos=(-0.002, -0.024),
        resolution=(1080, 2340)),
        "Ожидаем списка языков"
    )
    touch(Template(
        r"tpl1670922068293.png",
        record_pos=(-0.381, 0.963),
        resolution=(1080, 2340))
    )


def test_privacy_tap():
    touch(Template(
        r"tpl1670922100323.png",
        record_pos=(-0.004, 0.144),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1670922116005.png",
        record_pos=(0.001, -0.249),
        resolution=(1080, 2340)),
        "Ожидаем зеленный щит таба приватности"
    )


def test_off_all_privacy():
    touch(Template(
        r"tpl1670922142371.png",
        record_pos=(0.035, -0.024),
        resolution=(1080, 2340))
    )
    touch(Template(
        r"tpl1670922157938.png",
        record_pos=(0.027, 0.197),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1670922178392.png",
        record_pos=(0.008, 0.082),
        resolution=(1080, 2340)),
        "Ожидаем отключеные свичеры политики"
    )


def test_on_all_privacy():
    touch(Template(
        r"tpl1670922892644.png",
        record_pos=(0.007, -0.033),
        resolution=(1080, 2340))
    )
    touch(Template(
        r"tpl1670922900570.png",
        record_pos=(0.003, 0.199),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1670922940292.png",
        record_pos=(0.058, 0.082),
        resolution=(1080, 2340)),
        "Ожидаем включенные свичеры политики"
    )
    ### Выходим из таба политики
    touch(Template(
        r"tpl1670922068293.png",
        record_pos=(-0.381, 0.963),
        resolution=(1080, 2340))
    )


def test_cloud_menu_present():
    assert_exists(Template(
        r"tpl1670923038845.png",
        record_pos=(-0.004, 0.339),
        resolution=(1080, 2340)),
        "Ожидаем наличие кнопок облочного сохранения"
    )


def test_link_in_setting_present():
    assert_exists(Template(
        r"tpl1670923277703.png",
        record_pos=(0.009, 0.495),
        resolution=(1080, 2340)),
        "Ожидаем наличие ссылок в меню"
    )


def test_setting_menu_exit():
    touch(Template(
        r"tpl1670922068293.png",
        record_pos=(-0.381, 0.963),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1670923393819.png",
        record_pos=(-0.283, -0.865),
        resolution=(1080, 2340)),
        "Ожидаем отображения элементов главного меню"
    )


def run_setting_feature():
    remove_log_dir('setting_feature')
    auto_setup(
        __file__,
        logdir=AUTO_SETUP_ARG.get('logdir'),
        devices=[AUTO_SETUP_ARG.get('devices'), ],
        project_root=AUTO_SETUP_ARG.get('project_root'),
    )
    start_app("com.jollyco.jbpuzzleadventure")
    run_logger(skip_system_pop)
    run_logger(test_press_setting_button)
    run_logger(test_sound_off)
    run_logger(test_vibro_off)
    run_logger(test_sound_and_vibro_on)
    run_logger(test_language_list_get)
    run_logger(test_privacy_tap)
    run_logger(test_off_all_privacy)
    run_logger(test_on_all_privacy)
    run_logger(test_cloud_menu_present)
    run_logger(test_link_in_setting_present)
    run_logger(test_setting_menu_exit)
    stop_app("com.jollyco.jbpuzzleadventure")
    simple_report(__file__, logpath=True, output='html_report/setting.html')