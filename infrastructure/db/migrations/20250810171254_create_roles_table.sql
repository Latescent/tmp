-- migrate:up
CREATE TABLE roles
(
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(50) UNIQUE NOT NULL,
    title      VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP
);
-- migrate:down
DROP TABLE IF EXISTS roles;
