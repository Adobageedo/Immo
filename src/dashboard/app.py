from flask import Flask, render_template, jsonify
from database.db import Database
from core.logger import setup_logger
import pandas as pd

logger = setup_logger("dashboard")
app = Flask(__name__)

db = Database()

@app.route("/")
def index():
    # Page principale du dashboard
    return render_template("index.html")

@app.route("/api/opportunities")
def opportunities():
    # Récupérer les meilleures opportunités depuis la DB
    query = "SELECT * FROM listings_melo ORDER BY price_per_m2 LIMIT 50;"
    df = pd.read_sql(query, db.conn)
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
