import re

from TotalSpider.settings import BASE_DIR

files = ["/csv/spider_job_pd_ai_p6.csv", "/csv/spider_job_pd.csv"]
output = "/csv/spider_job_pd_ai_all.csv"
str = [];
for file in files:
    with open(BASE_DIR + file, 'r') as file:
        for line in file.readlines():
            if re.search("ai|智能|机器学习", line):
                with open(BASE_DIR + output, "a", encoding='utf-8') as f:
                    f.write(line)
