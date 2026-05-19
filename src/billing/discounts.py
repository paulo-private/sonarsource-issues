from __future__ import annotations


def calculate_discounted_total_cents(
    line_items: list[dict[str, int]],
    *,
    loyalty_discount_percent: int = 0,
) -> int:
    """Return the invoice total after a simple loyalty discount."""
    subtotal_cents = sum(
        item["unit_price_cents"] * item.get("quantity", 1)
        for item in line_items
    )

    if loyalty_discount_percent <= 0:
        return subtotal_cents

    discount_cents = subtotal_cents * loyalty_discount_percent // 100
    return subtotal_cents - discount_cents
