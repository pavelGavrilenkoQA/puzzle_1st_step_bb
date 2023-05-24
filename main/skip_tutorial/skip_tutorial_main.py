__author__ = "TS"

from general_steps_tasia import *


def reload_app():
    stop_app("com.jollyco.jbpuzzleadventure")
    clear_app("com.jollyco.jbpuzzleadventure")
    start_app("com.jollyco.jbpuzzleadventure")


def skip_tutor():
    touch_button_tap()
    assert_pass()
    touch_button_back_popup()


def accept_privacy():
    touch_button_ok()


def puzzle_completed():
    assert_text_puzzle_completed()
    assert_exists_tutorial_image()
    assert_button_ok()
    touch_button_ok()


def pass_first_part():
    sleep(8.0)


def pass_next_part():
    sleep(6.0)
    touch_button_win()


def run_skip_tutorial():
    remove_log_dir('skip_tutorial')
    auto_setup(
        __file__,
        logdir=AUTO_SETUP_ARG.get('logdir'),
        devices=[AUTO_SETUP_ARG.get('devices'), ],
        project_root=AUTO_SETUP_ARG.get('project_root'),
    )
    run_logger(reload_app)
    run_logger(accept_privacy)
    run_logger(skip_tutor)
    run_logger(reload_app)
    run_logger(accept_privacy)
    run_logger(pass_first_part)
    run_logger(puzzle_completed)
    run_logger(skip_tutor)
    run_logger(reload_app)
    run_logger(accept_privacy)
    run_logger(pass_first_part)
    run_logger(puzzle_completed)
    run_logger(pass_next_part)
    run_logger(puzzle_completed)
    run_logger(skip_tutor)
    run_logger(reload_app)
    run_logger(accept_privacy)
    run_logger(pass_first_part)
    run_logger(puzzle_completed)
    run_logger(pass_next_part)
    run_logger(puzzle_completed)
    run_logger(pass_next_part)
    run_logger(puzzle_completed)
    run_logger(skip_tutor)
    stop_app("com.jollyco.jbpuzzleadventure")
    simple_report(__file__, logpath=True, output='html_report/skip_tutorial.html')