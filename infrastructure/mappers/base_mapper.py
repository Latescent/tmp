import keyword


class BaseMapper:
    @classmethod
    def map(
            cls,
            source: object,
            target_class: type,
            include: set[str] = None,
            exclude: set[str] = None,
            field_map: dict[str, str] = None,
            custom_conversions: dict[str, callable] = None
    ):
        if hasattr(source, '__table__'):
            source_dict = {c.name: getattr(source, c.name) for c in source.__table__.columns}
        else:
            source_dict = source.__dict__.copy()
            source_dict.pop("_sa_instance_state", None)

        include = include or set(source_dict.keys())
        exclude = exclude or set()
        field_map = field_map or {}
        custom_conversions = custom_conversions or {}

        mapped = {}
        post_init_fields = {}

        for src_key, value in source_dict.items():
            if src_key in exclude or src_key not in include:
                continue

            target_key = field_map.get(src_key, src_key)

            if src_key in custom_conversions:
                value = custom_conversions[src_key](value)

            if keyword.iskeyword(target_key):
                post_init_fields[target_key] = value
            else:
                mapped[target_key] = value

        instance = target_class(**mapped)

        for key, value in post_init_fields.items():
            setattr(instance, key, value)

        return instance
