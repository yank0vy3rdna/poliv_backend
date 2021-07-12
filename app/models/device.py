from tortoise import fields

from app.models.base import TimestampedMixin, AbstractBaseModel


class Device(TimestampedMixin, AbstractBaseModel):
    unique_str = fields.CharField(max_length=40, null=False, unique=True)
    rules: fields.ReverseRelation["Rule"]
    enabled = fields.BooleanField(null=False, default=False)

    info_from_device = fields.TextField(default="")

    def __repr__(self):
        return "Device(id='{}')".format(self.id)

    def to_dict(self):
        user_dict = self.__dict__.copy()
        return user_dict
