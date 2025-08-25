-- migrate:up
CREATE TABLE file_relations
(
    id          BIGSERIAL PRIMARY KEY,
    entity_id   BIGINT NOT NULL,
    entity_type VARCHAR(255) NOT NULL,
    file_id     BIGINT NOT NULL,
    created_at  TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_file_relations_files
        FOREIGN KEY (file_id)
        REFERENCES files(id)
        ON DELETE CASCADE
);
CREATE INDEX idx_file_relations_entity ON file_relations(entity_id, entity_type);
CREATE INDEX idx_file_relations_file_id ON file_relations(file_id);

-- migrate:down
DROP TABLE IF EXISTS file_relations;
