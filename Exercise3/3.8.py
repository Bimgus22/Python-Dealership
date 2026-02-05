sc_counties = {
    "Richland County": ["Columbia", "Blythewood", "Forest Acres"],
    "Greenville County": ["Greenville", "Mauldin", "Simpsonville"],
    "Charleston County": ["Charleston", "North Charleston", "Mount Pleasant"],
    "Lexington County": ["Lexington", "West Columbia", "Cayce"],
    "Horry County": ["Conway", "Myrtle Beach", "North Myrtle Beach"]
}

for county, cities in sc_counties.items():
    print(
        f"In {county}, the largest cities are "
        f"{cities[0]}, {cities[1]}, and {cities[2]}."
    )
