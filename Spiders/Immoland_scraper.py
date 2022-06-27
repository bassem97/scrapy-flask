import re

import scrapy

from Model.RealestateScraperItem import RealestateScraperItem


class Immoland_scraper(scrapy.Spider):
    name = 'quote'
    start_urls = [
        'https://www.immoland.tn/advanced-search/?lat=&lng=&use_radius=on&radius=2&status=a-vendre&type=&bedrooms=&bathrooms=&min-price=&max-price=', ]
    quotation_mark_pattern = re.compile(r'“|”')

    def parse(self, response):
        list = response.css('div.item-listing-wrap')

        for resource in list:
            item = RealestateScraperItem()

            item['typeImm'] = None
            item['gouvernorat'] = None
            item['delegation'] = None
            item['localite'] = None
            item['nbpiece_superficie_habitable'] = None
            item['agence'] = None
            item['tel'] = None
            item['constructible'] = None
            item['fonds'] = None
            item['installations_sportives'] = None
            item['climatisation'] = None
            item['chauffage'] = None
            item['plein_air'] = None
            item['service'] = None
            item['codeP'] = None
            item['salle_de_bain'] = None
            item['description'] = None
            item['dateAnnonce'] = None
            item['garage'] = None
            item['reference'] = None
            item['thumbnail_url'] = None
            item['thumbnail_name'] = None
            item['link'] = None
            item['title'] = None
            item['superficie_habitable'] = None
            item['superficie_terrain'] = None
            item['nbpiece'] = None
            item['adresse'] = None
            item['cuisine'] = None
            item['price'] = None
            item['anneeConst'] = None

            item['link'] = resource.css('h2.item-title a::attr(href)').get()
            item['title'] = resource.css('h2.item-title a::text').get()
            item['adresse'] = resource.css("address::text").get()
            item['price'] = resource.css("li.item-price::text").get()
            item['salle_de_bain'] = resource.css("li.h-baths span:nth-child(3)::text").get()
            item['nbpiece'] = resource.css("li.h-beds span:nth-child(3)::text").get()
            item['typeImm'] = resource.css("li.h-type span::text").get()
            item['agence'] = resource.css("div.item-author a::text").get()

            if resource.css("li.h-area span:nth-child(2)::text").get() is not None:
                item['superficie_habitable'] = resource.css("li.h-area span:nth-child(2)::text").get()

            if resource.css("img.img-fluid.wp-post-image::attr(src)").get() is not None:
                item['thumbnail_url'] = resource.css("img.img-fluid.wp-post-image::attr(src)").get()

            self.quotes_list.append({
                 'typeImm': item['typeImm'],
            'gouvernorat': item['gouvernorat'],
            'delegation': item['delegation'],
            'localite': item['localite'],
            'nbpiece_superficie_habitable': item['nbpiece_superficie_habitable'],
            'agence': item['agence'],
            'tel': item['tel'],
            'constructible': item['constructible'],
            'fonds': item['fonds'],
            'installations_sportives': item['installations_sportives'],
            'climatisation': item['climatisation'],
            'chauffage': item['chauffage'],
            'plein_air': item['plein_air'],
            'service': item['service'],
            'codeP': item['codeP'],
            'salle_de_bain': item['salle_de_bain'],
            'description': item['description'],
            'dateAnnonce': item['dateAnnonce'],
            'garage': item['garage'],
            'reference': item['reference'],
            'thumbnail_url': item['thumbnail_url'],
            'thumbnail_name': item['thumbnail_name'],
            'link': item['link'],
            'title': item['title'],
            'superficie_habitable': item['superficie_habitable'],
            'superficie_terrain': item['superficie_terrain'],
            'nbpiece': item['nbpiece'],
            'adresse': item['adresse'],
            'cuisine': item['cuisine'],
            'price': item['price'],
            'anneeConst': item['anneeConst']
            })
        next_page = response.css("ul.pagination.justify-content-center li:nth-last-child(2) a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
