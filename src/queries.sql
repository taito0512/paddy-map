SELECT final_label, COUNT(*) FROM parcels GROUP BY final_label;
SELECT local_gove, AVG(final_label='水田') FROM parcels GROUP BY local_gove;
SELECT COUNT(*) FROM parcels WHERE stage2_prob>=0.3;
