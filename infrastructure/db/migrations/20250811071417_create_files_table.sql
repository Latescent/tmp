-- migrate:up
CREATE TABLE files
(
    id         BIGSERIAL PRIMARY KEY,
    user_id    BIGINT,
    name       VARCHAR(255) NOT NULL,
    path       VARCHAR(255) NOT NULL,
    file_name  VARCHAR(255) NOT NULL,
    mime_type  VARCHAR(255) NOT NULL,
    format     VARCHAR(255) NOT NULL,
    width      INTEGER,
    height     INTEGER,
    size       INTEGER      NOT NULL,
    "type"     VARCHAR(255) NOT NULL,
    deleted_at TIMESTAMP(0),
    created_at TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_files_users
        FOREIGN KEY (user_id)
            REFERENCES users (id)
            ON DELETE CASCADE
);

CREATE INDEX idx_files_user_id ON files (user_id);

-- migrate:down
DROP TABLE IF EXISTS files;

