-- migrate:up
CREATE TABLE users
(
    id            SERIAL PRIMARY KEY,
    mobile        VARCHAR(20) UNIQUE NOT NULL,
    national_code VARCHAR(12) UNIQUE,
    first_name    VARCHAR(100),
    last_name     VARCHAR(100),
    role_id       INTEGER,
    created_at    TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP,
    updated_at    TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_users_roles
        FOREIGN KEY (role_id)
        REFERENCES roles (id)
        ON DELETE SET NULL
);
-- migrate:down
DROP TABLE IF EXISTS users;
