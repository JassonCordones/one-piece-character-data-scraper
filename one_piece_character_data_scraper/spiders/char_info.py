import scrapy
import string


class OnepieceSpider(scrapy.Spider):
    name = 'char_info'
    allowed_domains = ['onepiece.fandom.com']

    def start_requests(self):
        urls = ['https://onepiece.fandom.com/wiki/List_of_Canon_Characters']
        for url in urls:
            yield scrapy.Request(url, self.extract_links)

    def extract_links(self, response):
        characters = response.xpath(
            "//h2[1]//following::table[position()<3]//tbody/tr/td[2]/a/@href").getall()
        for character in characters:
            yield response.follow(character, callback=self.extract_info)

    def extract_info(self, response):
        character = response.xpath(
            "//aside/*[contains(@class,'pi-item pi-item-spacing pi-title')]/text()").get()
        sections = response.xpath(
            "//aside/*[contains(@class, 'pi-item pi-group')]")
        section_data = {}
        for section in sections:
            section_name = section.xpath("descendant::h2/text()").get()
            data_items = section.xpath("descendant::div[contains(@class, 'pi-item pi-data')]")
            data_labels = []
            data_values = []
            for item in data_items:
                data_labels.append(item.xpath("descendant::*[contains(@class, 'pi-data-label')]/text()").get())
                data_values.append(item.xpath("descendant::*[contains(@class, 'pi-data-value')]//text()").getall())
            section_items = dict(zip([label.translate(str.maketrans('', '', string.punctuation)) for label in data_labels], [''.join(value) for value in data_values]))  
            section_data[section_name] = section_items
        yield {character: section_data}
