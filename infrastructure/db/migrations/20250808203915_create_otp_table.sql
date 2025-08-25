-- migrate:up
CREATE TABLE otp
(
    id         SERIAL PRIMARY KEY,
    mobile     VARCHAR(20) NOT NULL,
    code       INTEGER     NOT NULL,
    expire_at  TIMESTAMP(0)  NOT NULL,
    created_at TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP
);
-- migrate:down
DROP TABLE IF EXISTS otp;
