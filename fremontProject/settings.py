# Scrapy settings for fremontproject project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'fremontProject'

SPIDER_MODULES = ['fremontProject.spiders']
NEWSPIDER_MODULE = 'fremontProject.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fremontproject (+http://www.yourdomain.com)'

# FOR TESTING CACHE HTTP
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0 # Set to 0 to never expire
