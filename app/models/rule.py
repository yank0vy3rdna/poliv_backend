from tortoise import fields

from app.models.base import TimestampedMixin, AbstractBaseModel
from app.models.device import Device


class Rule(TimestampedMixin, AbstractBaseModel):
    hour = fields.IntField(null=False)
    minute = fields.IntField(null=False)
    device: fields.ForeignKeyRelation[Device] = fields.ForeignKeyField("models.Device", related_name="rules")

    def __repr__(self):
        return "Rule(id='{}')".format(self.id)

    def to_dict(self):
        user_dict = self.__dict__.copy()
        return user_dict
