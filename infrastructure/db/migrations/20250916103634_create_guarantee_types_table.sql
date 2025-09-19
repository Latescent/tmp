-- migrate:up
CREATE TABLE guarantee_types
(
    id              BIGSERIAL PRIMARY KEY,
    title           VARCHAR(255) NOT NULL,
    slug            VARCHAR(255),
    max_loan_amount int,
    created_at      TIMESTAMP(0)    NOT NULL DEFAULT now(),
    updated_at      TIMESTAMP(0)    NOT NULL DEFAULT now()
);
-- migrate:down
DROP TABLE IF EXISTS guarantee_types;
