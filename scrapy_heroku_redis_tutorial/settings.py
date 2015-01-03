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

# Store scraped item in redis for post-processing.
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 999,
}

# Specify the host and port to use when connecting to Redis (optional).
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# Specify the full Redis URL for connecting (optional).
# If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
# REDIS_URL = 'redis://user:pass@hostname:9001'
