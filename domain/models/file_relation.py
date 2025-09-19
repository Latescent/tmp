class FileRelation:
    def __init__(self, entity_id: int, entity_type: str, file_id: int):
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.file_id = file_id

    @classmethod
    def create(cls, entity_id: int, entity_type: str, file_id: int) -> 'FileRelation':
        return cls(entity_id, entity_type, file_id)
