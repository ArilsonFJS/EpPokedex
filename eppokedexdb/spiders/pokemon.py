# EP realizado por Arilson Francelino de Jesus da Silva e Vitoria Caroline Damacena Silva Reis

import scrapy


class PokemonSpider(scrapy.Spider):
    name = 'pokemon'
    start_urls = ['https://pokemondb.net/pokedex/all']

    def parse(self, response):
        # Encontre a tabela que contém os nomes dos Pokémon
        table = response.css('#pokedex')

        # Iterar pelas linhas da tabela (exceto o cabeçalho)
        for row in table.css('tr')[1:]:
            # Extrair o número do Pokémon da primeira coluna
            num = row.css('td:nth-child(1)::text').get()

            # Extrair a URL da página do Pokémon
            pokemon_url = response.urljoin(
                row.css('td:nth-child(2) a::attr(href)').get())

            # Extrair o nome do Pokémon da segunda coluna
            name = row.css('td:nth-child(2) a::text').get()

            # Extrair as próximas evoluções do Pokémon (PokéNum, nome e URL)
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

            # Extrair o tamanho do Pokémon
            height = row.css('td:nth-child(4)::text').get()

            # Extrair o peso do Pokémon
            weight = row.css('td:nth-child(5)::text').get()

            # Extrair os tipos do Pokémon
            types = row.css('td:nth-child(6) a::text').getall()

            # Se o nome não estiver vazio, retornar todas as informações como um item JSON
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
