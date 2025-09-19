-- migrate:up
CREATE TABLE enumerations
(
    id         BIGSERIAL PRIMARY KEY,
    title      VARCHAR(255) NOT NULL,
    slug       VARCHAR(255),
    parent_id  BIGINT       REFERENCES enumerations (id) ON DELETE SET NULL,
    created_at TIMESTAMP(0) NOT NULL DEFAULT now(),
    updated_at TIMESTAMP(0) NOT NULL DEFAULT now()
);
-- migrate:down
DROP TABLE IF EXISTS enumerations;
