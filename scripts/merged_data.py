from raw_data import get_raw_dataframes


def get_weather_migraine_dataframe():
    df_city, df_country, df_weather, df_migraine = get_raw_dataframes()

    # Combine cities and daily weather dataframes into one
    df_cities_weather = df_city.merge(
        df_weather,
        how="left",
        left_on=["station_id", "city_name"],
        right_on=["station_id", "city_name"],
    )

    # Combine countries and cities/daily weather dataframe into one
    df_combined_weather = df_cities_weather.merge(
        df_country,
        how="left",
        left_on=["country", "iso2", "iso3"],
        right_on=["country", "iso2", "iso3"],
    )

    # Merge df_cities_daily_weather and df_migraine
    df_weather_migraine = df_combined_weather.merge(
        df_migraine, how="left", left_on="city_name", right_on="location_name"
    )

    return df_weather_migraine
