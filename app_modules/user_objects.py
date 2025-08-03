# 
# Peewee objects for User items
#

from peewee import CharField, DateField, TextField, IntegerField, ForeignKeyField
from app_modules.db_commons import BaseAppObject

#
# == Peewee Objects =======================================================
#

class User (BaseAppObject):

    user_name = CharField()
    full_name = CharField()
    birth_place = CharField(max_length=128)
    birth_date = DateField()
    emp_start = DateField()


class Role (BaseAppObject):
    role_name = CharField()
    role_description = TextField()
    max_users = IntegerField()

class UserRole (BaseAppObject):
    user_id = ForeignKeyField(User)
    user_role = ForeignKeyField(Role)
    assignment_date = DateField()

#
# == Create DB Tables ===================================================
#
def create_user_tables():
    User.sync_model()
    Role.sync_model()
    UserRole.sync_model()

#
# == Utility Functions ==================================================
#