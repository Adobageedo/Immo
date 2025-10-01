import requests
from config.config import Config
from core.logger import setup_logger

logger = setup_logger("dvf_client")

class DVFClient:
    """Client pour interagir avec l'API DVF+."""

    def __init__(self):
        self.base_url = Config.DVF_BASE_URL
        self.headers = {"Authorization": f"Bearer {Config.DVF_API_KEY}"}

    def fetch_transactions(self, code_insee=None, start_date=None, end_date=None, page=1):
        """
        Récupère les transactions DVF.
        Optionnel: filtrage par code INSEE ou période.
        Pagination gérée par l'API.
        """
        transactions = []
        while True:
            try:
                params = {
                    "code_insee": code_insee,
                    "start_date": start_date,
                    "end_date": end_date,
                    "page": page,
                    "per_page": 100
                }
                response = requests.get(f"{self.base_url}/transactions", headers=self.headers, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()
                if not data.get("transactions"):
                    break
                transactions.extend(data["transactions"])
                page += 1
            except Exception as e:
                logger.error(f"Erreur récupération DVF page {page}: {e}")
                break
        return transactions
