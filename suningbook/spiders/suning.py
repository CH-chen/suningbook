# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy

class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        # li_list = response.xpath("//div[@class='menu-list']//div[@class='submenu-left']/ul/li")
        # #//div[@class="menu-list"]/div[14]//div[@class="submenu-left"]/p/a/text()
        # for li in li_list:
        #     item = {}
        #     item["title_1"] = li.xpath("./a/text()").extract_first()
        #     item["href_1"] = li.xpath("./a/@href").extract_first()
        #     print(item)
        #     yield item
        # menu_list = response.xpath("//div[@class='menu-list']/div[@class='menu-sub']")
        # for menu_sub in menu_list:
        #     item = {}
        #     item["title_1"] = menu_sub.xpath("./div/p/a/text()").extract()
        #     item["href_1"] = menu_sub.xpath("./div/p/a/@href").extract()
        #
        #     item["title_2"] = menu_sub.xpath("./div/ul/li/a/text()").extract()
        #     item["href_2"] = menu_sub.xpath("./div/ul/li/a/@href").extract()
        #
        #
        #     print(item)
        #     yield item

        # menu_list = response.xpath("//div[@class='menu-list']/div[@class='menu-sub']")
        #
        # for menu in menu_list:
        #     item = {}
        #     p_list = menu.xpath("./div[1]/p")
        #     ul_list = menu.xpath("./div/ul")
        #     for p in p_list:
        #
        #         item["title_1"] = p.xpath("./a/text()").extract()
        #         item["href_1"] = p.xpath("./a/@href").extract()
        #         # print(item)
        #
        #     for ul in ul_list:
        #
        #         li_list = ul.xpath("./li")
        #         for li in li_list:
        #
        #             item["title_2"] = li.xpath("./a/text()").extract_first()
        #             item["href_2"] = li.xpath("./a/@href").extract_first()
        #
        #             print(item)
        #             yield item
        menu_list = response.xpath("//div[@class='menu-list']/div[@class='menu-sub']")
        print("========")
        for menu in menu_list:
            item = {}
            div_list = menu.xpath("./div")
            for div_lr in div_list:
                p_list = div_lr.xpath("./p")
                ul_list = div_lr.xpath("./ul")
    #<div><p>小说</p><ul><li></li><li></li></ul><p>青春文学</p><ul><li></li><li></li></ul><p>艺术</p><ul><li></li><li></li></ul></div>
    #由于p标签和ul是同级的，但p标签是大分类，所以要让li下的a附属于大分类，就要同时循环，用zip
                for p,ul in zip(p_list,ul_list):
                    item["title_1"] = p.xpath("./a/text()").extract()
                    item["href_1"] = p.xpath("./a/@href").extract()

                    li_list = ul.xpath("./li")
                    for li in li_list:
                        #https://list.suning.com/1-502688-0.html
                        #https://list.suning.com/1-502688-0-0-0-0-0-14-0-4.html
                        # item["url"] = response.xpath("")
                        item["title_2"] = li.xpath("./a/text()").extract_first()

                        item["href_2"] = li.xpath("./a/@href").extract_first()
                        item["href_2"] = item["href_2"].rsplit('.',1)[0]+"-0-0-0-0-14-0-4.html"

                        # print(item)
                        # yield item
                        yield scrapy.Request(
                            item["href_2"], #列表页
                            callback = self.parse_list,
                            meta = {"item":deepcopy(item)}
                        )

                        # https://list.suning.com/emall/showProductList.do?ci=502679&pg=03&cp=0&il=0&iy=-1&adNumber=0&n=1&ch=4&prune=0&sesab=ACBAAB&id=IDENTIFYING&cc=010&paging=1&sub=0
                        # next_part_url = 'https://list.suning.com/emall/showProductList.do?ci={}&pg=03&cp={}&il=0&iy=-1&adNumber=0&n=1&ch=4&prune=0&sesab=ACBAAB&id=IDENTIFYING&cc=010&paging=1&sub=0'
                        # ci = item["href_2"].split("-")[1]
                        # cp = item["href_2"].split("-")[2]
                        # cp = cp.split(".")[0]
                        # next_part_url = next_part_url.format(ci, cp)
                        # # item["href_3"] =next_part_url
                        # yield scrapy.Request(
                        #     next_part_url,
                        #     callback=self.parse_list,
                        #     meta={"item": deepcopy(item)}
                        # )




    def parse_list(self,response):
        print(response.request.url)
        # print(response.meta)
        item = deepcopy(response.meta["item"])

        # li_list1 = response.xpath("//div[@id='filter-results']/ul/li")
        li_list1 = response.xpath("//li[@name='']")

        for li in li_list1:
            item["book_name"] = li.xpath(".//p[@class='sell-point']/a/text()").extract_first()
            # item["book_href"] = li.xpath(".//div[@class='res-info']/p[2]/a/@href").extract_first()
            # item["book_price"] = li.xpath(".//div[@class='res-info']/p[1]/em/text()").extract_first()
            # item["shop_name"] = li.xpath(".//div[@class='res-info']/p[4]/@salesname").extract_first()
            # item["shop_price"] = li.xpath(".//div[@class='res-info']/p[4]/a/@href").extract_first()
            # print(item)
            yield item
            # item1 = deepcopy(item)
            # print(item1)

        page_count = response.xpath("//a[@id='nextPage']/preceding-sibling::*[1]/text()").extract_first()
        if page_count:
            # current_page_num = int(response.xpath("//a[@class='cur']/text()").extract_first())
            current_page = response.xpath("//link[@rel='canonical']/@href").extract_first()
            current_page_num = int(current_page.split('-')[2])
            # url = 'https://list.suning.com/1-502687-1-0-0-0-0-14-0-4.html'
            # next = response.xpath('//a[@id="nextPage"]/@href').extract_first()
            url_num = item["href_2"].rsplit('-')[1]
            if current_page_num < int(page_count):
                next_url = 'https://list.suning.com/1-{}-{}-0-0-0-0-14-0-4.html'.format(url_num,current_page_num + 1)

                yield scrapy.Request(
                    next_url,
                    callback=self.parse_list,
                    meta={"item": response.meta["item"]}
                )
