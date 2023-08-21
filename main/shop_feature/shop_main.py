# -*- encoding=utf8 -*-
__author__ = "TS"

from airtest.report.report import simple_report
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir
from general_steps_tasia import *


def test_debug_clear():
    touch_debug()
    touch_button_simulate_remote_ads()
    touch_reload()


def test_press_market_button():
    touch_icon_shop()
    assert_text_shop()


def test_pop_up_no_ads():
    assert_ads_offer_shop()


def test_purchases():
    assert_ads_hint()
    assert_shop_hint_x1()
    assert_limit()
    assert_shop_hint_x5()
    assert_shop_hint_x20()
    assert_shop_hint_x100()


# def test_receiving_hint():
#     touch_button_claim()
#     assert_1()
#
#
# def test_ads_coins():
#     touch_debug()
#     touch_plus_100()
#     touch_hide()
#     touch_ads_coins()
#     touch_close_ads()
#     assert_coins_x10()
#     assert_x10()
#     assert_claim()
#
#
# def test_receiving_coins():
#     touch_button_claim()
#     assert_coins11()
#
#
# def debug():
#     touch_debug()
#     for i in range(8):
#         (touch_plus_100())
#     touch_plus_1()
#     touch_reload()
#     assert_91()
#
#
# def test_purchases_for_50coins():
#     touch_icon_shop()
#     touch_50()
#     assert_hint_x1()
#     assert_x1()
#     touch_button_claim()
#     assert_hint3()
#
#
# def test_purchases_for_200coins():
#     touch_200()
#     assert_hint_x1()
#     assert_5()
#     touch_button_claim()
#     assert_8()
#
#
# def test_purchases_for_600coins():
#     touch_600()
#     assert_hint_x1()
#     assert_20()
#     touch_button_claim()
#     assert_28()
#
#
# def test_purchases_for_0dollars():
#     touch_price_0()
#     assert_text_hint_ads()
#     android_quantity1()
#     android_price0()
#     touch_buy()
#     assert_hint_x1()
#     assert_x1()
#     touch_button_claim()
#     assert_29()
#
#
def test_purchase_failed():
    touch_price_4()
    touch_loading()
    assert_text_oops()
    touch_button_yes()


def run_shop_new():
    remove_log_dir('shop_feature')
    auto_setup(
        __file__,
        logdir=AUTO_SETUP_ARG.get('logdir'),
        devices=[AUTO_SETUP_ARG.get('devices'), ],
        project_root=AUTO_SETUP_ARG.get('project_root'),
    )
    start_app("com.jollyco.jbpuzzleadventure")
    run_logger(skip_system_pop)
    run_logger(test_debug_clear)
    run_logger(test_press_market_button)
    run_logger(test_pop_up_no_ads)
    run_logger(test_purchases)
    # run_logger(test_ads_coins)
    # run_logger(test_receiving_coins)
    # run_logger(debug)
    # run_logger(test_purchases_for_50coins)
    # run_logger(test_purchases_for_200coins)
    # run_logger(test_purchases_for_600coins)
    # run_logger(test_purchases_for_0dollars)
    run_logger(test_purchase_failed)
    stop_app("com.jollyco.jbpuzzleadventure")
    simple_report(__file__, logpath=True, output='html_report/shop_feature.html')
