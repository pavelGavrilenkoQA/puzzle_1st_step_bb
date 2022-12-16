# -*- encoding=utf8 -*-
__author__ = "QA PG"

from airtest.core.api import *
from airtest.report.report import simple_report
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir


def test_open_free_pack():
    touch(Template(
        r"tpl1671007475423.png",
        record_pos=(-0.319, -0.529),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1671112981459.png",
        record_pos=(0.001, -0.477),
        resolution=(1080, 2340)),
        "Ожидаем пазл внутри пака"
    )


def test_open_art():
    touch(Template(
        r"tpl1671112981459.png",
        record_pos=(0.001, -0.477),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1671007554979.png",
        record_pos=(-0.004, 0.531),
        resolution=(1080, 2340)),
        "Ожидаем наличие кнопки старта при открытии арта"
    )


def test_rotation_button_on():
    touch(Template(
        r"tpl1671007673702.png",
        record_pos=(0.111, 0.297),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1671007693112.png",
        record_pos=(0.006, 0.294),
        resolution=(1080, 2340)),
        "Ожидаем включение свичера поворта"
    )
    assert_not_exists(Template(
        r"tpl1671007708261.png",
        record_pos=(0.068, 0.413),
        resolution=(1080, 2340)),
        "Ожидаем изменение награды"
    )


def test_rotation_button_off():
    touch(Template(
        r"tpl1671007906808.png",
        record_pos=(0.085, 0.3),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1671007938748.png",
        record_pos=(0.009, 0.291),
        resolution=(1080, 2340)),
        "Ожидаем отключение свичера поворта")
    assert_not_exists(Template(
        r"tpl1671007951535.png",
        record_pos=(0.069, 0.413),
        resolution=(1080, 2340)),
        "Ожидаем изменение награды")


def test_swipe_count_element_to_16():
    swipe(Template(
        r"tpl1671008006471.png",
        record_pos=(0.095, 0.185),
        resolution=(1080, 2340)),
        vector=[-0.1300, -0.0062]
    )
    # КД для заверешения анимации свайпа
    sleep(2)
    assert_exists(Template(
        r"tpl1671008077643.png",
        record_pos=(-0.011, 0.219),
        resolution=(1080, 2340)),
        "Ожидаем отцетровку элемента 16"
    )
    assert_not_exists(Template(
        r"tpl1671007708261.png",
        record_pos=(0.068, 0.413),
        resolution=(1080, 2340)),
        "Ожидаем изменение награды"
    )


def test_start_art_puzzle():
    touch(Template(
        r"tpl1671008126415.png",
        record_pos=(0.003, 0.535),
        resolution=(1080, 2340))
    )
    # Проверяем наличие попапа сбора другого пазла
    if exists(Template(
            r"tpl1671009261312.png",
            record_pos=(0.001, -0.008),
            resolution=(1080, 2340))
    ):
        # При отображении подтверждаем переход к сбору нового пазла
        touch(Template(
            r"tpl1671009289719.png",
            record_pos=(-0.131, 0.06),
            resolution=(1080, 2340))
        )

    assert_exists(Template(
        r"tpl1671008147570.png",
        record_pos=(0.292, 0.936),
        resolution=(1080, 2340)),
        "Ожидаем кнопки уровня для подтверждения загрузки"
    )


def test_exit_popup():
    touch(Template(
        r"tpl1671008217045.png",
        record_pos=(-0.383, 0.942),
        resolution=(1080, 2340))
    )
    touch(Template(
        r"tpl1671008280676.png",
        record_pos=(0.384, 0.966),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1671008301646.png",
        record_pos=(-0.001, -0.013),
        resolution=(1080, 2340)),
        "Ожидаем отображение попапа подтверждения выхода"
    )


def test_exit_popup_close():
    touch(Template(
        r"tpl1671008348027.png",
        record_pos=(0.156, 0.053),
        resolution=(1080, 2340))
    )
    assert_not_exists(Template(
        r"tpl1671008147570.png",
        record_pos=(0.292, 0.936),
        resolution=(1080, 2340)),
        "Ожидаем отсутвие элементов уровня"
    )
    assert_not_exists(Template(
        r"tpl1671007475423.png",
        record_pos=(-0.319, -0.529),
        resolution=(1080, 2340)),
        "Ожидаем отсувие якоря главной"
    )
    assert_not_exists(Template(
        r"tpl1671112981459.png",
        record_pos=(0.001, -0.477),
        resolution=(1080, 2340)),
        "Ожидаем отсутвие якоря листа артов")


def test_exit_popup_accept():
    touch(Template(
        r"tpl1671008280676.png",
        record_pos=(0.384, 0.966),
        resolution=(1080, 2340))
    )
    touch(Template(
        r"tpl1671008499695.png",
        record_pos=(-0.131, 0.048),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1671008576921.png",
        record_pos=(-0.381, 0.967),
        resolution=(1080, 2340)),
        "Ожидаем кнопку выхода из списка"
    )


def test_to_main_from_art_list():
    touch(Template(
        r"tpl1671008576921.png",
        record_pos=(-0.381, 0.967),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1671007475423.png",
        record_pos=(-0.319, -0.529),
        resolution=(1080, 2340)),
        "Ожидаем отображение пака"
    )


def run_puzzle_tab_feature():
    remove_log_dir('puzzle_tab_feature')
    auto_setup(
        __file__,
        logdir=AUTO_SETUP_ARG.get('logdir'),
        devices=[AUTO_SETUP_ARG.get('devices'), ],
        project_root=AUTO_SETUP_ARG.get('project_root'),
    )
    start_app("com.jollyco.jbpuzzleadventure")
    run_logger(test_open_free_pack)
    run_logger(test_open_art)
    run_logger(test_rotation_button_on)
    run_logger(test_rotation_button_off)
    run_logger(test_swipe_count_element_to_16)
    run_logger(test_start_art_puzzle)
    run_logger(test_exit_popup)
    run_logger(test_exit_popup_close)
    run_logger(test_exit_popup_accept)
    run_logger(test_to_main_from_art_list)
    stop_app("com.jollyco.jbpuzzleadventure")
    simple_report(__file__, logpath=True, output='html_report/puzzle_tab.html')