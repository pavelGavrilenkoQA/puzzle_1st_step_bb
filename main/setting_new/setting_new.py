__author__ = "QA SASHA"

from general_steps import *


def test_press_setting_button():
    touch_button_settings()
    assert_exists_text_setting()


def test_sound_off():
    touch_swipe_sound_on()
    assert_exists_swipe_sound_off()


def test_vibro_off():
    touch_sound_vibration_on()
    assert_exists_swipe_vibration_off()


def test_sound_and_vibro_on():
    touch_swipe_sound_on()
    touch_swipe_sound_off()
    assert_exists_sound_vibration_on()


def test_language_list_get():
    touch_english_flag_text()
    assert_exists_all_languages()
    touch_button_back()
    sleep(2)
    touch_button_back()


def test_privacy_tap():
    touch_button_privacy()
    assert_exists_green_privacy_shield()


def test_off_all_privacy():
    touch_swipe_analytics_on()
    touch_swipe_analytics_on()
    assert_exists_swipe_analytics_personalized_off()


def test_on_all_privacy():
    touch_swipe_analytics_off()
    touch_swipe_personalized_off()
    assert_exists_swipe_analytics_personalized_ads_on()()
    touch_button_back()


def test_cloud_menu_present():
    assert_exists_cloud_menu()


def test_link_in_setting_present():
    assert_link_in_setting()


def test_setting_menu_exit():
    touch_button_back()
    assert_exists_setting_and_coins()


def run_setting_new():
    remove_log_dir('setting_new.py')
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
    simple_report(__file__, logpath=True, output='html_report/setting_new.html')
