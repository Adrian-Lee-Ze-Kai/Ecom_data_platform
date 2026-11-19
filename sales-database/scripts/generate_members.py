"""Generate the synthetic members used to seed the database.

Output: ../data/members.csv (50 rows, deterministic thanks to a fixed seed).

Membership IDs follow the format <last_name>_<first 5 hex chars of SHA256(YYYYMMDD birthday)>.
Uses only the Python standard library.
"""

import csv
import hashlib
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 42
NUM_MEMBERS = 50

FIRST_NAMES = [
    "Aiden", "Bella", "Caleb", "Chloe", "Daniel", "Elena", "Ethan", "Fiona", "Gabriel", "Hannah",
    "Isaac", "Jasmine", "Kai", "Leah", "Lucas", "Maya", "Nathan", "Olivia", "Owen", "Priya",
    "Rachel", "Ryan", "Sofia", "Theo", "Uma", "Victor", "Wei", "Yara", "Zachary", "Zoe",
]
LAST_NAMES = [
    "Anderson", "Bennett", "Chen", "Dawson", "Ellis", "Fernandez", "Garcia", "Hughes", "Ibrahim",
    "Jensen", "Kumar", "Lim", "Morales", "Nguyen", "Okafor", "Patel", "Quinn", "Reyes", "Silva",
    "Tan", "Underwood", "Vargas", "Wong", "Xu", "Young", "Zhang",
]


def membership_id(last_name: str, birthday: str) -> str:
    """Build the membership ID from the last name and a YYYYMMDD birthday."""
    return f"{last_name}_{hashlib.sha256(birthday.encode('utf-8')).hexdigest()[:5]}"


def main() -> None:
    rng = random.Random(SEED)
    start, end = date(1960, 1, 1), date(2003, 12, 31)
    members, seen_ids = [], set()

    while len(members) < NUM_MEMBERS:
        first, last = rng.choice(FIRST_NAMES), rng.choice(LAST_NAMES)
        birthday = (start + timedelta(days=rng.randint(0, (end - start).days))).strftime("%Y%m%d")
        mid = membership_id(last, birthday)
        if mid in seen_ids:  # IDs are the primary key, so skip collisions
            continue
        seen_ids.add(mid)
        members.append({
            "membership_id": mid,
            "first_name": first,
            "last_name": last,
            "email": f"{first.lower()}.{last.lower()}@example.com",
            "mobile_no": str(rng.randint(80000000, 99999999)),
            "birthday": birthday,
        })

    out = Path(__file__).resolve().parent.parent / "data" / "members.csv"
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(members[0]))
        writer.writeheader()
        writer.writerows(members)
    print(f"Wrote {len(members)} members to {out}")


if __name__ == "__main__":
    main()
