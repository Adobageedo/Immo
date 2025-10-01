-- Table pour les annonces Melo
CREATE TABLE IF NOT EXISTS listings_melo (
    id TEXT PRIMARY KEY,
    price NUMERIC,
    surface NUMERIC,
    type TEXT,
    address TEXT,
    lat NUMERIC,
    lon NUMERIC,
    price_per_m2 NUMERIC
);

-- Table pour les transactions DVF+
CREATE TABLE IF NOT EXISTS transactions_dvf (
    id TEXT PRIMARY KEY,
    price NUMERIC,
    surface NUMERIC,
    type TEXT,
    address TEXT,
    lat NUMERIC,
    lon NUMERIC,
    price_per_m2 NUMERIC
);

-- Table zones géographiques (optionnelle)
CREATE TABLE IF NOT EXISTS zones_geo (
    id SERIAL PRIMARY KEY,
    code_insee TEXT,
    name TEXT,
    geom GEOMETRY(MultiPolygon, 4326)
);

-- Index pour accélérer les requêtes géographiques
CREATE INDEX IF NOT EXISTS idx_listings_geo ON listings_melo USING GIST (ST_SetSRID(ST_MakePoint(lon, lat), 4326));
CREATE INDEX IF NOT EXISTS idx_transactions_geo ON transactions_dvf USING GIST (ST_SetSRID(ST_MakePoint(lon, lat), 4326));
