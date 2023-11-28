def get_population(country_dict):
  population_dict = {
    '2022': country_dict['2022 Population'],
    '2020': country_dict['2020 Population'],
    '2010': country_dict['2010 Population'],
    '2000': country_dict['2000 Population'],
    '1990': country_dict['1990 Population'],
    '1980': country_dict['1980 Population'],
    '1970': country_dict['1970 Population']
  }
  labels = population_dict.key()
  values = population_dict.values()
  return labels, values

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result

