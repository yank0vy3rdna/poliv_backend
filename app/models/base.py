from tortoise import Model, fields


class AbstractBaseModel(Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True


class TimestampedMixin:
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
