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


# def test_politic_accept():
#   touch(Template(r"button_ok.png"))
#  sleep(6)
#  assert_exists(Template(r"tutorial_image.png"))

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
    sleep(3)


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
    sleep(1.0)


def touch_button_settings():
    touch(button_settings())
    sleep(1.0)


def english_language():
    if not exists(english_language()):
        touch(setting_menu())
        touch(english_language())
        sleep(2)
        assert_exists(english_language())


def touch_travelling_pack():
    sleep(2)
    touch(travelling_pack_color())
    touch(travelling_pack_bw())
    touch(button_start())
    sleep(6)


def touch_button_start():
    touch(button_start())
    sleep(2.0)




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

def sound_vibration_on():
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
    touch(swipe_analytics_on())


def assert_exists_swipe_analytics_personalized_off():
    assert_exists(swipe_analytics_personalized_ads_off())


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
    assert_exists( cloud_menu())


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
    sleep(1.0)


def assert_daily_challenge():
    assert_exists(daily_challenge())


def assert_reward():
    assert_exists(reward())


# def test_tap_left_daily_puzzle():
#    sleep(3)
#    touch(Template(
#        r"part_of_daily.png"))
#    assert_exists(Template(
#        r"button_start.png"))
#    touch(Template(
#        r"button_back.png"))


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


def assert_exists():
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
    assert_not_exists( coins_6())


# def test_swipe_count_element_to_16():
#    swipe(Template(
#        r"swipe_elements_to_16.png"))
#    sleep(2)
#    assert_exists(Template(
#        r"elements_16.png"))
#    assert_not_exists(Template(
#        r"coins_3.png"))

def swipe_elements_to_16():
    swipe(Template(
        r"swipe_elements_to_16.png"))


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

def another_puzzle_in_progress():
    sleep(4)
    if exists(another_puzzle_in_progress()):
        sleep(3)


def touch_button_yes():
    touch(button_yes())
    sleep(3.0)


def assert_exists_button_level_assert():
    assert_exists(button_level_assert())


# def test_exit_popup():
#    touch(Template(
#        r"button_exit.png"))
#    assert_exists(Template(
#        r"tpl1671008301646.png"))

def touch_button_exit():
    touch(button_exit())
    sleep(1.0)


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
    sleep(1.0)


def assert_not_exists_button_level_assert():
    assert_not_exists(button_level_assert())


def assert_not_exists_sugar_mesh_pack():
    assert_not_exists(sugar_mesh_pack())


def assert_not_exists_sugar_mesh_bw():
    assert_not_exists(sugar_mesh_bw())


def assert_exists_completed_pack_with_1_art():
    assert_exists(completed_pack_with_1_art())


def touch_completed_pack_with_1_art():
    touch(completed_pack_with_1_art())


def assert_exists_completed_9_elements():
    assert_exists(completed_9_elements())


def touch_elements_16_2():
    touch(elements_16_2())


def assert_exists_completed_16_elements():
    sleep(4.0)
    assert_exists(completed_16_elements())


def touch_next_element():
    touch(next_element())


def touch_puzzle_25_elements():
    touch(elements_25())


def completed_25_level():
    assert_exists(completed_25_level())


def elements_49():
    touch(elements_49())


def completed_49_elements():
    assert_exists(completed_49_elements())


def test_play_puzzle_64_elements():
    touch(elements_64())


def completed_64_elements():
    assert_exists(completed_64_elements())


def elements_81():
    touch(elements_81())


def completed_81_elements():
    assert_exists(completed_81_elements())


def elements_144():
    touch(elements_144())


def completed_144_elements():
    assert_exists(completed_144_elements())


def elements_256():
    touch(elements_256())


def completed_elements_256():
    assert_exists(completed_elements_256())


def touch_50():
    touch(locked_50())
    sleep(1)


def touch_200():
    touch(locked_200())
    sleep(1)


def touch_600():
    touch(locked_600())
    sleep(1)


def assert_not_exists_claim():
    assert_not_exists(button_claim())


def touch_ads_hint():
    touch(ads_hint())
    sleep(20.0)


def touch_ads_coins():
    touch(ads_coins())
    sleep(20.0)


def touch_close_ads():
    touch(close_ads())
    sleep(2.0)


def assert_hint_x1():
    assert_exists(hint_x1)


def assert_hint3():
    assert_exists(hint_3())


def touch_button_claim():
    touch(button_claim())
    sleep(1.0)


def assert_1():
    assert_exists(hint_1())


def touch_debug():
    touch(debug())


def touch_plus_100():
    touch(plus_100())


def touch_hide():
    touch(hide())


def assert_coins_x10():
    assert_exists(coins_x10())


def assert_x10():
    assert_exists(x10())


def touch_plus_1():
    touch(plus_1())


def touch_reload():
    touch(reload())


def assert_x1():
    assert_exists(x1())


def assert_claim():
    assert_exists(button_claim())


def assert_hint11():
    assert_exists(cons_11())


def assert_91():
    assert_exists(assert_91())


def assert_5():
    assert_exists(hint_5())


def assert_8():
    assert_exists(hint_8())


def assert_20():
    assert_exists(hint_20())


def assert_28():
    assert_exists(hint_28())


def swipe_shop():
    swipe(swipe_shop(),
          vector=[-0.0132, -0.2193]
          )


def android_price0():
    assert_exists(android_price_0())


def android_quantity1():
    assert_exists(android_quantity_1())


def price_0():
    touch(price_0_dollars())


def touch_android_choice():
    touch(touch_android_choice())


def touch_card_approve():
    touch(android_card())


def touch_buy():
    touch(android_buy())


def assert_29():
    assert_exists(hint_29())


def price_4():
    touch(price_4_dollars())


def touch_loading():
    touch(loading())


def assert_text_oops():
    assert_exists(text_oops())


def assert_completed_0_daily_puzzle():
    assert_exists(completed_0_daily_puzzle())


def assert_completed_1_daily_puzzle():
    assert_exists(completed_1_daily_puzzle())


def assert_completed_2_daily_puzzle():
    assert_exists(completed_2_daily_puzzle())


def assert_completed_3_daily_puzzle():
    assert_exists(completed_3_daily_puzzle())


def touch_daily_puzzle_1():
    touch(daily_puzzle_1())
    sleep(1)


def touch_daily_puzzle_2():
    touch(daily_puzzle_2())
    sleep(1)


def touch_daily_puzzle_3():
    touch(daily_puzzle_3())
    sleep(1)


def assert_text_exit():
    assert_exists(text_exit())


def assert_hourglass_1():
    assert_exists(hourglass_1())


def assert_hourglass_2():
    assert_exists(hourglass_2())


def assert_hourglass_3():
    assert_exists(hourglass_3())


def assert_hourglass_main():
    assert_exists(hourglass_main())


def touch_button_continue():
    touch(text_continue())
    sleep(3.0)


def touch_hint_main():
    touch(hint_main())
    sleep(1.0)


def assert_text_hint():
    assert_exists(text_hint())


def assert_text_puzzle_completed():
    assert_exists(text_puzzle_completed())


def assert_button_save():
    assert_exists(button_save())


def assert_checkmark_1():
    assert_exists(checkmark_1())


def assert_checkmark_2():
    assert_exists(checkmark_2())


def assert_checkmark_3():
    assert_exists(checkmark_3())


def assert_x25():
    assert_exists(x25())


def assert_x2():
    assert_exists(x2())


def assert_x4():
    assert_exists(x4())


def touch_ads_reward():
    touch(ads_reward())
    sleep(20.0)


def assert_text_back():
    assert_exists(text_back())


def assert_not_attention():
    assert_not_exists(attention())











