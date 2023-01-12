__author__ = "QA PG"


from marker_feature import market_main
from setting_feature import setting_main
from daily_feature import daily_main
from puzzle_tab_feature import puzzle_tab_main
from tutorial_feature import tutorial_main
from try_test_method import remove_txt_result_file


if __name__ == "__main__":
    remove_txt_result_file()
    tutorial_main.run_tutorial_feature()
    setting_main.run_setting_feature()
    daily_main.run_daily_feature()
    market_main.run_market_feature()
    puzzle_tab_main.run_puzzle_tab_feature()
