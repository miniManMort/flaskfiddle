# 
# Peewee objects for User items
#

from peewee import CharField, DateField
from app_modules.db_commons import BaseAppObject


class User (BaseAppObject):

    user_name = CharField()
    full_name = CharField()
    birth_date = DateField()


def create_user_tables():
    User.create_table()
