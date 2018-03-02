import scrapy
from job.items import JobItem


class JobSpider(scrapy.Spider):
    name='jobspider'
    start_urls=['http://nc.58.com/job/?param7503=1&from=yjz2_zhaopin&PGTID=0d202408-0029-dc1e-83ae-42677992cbaa&ClickID=1']
    #爬取导航页的链接
    def parse(self,response):
        #爬取链接
        urls=response.xpath('//*[@id="jingzhun"]/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_page)
    #爬取详细信息
    def parse_page(self,response):
        item=JobItem()
        profession = response.xpath('/html/body/div[3]/div[3]/div[1]/span/text()').extract()
        description=response.xpath('/html/body/div[3]/div[3]/div[2]/div[1]/div[1]/div[1]/text()').extract()
        requirement=response.xpath('/html/body/div[3]/div[3]/div[1]/div[4]/text()').extract()
        companyName=response.xpath('/html/body/div[3]/div[4]/div[1]/div/div[1]/div[1]/a/text()').extract()
        companyDescription=response.xpath('/html/body/div[3]/div[3]/div[2]/div[2]/div[1]/div/div/div/p/text()').extract()
        scale=response.xpath('/html/body/div[3]/div[4]/div[1]/div/p[2]/text()').extract()
        companyCategory=response.xpath('/html/body/div[3]/div[4]/div[1]/div/p[1]/a/text()').extract()
        item['profession']=profession
        item['description']=description
        item['requirement']=requirement
        item['companyName']=companyName
        item['companyDescription']=companyDescription
        item['scale']=scale
        item['companyCategory']=companyCategory
        yield item

