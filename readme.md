scrapy startproject namescraper
scrapy genspider namespider name.com
open chell
scrapy shell
fetch('https://www.chocolate.co.uk/collections/all')
response.css('product-item')

And then edit your scrapy.cfg file like so:
## scrapy.cfg
[settings]
default = chocolatescraper.settings
shell = ipython

response.css('product-item').get()

products = response.css('product-item')

product = products[0]

text inside a tag with class product-item-meta__title
product.css('a.product-item-meta__title::text').get()

remove unwanted text 
product.css('span.price').get().replace('<span class="price">\n              <span class="visually-hidden">Sale price</span>','').replace('</span>','')


to get an attribute such as an href

product.css('div.product-item-meta a').attrib['href']

"name" : product.css('a.product-item-meta__title::text').get()
"price" : product.css('span.price').get().replace('<span class="price">\n              <span class="visually-hidden">Sale price</span>','').replace('</span>','').remove("£", "")
"url" : product.css('div.product-item-meta a').attrib['href']

save as json or csv
scrapy crawl chocolatespider -O choco.json