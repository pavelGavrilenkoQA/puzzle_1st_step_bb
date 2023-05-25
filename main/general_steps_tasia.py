__author__ = "QA PG"

from page_object import *
from global_auto_agr import PAGE_ROOT_TAISIA


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


def assert_exist_empty_elements_list():
    sleep(6)
    assert_exists(empty_elements_list())


def touch_button_win():
    sleep(5)
    touch(button_win())
    sleep(3)


def assert_exists_empty_field():
    sleep(6)
    assert_exists(empty_field())
    sleep(1)


def asserts_exists_completed_art_tutorial():
    sleep(7)
    assert_exists(completed_art_tutorial())


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
    sleep(4)
    touch(button_start())
    sleep(2.0)


def assert_exists_text_setting():
    assert_exists(text_setting())


def touch_swipe_sound_on():
    touch(touch_swipe_sound_on())


def touch_swipe_sound_on():
    touch(swipe_sound_on())


def touch_swipe_sound_off():
    touch(swipe_sound_off())


def assert_exists_swipe_sound_off():
    assert_exists(swipe_sound_off())


def touch_swipe_vibration_on():
    touch(swipe_vibration_on())


def assert_exists_swipe_vibration_off():
    assert_exists(swipe_vibration_off())


def sound_vibration_on():
    touch(sound_vibration_on())


def touch_swipe_vibration_off():
    touch(swipe_vibration_off())


def assert_exists_sound_vibration_on():
    assert_exists(sound_vibration_on())


def touch_english_flag_text():
    touch(english_flag_text())


def assert_exists_all_languages():
    assert_exists(all_languages())


def touch_button_privacy():
    touch(button_privacy())


def assert_exists_green_privacy_shield():
    sleep(2)
    assert_exists(green_privacy_shield())


def touch_swipe_analytics_on():
    touch(swipe_analytics_on())


def touch_swipe_personalized_ads_on():
    touch(swipe_analytics_on())


def assert_exists_swipe_analytics_personalized_off():
    assert_exists(swipe_analytics_personalized_ads_off())


def assert_exists_swipe_analytics_personalized_ads_on():
    assert_exists(swipe_analytics_personalized_ads_on())


def touch_swipe_analytics_off():
    touch(swipe_analytics_off())


def touch_swipe_personalized_off():
    touch(swipe_personalized_off())


def assert_exists_cloud_menu():
    assert_exists(cloud_menu())


def assert_link_in_setting():
    assert_exists(link_in_setting())


def assert_exists_setting_and_coins():
    assert_exists(setting_and_coins())


def touch_button_daily():
    sleep(5.0)
    touch(button_daily())
    sleep(2.0)


def assert_daily_challenge():
    assert_exists(daily_challenge())


def assert_reward():
    assert_exists(reward())


def assert_button_back():
    assert_exists(button_back())


def assert_button_start():
    assert_exists(button_start())


def touch_icon_shop():
    touch(icon_shop())
    sleep(2.0)


def assert_text_shop():
    assert_exists(text_shop())


def touch_first_product_buy():
    touch(first_product_buy())


def touch_locked_text_shop():
    touch(locked_text_shop())


def swipe_product_list():
    swipe(product_list())


def assert_exists_product_3k_coins():
    assert_exists(product_3k_coins())


def test_failed():
    assert_exists(Template(
        r"tp607000284.png"))


def touch_sugar_mesh_pack():
    touch(sugar_mesh_pack())


def assert_exists_sugar_mesh_bw():
    assert_exists(sugar_mesh_bw())


def assert_exists_sugar_mesh_pack():
    assert_exists(sugar_mesh_pack())


def touch_sugar_mesh_bw():
    touch(sugar_mesh_bw())


def assert_exists_button_win():
    assert_exists(button_win())


def touch_swipe_rotation_off():
    touch(swipe_rotation_off())


def assert_exists_swipe_():
    sleep(2)
    assert_exists(swipe_rotation_on())


def assert_not_exists_coins_3():
    assert_not_exists(coins_3())


def touch_swipe_rotation_on():
    touch(swipe_rotation_on())


def assert_exists_swipe_rotation_off():
    assert_exists(swipe_rotation_off())


def assert_not_exists_coins_6():
    assert_not_exists(coins_6())


def swipe_elements_to_16():
    swipe(Template(
        r"swipe_elements_to_16.png"))


def assert_exists_element_16():
    sleep(2)
    assert_exists(elements_16())


def assert_not_exists_coins_3():
    assert_not_exists(coins_3())


def another_puzzle_in_progress():
    sleep(4)
    if exists(another_puzzle_in_progress()):
        sleep(3)


def touch_button_yes():
    touch(button_yes())
    sleep(3.0)


def assert_exists_button_level_assert():
    assert_exists(button_level_assert())


def touch_button_exit():
    touch(button_exit())
    sleep(1.0)


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


def elements_49():
    touch(elements_49())


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


def elements_81():
    touch(elements_81())


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
    sleep(24.0)


def touch_ads_coins():
    touch(ads_coins())
    sleep(24.0)


def touch_close_ads():
    touch(close_ads())
    sleep(2.0)


def assert_hint_x1():
    sleep(1.0)
    assert_exists(hint_x1())


def assert_hint3():
    assert_exists(hint_3())


def touch_button_claim():
    touch(button_claim())
    sleep(3.0)


def assert_1():
    assert_exists(hint_1())


def touch_debug():
    touch(debug())
    sleep(1.0)


def touch_plus_100():
    touch(plus_100())
    sleep(1.0)


def touch_hide():
    touch(hide())
    sleep(1.0)


def assert_coins_x10():
    assert_exists(coins_x10())


def assert_x10():
    assert_exists(x10())


def touch_plus_1():
    touch(plus_1())
    sleep(1.0)


def touch_reload():
    touch(reload())
    sleep(1.0)


def assert_x1():
    assert_exists(x1())


def assert_claim():
    assert_exists(button_claim())


def assert_coins11():
    sleep(1)
    assert_exists(coins_11())


def assert_91():
    sleep(1)
    assert_exists(coins_91())


def assert_5():
    assert_exists(hint_5())


def assert_8():
    sleep(1)
    assert_exists(hint_8())


def assert_20():
    assert_exists(hint_20())


def assert_28():
    assert_exists(hint_28())


def swipe_shop():
    swipe(Template(fr"{PAGE_ROOT_TAISIA}swipe_shop.png",
                   record_pos=(-0.103, 0.128),
                   resolution=(1080, 2400)),
          vector=[-0.0145, -0.1634])
    sleep(2.0)


def android_price0():
    assert_exists(android_price_0())


def android_quantity1():
    assert_exists(android_quantity_1())


def touch_price_0():
    touch(price_0_dollars())
    sleep(5.0)


def touch_android_choice():
    touch(android_choice())
    sleep(1.0)


def touch_card_approve():
    touch(android_card())
    sleep(1.0)


def touch_buy():
    touch(android_buy())
    sleep(1.0)


def assert_29():
    sleep(1)
    assert_exists(hint_29())


def touch_price_4():
    touch(price_4_dollars())
    sleep(1.0)


def touch_loading():
    touch(loading())
    sleep(1.0)


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
    touch((198, 970))
    sleep(1)


def touch_daily_puzzle_2():
    touch((542, 874))
    sleep(1)


def touch_daily_puzzle_3():
    touch((892, 959))
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
    sleep(2.0)
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
    sleep(24.0)


def assert_text_back():
    assert_exists(text_back())


def assert_not_attention():
    assert_not_exists(attention())


def assert_not_text_oops():
    assert_not_exists(text_oops())


def assert_not_text_exit():
    assert_not_exists(text_exit())


def assert_not_text_hint():
    assert_not_exists(text_hint())


def assert_text_no_hint():
    assert_exists(text_no_hint())


def assert_4():
    assert_exists(hint_4())


def assert_25():
    assert_exists(coins_25())


def touch_button_claim_daily_reward():
    touch(button_claim_daily_reward())
    sleep(1.0)


def touch_minus_10():
    touch(minus_10())
    sleep(1.0)


def touch_minus_1():
    touch(minus_1())
    sleep(1.0)


def assert_text_hint_ads():
    assert_exists(text_hint_ads())


def touch_button_back_popup():
    sleep(2)
    touch(button_back_popup())
    sleep(2.0)


def assert_pass():
    sleep(2)
    assert_exists(button_pass())
    sleep(1.0)


def touch_button_claim():
    touch(button_claim())
    sleep(7)


def touch_button_tap():
    sleep(2)
    touch(button_tap())
    sleep(5)


def assert_button_ok():
    assert_exists(button_ok())
