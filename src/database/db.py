import psycopg2
from psycopg2.extras import execute_values
from config.config import Config
from core.logger import setup_logger

logger = setup_logger("database")

class Database:
    """Connexion et opérations CRUD sur PostgreSQL/PostGIS."""

    def __init__(self):
        self.conn = psycopg2.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            dbname=Config.DB_NAME
        )
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    # -----------------------------
    # Insert Listings Melo
    # -----------------------------
    def insert_listings(self, listings):
        if not listings:
            return
        query = """
            INSERT INTO listings_melo (id, price, surface, type, address, lat, lon, price_per_m2)
            VALUES %s
            ON CONFLICT (id) DO NOTHING
        """
        values = [
            (
                item.get("id"),
                item.get("price"),
                item.get("surface"),
                item.get("type"),
                item.get("address"),
                item.get("lat"),
                item.get("lon"),
                item.get("price_per_m2")
            )
            for item in listings
        ]
        try:
            execute_values(self.cursor, query, values)
            logger.info(f"{len(values)} annonces Melo insérées en base")
        except Exception as e:
            logger.error(f"Erreur insertion listings Melo: {e}")

    # -----------------------------
    # Insert Transactions DVF
    # -----------------------------
    def insert_transactions(self, transactions):
        if not transactions:
            return
        query = """
            INSERT INTO transactions_dvf (id, price, surface, type, address, lat, lon, price_per_m2)
            VALUES %s
            ON CONFLICT (id) DO NOTHING
        """
        values = [
            (
                item.get("id"),
                item.get("price"),
                item.get("surface"),
                item.get("type"),
                item.get("address"),
                item.get("lat"),
                item.get("lon"),
                item.get("price_per_m2")
            )
            for item in transactions
        ]
        try:
            execute_values(self.cursor, query, values)
            logger.info(f"{len(values)} transactions DVF insérées en base")
        except Exception as e:
            logger.error(f"Erreur insertion transactions DVF: {e}")

    def close(self):
        self.cursor.close()
        self.conn.close()
