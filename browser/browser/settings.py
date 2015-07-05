# -*- coding: utf-8 -*-

# Scrapy settings for browser project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'browser'

SPIDER_MODULES = ['browser.spiders']
NEWSPIDER_MODULE = 'browser.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'browser (+http://www.yourdomain.com)'

USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0'


