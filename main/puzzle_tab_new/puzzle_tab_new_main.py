__author__ = "QA SASHA"

from general_steps_alex import *
from airtest.core.api import *
from airtest.report.report import simple_report
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir
from general_steps_alex import skip_system_pop


def skip_daily_popup():
    if exists(button_pass()):
        touch_button_back_popup()


def test_open_free_pack():
    touch_sugar_mesh_pack()
    assert_exists_sugar_mesh_bw()


def test_open_art():
    touch_sugar_mesh_bw()
    assert_button_start()


def test_rotation_button_on():
    touch_swipe_rotation_off()
    assert_exists_swipe_()
    assert_not_exists_coins_3()


def test_rotation_button_off():
    touch_swipe_rotation_on()
    assert_exists_swipe_rotation_off()
    assert_not_exists_coins_6()


def test_swipe_count_element_to_16():
    swipe_elements_16()
    assert_exists_element_16()
    assert_not_exists_coins_3()


def test_start_art_puzzle():
    touch_button_start()
    if test_another_puzzle_in_progress():
        touch_button_yes()
    assert_exists_button_level_assert()


def test_exit_popup():
    touch_button_settings()
    touch_button_exit()
    popap_before_exit()
    #assert_exists(popap_before_exit_1())


def test_exit_popup_close():
    touch_button_no()
    assert_not_exists_button_level_assert()
    assert_not_exists_sugar_mesh_pack()
    assert_not_exists_sugar_mesh_bw()


def test_exit_popup_accept():
    touch_button_exit()
    touch_button_yes()
    assert_button_back()


def test_to_main_from_art_list():
    touch_button_back()
    assert_exists_sugar_mesh_pack()


def run_puzzle_tab_new():
    remove_log_dir('puzzle_tab_new')
    auto_setup(
        __file__,
        logdir=AUTO_SETUP_ARG.get('logdir'),
        devices=[AUTO_SETUP_ARG.get('devices'), ],
        project_root=AUTO_SETUP_ARG.get('project_root'),
    )
    start_app("com.jollyco.jbpuzzleadventure")
    run_logger(skip_system_pop)
    run_logger(skip_daily_popup)
    run_logger(test_open_free_pack)
    run_logger(test_open_art)
    run_logger(test_rotation_button_on)
    run_logger(test_rotation_button_off)
    run_logger(test_swipe_count_element_to_16)
    run_logger(test_start_art_puzzle)
    run_logger(test_exit_popup)
    run_logger(test_exit_popup_close)
    run_logger(test_exit_popup_accept)
    run_logger(test_to_main_from_art_list)
    stop_app("com.jollyco.jbpuzzleadventure")
    simple_report(__file__, logpath=True, output='html_report/puzzle_tab_new.html')


