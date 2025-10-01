import requests
from config.config import Config
from core.logger import setup_logger

logger = setup_logger("melo_client")

class MeloClient:
    """Client pour interagir avec l'API Melo."""

    def __init__(self):
        self.base_url = Config.MELO_BASE_URL
        self.headers = {"Authorization": f"Bearer {Config.MELO_API_KEY}"}

    def get_new_listings(self, page=1, per_page=100):
        """Récupère les annonces récentes (paginated)."""
        listings = []
        while True:
            try:
                url = f"{self.base_url}/listings?page={page}&per_page={per_page}"
                response = requests.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                data = response.json()
                if not data.get("listings"):
                    break
                listings.extend(data["listings"])
                page += 1
            except Exception as e:
                logger.error(f"Erreur récupération Melo page {page}: {e}")
                break
        return listings

    def get_listing_by_id(self, listing_id):
        """Récupère le détail d'une annonce spécifique."""
        try:
            url = f"{self.base_url}/listings/{listing_id}"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Erreur récupération Melo ID {listing_id}: {e}")
            return None
