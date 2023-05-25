__author__ = "QA PG"


from try_test_method import remove_txt_result_file
from skip_tutorial import skip_tutorial_main
from shop_new import shop
from daily import daily_main
from tutorial_new import tutorial_new_main
from setting_new_feature import setting_new
from puzzle_tab_new import puzzle_tab_new_main
from elements_new import elements_new_main
from popup import popup_main


if __name__ == "__main__":
    remove_txt_result_file()
    tutorial_new_main.run_tutorial_new()
    daily_main.run_daily()
    shop.run_shop_new()
    setting_new.run_setting_new()
    puzzle_tab_new_main.run_puzzle_tab_new()
    elements_new_main.run_elements_in_art_new()
    skip_tutorial_main.run_skip_tutorial()
    popup_main.run_popup()

