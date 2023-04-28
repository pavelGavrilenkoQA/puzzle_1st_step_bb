__author__ = "QA PG"

from airtest.core.api import *
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir
from airtest.report.report import simple_report
from general_steps_tasia import skip_system_pop


def test_press_daily_button():
    touch(Template(r"tpl1673604451409.png", record_pos=(-0.085, 0.708), resolution=(1200, 1920)))
    assert_exists(Template(
        r"tpl1670943541988.png",
        record_pos=(0.007, -0.562),
        resolution=(1080, 2340)), "Ожидаем заголовок дейли"
    ) and assert_exists(Template(
        r"tpl1670943568557.png",
        record_pos=(0.029, 0.217),
        resolution=(1080, 2340)),
        "Ожидаем заголовок награды"
    )


def test_tap_left_daily_puzzle():
    sleep(3)
    touch(Template(r"tpl1673529283798.png", record_pos=(-0.185, -0.21), resolution=(1080, 2340)))
    assert_exists(Template(
        r"tpl1670943619339.png",
        record_pos=(0.003, 0.529),
        resolution=(1080, 2340)),
        "Ожидаем кнопку старт"
    )
    #Возвращаемся к дейли меню
    touch(Template(r"tpl1670943635529.png", record_pos=(-0.385, 0.964), resolution=(1080, 2340)))


def test_tap_middle_daily_puzzle():
    sleep(3)
    touch(Template(r"tpl1673529448486.png", record_pos=(0.134, -0.335), resolution=(1200, 2000)))
    assert_exists(Template(
        r"tpl1670943619339.png",
        record_pos=(0.003, 0.529),
        resolution=(1080, 2340)),
        "Ожидаем кнопку старт"
    )
    # Возвращаемся к дейли меню
    touch(Template(r"tpl1670943635529.png", record_pos=(-0.385, 0.964), resolution=(1080, 2340)))


def test_tap_right_daily_puzzle():
    sleep(3)
    touch(Template(r"tpl1673529577314.png", record_pos=(0.464, -0.212), resolution=(1080, 2340)))
    assert_exists(Template(
        r"tpl1670943619339.png",
        record_pos=(0.003, 0.529),
        resolution=(1080, 2340)),
        "Ожидаем кнопку старт"
    )
    # Возвращаемся к дейли меню новое
    touch(Template(r"tpl1670943635529.png", record_pos=(-0.385, 0.964), resolution=(1080, 2340)))


def test_tap_lock_puzzle():
    sleep(3)
    touch(Template(r"tpl1670943847437.png", record_pos=(0.311, 1.008), resolution=(1080, 2340)))
    assert_exists(Template(
        r"tpl1670943925143.png",
        record_pos=(0.219, 0.931),
        resolution=(1080, 2340)),
        "Ожидаем надпись в скором времени"
    )


def run_daily_feature():
    remove_log_dir('daily_feature')
    auto_setup(
        __file__,
        logdir=AUTO_SETUP_ARG.get('logdir'),
        devices=[AUTO_SETUP_ARG.get('devices'), ],
        project_root=AUTO_SETUP_ARG.get('project_root'),
    )
    start_app("com.jollyco.jbpuzzleadventure")
    run_logger(skip_system_pop)
    run_logger(test_press_daily_button)
    run_logger(test_tap_left_daily_puzzle)
    run_logger(test_tap_middle_daily_puzzle)
    run_logger(test_tap_right_daily_puzzle)
    run_logger(test_tap_lock_puzzle)
    stop_app("com.jollyco.jbpuzzleadventure")
    simple_report(__file__, logpath=True, output='html_report/daily.html')
