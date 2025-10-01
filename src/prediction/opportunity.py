from core.logger import setup_logger

logger = setup_logger("opportunity")

def detect_best_opportunities(listings_df, top_n=50):
    """
    Classe les annonces selon l'attractivité globale :
    - Score attractivité (Phase 2)
    - Prix prédit vs prix réel
    """
    df = listings_df.copy()
    df["value_gap"] = df["predicted_price_per_m2"] - df["price_per_m2"]
    df["final_score"] = df["score"] + df["value_gap"]
    df = df.sort_values(by="final_score", ascending=False)
    logger.info(f"{len(df)} annonces triées selon attractivité")
    return df.head(top_n)
