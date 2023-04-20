__author__ = "QA PG"

from airtest.core.api import *
from airtest.report.report import simple_report
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir
from page_object import *


def skip_system_pop():
    sleep(10)
    keyevent("BACK")
    sleep(6)
    keyevent("BACK")
    sleep(6)
    keyevent("BACK")
    sleep(6)


def touch_button_ok():
    touch(button_ok())


def assert_exists_tutorial_image():
    sleep(6)
    assert_exists(tutorial_image())


# def test_tutorial_part_1():
#    touch(Template(
#        r"button_ok.png"))
#    sleep(6)
#    assert_exists(Template(
#        r"empty_elements_list.png"))
#    sleep(5)
#    touch(Template(
#        r"button_win.png"))
#   sleep(7)
#    assert_exists(Template(
#        r"tutorial_image.png"))

def assert_exist_empty_elements_list():
    sleep(6)
    assert_exists(empty_elements_list())


def touch_button_win():
    sleep(5)
    touch(button_win())


# def test_tutorial_part_2():
#    touch(Template(
#        r"button_ok.png"))
#    sleep(6)
#    assert_exists(Template(
#        r"empty_field.png"))
#    touch(Template(
#        r"button_win.png"))
#    assert_exists(Template(
#        r"tutorial_image.png"))

def assert_exists_empty_field():
    sleep(6)
    assert_exists(empty_field())


# def test_tutorial_part_3():
#    touch(Template(
#        r"button_ok.png"))
#    sleep(7)
#    assert_exists(Template(
#        r"completed_art_tutorial.png"))

def asserts_exists_completed_art_tutorial():
    sleep(7)
    assert_exists(completed_art_tutorial())


# def test_language_check():
#    sleep(2)
#    touch(Template(
#        r"button_back.png"))
#    sleep(2)
#    touch(Template(
#       r"button_back.png"))
#    sleep(2)
#    touch(Template(
#        r"button_settings.png"))
#    if not exists(Template(
#        r"english_language.png")):
#        touch(Template(
#        r"setting_menu.png"))
#    touch(Template(
#         r"english_language.png"))
#    sleep(2)
#    assert_exists(Template(
#         r"english_language.png"))
#    touch(Template(
#        r"button_back.png"))
#    sleep(2)
#    touch(Template(
#        r"travelling_pack_color.png"))
#    touch(Template(
#        r"travelling_pack_bw.png"))
#    touch(Template(
#        r"button_start.png"))
#    sleep(6)

def touch_button_back():
    sleep(2)
    touch(button_back())


# def touch_button_settings():
#     sleep(2)
#     touch(button_settings())


def switch_english_language_test():
    if not exists(english_language_test()):
        touch(setting_menu())
        touch(english_language_test())
        sleep(2)
        assert_exists(english_language_test())


def touch_travelling_pack():
    sleep(2)
    touch(travelling_pack_color())
    touch(travelling_pack_bw())
    touch(button_start())
    sleep(6)


def touch_button_start():
    sleep(4)
    touch(button_start())


# def test_press_setting_button():
#    touch(Template(
#        r"button_settings.png"))
#    assert_exists(Template(
#        r"text_setting.png"))

def assert_exists_text_setting():
    assert_exists(text_setting())


# def test_sound_off():
#    touch(Template(
#       r"swipe_sound_on.png"))
#    assert_exists(Template(
#        r"swipe_sound_off.png"))

def touch_swipe_sound_on():
    touch(touch_swipe_sound_on())


def touch_swipe_sound_on():
    touch(swipe_sound_on())


def touch_swipe_sound_off():
    touch(swipe_sound_off())


def assert_exists_swipe_sound_off():
    assert_exists(swipe_sound_off())


# def test_vibro_off():
#   touch(Template(
#        r"swipe_vibration_on.png"))
#    assert_exists(Template(
#        r"swipe_vibration_off.png"))

def touch_swipe_vibration_on():
    touch(swipe_vibration_on())


def assert_exists_swipe_vibration_off():
    assert_exists(swipe_vibration_off())


# def test_sound_and_vibro_on():
#    touch(Template(
#        r"sound_vibration_on.png"))
#    touch(Template(
#        r"swipe_vibration_off.png"))
#    assert_exists(Template(
#        r"sound_vibration_on.png"))

def touch_sound_vibration_on():
    touch(sound_vibration_on())


def touch_swipe_vibration_off():
    touch(swipe_vibration_off())


def assert_exists_sound_vibration_on():
    assert_exists(sound_vibration_on())


# def test_language_list_get():
#    touch(Template(
#        r"english_flag_text.png"))
#    assert_exists(Template(
#        r"all_languages.png"))
#    touch(Template(
#        r"button_back.png"))

def touch_english_flag_text():
    touch(english_flag_text())


def assert_exists_all_languages():
    assert_exists(all_languages())


# def test_privacy_tap():
#    touch(Template(
#        r"button_privacy.png"))
#    assert_exists(Template(
#        r"green_privacy_shield.png"))

def touch_button_privacy():
    touch(button_privacy())


def assert_exists_green_privacy_shield():
    sleep(2)
    assert_exists(green_privacy_shield())


# def test_off_all_privacy():
#    touch(Template(
#        r"swipe_analytics_on.png"))
#    touch(Template(
#        r"swipe_personalized_ads_on.png"))
#    assert_exists(Template(
#        r"swipe_analytics_personalized_ads_off.png"))

def touch_swipe_analytics_on():
    touch(swipe_analytics_on())


def touch_swipe_personalized_ads_on():
    touch(personalized_ads_on())


def assert_exists_swipe_analytics_personalized_off():
    assert_exists(swipe_analytics_personalized_ads_off())


def assert_exists_swipe_analytics_personalized_ads_on():
    assert_exists(swipe_analytics_personalized_ads_on())


# def test_on_all_privacy():
#    touch(Template(
#        r"swipe_analytics_off.png"))
#    touch(Template(
#        r"swipe_personalized_off.png"))
#    assert_exists(Template(
#        r"swipe_analytics_personalized_on.png"))
#    touch(Template(
#        r"button_back.png"))

def touch_swipe_analytics_off():
    touch(swipe_analytics_off())


def touch_swipe_personalized_off():
    touch(swipe_personalized_off())


# def test_cloud_menu_present():
#    assert_exists(Template(
#        r"cloud_menu.png"))

def assert_exists_cloud_menu():
    assert_exists(cloud_menu())


# def test_link_in_setting_present():
#    assert_exists(Template(
#        r"link_in_setting.png"))

def assert_link_in_setting():
    assert_exists(link_in_setting())


# def test_setting_menu_exit():
#    touch(Template(
#        r"button_back.png"))
#    assert_exists(Template(
#        r"setting_and_coins.png"))

def assert_exists_setting_and_coins():
    assert_exists(setting_and_coins())


# def test_press_daily_button(assert_exists=None):
#    touch(Template(
#        r"button_daily.png"))
#    assert_exists(Template(
#        r"daily_challenge.png"))
#    and assert_exists(Template(
#        r"reward.png"))

def touch_button_daily():
    touch(button_daily())


def assert_exists_daily_challenge():
    assert_exists(daily_challenge())


def assert_exists_reward():
    assert_exists(reward())


# def test_tap_left_daily_puzzle():
#    sleep(3)
#    touch(Template(
#        r"part_of_daily.png"))
#    assert_exists(Template(
#        r"button_start.png"))
#    touch(Template(
#        r"button_back.png"))

def assert_button_back():
    assert_exists(button_back())


def touch_part_of_daily():
    sleep(3)
    touch(part_of_daily())


def assert_button_start():
    assert_exists(button_start())


# def test_press_market_button():
#    touch(Template(
#        r"icon_shop.png"))
#    assert_exists(Template(
#        r"text_shop.png"))

def touch_icon_shop():
    touch(icon_shop())


def assert_exists_text_shop():
    assert_exists(text_shop())


# def test_first_product_buy():
#    touch(Template(
#        r"first_product_buy.png"))
#    assert_exists(Template(
#        r"purchase_popap.png"))
#    touch(Template(
#        r"locked_text_shop.png"))

def touch_first_product_buy():
    touch(first_product_buy())


def assert_exists_purchase_popap():
    assert_exists(purchase_popap())


def touch_locked_text_shop():
    touch(locked_text_shop())


# def test_swipe_product_list():
#    swipe(Template(
#        r"product_list.png"))
#    assert_exists(Template(
#        r"product_3k_coins.png"))

def swipe_product_list():
    swipe(product_list())


def assert_exists_product_3k_coins():
    assert_exists(product_3k_coins())


# def test_failed():
#    assert_exists(Template(
#        r"tp607000284.png"))

def test_failed():
    assert_exists(Template(
        r"tp607000284.png"))


# def test_open_free_pack():
#    touch(Template(
#        r"sugar_mesh_pack.png"))
#    assert_exists(Template(
#         r"sugar_mesh_bw.png"))

def touch_sugar_mesh_pack():
    touch(sugar_mesh_pack())


def assert_exists_sugar_mesh_bw():
    assert_exists(sugar_mesh_bw())


def assert_exists_sugar_mesh_pack():
    assert_exists(sugar_mesh_pack())


# def test_open_art():
#    touch(Template(
#        r"sugar_mesh_bw.png"))
#    assert_exists(Template(
#        r"button_win.png"))

def touch_sugar_mesh_bw():
    touch(sugar_mesh_bw())


def assert_exists_button_win():
    assert_exists(button_win())


# def test_rotation_button_on():
#    touch(Template(
#        r"swipe_rotation_off.png"))
#    assert_exists(Template(
#        r"swipe_rotation_on.png"))
#    assert_not_exists(Template(
#        r"coins_3.png"))

def touch_swipe_rotation_off():
    touch(swipe_rotation_off())


def assert_exists_swipe_():
    sleep(2)
    assert_exists(swipe_rotation_on())


def assert_not_exists_coins_3():
    assert_not_exists(coins_3())


# def test_rotation_button_off():
#    touch(Template(
#        r"swipe_rotation_on.png"))
#    assert_exists(Template(
#        r"swipe_rotation_off.png"))
#    assert_not_exists(Template(
#        r"coins_6.png"))

def touch_swipe_rotation_on():
    touch(swipe_rotation_on())


def assert_exists_swipe_rotation_off():
    assert_exists(swipe_rotation_off())


def assert_not_exists_coins_6():
    assert_not_exists(coins_6())


# def test_swipe_count_element_to_16():
#    swipe(Template(
#        r"swipe_elements_to_16.png"))
#    sleep(2)
#    assert_exists(Template(
#        r"elements_16.png"))
#    assert_not_exists(Template(
#        r"coins_3.png"))

def swipe_elements_16():
    swipe(swipe_elements_to_16())


def assert_exists_element_16():
    sleep(2)
    assert_exists(elements_16())


def assert_not_exists_coins_3():
    assert_not_exists(coins_3())


# def test_start_art_puzzle():
#    sleep(4)
#    if exists(Template(
#            r"another_puzzle_in_progress.png"))
#        sleep(3)
#        touch(Template(
#            r"button_yes.png"))
#        assert_exists(Template(
#            r"buton_level_assert.png"))

def test_another_puzzle_in_progress():
    sleep(4)
    if exists(another_puzzle_in_progress()):
        sleep(3)
        return True


def touch_button_yes():
    touch(button_yes())


def assert_exists_button_level_assert():
    assert_exists(button_level_assert())


# def test_exit_popup():
#    touch(Template(
#        r"button_exit.png"))
#    assert_exists(Template(
#        r"tpl1671008301646.png"))

def touch_button_exit():
    touch(button_exit())


def popap_before_exit():
    assert_exists(popap_before_exit_1())


# def test_exit_popup_close():
#    touch(Template(
#        r"button_no.png"))
#    assert_not_exists(Template(
#        r"buton_level_assert.png"))
#    assert_not_exists(Template(
#        r"sugar_mesh_pack.png"))
#    assert_not_exists(Template(
#        r"sugar_mesh_bw.png"))

def touch_button_no():
    touch(button_no())


def assert_not_exists_button_level_assert():
    assert_not_exists(button_level_assert())


def assert_not_exists_sugar_mesh_pack():
    assert_not_exists(sugar_mesh_pack())


def assert_not_exists_sugar_mesh_bw():
    assert_not_exists(sugar_mesh_bw())


def assert_exists_completed_pack_with_1_art():
    sleep(2)
    assert_exists(completed_pack_with_1_art())


def touch_completed_pack_with_1_art():
    sleep(2)
    touch(completed_pack_with_1_art())
    sleep(2)


def assert_exists_completed_9_elements():
    sleep(4)
    assert_exists(completed_9_elements())


def touch_elements_16_2():
    touch(elements_16_2())


def assert_exists_completed_16_elements():
    sleep(4.0)
    assert_exists(completed_16_elements())


def touch_next_element():
    sleep(2)
    touch(next_element())


def touch_puzzle_25_elements():
    touch(elements_25())


def assert_completed_25_level():
    assert_exists(completed_25_level())


def touch_elements_49():
    touch(element_49())


def assert_completed_49_elements():
    assert_exists(completed_49_elements())
    sleep(2)


def assert_64_elements():
    assert_exists(elements_64())


def touch_64_elements():
    touch(elements_64())


def assert_completed_64_element():
    assert_exists(completed_64_elements())
    sleep(2)


def assert_elements_81():
    sleep(2)
    assert_exists(element_81())


def touch_elements_81():
    touch(element_81())


def completed_81_element():
    assert_exists(completed_81_elements())


def touch_elements_144():
    touch(elements_144())


def assert_elements_144():
    assert_exists(elements_144())


def completed_144_element():
    assert_exists(completed_144_elements())


def touch_elements_256():
    touch(elements_256())
    sleep(2)


def assert_elements_256():
    assert_exists(elements_256())


def completed_element_256():
    assert_exists(completed_elements_256())


def claim_in_russian():
    sleep(8)
    if exists(button_claim_in_russian()):
        touch(button_claim_in_russian())


def touch_button_claim():
    sleep(7)
    touch(button_claim())


def touch_button_settings():
    sleep(2)
    touch(button_settings_2())