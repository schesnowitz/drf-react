# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ChocolatescraperPipeline:
    def process_item(self, item, spider):
        return item


class PriceToUSDPipeline:
    pound_to_dollar_rate = 1.3

    def process_item(self, item, spider):
        adaper = ItemAdapter(item)

        if adaper.get("price"):
            float_price = float(adaper['price'])

            adaper['price'] = float_price * self.pound_to_dollar_rate

            return item
        else:
            raise DropItem(f"price not found in {item}")

class DuplicatesPipeline:

    def __init__(self):
        self.names_seen = set()


    def process_item(self, item, spider):
        adapter = ItemAdapter(item)         

        if adapter['name'] in self.names_seen:
                        raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.names_seen.add(adapter['name'])
            return item
        

import psycopg2

class SavingToPostgresPipeline(object):

    def __init__(self):
        self.create_connection()


    def create_connection(self):
        self.conn = psycopg2.connect(
            # DATABASE_URL = "postgresql://postgres:YbBYHfK4So4dojs7nylI@containers-us-west-181.railway.app:5561/railway",
            dbname="railway",
            host="containers-us-west-181.railway.app",
            password="YbBYHfK4So4dojs7nylI",
            port="5561",
            user="postgres"
            )

        self.cure = self.conn.cursor()


    def process_item(self, item, spider):
        self.store_db(item)
        #we need to return the item below as scrapy expects us to!
        return item

    def store_in_db(self, item):
        self.curr.execute(""" insert into chocolate_products values (%s,%s,%s)""", (
            item["title"][0],
            item["price"][0],
            item["url"][0]
        ))
        self.conn.commit()

