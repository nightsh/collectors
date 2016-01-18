# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from datetime import date, timedelta
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from . import utils
from .item import Item


class Spider(CrawlSpider):

    # Public

    name = 'isrctn'
    allowed_domains = ['isrctn.com']
    rules = [
        Rule(LinkExtractor(allow=utils.make_pattern('search'))),
        Rule(LinkExtractor(allow=r'ISRCTN\d+'), callback='parse_item'),
    ]

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Inherit parent
        super(Spider, self).__init__(*args, **kwargs)

        # Defaul values
        if date_from is None:
            date_from = str(date.today() - timedelta(days=1))
        if date_to is None:
            date_to = str(date.today())

        # Make start urls
        self.start_urls = utils.make_start_urls(
                base='http://www.isrctn.com/search',
                date_from=date_from, date_to=date_to)

    def parse_item(self, res):

        # Create item
        item = Item()

        path = '.ComplexTitle_primary::text'
        item['isrctn_id'] = res.css(path).extract_first()

        return item
