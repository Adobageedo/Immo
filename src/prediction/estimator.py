import pandas as pd
from sklearn.linear_model import LinearRegression
from core.logger import setup_logger

logger = setup_logger("estimator")

class PriceEstimator:
    """Estime le prix au m² par quartier à partir des données DVF."""

    def __init__(self):
        self.model = LinearRegression()
        self.trained = False

    def train(self, transactions_df, features=["surface"], target="price_per_m2"):
        """Entraîne un modèle simple prix/m² par caractéristiques."""
        df = transactions_df.copy()
        df["price_per_m2"] = df["price"] / df["surface"]
        X = df[features]
        y = df[target]
        self.model.fit(X, y)
        self.trained = True
        logger.info("Modèle d'estimation du prix entraîné")

    def predict(self, listings_df, features=["surface"]):
        """Prédit le prix au m² pour de nouvelles annonces."""
        if not self.trained:
            raise Exception("Le modèle doit être entraîné avant prédiction")
        X_new = listings_df[features]
        listings_df["predicted_price_per_m2"] = self.model.predict(X_new)
        listings_df["predicted_price"] = listings_df["predicted_price_per_m2"] * listings_df["surface"]
        return listings_df
