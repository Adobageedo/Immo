from clients.melo_client import MeloClient
from clients.dvf_client import DVFClient
from data.data_cleaning import clean_listings, clean_transactions
from data.data_enrichment import enrich_listings, enrich_transactions
from database.db import Database
from core.logger import setup_logger
from core.metrics import Metrics
from config.config import Config

logger = setup_logger()
metrics = Metrics()

class Pipeline:
    """Pipeline de collecte et stockage des données immobilières."""

    def __init__(self):
        self.db = Database()
        self.melo_client = MeloClient()
        self.dvf_client = DVFClient()

    def run(self):
        logger.info("=== Démarrage du pipeline ===")

        # ------------------------
        # 1. Récupérer les annonces Melo
        # ------------------------
        try:
            listings = self.melo_client.get_new_listings()
            logger.info(f"{len(listings)} annonces Melo récupérées")
            metrics.increment_melo(len(listings))

            listings_clean = clean_listings(listings)
            listings_enriched = enrich_listings(listings_clean)
            self.db.insert_listings(listings_enriched)
            logger.info("Annonces Melo stockées en base")
        except Exception as e:
            metrics.increment_errors()
            logger.error(f"Erreur traitement Melo: {e}")

        # ------------------------
        # 2. Récupérer les transactions DVF+
        # ------------------------
        try:
            transactions = self.dvf_client.fetch_transactions()
            logger.info(f"{len(transactions)} transactions DVF récupérées")
            metrics.increment_dvf(len(transactions))

            transactions_clean = clean_transactions(transactions)
            transactions_enriched = enrich_transactions(transactions_clean)
            self.db.insert_transactions(transactions_enriched)
            logger.info("Transactions DVF stockées en base")
        except Exception as e:
            metrics.increment_errors()
            logger.error(f"Erreur traitement DVF: {e}")

        logger.info("=== Pipeline terminé ===")
        logger.info(f"Metrics: {metrics.report()}")
