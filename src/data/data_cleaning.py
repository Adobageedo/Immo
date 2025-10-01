import pandas as pd
from core.logger import setup_logger

logger = setup_logger("data_cleaning")

# -----------------------------
# Melo
# -----------------------------
def clean_listings(listings):
    """Nettoyage et normalisation des annonces Melo."""
    df = pd.DataFrame(listings)
    # Supprimer les doublons
    df.drop_duplicates(subset=["id"], inplace=True)
    # Nettoyer les champs essentiels
    df = df[df["price"].notnull() & df["surface"].notnull()]
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["surface"] = pd.to_numeric(df["surface"], errors="coerce")
    df.dropna(subset=["price", "surface"], inplace=True)
    logger.info(f"{len(df)} annonces Melo nettoyées")
    return df.to_dict(orient="records")

# -----------------------------
# DVF+
# -----------------------------
def clean_transactions(transactions):
    """Nettoyage et normalisation des transactions DVF+."""
    df = pd.DataFrame(transactions)
    df.drop_duplicates(subset=["id"], inplace=True)
    df = df[df["price"].notnull() & df["surface"].notnull()]
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["surface"] = pd.to_numeric(df["surface"], errors="coerce")
    df.dropna(subset=["price", "surface"], inplace=True)
    logger.info(f"{len(df)} transactions DVF nettoyées")
    return df.to_dict(orient="records")
