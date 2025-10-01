class Metrics:
    """Suivi des statistiques de traitement pour la phase 1."""

    def __init__(self):
        self.melo_count = 0
        self.dvf_count = 0
        self.errors = 0

    def increment_melo(self, n=1):
        self.melo_count += n

    def increment_dvf(self, n=1):
        self.dvf_count += n

    def increment_errors(self, n=1):
        self.errors += n

    def report(self):
        return {
            "melo_processed": self.melo_count,
            "dvf_processed": self.dvf_count,
            "errors": self.errors
        }
