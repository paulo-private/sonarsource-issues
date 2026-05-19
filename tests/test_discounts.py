from src.billing.discounts import calculate_discounted_total_cents


def test_calculate_discounted_total_cents() -> None:
    total = calculate_discounted_total_cents(
        [
            {"unit_price_cents": 1_000, "quantity": 2},
            {"unit_price_cents": 500, "quantity": 1},
        ],
        loyalty_discount_percent=10,
    )

    assert total == 2_250
