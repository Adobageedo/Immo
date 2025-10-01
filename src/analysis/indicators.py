import pandas as pd
from core.logger import setup_logger

logger = setup_logger("indicators")

def compute_median_price(df, group_by_field="code_insee"):
    """Calcule le prix médian au m² par zone (quartier, code INSEE...)."""
    df["price_per_m2"] = df["price"] / df["surface"]
    median_df = df.groupby(group_by_field)["price_per_m2"].median().reset_index()
    median_df.rename(columns={"price_per_m2": "median_price_per_m2"}, inplace=True)
    logger.info(f"Médiane prix calculée pour {len(median_df)} zones")
    return median_df

def compute_mean_price(df, group_by_field="code_insee"):
    """Calcule le prix moyen au m² par zone."""
    df["price_per_m2"] = df["price"] / df["surface"]
    mean_df = df.groupby(group_by_field)["price_per_m2"].mean().reset_index()
    mean_df.rename(columns={"price_per_m2": "mean_price_per_m2"}, inplace=True)
    logger.info(f"Moyenne prix calculée pour {len(mean_df)} zones")
    return mean_df
