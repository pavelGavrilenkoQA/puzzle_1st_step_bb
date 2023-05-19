__author__ = "TS"


from general_steps_tasia import *


def skip_daily_popup():
    touch_button_back_popup()


def test_press_daily_button():
    touch_button_daily()
    assert_daily_challenge()
    assert_reward()
    assert_completed_0_daily_puzzle()


def test_exit_to_main_menu():
    touch_daily_puzzle_1()
    assert_button_start()
    touch_button_back()
    assert_daily_challenge()
    touch_daily_puzzle_2()
    assert_button_start()
    touch_button_back()
    assert_daily_challenge()
    touch_daily_puzzle_3()
    assert_button_start()
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
    assert_not_text_exit()
    touch_button_exit()
    assert_text_exit()
    touch_button_yes()
    assert_hourglass_1()
    assert_completed_0_daily_puzzle()


def test_first_puzzle_continue():
    touch_daily_puzzle_1()
    assert_hourglass_main()
    touch_button_continue()
    touch_button_settings()
    touch_button_exit()
    touch_button_yes()
    assert_hourglass_1()
    assert_completed_0_daily_puzzle()


def test_second_unresolved_puzzle():
    touch_daily_puzzle_2()
    touch_button_start()
    assert_text_oops()
    touch_button_no()
    assert_not_text_oops()
    touch_button_start()
    assert_text_oops()
    touch_button_yes()
    touch_button_settings()
    touch_button_exit()
    touch_button_yes()
    assert_hourglass_2()
    assert_completed_0_daily_puzzle()


def test_second_puzzle_continue():
    touch_daily_puzzle_2()
    assert_hourglass_main()
    touch_button_continue()
    touch_button_settings()
    touch_button_exit()
    touch_button_yes()
    assert_hourglass_2()
    assert_completed_0_daily_puzzle()


def test_third_unresolved_puzzle():
    touch_daily_puzzle_3()
    touch_button_start()
    assert_text_oops()
    touch_button_yes()
    touch_button_settings()
    touch_button_exit()
    touch_button_yes()
    assert_hourglass_3()
    assert_completed_0_daily_puzzle()


def test_third_puzzle_continue():
    touch_daily_puzzle_3()
    assert_hourglass_main()
    touch_button_continue()
    touch_button_settings()
    touch_button_exit()
    touch_button_yes()
    assert_hourglass_3()
    assert_completed_0_daily_puzzle()


def test_first_resolved_puzzle():
    touch_daily_puzzle_1()
    touch_button_start()
    assert_text_oops()
    touch_button_yes()
    touch_button_win()
    assert_text_puzzle_completed()
    assert_button_save()
    touch_button_ok()
    assert_checkmark_1()
    assert_completed_1_daily_puzzle()


def test_second_resolved_puzzle():
    touch_debug()
    touch_plus_1()
    touch_hide()
    touch_button_daily()
    touch_daily_puzzle_2()
    touch_button_start()
    touch_hint_main()
    assert_text_hint()
    touch_button_no()
    assert_not_text_hint()
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
    touch_hint_main()
    assert_text_no_hint()
    touch_button_no()
    touch_hint_main()
    assert_text_no_hint()
    touch_button_yes()
    assert_text_shop()
    touch_button_back()
    touch_button_win()
    assert_text_puzzle_completed()
    assert_button_save()
    touch_button_ok()
    assert_checkmark_3()
    assert_completed_3_daily_puzzle()


def test_reload_scene():
    touch_debug()
    touch_reload()
    touch_button_daily()
    assert_daily_challenge()
    assert_checkmark_1()
    assert_checkmark_2()
    assert_checkmark_3()
    assert_completed_3_daily_puzzle()
    touch_daily_puzzle_1()
    assert_daily_challenge()
    assert_checkmark_1()
    touch_daily_puzzle_2()
    assert_daily_challenge()
    assert_checkmark_2()
    touch_daily_puzzle_3()
    assert_daily_challenge()
    assert_checkmark_3()
    assert_completed_3_daily_puzzle()


def test_reward():
    touch_button_claim_daily_reward()
    assert_coins_x10()
    assert_x25()
    touch_button_claim()
    assert_hint_x1()
    assert_x2()
    touch_ads_reward()
    touch_close_ads()
    assert_hint_x1()
    assert_x4()
    touch_button_claim()
    assert_25()
    assert_4()
    assert_text_back()
    assert_not_attention()


def run_daily():
    remove_log_dir('daily')
    auto_setup(
        __file__,
        logdir=AUTO_SETUP_ARG.get('logdir'),
        devices=[AUTO_SETUP_ARG.get('devices'), ],
        project_root=AUTO_SETUP_ARG.get('project_root'),
    )
    start_app("com.jollyco.jbpuzzleadventure")
    run_logger(skip_system_pop)
    run_logger(skip_daily_popup)
    run_logger(test_press_daily_button)
    run_logger(test_exit_to_main_menu)
    run_logger(test_first_unresolved_puzzle)
    run_logger(test_first_puzzle_continue)
    run_logger(test_second_unresolved_puzzle)
    run_logger(test_second_puzzle_continue)
    run_logger(test_third_unresolved_puzzle)
    run_logger(test_third_puzzle_continue)
    run_logger(test_first_resolved_puzzle)
    run_logger(test_second_resolved_puzzle)
    run_logger(test_third_resolved_puzzle)
    run_logger(test_reload_scene)
    run_logger(test_reward)
    stop_app("com.jollyco.jbpuzzleadventure")
    simple_report(__file__, logpath=True, output='html_report/daily.html')





