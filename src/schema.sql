CREATE TABLE IF NOT EXISTS parcels (
	polygon_uu TEXT PRIMARY KEY, -- 筆のID
	point_lat REAL,              -- 緯度
	point_lng REAL,              -- 経度
	final_label TEXT,            -- 色分け
	stage2_prob REAL,            -- 確信度
	local_gove INTEGER           -- 地域
);
