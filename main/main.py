__author__ = "QA PG"


from try_test_method import remove_txt_result_file
from skip_tutorial_feature import skip_tutorial_main
from shop_feature import shop_main
from daily_feature import daily_main
from tutorial_feature import tutorial_main
from setting_feature import setting_main
from puzzle_tab_feature import puzzle_tab_main
from elements_feature import elements_main
from popup_feature import popup_main


if __name__ == "__main__":
    remove_txt_result_file()
    tutorial_main.run_tutorial_new()
    daily_main.run_daily()
    shop_main.run_shop_new()
    setting_main.run_setting_new()
    puzzle_tab_main.run_puzzle_tab_new()
    elements_main.run_elements_in_art_new()
    skip_tutorial_main.run_skip_tutorial()
    popup_main.run_popup()

