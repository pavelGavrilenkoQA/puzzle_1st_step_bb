__author__ = "QA PG"

import tutorial_new.tutorial_new_main
from marker_feature import market_main
from setting_feature import setting_main
from daily_feature import daily_main
from puzzle_tab_feature import puzzle_tab_main
from tutorial_feature import tutorial_main
from elements_in_art import elements_in_art_main
from try_test_method import remove_txt_result_file
from elements_in_art import elements_in_art_main
from tutorial_new import tutorial_new_main
from setting_new_feature import setting_new
from puzzle_tab_new import  puzzle_tab_new_main
from elements_new import elements_new_main

if __name__ == "__main__":
     remove_txt_result_file()
     # tutorial_main.run_tutorial_feature()
     # setting_main.run_setting_feature()
     # daily_main.run_daily_feature()
     # market_main.run_market_feature()
     # puzzle_tab_main.run_puzzle_tab_feature()
     # elements_in_art_main.run_elements_in_art()
     tutorial_new_main.run_tutorial_new()
     setting_new.run_setting_new()
     puzzle_tab_new_main.run_puzzle_tab_new()
     elements_new_main.run_elements_in_art_new()
