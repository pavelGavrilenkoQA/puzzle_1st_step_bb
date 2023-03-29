__author__ = "QA PG"

from airtest.core.api import *
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir
from airtest.report.report import simple_report
from general_steps import skip_system_pop
from general_steps import *


def test_press_daily_button():
    touch_button_daily()
    assert_daily_challenge()
    assert_reward()
    assert_completed_0_daily_puzzle()


def test_exit_to_main_menu():
    touch_daily_puzzle_1()
    touch_button_back()
    assert_daily_challenge()
    touch_daily_puzzle_2()
    touch_button_back()
    assert_daily_challenge()
    touch_daily_puzzle_3()
    touch_button_back()
    assert_daily_challenge()


def test_first_unresolved_puzzle():
    touch_daily_puzzle_1()
    touch_button_start()
    touch_button_settings()
    touch_button_back()
    touch_button_settings()
    touch_button_exit()
    assert_text_exit()
    touch_button_no()
    touch_button_exit()
    assert_text_exit()
    
