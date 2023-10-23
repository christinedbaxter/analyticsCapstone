import numpy as np

def assign_country(location, city_country_df):
    if np.isin(location, city_country_df['country'].values):
        return location
    else:
        return 'United States of America'


def assign_state(location, city_country_df):
    if not np.isin(location, city_country_df['state'].values):
        return location  # Return the location if it's not in the list of countries, assuming it's a state
    else:
        return None  # Return None or some default value if the location is a country