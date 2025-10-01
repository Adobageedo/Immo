import pandas as pd
from core.logger import setup_logger

logger = setup_logger("trends")

def compute_price_trends(transactions_df, time_field="date_transaction", freq="M"):
    """
    Calcule les tendances de prix par zone et période (mensuelle/trimestrielle)
    """
    df = transactions_df.copy()
    df["price_per_m2"] = df["price"] / df["surface"]
    df[time_field] = pd.to_datetime(df[time_field])

    trend_df = (
        df.groupby([pd.Grouper(key=time_field, freq=freq), "code_insee"])
        ["price_per_m2"]
        .median()
        .reset_index()
    )
    logger.info(f"Tendances calculées pour {trend_df['code_insee'].nunique()} zones")
    return trend_df
