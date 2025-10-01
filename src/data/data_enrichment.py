from geopy.geocoders import Nominatim
from core.logger import setup_logger

logger = setup_logger("data_enrichment")
geolocator = Nominatim(user_agent="real_estate_pipeline")

# -----------------------------
# Melo
# -----------------------------
def enrich_listings(listings):
    """Ajoute informations géographiques et calculs dérivés sur les annonces."""
    for item in listings:
        # Calcul prix/m²
        item["price_per_m2"] = item["price"] / item["surface"] if item["surface"] else None
        # Géocodage optionnel
        if "address" in item and item["address"]:
            try:
                location = geolocator.geocode(item["address"])
                if location:
                    item["lat"] = location.latitude
                    item["lon"] = location.longitude
            except Exception as e:
                logger.warning(f"Erreur géocodage Melo: {e}")
    return listings

# -----------------------------
# DVF+
# -----------------------------
def enrich_transactions(transactions):
    """Ajoute calculs dérivés sur les transactions DVF+."""
    for item in transactions:
        item["price_per_m2"] = item["price"] / item["surface"] if item["surface"] else None
        # Géocodage optionnel si adresse disponible
        if "address" in item and item["address"]:
            try:
                location = geolocator.geocode(item["address"])
                if location:
                    item["lat"] = location.latitude
                    item["lon"] = location.longitude
            except Exception as e:
                logger.warning(f"Erreur géocodage DVF: {e}")
    return transactions
