# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealestateScraperItem(scrapy.Item):
    #default_input_processor = MapCompose(unicode.strip)
    # define the fields for your item here like:
    typeImm=scrapy.Field()#
    gouvernorat=scrapy.Field()
    delegation=scrapy.Field()
    localite=scrapy.Field()
    nbpiece_superficie_habitable = scrapy.Field()
    agence=scrapy.Field()
    tel=scrapy.Field()
    constructible=scrapy.Field()#
    fonds=scrapy.Field()#
    installations_sportives=scrapy.Field()
    climatisation=scrapy.Field()
    chauffage=scrapy.Field()
    plein_air=scrapy.Field()
    service=scrapy.Field()
    codeP=scrapy.Field()
    salle_de_bain=scrapy.Field()
    description=scrapy.Field()
    dateAnnonce=scrapy.Field()
    garage=scrapy.Field()
    reference=scrapy.Field()
    thumbnail_url=scrapy.Field()
    thumbnail_name=scrapy.Field()
    link=scrapy.Field()
    title=scrapy.Field()
    superficie_habitable=scrapy.Field()
    superficie_terrain=scrapy.Field()#
    nbpiece=scrapy.Field()
    adresse=scrapy.Field()
    cuisine=scrapy.Field()
    price=scrapy.Field()
    anneeConst=scrapy.Field()#




    
