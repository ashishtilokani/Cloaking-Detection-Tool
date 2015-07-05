# -*- coding: utf-8 -*-

# Scrapy settings for googleBot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'googleBot'

SPIDER_MODULES = ['googleBot.spiders']
NEWSPIDER_MODULE = 'googleBot.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'googleBot (+http://www.yourdomain.com)'

USER_AGENT = 'Googlebot/2.1 (+http://www.google.com/bot.html)'
