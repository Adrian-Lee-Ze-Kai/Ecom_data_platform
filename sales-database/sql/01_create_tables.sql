CREATE TABLE members (
    membership_id  TEXT PRIMARY KEY,
    first_name     TEXT NOT NULL,
    last_name      TEXT NOT NULL,
    email          TEXT NOT NULL,
    mobile_no      TEXT NOT NULL,
    birthday       DATE NOT NULL
);

CREATE TABLE items(
    item_id TEXT PRIMARY KEY,
    item_name TEXT NOT NULL,
    manufacturer_name TEXT NOT NULL,
    cost NUMERIC(10,2) NOT NULL CHECK(cost > 0),
    weight_kg NUMERIC(10,3) NOT NULL CHECK(weight_kg > 0)
);

CREATE TABLE transactions(
    transaction_id TEXT PRIMARY KEY,
    membership_id TEXT NOT NULL REFERENCES members(membership_id),
    transaction_date TIMESTAMP NOT NULL,
    total_cost NUMERIC(10,2) NOT NULL CHECK(total_cost > 0),
    total_weight_kg NUMERIC(10,3) NOT NULL CHECK(total_weight_kg > 0)
);

CREATE TABLE transaction_items(
    transaction_id TEXT NOT NULL REFERENCES transactions(transaction_id),
    item_id TEXT NOT NULL REFERENCES items(item_id),
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    unit_price NUMERIC(10,2) NOT NULL CHECK(unit_price > 0),
    PRIMARY KEY (transaction_id, item_id)
);

-- Index foreign keys and dates used in joins and reporting (PostgreSQL does not index foreign keys automatically)
CREATE INDEX idx_transactions_member ON transactions(membership_id);
CREATE INDEX idx_transaction_items_item ON transaction_items(item_id);
CREATE INDEX idx_transactions_date ON transactions(transaction_date);