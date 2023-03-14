__author__ = "QA SASHA"

from airtest.core.api import *
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir
from airtest.report.report import simple_report


def test_play_puzzle_9_elements():
    touch(Template(r"tpl1672750540154.png", record_pos=(-0.002, -0.531), resolution=(1080, 2340)))
    touch(Template(r"tpl1672750592447.png", record_pos=(-0.004, -0.469), resolution=(1080, 2340)))
    touch(Template(r"tpl1672751319901.png", record_pos=(-0.008, 0.536), resolution=(1080, 2340)))
    sleep(2)
    if exists(Template(
                  r"tpl1677495070425.png",
                   record_pos=(-0.006, -0.015),
                   resolution=(1080, 2340))
    ):
        touch(Template(
            r"tpl1671009289719.png", record_pos=(-0.131, 0.06), resolution=(1080, 2340))
        )

    sleep(5)
    touch(Template(r"tpl1672750809476.png", record_pos=(-0.314, 1.044), resolution=(1080, 2340)))
    sleep(7)
    touch(Template(
        r"tpl1672750883672.png", record_pos=(0.191, 0.649), resolution=(1080, 2340))
    )

    assert_exists(Template(
        r"tpl1672833517951.png",
        record_pos=(-0.004, -0.719),
        resolution=(1080, 2340))
    )
    touch(Template(

       r"tpl1672751543912.png", record_pos=(-0.008, -0.742), resolution=(1080, 2340))
    )
    sleep(2.0)


def test_play_puzzle_16_elements():
    assert_exists(Template(
        r"tpl1672833542147.png",
        record_pos=(-0.001, 0.181),
        resolution=(1080, 2340)),
     )

    touch(Template(r"tpl1672751671707.png", record_pos=(0.187, 0.184), resolution=(1080, 2340)))
    touch(Template(r"tpl1672751319901.png", record_pos=(-0.008, 0.536), resolution=(1080, 2340)))
    sleep(5)
    touch(Template(r"tpl1672750809476.png", record_pos=(-0.314, 1.044), resolution=(1080, 2340)))
    sleep(7)
    touch(Template(r"tpl1672750883672.png", record_pos=(0.191, 0.649), resolution=(1080, 2340)))

    sleep(2)
    touch(Template(r"tpl1672751543912.png", record_pos=(-0.008, -0.742), resolution=(1080, 2340)))
    sleep(4.0)
    assert_exists(Template(
        r"tpl1672834051788.png",
        record_pos=(0.187, 0.184),
        resolution=(1080, 2340)),
                  )
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))


def test_play_puzzle_25_elements():
    touch(Template(r"tpl1672751826251.png", record_pos=(0.183, 0.185), resolution=(1080, 2340)))
    touch(Template(r"tpl1672751319901.png", record_pos=(-0.008, 0.536), resolution=(1080, 2340)))
    sleep(5)
    touch(Template(r"tpl1672750809476.png", record_pos=(-0.314, 1.044), resolution=(1080, 2340)))
    sleep(7)
    touch(Template(r"tpl1672750883672.png", record_pos=(0.191, 0.649), resolution=(1080, 2340)))

    sleep(2)
    touch(Template(r"tpl1672751543912.png", record_pos=(-0.008, -0.742), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    assert_exists(Template(
        r"tpl1672834083592.png",
        record_pos=(0.189, 0.178),
        resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))


def test_play_puzzle_49_elements():
    touch(Template(r"tpl1672752081030.png", record_pos=(0.18, 0.177), resolution=(1080, 2340)))
    touch(Template(r"tpl1672751319901.png", record_pos=(-0.008, 0.536), resolution=(1080, 2340)))
    sleep(4)
    touch(Template(r"tpl1672750809476.png", record_pos=(-0.314, 1.044), resolution=(1080, 2340)))
    sleep(7)
    touch(Template(r"tpl1672750883672.png", record_pos=(0.191, 0.649), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672751543912.png", record_pos=(-0.008, -0.742), resolution=(1080, 2340)))
    sleep(2.0)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    assert_exists(Template(
        r"tpl1672834114518.png",
        record_pos=(0.187, 0.183),
        resolution=(1080, 2340))
    )
    sleep(2)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))


def test_play_puzzle_64_elements():
    touch(Template(r"tpl1672752175627.png", record_pos=(0.183, 0.188), resolution=(1080, 2340)))
    touch(Template(r"tpl1672751319901.png", record_pos=(-0.008, 0.536), resolution=(1080, 2340)))
    sleep(4)
    touch(Template(r"tpl1672750809476.png", record_pos=(-0.314, 1.044), resolution=(1080, 2340)))
    sleep(7)
    touch(Template(r"tpl1672750883672.png", record_pos=(0.191, 0.649), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672751543912.png", record_pos=(-0.008, -0.742), resolution=(1080, 2340)))
    sleep(2.0)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    assert_exists(Template(
        r"tpl1672834168495.png",
        record_pos=(0.194, 0.183),
        resolution=(1080, 2340)),
                  )
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))


def test_play_puzzle_81_elements():
    touch(Template(r"tpl1672752326117.png", record_pos=(0.177, 0.17), resolution=(1080, 2340)))
    touch(Template(r"tpl1672751319901.png", record_pos=(-0.008, 0.536), resolution=(1080, 2340)))
    sleep(4)
    touch(Template(r"tpl1672750809476.png", record_pos=(-0.314, 1.044), resolution=(1080, 2340)))
    sleep(7)
    touch(Template(r"tpl1672750883672.png", record_pos=(0.191, 0.649), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672751543912.png", record_pos=(-0.008, -0.742), resolution=(1080, 2340)))
    sleep(2.0)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    assert_exists(Template(
        r"tpl1672834194051.png",
        record_pos=(0.189, 0.181),
        resolution=(1080, 2340)),
    )

    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))


def test_play_puzzle_144_elements():
    touch(Template(r"tpl1672752431432.png", record_pos=(0.183, 0.173), resolution=(1080, 2340)))
    touch(Template(r"tpl1672751319901.png", record_pos=(-0.008, 0.536), resolution=(1080, 2340)))
    sleep(4)
    touch(Template(r"tpl1672750809476.png", record_pos=(-0.314, 1.044), resolution=(1080, 2340)))
    sleep(7)
    touch(Template(r"tpl1672750883672.png", record_pos=(0.191, 0.649), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672751543912.png", record_pos=(-0.008, -0.742), resolution=(1080, 2340)))
    sleep(2.0)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    sleep(1)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    sleep(1)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    sleep(1)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    sleep(1)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    assert_exists(Template(
        r"tpl1672834221655.png",
        record_pos=(0.203, 0.185),
        resolution=(1080, 2340)),
        )

    touch(Template(r"tpl1672751799437.png",
    record_pos=(0.343, 0.191),
    resolution=(1080, 2340)))


def test_play_puzzle_256_elements():
    touch(Template(r"tpl1672752533865.png", record_pos=(0.202, 0.184), resolution=(1080, 2340)))
    touch(Template(r"tpl1672751319901.png", record_pos=(-0.008, 0.536), resolution=(1080, 2340)))
    sleep(4)
    touch(Template(r"tpl1672750809476.png", record_pos=(-0.314, 1.044), resolution=(1080, 2340)))
    sleep(7)
    touch(Template(r"tpl1672750883672.png", record_pos=(0.191, 0.649), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1672751543912.png", record_pos=(-0.008, -0.742), resolution=(1080, 2340)))
    sleep(2.0)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    sleep(1)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    sleep(1)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    sleep(1)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    sleep(1)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    sleep(1)
    touch(Template(r"tpl1672751799437.png", record_pos=(0.343, 0.191), resolution=(1080, 2340)))
    assert_exists(Template(r"tpl1672834272858.png", record_pos=(0.197, 0.178), resolution=(1080, 2340)),
                  )


def run_elements_in_art():
    remove_log_dir('elements_in_art')
    auto_setup(
        __file__,
        logdir=AUTO_SETUP_ARG.get('logdir'),
        devices=[AUTO_SETUP_ARG.get('devices'), ],
        project_root=AUTO_SETUP_ARG.get('project_root'),
    )
    start_app("com.jollyco.jbpuzzleadventure")
    run_logger(test_play_puzzle_9_elements)
    run_logger(test_play_puzzle_16_elements)
    run_logger(test_play_puzzle_25_elements)
    run_logger(test_play_puzzle_49_elements)
    run_logger(test_play_puzzle_64_elements)
    run_logger(test_play_puzzle_81_elements)
    run_logger(test_play_puzzle_144_elements)
    run_logger(test_play_puzzle_256_elements)
    stop_app("com.jollyco.jbpuzzleadventure")
    simple_report(__file__, logpath=True, output='html_report/elements.html')
