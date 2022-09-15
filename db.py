from peewee import *

sqlConnect = SqliteDatabase("./db/bank.db", pragmas={'journal_mode': 'wal'})


class BaseModel(Model):
    """A base model that will use our SQLITE3 database"""

    class Meta:
        database = sqlConnect


class AccountDb(BaseModel):
    account = CharField()
    phone = CharField()
    email = CharField()
    balance = FloatField()
