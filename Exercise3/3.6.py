sc_counties = {
    "Richland County": "Columbia",
    "Greenville County": "Greenville",
    "Charleston County": "Charleston",
    "Horry County": "Conway",
    "Lexington County": "Lexington",
    "York County": "York"
}

county_list = [
    "Richland County",
    "Greenville County",
    "Charleston County",
    "Horry County",
    "Lexington County",
    "York County",
    "Spartanburg County",
    "Anderson County",
    "Florence County",
    "Beaufort County"
]

for county in county_list:
    if county in sc_counties:
        print(
            f"{county} is in our dictionary, and the capital/seat is "
            f"{sc_counties[county]}."
        )
    else:
        print(
            f"{county} is not in our dictionary. "
            f"We will add this county shortly. Thanks!"
        )
