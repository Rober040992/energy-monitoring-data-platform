from core.rules.data_quality import (
    classify_data_quality,
    DATA_QUALITY_VALID,
    DATA_QUALITY_INCONSISTENT,
    DATA_QUALITY_INCOMPLETE,
)


def test_incomplete_when_missing_fields():
    result = classify_data_quality(
        building_id=None,
        provider="provider-a",
        consumption=10.0,
        temperature=20.0,
    )
    assert result == DATA_QUALITY_INCOMPLETE


def test_inconsistent_when_consumption_is_negative():
    result = classify_data_quality(
        building_id="b-1",
        provider="provider-a",
        consumption=-5.0,
        temperature=20.0,
    )
    assert result == DATA_QUALITY_INCONSISTENT


def test_valid_when_all_values_are_correct():
    result = classify_data_quality(
        building_id="b-1",
        provider="provider-a",
        consumption=15.0,
        temperature=22.0,
    )
    assert result == DATA_QUALITY_VALID
