-- migrate:up
CREATE TABLE access_tokens
(
    id         SERIAL PRIMARY KEY,
    token      VARCHAR(255) UNIQUE NOT NULL,
    user_id    INTEGER             NOT NULL,
    expires_at TIMESTAMPTZ         NOT NULL,
    created_at TIMESTAMPTZ(0) DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ(0) DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_access_tokens_users
        FOREIGN KEY (user_id)
            REFERENCES users (id)
            ON DELETE CASCADE
);

-- migrate:down
DROP TABLE IF EXISTS access_tokens;

