import pandas as pd
from core.logger import setup_logger

logger = setup_logger("scoring")

def score_listings(listings_df, median_prices_df, group_field="code_insee"):
    """
    Score les annonces selon leur attractivité:
    - Prix inférieur au prix médian de la zone = mieux noté
    - Surface et type peuvent être ajoutés dans un score global
    """
    df = listings_df.copy()
    df = df.merge(median_prices_df, on=group_field, how="left")
    df["score"] = 100 * (1 - (df["price_per_m2"] / df["median_price_per_m2"]))
    df["score"] = df["score"].clip(lower=0)
    logger.info(f"Scores calculés pour {len(df)} annonces")
    return df
