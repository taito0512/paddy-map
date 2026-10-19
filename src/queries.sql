-- ラベル別の件数
SELECT final_label, COUNT(*) FROM parcels GROUP BY final_label;
-- 地域別の水田率
SELECT local_gove, AVG(final_label='水田') FROM parcels GROUP BY local_gove;
-- 確信度 0.3 以上の件数
SELECT COUNT(*) FROM parcels WHERE stage2_prob>=0.3;
