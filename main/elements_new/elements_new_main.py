__author__ = "QA SASHA"

from general_steps import *
from tutorial_main import run_tutorial_feature
from airtest.core.api import *
from airtest.report.report import simple_report
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir
from general_steps import skip_system_pop


def test_play_puzzle_9_elements():
    touch_travelling_pack()
    another_puzzle_in_progress()
    touch_button_yes()
    touch_button_win()
    touch_button_claim()
    assert_exists_completed_pack_with_1_art()
    touch_completed_pack_with_1_art()


def test_play_puzzle_16_elements():
    assert_exists_completed_9_elements()
    touch_elements_16_2()
    touch_button_start()
    touch_button_win()
    touch_button_claim()
    touch_completed_pack_with_1_art()
    assert_exists_completed_9_elements()
    touch_next_element()


def test_play_puzzle_25_elements():
    touch_puzzle_25_elements()
    touch_button_start()
    touch_button_win()
    touch_button_claim()
    touch_completed_pack_with_1_art()
    touch_next_element()
    assert_completed_25_level()
    touch_next_element()


def test_play_puzzle_49_elements():
    touch_elements_49()
    touch_button_start()
    touch_button_win()
    touch_button_claim()
    touch_completed_pack_with_1_art()
    touch_next_element()
    touch_next_element()
    touch_next_element()
    assert_completed_49_elements()
    touch_next_element()


def test_play_puzzle_64_elements():
    assert_64_elements()
    touch_button_start()
    touch_button_win()
    touch_button_claim()
    touch_completed_pack_with_1_art()
    touch_next_element()
    touch_next_element()
    touch_next_element()
    touch_next_element()
    assert_completed_64_element()
    touch_next_element()


def test_play_puzzle_81_elements():
    assert_elements_81()
    touch_button_start()
    touch_button_win()
    touch_button_claim()
    touch_completed_pack_with_1_art()
    touch_next_element()
    touch_next_element()
    touch_next_element()
    touch_next_element()
    completed_81_element()
    touch_next_element()
    touch_next_element()


def test_play_puzzle_144_elements():
    assert_elements_144()
    touch_button_start()
    touch_button_win()
    touch_button_claim()
    touch_completed_pack_with_1_art()
    touch_next_element()
    touch_next_element()
    touch_next_element()
    touch_next_element()
    touch_next_element()
    touch_next_element()
    completed_144_element()


def test_play_puzzle_256_elements():
    assert_elements_256()
    touch_elements_256()
    touch_button_start()
    touch_button_win()
    touch_button_claim()
    touch_completed_pack_with_1_art()
    touch_next_element()
    touch_next_element()
    touch_next_element()
    touch_next_element()
    touch_next_element()
    touch_next_element()
    completed_element_256()


def run_elements_in_art_new():
    remove_log_dir('elements_new')
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
    simple_report(__file__, logpath=True, output='html_report/elements_new.html')

