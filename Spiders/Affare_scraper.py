import scrapy
import re

from Model.RealestateScraperItem import RealestateScraperItem


class Affare_scraper(scrapy.Spider):
    name = 'quote'
    start_urls = ['https://www.affare.tn/petites-annonces/tunisie/vente-appartement',
                  'https://www.affare.tn/petites-annonces/tunisie/vente-maison',
                  'https://www.affare.tn/petites-annonces/tunisie/terrain'
                  ]

    for i in range(1, 250):
        start_urls.append('https://www.affare.tn/petites-annonces/tunisie/vente-appartement?o=' + str(i))

    for i in range(1, 363):
        start_urls.append('https://www.affare.tn/petites-annonces/tunisie/vente-maison?o=' + str(i))

    for i in range(1, 376):
        start_urls.append('https://www.affare.tn/petites-annonces/tunisie/terrain?o=' + str(i))
    quotation_mark_pattern = re.compile(r'“|”')

    def parse(self, response):
        list = response.css("div.col-xs-12.col-sm-8 div div:nth-child(3) div.AnnoncesList_product_x__BzrCL   ")
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






            item['description'] = resource.css("a div:nth-child(2) div::text").get()
            item['price'] = resource.css("span.AnnoncesList_price__J_vIo::text").get()
            item['adresse'] = resource.css("div.AnnoncesList_section7877o__bOPTn div:nth-child(3) p::text").get()
            item['nbpiece'] = resource.css("div.AnnoncesList_section7877o__bOPTn div:nth-child(3) p:nth-child(2) span::text").get()
            item['superficie_habitable'] = resource.css("div.AnnoncesList_section7877o__bOPTn div:nth-child(3) p:nth-child(2) span:nth-child(2)::text").get()
            item['dateAnnonce'] = resource.css("div.AnnoncesList_section7877o__bOPTn div:nth-child(3) p:nth-child(3)::text").get()
            item['link'] = resource.css("a::attr(href)").get()


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
        next_page = response.css("ul.pagination-lg.pagination li:last-child a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
