import Scrapy
class JobSpider(Scrapy.Spider):
    name='jobspider'
    start_urls=['http://nc.58.com/job/?param7503=1&from=yjz2_zhaopin&PGTID=0d202408-0029-dc1e-83ae-42677992cbaa&ClickID=1']
    