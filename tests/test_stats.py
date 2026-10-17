from stats import count_labels, paddy_ratio, paddy_ratio_by_region, filter_by_confidence


def test_count_labels():
    counts = count_labels("data/sample.csv")
    assert counts["水田"] == 92


def test_paddy_ratio():
    ratio = paddy_ratio("data/sample.csv")
    assert ratio == 0.92


def test_paddy_ratio_by_region():
    ratios = paddy_ratio_by_region("data/sample.csv")
    assert ratios[82350] == 0.92


def test_filter_by_confidence():
    filtered_df = filter_by_confidence("data/sample.csv", 0.3)
    assert len(filtered_df) == 3


def test_filter_by_confidence_05():
    filtered_df = filter_by_confidence("data/sample.csv", 0.5)
    assert len(filtered_df) == 1
