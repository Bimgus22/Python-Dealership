richland_county = {
    "columbia": 136632,
    "forest acres": 10606,
    "blythewood": 6254,
    "eastover": 867,
    "arcadia lakes": 294
}

greenville_county = {
    "greenville": 72649,
    "mauldin": 25748,
    "simpsonville": 23542,
    "taylors": 23746,
    "travelers rest": 7277
}

charleston_county = {
    "charleston": 155369,
    "mount pleasant": 92459,
    "north charleston": 114852,
    "goose creek": 45463,
    "hanahan": 26008
}

lexington_county = {
    "lexington": 23957,
    "west columbia": 17870,
    "cayce": 13817,
    "chapin": 1849,
    "irmo": 12258
}

horry_county = {
    "conway": 25756,
    "myrtle beach": 35328,
    "north myrtle beach": 19330,
    "aynor": 1053,
    "loris": 2697
}

sc_county_list = [
    richland_county,
    greenville_county,
    charleston_county,
    lexington_county,
    horry_county
]

for county in sc_county_list:
    for city, population in county.items():
        print(
            f"In {city.title()}, the current population is {population}."
        )
