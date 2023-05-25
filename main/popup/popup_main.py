__author__ = "TS"

from general_steps_tasia import *


def reload_app():
    stop_app("com.jollyco.jbpuzzleadventure")
    clear_app("com.jollyco.jbpuzzleadventure")
    start_app("com.jollyco.jbpuzzleadventure")


def accept_privacy():
    touch_button_ok()


def skip_tutor():
    touch_button_tap()


def daly_popup_close():
    touch_button_back_popup()
    assert_exists_sugar_mesh_pack()


def daily_popup_exist():
    assert_button_back_popup()
    assert_text_complete()
    assert_pass()


def pass_daily_from_out_popup():
    touch_pass()
    assert_daily_challenge()
    assert_reward()
    assert_completed_0_daily_puzzle()


def turn_on_ads_in_debug():
    touch_debug()
    touch_debug_checkmark()
    assert_debug_checkmark_yes()
    touch_reload()


def start_art():
    assert_exists_sugar_mesh_pack()
    touch_sugar_mesh_pack()
    assert_exists_sugar_mesh_bw()
    touch_sugar_mesh_bw()
    touch_button_start()


def best_offer_popup():
    sleep(60)
    assert_text_best_offer()
    assert_hint_best_offer()
    assert_button_back_popup()
    touch_button_back_popup()


def pass_art():
    touch_button_win()
    touch_close_ads()
    touch_button_claim()


def no_ads_popup():
    assert_popup_ads()
    assert_text_disable()
    touch_button_back_popup()


def exit_to_main():
    assert_exists_sugar_mesh_pack()


def run_popup():
    remove_log_dir('popup')
    auto_setup(
        __file__,
        logdir=AUTO_SETUP_ARG.get('logdir'),
        devices=[AUTO_SETUP_ARG.get('devices'), ],
        project_root=AUTO_SETUP_ARG.get('project_root'),
    )
    start_app("com.jollyco.jbpuzzleadventure")
    run_logger(daily_popup_exist)
    run_logger(daly_popup_close)
    stop_app("com.jollyco.jbpuzzleadventure")
    start_app("com.jollyco.jbpuzzleadventure")
    run_logger(daily_popup_exist)
    run_logger(pass_daily_from_out_popup)
    run_logger(turn_on_ads_in_debug)
    run_logger(start_art)
    run_logger(best_offer_popup)
    run_logger(pass_art)
    run_logger(no_ads_popup)
    run_logger(exit_to_main)
    stop_app("com.jollyco.jbpuzzleadventure")
    simple_report(__file__, logpath=True, output='html_report/popup.html')