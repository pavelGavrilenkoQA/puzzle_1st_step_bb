# -*- encoding=utf8 -*-
__author__ = "QA PG"

from airtest.core.api import *
from airtest.report.report import simple_report
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir
from general_steps import skip_system_pop


def test_politic_accept():
    touch(Template(
        r"tpl1672664808761.png",
        record_pos=(-0.003, 0.328),
        resolution=(1080, 2340))
    )
    sleep(6)
    assert_exists(Template(
        r"tpl1672664849254.png",
        record_pos=(-0.003, -0.211),
        resolution=(1080, 2340)),
        "Ожидаем решенный пазл туториал после принятия политики"
    )


def test_tutorial_part_1():
    touch(Template(
        r"tpl1672664808761.png",
        record_pos=(-0.003, 0.328),
        resolution=(1080, 2340))
    )
    sleep(6)
    assert_exists(Template(
        r"tpl1672664959749.png",
        record_pos=(0.271, 0.71),
        resolution=(1080, 2340)),
        "Ожидаем появления части панели элементов"
    )
    sleep(5)
    touch(Template(
        r"tpl1672665048156.png",
        record_pos=(-0.321, 1.038),
        resolution=(1080, 2340))
    )
    sleep(7)
    assert_exists(Template(
        r"tpl1672664849254.png",
        record_pos=(-0.003, -0.211),
        resolution=(1080, 2340)),
        "Ожидаем решенный пазл туториал после первой части тутора"
    )


def test_tutorial_part_2():
    touch(Template(
        r"tpl1672664808761.png",
        record_pos=(-0.003, 0.328),
        resolution=(1080, 2340))
    )
    sleep(6)
    assert_exists(Template(
        r"tpl1672665146926.png",
        record_pos=(0.224, -0.213),
        resolution=(1080, 2340)),
        "Ожидаем пустое поле и наличие верхней части панели элементов"
    )
    touch(Template(
        r"tpl1672665048156.png",
        record_pos=(-0.321, 1.038),
        resolution=(1080, 2340))
    )
    assert_exists(Template(
        r"tpl1672664849254.png",
        record_pos=(-0.003, -0.211),
        resolution=(1080, 2340)),
        "Ожидаем решенный пазл туториал после второй чатси тутора"
    )


def test_tutorial_part_3():
    touch(Template(
        r"tpl1672664808761.png",
        record_pos=(-0.003, 0.328),
        resolution=(1080, 2340))
    )
    sleep(7)
    assert_exists(Template(
        r"tpl1677494484072.png",
        record_pos=(0.008, -0.206),
        resolution=(1080, 2340)),
        "Отображение завершенного арта туториала"
    )


def test_language_check():
    sleep(2)
    touch(Template(r"tpl1672665432382.png", record_pos=(-0.381, 0.969), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672665432382.png", record_pos=(-0.381, 0.969), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672665460512.png", record_pos=(-0.403, -0.857), resolution=(1080, 2340)))
    ### Проверяем подключеный язык, при необходимости переключаем на английский
    if not exists(Template(r"tpl1672665487700.png", record_pos=(-0.213, -0.015), resolution=(1080, 2340))):
        touch(Template(r"tpl1672665535609.png", record_pos=(0.265, -0.057), resolution=(1080, 2340)))
        touch(Template(r"tpl1672665487700.png", record_pos=(-0.213, -0.015), resolution=(1080, 2340)))
        sleep(2)
        assert_exists(Template(
            r"tpl1672665487700.png",
            record_pos=(-0.213, -0.015),
            resolution=(1080, 2340)),
            "Ожидаем переключение на английский язык"
        )
    ### Выполняем активное действие для сохранения статуса прохождения обучения
    touch(Template(r"tpl1672665432382.png", record_pos=(-0.381, 0.969), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672671623360.png", record_pos=(0.007, -0.537), resolution=(1080, 2340)))
    touch(Template(r"tpl1672671633756.png", record_pos=(-0.003, -0.476), resolution=(1080, 2340)))
    touch(Template(r"tpl1672671642469.png", record_pos=(-0.003, 0.531), resolution=(1080, 2340)))
    sleep(6)


def run_tutorial_feature():
    remove_log_dir('tutorial_feature')
    auto_setup(
        __file__,
        logdir=AUTO_SETUP_ARG.get('logdir'),
        devices=[AUTO_SETUP_ARG.get('devices'), ],
        project_root=AUTO_SETUP_ARG.get('project_root'),
    )
    clear_app("com.jollyco.jbpuzzleadventure")
    start_app("com.jollyco.jbpuzzleadventure")
    run_logger(skip_system_pop)
    run_logger(test_politic_accept)
    run_logger(test_tutorial_part_1)
    run_logger(test_tutorial_part_2)
    run_logger(test_tutorial_part_3)
    run_logger(test_language_check)
    stop_app("com.jollyco.jbpuzzleadventure")
    simple_report(__file__, logpath=True, output='html_report/tutorial.html')

