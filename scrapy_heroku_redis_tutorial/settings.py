# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_heroku_redis_tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_heroku_redis_tutorial'

SPIDER_MODULES = ['scrapy_heroku_redis_tutorial.spiders']
NEWSPIDER_MODULE = 'scrapy_heroku_redis_tutorial.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_heroku_redis_tutorial (+http://www.yourdomain.com)'

# Store scraped item in redis for post-processing.
ITEM_PIPELINES = [
    'scrapy_redis.pipelines.RedisPipeline',
]

# Specify the full Redis URL for connecting
REDIS_URL = 'redis://user:pass@hostname:9001'