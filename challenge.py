import pandas as pd


def valid_string_format(string):
    return all(c.isalpha() or c == "." for c in string)


def filter_wrong_string_format(df, columns):
    return df[df[columns].apply(lambda row: row.apply(valid_string_format)).all(axis=1)]


def main():
    try:
        media = pd.read_csv("media_source.csv").dropna()
        mmp = pd.read_csv("mmp.csv").dropna()
    except FileNotFoundError as e:
        print(e)
        return

    media = filter_wrong_string_format(
        media, ["app_id"]
    )
    mmp = filter_wrong_string_format(
        mmp, ["app_id"]
    )

    merged = pd.merge(
        media,
        mmp,
        on=["date", "app_id", "campaign_name", "creative_name", "country"],
        how="inner",
        suffixes=("_media", "_mmp"),
    )

    merged["total_spend"] = merged.spend_media + merged.spend_mmp

    merged["CPI"] = merged.total_spend / merged.installs
    merged["CPC"] = merged.total_spend / merged.clicks

    # Cual es el pais con mas gasto?
    country_max_spend = merged.groupby("country")["total_spend"].sum().idxmax()

    # Cual es la campaña que mejor performance tuvo (menor CPI)
    best_campaign_cpi = merged.groupby("campaign_name")["CPI"].mean().idxmin()

    # Cual es la campaña con mas installs
    campaign_most_installs = merged.groupby("campaign_name")["installs"].sum().idxmax()

    # Cual fue el dia que mas installs
    day_most_installs = merged.groupby("date")["installs"].sum().idxmax()

    print("Pais con mas gasto:", country_max_spend)
    print("Campaña con mejor performance (menor CPI):", best_campaign_cpi)
    print("Campaña con mas installs:", campaign_most_installs)
    print("Dia con mas installs:", day_most_installs)


main()

