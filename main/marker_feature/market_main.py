# -*- encoding=utf8 -*-
__author__ = "QA PG"

from airtest.core.api import *
from airtest.report.report import simple_report
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir
from general_steps_alex import skip_system_pop


def test_press_market_button():
    touch(Template(r"tpl1670846241984.png", record_pos=(-0.372, 1.007), resolution=(1080, 2340)))
    assert_exists(Template(r"tpl1670846271079.png", record_pos=(0.01, -0.542), resolution=(1080, 2340)), "Ожидаем плашку магазина")


def test_first_product_buy():
    touch(Template(r"tpl1673533172354.png", record_pos=(0.351, 0.006), resolution=(1080, 2340)))
    assert_exists(Template(r"tpl1673532913329.png", record_pos=(-0.188, 0.412), resolution=(1200, 2000)), "Ожидаем часть попапа покупки")

    # Выход из меню оплаты тапом по заголовку через залоченный экран
    touch(Template(r"tpl1673516370052.png", record_pos=(-0.002, -0.538), resolution=(1080, 2340)))
    sleep(1)


def test_swipe_product_list():
    swipe(Template(r"tpl1670918388195.png", record_pos=(0.01, 0.294), resolution=(1080, 2340)), vector=[-0.0194, -0.8])
    assert_exists(Template(r"tpl1670918519701.png", record_pos=(-0.131, 0.549), resolution=(1080, 2340)), "Ожидаем отображение товара 3к монет")


# def test_last_product_buy():
#
#     touch(Template(r"tpl1670918650500.png", record_pos=(0.281, 0.561), resolution=(1080, 2340)))
#     assert_exists(Template(r"tpl1670918671500.png", record_pos=(0.007, 0.374), resolution=(1080, 2340)), "Please fill in the test point.")
#     # Выход из меню оплаты тапом по заголовку через залоченный экран
#     touch(Template(r"tpl1673516370052.png", record_pos=(-0.002, -0.538), resolution=(1080, 2340)))
#     sleep(1)


def test_failed():
    assert_exists(Template(r"tp607000284.png", record_pos=(-0.372, 1.007), resolution=(1080, 2340)))


def run_market_feature():
    remove_log_dir('marker_feature')
    auto_setup(
        __file__,
        logdir=AUTO_SETUP_ARG.get('logdir'),
        devices=[AUTO_SETUP_ARG.get('devices'), ],
        project_root=AUTO_SETUP_ARG.get('project_root'),
    )
    start_app("com.jollyco.jbpuzzleadventure")
    run_logger(skip_system_pop)
    run_logger(test_press_market_button)
    run_logger(test_first_product_buy)
    run_logger(test_swipe_product_list)
    # не стабилен для разных разрешений. продумать оптимизацию
    # run_logger(test_last_product_buy)
    run_logger(test_failed)
    stop_app("com.jollyco.jbpuzzleadventure")
    simple_report(__file__, logpath=True, output='html_report/market.html')



