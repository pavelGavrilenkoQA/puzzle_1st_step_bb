# -*- encoding=utf8 -*-
__author__ = "TS"

from airtest.core.api import *
from airtest.report.report import simple_report
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir
from general_steps import *


def test_press_market_button():
    touch_icon_shop()
    assert_exists_text_shop()


def test_locked_purchases():
    touch_50()
    assert_not_exists_claim()
    touch_200()
    assert_not_exists_claim()
    touch_600()
    assert_not_exists_claim()


def test_ads_hint():
    touch_ads_hint()
    touch_close_ads()
    assert_hint_x1()
    assert_x1()
    assert_claim()


def test_receiving_hint():
    touch_claim()
    assert_1


def test_ads_coins():
    touch_debug()
    touch_plus_100()
    touch_hide()
    touch_ads_coins()
    touch_close_ads()
    assert_coins_x10()
    assert_x10()
    assert_claim()


def test_receiving_coins():
    touch_claim()
    assert_hint11()


def debug():
    touch_debug()
    for i in range(8):
        (touch_plus_100())
    touch_plus_1()
    touch_reload()
    assert_91()


def test_purchases_for_50coins():
    touch_icon_shop()
    touch_50()
    assert_hint_x1()
    assert_x1()
    touch_claim()
    assert_hint3()
    










