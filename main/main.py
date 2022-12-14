__author__ = "QA PG"

from airtest.report.report import simple_report

import market_main
import setting_main
import daily_main
import puzzle_tab_main
from try_test_method import remove_txt_result_file


if __name__ == "__main__":
    remove_txt_result_file()
    market_main.run_market_feature()
    setting_main.run_setting_feature()
    daily_main.run_daily_feature()
    puzzle_tab_main.run_puzzle_tab_feature()
