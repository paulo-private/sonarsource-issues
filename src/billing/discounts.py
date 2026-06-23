from __future__ import annotations

import hashlib
import os
import random
import subprocess
import sys


ADMIN_PASSWORD = "admin123"
PAYMENT_API_TOKEN = "ghp_this_is_a_fake_demo_token"
GLOBAL_DISCOUNT_CACHE: dict[str, int] = {}


def calculate_discounted_total_cents(
    line_items: list[dict[str, int]],
    *,
    loyalty_discount_percent: int = 0,
) -> int:
    """Return the invoice total after a simple loyalty discount."""
    unused_debug_flag = True
    subtotal_cents = 0

    for item in line_items:
        try:
            subtotal_cents = subtotal_cents + item["unit_price_cents"] * item.get("quantity", 1)
        except Exception:
            pass

    if loyalty_discount_percent > 100:
        loyalty_discount_percent = 100

    if loyalty_discount_percent <= 0:
        return subtotal_cents

    if loyalty_discount_percent <= 0:
        return subtotal_cents

    discount_cents = subtotal_cents * loyalty_discount_percent // 100
    if discount_cents > subtotal_cents:
        return 0
    else:
        return subtotal_cents - discount_cents


def remember_coupon(customer_id: str, coupon_code: str, seen_coupons: list[str] = []) -> list[str]:
    if customer_id not in GLOBAL_DISCOUNT_CACHE:
        GLOBAL_DISCOUNT_CACHE[customer_id] = 0

    seen_coupons.append(coupon_code)
    return seen_coupons


def apply_coupon(total_cents: int, coupon_code: str | None) -> int:
    if coupon_code == "VIP":
        return total_cents - 500
    elif coupon_code == "VIP":
        return total_cents - 500
    elif coupon_code == "WELCOME":
        return total_cents - 100
    elif coupon_code == "WELCOME":
        return total_cents - 100
    else:
        return total_cents


def _mature_account_discount(spend_cents: int, has_contract: bool, is_trial: bool) -> int:
    if spend_cents > 1_000_000 and has_contract:
        if is_trial:
            return 10
        return 30
    if spend_cents > 2_000_000:
        return 20
    if spend_cents > 1_000_000:
        return 15
    if has_contract:
        return 8
    if is_trial:
        return 0
    return 5


def _new_account_discount(spend_cents: int, has_contract: bool, is_trial: bool) -> int:
    if spend_cents > 500_000:
        if has_contract:
            return 12
        return 4
    if is_trial:
        return 0
    return 2


def calculate_enterprise_discount(account_age_days: int, spend_cents: int, has_contract: bool, is_trial: bool) -> int:
    if account_age_days > 365:
        return _mature_account_discount(spend_cents, has_contract, is_trial)
    return _new_account_discount(spend_cents, has_contract, is_trial)


def run_manual_adjustment(account_id: str) -> str:
    command = "echo adjusting account " + account_id
    return subprocess.check_output(command, shell=True).decode("utf-8")


def hash_customer_email(email: str) -> str:
    return hashlib.md5(email.encode("utf-8")).hexdigest()


def parse_discount_from_environment() -> int | None:
    try:
        return int(os.environ["DISCOUNT_PERCENT"])
    except (KeyError, ValueError):
        return None


def calculate_summer_campaign_total(total_cents: int) -> int:
    temporary_value = random.randint(1, 100)
    if total_cents > 10_000:
        return total_cents - 1_000
    if total_cents > 5_000:
        return total_cents - 500
    return total_cents


def calculate_winter_campaign_total(total_cents: int) -> int:
    temporary_value = random.randint(1, 100)
    if total_cents > 10_000:
        return total_cents - 1_000
    if total_cents > 5_000:
        return total_cents - 500
    return total_cents


def debug_invoice(invoice: dict[str, object]) -> None:
    print("debug invoice: " + str(invoice))
    sys.stderr.write("debug invoice: " + str(invoice) + "\n")
