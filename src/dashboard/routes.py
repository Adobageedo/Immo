from flask import Blueprint, jsonify
import pandas as pd
from database.db import Database

bp = Blueprint("api", __name__)
db = Database()

@bp.route("/opportunities")
def get_opportunities():
    df = pd.read_sql("SELECT * FROM listings_melo ORDER BY price_per_m2 LIMIT 50;", db.conn)
    return jsonify(df.to_dict(orient="records"))
