__author__ = "QA PG"

from airtest.core.api import *
from airtest.report.report import simple_report
from global_auto_agr import AUTO_SETUP_ARG
from try_test_method import run_logger, remove_log_dir


def skip_system_pop():
    sleep(10)
    keyevent("BACK")
    sleep(6)
    keyevent("BACK")
    sleep(6)
    keyevent("BACK")
    sleep(6)
