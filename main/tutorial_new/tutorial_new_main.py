__author__ = "QA SASHA"

from general_steps import *
from tutorial_main import run_tutorial_feature
from airtest.core.api import *
from airtest.report.report import simple_report
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir
from general_steps import skip_system_pop


def test_politic_accept():
    touch_button_ok()
    assert_exists_tutorial_image()


def test_tutorial_part_1():
    touch_button_ok()
    assert_exist_empty_elements_list()
    touch_button_win()
    assert_exists_tutorial_image()


def test_tutorial_part_2():
    touch_button_ok()
    assert_exists_empty_field()
    touch_button_win()
    assert_exists_tutorial_image()


def test_tutorial_part_3():
    touch_button_ok()


def saved_purchase():
    claim_in_russian()


def test_language_check():
    touch_button_back()
    touch_button_back()
    touch_button_settings()
    switch_english_language_test()
    touch_button_back()
    touch_travelling_pack()



def run_tutorial_new():
    remove_log_dir('tutorial_new')
    auto_setup(
        __file__,
        logdir=AUTO_SETUP_ARG.get('logdir'),
        devices=[AUTO_SETUP_ARG.get('devices'), ],
        project_root=AUTO_SETUP_ARG.get('project_root'),
    )
     # очистка апп даты только для Андроида, при запуске на Иос будет падать, отключать при пуске на оси
    clear_app("com.jollyco.jbpuzzleadventure")
    start_app("com.jollyco.jbpuzzleadventure")
    run_logger(skip_system_pop)
    run_logger(test_politic_accept)
    run_logger(test_tutorial_part_1)
    run_logger(test_tutorial_part_2)
    run_logger(test_tutorial_part_3)
    run_logger(saved_purchase)
    run_logger(test_language_check)
    stop_app("com.jollyco.jbpuzzleadventure")
    simple_report(__file__, logpath=True, output='html_report/tutorial_new_main.html')
