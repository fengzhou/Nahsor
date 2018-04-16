# -*- coding:utf-8 -*-
import pytest


hjson = {
    "name":"name",
    "POST":"POST"
}

def pytest_collect_file():
    for key, value in hjson:
        assert key == value

    