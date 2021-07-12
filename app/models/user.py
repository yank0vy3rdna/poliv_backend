from tortoise import fields

from app.models.base import AbstractBaseModel


class User(AbstractBaseModel):
    username = fields.CharField(max_length=255, null=False)
    hashed_password = fields.CharField(max_length=255, null=False)

    def __repr__(self):
        return "User(id='{}')".format(self.id)

    def to_dict(self):
        user_dict = self.__dict__.copy()
        user_dict.update({"user_id": self.id})
        user_dict['hashed_password'] = None
        return user_dict
