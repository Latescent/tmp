from typing import Optional


class Enumeration:
    def __init__(self, title: str, slug: str, **kwargs) -> None:
        self.id: Optional[int] = kwargs.get('id')
        self.title: str = title
        self.slug: str = slug
        self.parent_id: Optional[int] = kwargs.get('parent_id')

    @classmethod
    def create(cls, title: str, slug: str, parent_id: Optional[int] = None):
        return cls(title=title, slug=slug, parent_id=parent_id)