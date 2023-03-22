__author__ = "QA SASHA"

from general_steps import touch_button_ok, assert_exists_tutorial_image, assert_exist_empty_elements_list, \
    touch_button_win, assert_exists_empty_field, asserts_exists_completed_art_tutorial, touch_button_back, \
    touch_button_settings, english_language, touch_travelling_pack
from tutorial_main import run_tutorial_feature


def tutorial_new():
    touch_button_ok()
    assert_exists_tutorial_image()
    touch_button_ok()
    assert_exist_empty_elements_list()
    touch_button_win()
    assert_exists_tutorial_image()
    touch_button_ok()
    assert_exists_empty_field()
    touch_button_win()
    assert_exists_tutorial_image()
    touch_button_ok()
    assert_exists_empty_field()
    touch_button_win()
    assert_exists_tutorial_image()
    touch_button_ok()
    asserts_exists_completed_art_tutorial()
    touch_button_back()
    touch_button_back()
    touch_button_settings()
    english_language()
    touch_button_back()
    touch_travelling_pack()
    run_tutorial_feature()







