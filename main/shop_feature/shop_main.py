# -*- encoding=utf8 -*-
__author__ = "TS"

from airtest.core.api import *
from airtest.report.report import simple_report
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir
from general_steps import skip_system_pop


def test_press_market_button():
    sleep(8)
    touch(Template(r"tpl1678884817931.png",
                   record_pos=(-0.379, 1.036),
                   resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1678884965851.png",
                           record_pos=(-0.002, -0.546),
                           resolution=(1080, 2400)), "Shop")


def test_shop_failed():
    touch(Template(r"tpl1678886094788.png",
                   record_pos=(0.308, 0.006),
                   resolution=(1080, 2400)))
    sleep(1.0)
    assert_not_exists(Template(r"tpl1678885322023.png",
                               record_pos=(0.0, 0.381),
                               resolution=(1080, 2400)))
    touch(Template(r"tpl1678886142174.png",
                   record_pos=(0.308, 0.17),
                   resolution=(1080, 2400)))
    sleep(1.0)
    assert_not_exists(Template(r"tpl1678885322023.png",
                               record_pos=(0.0, 0.381),
                               resolution=(1080, 2400)))
    touch(Template(r"tpl1678886163541.png",
                   record_pos=(0.308, 0.329),
                   resolution=(1080, 2400)))
    sleep(1.0)
    assert_not_exists(Template(r"tpl1678885322023.png",
                               record_pos=(0.0, 0.381),
                               resolution=(1080, 2400)))


def test_ads_hint():
    touch(Template(r"tpl1678885084910.png",
                   record_pos=(0.272, -0.334),
                   resolution=(1080, 2400)))
    sleep(20.0)
    touch(Template(r"tpl1678885160128.png",
                   record_pos=(0.392, -0.898),
                   resolution=(1080, 2400)))
    sleep(2.0)
    assert_exists(Template(r"tpl1678885189932.png",
                           record_pos=(0.001, -0.24),
                           resolution=(1080, 2400)), "Hint")
    assert_exists(Template(r"tpl1678885278475.png",
                           record_pos=(-0.001, 0.11),
                           resolution=(1080, 2400)), "x1")
    touch(Template(r"tpl1678885322023.png",
                   record_pos=(0.0, 0.381),
                   resolution=(1080, 2400)))
    sleep(1.0)
    assert_exists(Template(r"tpl1678885445348.png",
                           record_pos=(0.399, -0.909),
                           resolution=(1080, 2400)), "1")
    sleep(1.0)


def test_ads_coins():

    touch(Template(r"tpl1678885772209.png",
                   record_pos=(0.429, 1.068),
                   resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1678885897306.png",
                   record_pos=(0.094, -0.592),
                   resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1678886000001.png",
                   record_pos=(-0.219, 1.029),
                   resolution=(1080, 2400)))
    sleep(1.0)

    touch(Template(r"tpl1678885514821.png",
                   record_pos=(0.273, -0.172),
                   resolution=(1080, 2400)))
    sleep(20.0)
    touch(Template(r"tpl1678885160128.png",
                   record_pos=(0.392, -0.898),
                   resolution=(1080, 2400)))
    sleep(2.0)
    assert_exists(Template(r"tpl1678885616274.png",
                           record_pos=(0.001, -0.234),
                           resolution=(1080, 2400)), "Coin")
    assert_exists(Template(r"tpl1678885667252.png",
                           record_pos=(-0.003, 0.112),
                           resolution=(1080, 2400)), "x10")
    touch(Template(r"tpl1678885322023.png",
                   record_pos=(0.0, 0.381),
                   resolution=(1080, 2400)))
    assert_exists(Template(r"tpl1678886055763.png",
                           record_pos=(0.001, -0.907),
                           resolution=(1080, 2400)), "11")
    sleep(3.0)


def test_purchases_for_coins():
    touch(Template(r"tpl1678885772209.png",
                   record_pos=(0.429, 1.068),
                   resolution=(1080, 2400)))
    touch(Template(r"tpl1678885897306.png",
                   record_pos=(0.094, -0.592),
                   resolution=(1080, 2400)))
    touch(Template(r"tpl1678885897306.png",
                   record_pos=(0.094, -0.592),
                   resolution=(1080, 2400)))
    touch(Template(r"tpl1678885897306.png",
                   record_pos=(0.094, -0.592),
                   resolution=(1080, 2400)))
    touch(Template(r"tpl1678885897306.png",
                   record_pos=(0.094, -0.592),
                   resolution=(1080, 2400)))
    touch(Template(r"tpl1678885897306.png",
                   record_pos=(0.094, -0.592),
                   resolution=(1080, 2400)))
    touch(Template(r"tpl1678885897306.png",
                   record_pos=(0.094, -0.592),
                   resolution=(1080, 2400)))
    touch(Template(r"tpl1678885897306.png",
                   record_pos=(0.094, -0.592),
                   resolution=(1080, 2400)))
    touch(Template(r"tpl1678885897306.png",
                   record_pos=(0.094, -0.592),
                   resolution=(1080, 2400)))
    touch(Template(r"tpl1678886841413.png",
                   record_pos=(-0.283, -0.592),
                   resolution=(1080, 2400)))
    touch(Template(r"tpl1678886473551.png",
                   record_pos=(-0.198, 0.902),
                   resolution=(1080, 2400)))
    sleep(3.0)
    touch(Template(r"tpl1678884817931.png",
                   record_pos=(-0.379, 1.036),
                   resolution=(1080, 2400)))
    sleep(1.0)

    touch(Template(r"tpl1678886094788.png",
                   record_pos=(0.308, 0.006),
                   resolution=(1080, 2400)))
    sleep(1.0)
    assert_exists(Template(r"tpl1678885189932.png",
                           record_pos=(0.001, -0.24),
                           resolution=(1080, 2400)), "Hint")
    assert_exists(Template(r"tpl1678885278475.png",
                           record_pos=(-0.001, 0.11),
                           resolution=(1080, 2400)), "x1")
    touch(Template(r"tpl1678885322023.png",
                   record_pos=(0.0, 0.381),
                   resolution=(1080, 2400)))
    sleep(2.0)
    assert_exists(Template(r"tpl1678886892072.png",
                           record_pos=(0.395, -0.912),
                           resolution=(1080, 2400)), "3")
    sleep(1.0)
    touch(Template(r"tpl1678886142174.png",
                   record_pos=(0.308, 0.17),
                   resolution=(1080, 2400)))
    sleep(1.0)
    assert_exists(Template(r"tpl1678885189932.png",
                           record_pos=(0.001, -0.24),
                           resolution=(1080, 2400)), "Hint")
    assert_exists(Template(r"tpl1678886641504.png",
                           record_pos=(0.02, 0.11),
                           resolution=(1080, 2400)), "5")
    touch(Template(r"tpl1678885322023.png",
                   record_pos=(0.0, 0.381),
                   resolution=(1080, 2400)))
    sleep(2.0)
    assert_exists(Template(r"tpl1678887023215.png",
                           record_pos=(0.393, -0.91),
                           resolution=(1080, 2400)), "8")
    touch(Template(r"tpl1678886163541.png",
                   record_pos=(0.308, 0.329),
                   resolution=(1080, 2400)))
    sleep(1.0)
    assert_exists(Template(r"tpl1678885189932.png",
                           record_pos=(0.001, -0.24),
                           resolution=(1080, 2400)), "Hint")
    assert_exists(Template(r"tpl1678886696379.png",
                           record_pos=(0.02, 0.108),
                           resolution=(1080, 2400)), "20")
    touch(Template(r"tpl1678885322023.png",
                   record_pos=(0.0, 0.381),
                   resolution=(1080, 2400)))
    sleep(2.0)
    assert_exists(Template(r"tpl1678887126679.png",
                           record_pos=(0.372, -0.91),
                           resolution=(1080, 2400)), "28")


def test_purchases_for_dollars():
    swipe(Template(r"tpl1678886732306.png",
                   record_pos=(-0.01, 0.128),
                   resolution=(1080, 2400)),
          vector=[-0.0132, -0.2193])

    touch(Template(r"tpl1678887207476.png",
                   record_pos=(0.231, 0.071),
                   resolution=(1080, 2400)))
    sleep(3.0)
    assert_exists(Template(r"tpl1678887470007.png",
                           record_pos=(-0.18, 0.582),
                           resolution=(1080, 2400)), "1")
    assert_exists(Template(r"tpl1678887488850.png",
                           record_pos=(0.34, 0.579),
                           resolution=(1080, 2400)), "$0")

    touch(Template(r"tpl1678887331922.png",
                   record_pos=(0.404, 0.787),
                   resolution=(1080, 2400)))
    sleep(1.0)

    touch(Template(r"tpl1678887416675.png",
                   record_pos=(-0.396, -0.698),
                   resolution=(1080, 2400)))
    sleep(1.0)

    touch(Template(r"tpl1678887436589.png",
                   record_pos=(-0.002, 1.03),
                   resolution=(1080, 2400)))
    sleep(3.0)
    assert_exists(Template(r"tpl1678885189932.png",
                           record_pos=(0.001, -0.24),
                           resolution=(1080, 2400)), "Hint")
    assert_exists(Template(r"tpl1678885278475.png",
                           record_pos=(-0.001, 0.11),
                           resolution=(1080, 2400)), "x1")
    touch(Template(r"tpl1678885322023.png",
                   record_pos=(0.0, 0.381),
                   resolution=(1080, 2400)))
    sleep(2.0)
    assert_exists(Template(r"tpl1678887563338.png",
                           record_pos=(0.374, -0.909),
                           resolution=(1080, 2400)), "29")

    touch(Template(r"tpl1678890179493.png",
                   record_pos=(0.227, 0.394),
                   resolution=(1080, 2400)))
    sleep(2.0)
    touch(Template(r"tpl1678890193321.png",
                   record_pos=(0.103, -0.082),
                   resolution=(1080, 2400)))
    sleep(2.0)
    assert_exists(Template(r"tpl1678890220627.png",
                           record_pos=(-0.001, -0.251),
                           resolution=(1080, 2400)), "Oops")
    touch(Template(r"tpl1678890255960.png",
                   record_pos=(0.0, 0.099),
                   resolution=(1080, 2400)))


def run_shop_feature():
    remove_log_dir('shop_feature')
    auto_setup(
        __file__,
        logdir=AUTO_SETUP_ARG.get('logdir'),
        devices=[AUTO_SETUP_ARG.get('devices'), ],
        project_root=AUTO_SETUP_ARG.get('project_root'),
    )
    start_app("com.jollyco.jbpuzzleadventure")
    run_logger(skip_system_pop)
    run_logger(test_press_market_button)
    run_logger(test_ads_hint)
    run_logger(test_ads_coins)
    run_logger(test_purchases_for_coins)
    run_logger(test_purchases_for_dollars)
    stop_app("com.jollyco.jbpuzzleadventure")
    simple_report(__file__, logpath=True, output='html_report/shop.html')