# -*- coding: utf-8 -*-
__author__ = 'chukai'
__date__ = '2019-04-13 02:02:20'

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


execute(["scrapy", "crawl", "lagou"])