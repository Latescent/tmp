-- migrate:up
CREATE TABLE loan_requests
(
    id                 BIGSERIAL PRIMARY KEY,
    user_id            BIGINT    NOT NULL REFERENCES users (id),
    loan_code          CHAR(8)   NOT NULL UNIQUE,
    amount             BIGINT    NOT NULL,
    status_id          BIGINT    NOT NULL REFERENCES enumerations (id),
    guarantor_id       BIGINT    NULL REFERENCES users (id),
    guarantee_type_id  BIGINT    NOT NULL REFERENCES guarantee_types (id),
    installment_count  SMALLINT  NOT NULL,
    installment_amount BIGINT    NOT NULL,
    created_at         TIMESTAMP NOT NULL DEFAULT now(),
    updated_at         TIMESTAMP NOT NULL DEFAULT now()
);
-- migrate:down
DROP TABLE IF EXISTS loan_requests;