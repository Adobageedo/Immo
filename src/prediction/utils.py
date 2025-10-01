def merge_analysis_predictions(listings_df, median_prices_df):
    """
    Fusionne les données analysées avec les prix prédits
    pour préparer la sélection des meilleures opportunités
    """
    df = listings_df.merge(median_prices_df, on="code_insee", how="left", suffixes=("", "_median"))
    return df
