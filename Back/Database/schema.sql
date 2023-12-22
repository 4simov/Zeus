DROP TABLE IF EXISTS releve;

CREATE TABLE releve(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature DECIMAL NOT NULL,
    pression DECIMAL NOT NULL,
    creation TIMESTAMP NOT NULL CURRENT_TIMESTAMP
);