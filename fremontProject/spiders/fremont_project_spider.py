from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from fremontProject.items import FremontProjectItem

from scrapy import log
from scrapy.http import Request
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
import re

class FremontProjectSpider(BaseSpider):
  base_url = "http://www.thefremontproject.com/rabbithole/"
  name = "fremontProject"
  start_urls = [base_url]

  def __init__(self, category=None, *args, **kwargs):
    super(FremontProjectSpider, self).__init__(*args, **kwargs)
    # initialize globals here
    self.current_page = 1

  def parse(self, response):
    self.current_page += 1
    hxs = HtmlXPathSelector(response)
    items = []
    # See if next link
    nextPage = hxs.select("//a[@id='next-link']/@href").extract()
    if nextPage != []:
      # Extract item
      item = FremontProjectItem()
      item['title'] = hxs.select('//div[contains(concat(" ", normalize-space(@class), " "), " lead-text ")]/p/text()').extract()[0]
      joke = hxs.select('//div[contains(concat(" ", normalize-space(@class), " "), " logo-text ")]/text()').extract()[0]
      item['joke'] = joke.strip()
      items.append(item)
      with open('jokes.txt', 'a') as f:
        f.write('{0}\n{1}\n\n'.format(item['title'], item['joke']))
      # Get next URL
      relative_url = nextPage[0]
      base_url = get_base_url(response)
      final_url = urljoin_rfc(base_url, relative_url)
      items.append(Request(url= final_url, callback= self.parse))
    else:
      print "RESPONSE START"
      print response
      print "RESPONSE END"
    return items

    # hxs.select("//table[@id='productTable']/tbody/tr/td[contains(concat(' ', normalize-space(@class), ' '), ' CLS 1 ')]")[0].extract()
