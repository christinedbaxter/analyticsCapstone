from raw_data import get_raw_dataframes


def get_weather_migraine_dataframe():
    df_cities, df_countries, df_daily_weather, df_migraine = get_raw_dataframes()

    # Combine cities and daily weather dataframes into one
    df_cities_daily_weather = df_cities.merge(
        df_daily_weather,
        how="left",
        left_on=["station_id", "city_name"],
        right_on=["station_id", "city_name"],
    )

    # Merge df_cities_daily_weather and df_migraine
    df_weather_migraine = df_cities_daily_weather.merge(
        df_migraine, how="left", left_on="city_name", right_on="location_name"
    )

    return df_weather_migraine
