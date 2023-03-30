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
    touch_button_yes()
    assert_hourglass_1()


def test_first_puzzle_continue():
    touch_daily_puzzle_1()
    assert_hourglass_main()
    touch_button_continue()
    touch_button_settings()
    touch_button_exit()
    touch_button_yes()
    assert_hourglass_1()


def test_second_unresolved_puzzle():
    touch_daily_puzzle_2()
    touch_button_start()
    assert_text_oops()
    touch_button_no()
    touch_button_start()
    assert_text_oops()
    touch_button_yes()
    touch_button_settings()
    touch_button_back()
    touch_button_settings()
    touch_button_exit()
    assert_text_exit()
    touch_button_no()
    touch_button_exit()
    assert_text_exit()
    touch_button_yes()
    assert_hourglass_2()


def test_second_puzzle_continue():
    touch_daily_puzzle_2()
    assert_hourglass_main()
    touch_button_continue()
    touch_button_settings()
    touch_button_exit()
    touch_button_yes()
    assert_hourglass_2()


def test_third_unresolved_puzzle():
    touch_daily_puzzle_3()
    touch_button_start()
    assert_text_oops()
    touch_button_no()
    touch_button_start()
    assert_text_oops()
    touch_button_yes()
    touch_button_settings()
    touch_button_back()
    touch_button_settings()
    touch_button_exit()
    assert_text_exit()
    touch_button_no()
    touch_button_exit()
    assert_text_exit()
    touch_button_yes()
    assert_hourglass_3()


def test_third_puzzle_continue():
    touch_daily_puzzle_3()
    assert_hourglass_main()
    touch_button_continue()
    touch_button_settings()
    touch_button_exit()
    touch_button_yes()
    assert_hourglass_3()


def test_first_resolved_puzzle():
    touch_daily_puzzle_3()
    touch_button_start()
    assert_text_oops()
    touch_button_no()
    touch_button_start()
    assert_text_oops()
    touch_button_yes()
    touch_hint_main()
    assert_text_hint()
    touch_button_no()
    touch_hint_main()
    assert_text_hint()
    touch_button_yes()
    touch_button_win()
    assert_text_puzzle_completed()
    assert_button_save()
    touch_button_ok()
    assert_checkmark_1()
    assert_completed_1_daily_puzzle()


def test_second_resolved_puzzle():
    touch_daily_puzzle_2()
    touch_button_start()
    assert_text_oops()
    touch_button_no()
    touch_button_start()
    assert_text_oops()
    touch_button_yes()
    touch_hint_main()
    assert_text_hint()
    touch_button_no()
    touch_hint_main()
    assert_text_hint()
    touch_button_yes()
    touch_button_win()
    assert_text_puzzle_completed()
    assert_button_save()
    touch_button_ok()
    assert_checkmark_1()
    assert_completed_2_daily_puzzle()


def test_second_resolved_puzzle():
    touch_daily_puzzle_2()
    touch_button_start()
    assert_text_oops()
    touch_button_no()
    touch_button_start()
    assert_text_oops()
    touch_button_yes()
    touch_hint_main()
    assert_text_hint()
    touch_button_no()
    touch_hint_main()
    assert_text_hint()
    touch_button_yes()
    touch_button_win()
    assert_text_puzzle_completed()
    assert_button_save()
    touch_button_ok()
    assert_checkmark_2()
    assert_completed_2_daily_puzzle()


def test_third_resolved_puzzle():
    touch_daily_puzzle_3()
    touch_button_start()
    assert_text_oops()
    touch_button_no()
    touch_button_start()
    assert_text_oops()
    touch_button_yes()
    touch_hint_main()
    assert_text_hint()
    touch_button_no()
    touch_hint_main()
    assert_text_hint()
    touch_button_yes()
    touch_button_win()
    assert_text_puzzle_completed()
    assert_button_save()
    touch_button_ok()
    assert_checkmark_3()
    assert_completed_3_daily_puzzle()


def test_reward():
    assert_coins_x10()
    assert_x25()
    touch_button_claim()
    assert_hint_x1()
    assert_x2()
    touch_ads_reward()
    close_ads()
    assert_hint_x1()
    assert_x4()
    touch_button_claim()
    assert_text_back()
    assert_not_attention





