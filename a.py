from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///mydb.db', echo = True)
meta = MetaData()
Word = Table(
   'Word', meta, 
   Column('Word', String, primary_key = True),)
Definition = Table(
   'Definition', meta, 
   Column('Definition', String, primary_key = True),)
Examples = Table(
   'Examples', meta, 
   Column('Examples', String, primary_key = True),)
Synonimes = Table(
   'Synonimes', meta, 
   Column('Synonimes', String, primary_key = True),)
Antonyms = Table(
   'Antonyms', meta, 
   Column('Antonyms', String, primary_key = True),)
meta.create_all(engine)
