# EP realizado por Arilson Francelino de Jesus da Silva e Vitoria Caroline Damacena Silva Reis

import scrapy


class PokemonSpider(scrapy.Spider):
    name = 'pokemon'
    start_urls = ['https://pokemondb.net/pokedex/all']

    def parse(self, response):
        table = response.css('#pokedex')

        for row in table.css('tr')[1:]:
            num = row.css('td:nth-child(1)::text').get()

            pokemon_url = response.urljoin(
                row.css('td:nth-child(2) a::attr(href)').get())

            name = row.css('td:nth-child(2) a::text').get()

            evolution = row.css('td:nth-child(3) a')

            if evolution:
                evolution_num = evolution.css('::text').get()
                evolution_name = evolution.css('::attr(title)').get()
                evolution_url = response.urljoin(
                    evolution.css('::attr(href)').get())
            else:
                evolution_num = None
                evolution_name = None
                evolution_url = None

            height = row.css('td:nth-child(4)::text').get()

            weight = row.css('td:nth-child(5)::text').get()

            types = row.css('td:nth-child(6) a::text').getall()

            if name:
                yield {
                    'num': num,
                    'pokemon_url': pokemon_url,
                    'name': name,
                    'evolution_num': evolution_num,
                    'evolution_name': evolution_name,
                    'evolution_url': evolution_url,
                    'height': height,
                    'weight': weight,
                    'types': types
                }
