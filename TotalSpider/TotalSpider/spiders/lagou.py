# -*- coding: utf-8 -*-
import os
import pickle
from datetime import datetime

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from TotalSpider.items import LagouJobItem, LagouJobItemLoader
from TotalSpider.settings import BASE_DIR


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.ladou.com']
    start_urls = ['https://www.lagou.com/jobs/list_%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD?labelWords=&fromSearch=true&suginput=']

    rules = (
        # Rule(LinkExtractor(allow=r'zhaopin/.*'), callback='parse_job', follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html$'), callback='parse_job', follow=True),
    )

    @staticmethod
    def parse_job(response):
        # 解析拉勾网的职位
        item_loader = LagouJobItemLoader(item=LagouJobItem(), response=response)
        item_loader.add_css("title", ".job-name::attr(title)")
        item_loader.add_value("url", response.url)
        item_loader.add_css("salary_min", ".job_request .salary::text")
        item_loader.add_xpath("job_city", "//*[@class='job_request']/p/span[2]/text()")
        item_loader.add_xpath("work_years_min", "//*[@class='job_request']/p/span[3]/text()")
        item_loader.add_xpath("degree_need", "//*[@class='job_request']/p/span[4]/text()")
        item_loader.add_xpath("job_type", "//*[@class='job_request']/p/span[5]/text()")
        item_loader.add_css("tags", '.position-label li::text')
        item_loader.add_css("publish_time", ".publish_time::text")
        item_loader.add_css("job_advantage", ".job-advantage p::text")
        item_loader.add_css("job_desc", ".job_bt div")
        item_loader.add_css("job_addr", ".work_addr")
        item_loader.add_css("company_name", "#job_company dt a img::attr(alt)")
        item_loader.add_css("company_url", "#job_company dt a::attr(href)")
        item_loader.add_value("crawl_time", datetime.now())

        job_item = item_loader.load_item()

        return job_item

    def start_requests(self):
        cookies = []
        if os.path.exists(BASE_DIR + "/cookies/lagou.cookies"):
            cookies = pickle.load(open(BASE_DIR + "/cookies/lagou.cookies", "rb"))
        if not cookies:
            from selenium import webdriver
            brower = webdriver.Chrome(executable_path=BASE_DIR + "/chromedriver")
            brower.get("https://passport.lagou.com/login/login.html")
            brower.find_element_by_css_selector(".form_body .input[type='text']").send_keys("850004903@qq.com")
            brower.find_element_by_css_selector(".form_body input[type='password']").send_keys("wen6650286")
            brower.find_element_by_css_selector("div[data-view='passwordLogin'] input.btn_lg").click()
            import time
            time.sleep(10)
            cookies = brower.get_cookies()
            # 写入cookie

            pickle.dump(cookies, open(BASE_DIR + "/cookies/lagou.cookies", "wb"))
        cookie_dict = {}
        for cookie in cookies:
            cookie_dict[cookie["name"]] = cookie["value"]
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True, cookies=cookie_dict)
