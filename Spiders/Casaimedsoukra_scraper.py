import scrapy

from Model.RealestateScraperItem import RealestateScraperItem


class Spider(scrapy.Spider):
    name = 'quote'
    start_urls = ['https://casaimedsoukra.com/vente/appartement',
                  'https://casaimedsoukra.com/vente/villa',
                  'https://casaimedsoukra.com/vente/terrain',
                  'https://casaimedsoukra.com/vente/commerciale',
                  'https://casaimedsoukra.com/vente/bureau'
                  ]

    def parse(self, response):
        list = response.css('div.col-xs-12.col.isoCol.sale')
        for resource in list:
            item = RealestateScraperItem()
            item['link'] = resource.css('h2.fontNeuron.text-capitalize a::attr(href)').get()
            item['title'] = resource.css('h2.fontNeuron.text-capitalize a::text').get()
            item['adresse'] = resource.css("p.couper-mot::text").get()
            item['price'] = resource.css("span.textSecondary::text").get()
            item['reference'] = resource.css("span.btn.btnSmall.btn-info.text-capitalize::text").get()

            if resource.css(
                    "footer.postColumnFoot  ul.list-unstyled li:nth-child(2) strong:nth-child(2)::text").get() is not None:
                item['nbpiece'] = resource.css(
                    "footer.postColumnFoot  ul.list-unstyled li:nth-child(2) strong:nth-child(2)::text").get()
            else:
                item['nbpiece'] = None

            if resource.css(
                    "footer.postColumnFoot  ul.list-unstyled li:nth-child(1) strong:nth-child(2)::text").get() is not None:
                item['superficie_habitable'] = resource.css(
                    "footer.postColumnFoot  ul.list-unstyled li:nth-child(1) strong:nth-child(2)::text").get()
            else:
                item['superficie_habitable'] = None

            if resource.css("div.imgHolder::attr(style)").get() is not None:
                item['thumbnail_url'] = resource.css("div.imgHolder::attr(style)").get()
            else:
                item['thumbnail_url'] = None

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

            self.quotes_list.append({
                "link": item['link'],
                "title": item['title'],
                "adresse": item['adresse'],
                "price": item['price'],
                "salle_de_salle_de_bain": item['salle_de_bain'],
                "nbpiece": item['nbpiece'],
                "typeImm": item['typeImm'],
                "agence": item['agence'],
                "garage": item['garage'],
                "constructible": item['constructible'],
                "fonds": item['fonds'],
                "installations_sportives": item['installations_sportives'],
                "climatisation": item['climatisation'],
                "chauffage": item['chauffage'],
                "plein_air": item['plein_air'],
                "service": item['service'],
                "dateAnnonce": item['dateAnnonce'],
                "thumbnail_url": item['thumbnail_url'],
                "thumbnail_name": item['thumbnail_name'],
                "reference": item['reference'],
                "localite": item['localite'],
                "delegation": item['delegation'],
                "gouvernorat": item['gouvernorat'],
                "nbpiece_superficie_habitable": item['nbpiece_superficie_habitable'],
                "description": item['description'],
                "superficie_habitable": item['superficie_habitable']
            })
        next_page = response.css("li.next.page-numbers a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
