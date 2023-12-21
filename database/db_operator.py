import datetime
from xid import XID
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from file_reader import read_file


Base = declarative_base()
class ResPromptMain(Base):
    __tablename__ = 'res_prompt_main'

    id = Column(Integer,primary_key=True)
    prompt_title = Column(String(200))
    prompt_content = Column(String(200))
    type = Column(String(10),default='guide')
    created_at = Column(DateTime,default=datetime.datetime.now)
    updated_at = Column(DateTime,default=datetime.datetime.now)
    is_enabled = Column(Integer,default=1)
    is_deleted = Column(Integer,default=0)

contents = read_file('resources/prompts.txt')


promptList = []
for text in contents:
    guid = XID()
    prompt = ResPromptMain(id = guid.string(),prompt_title=text, prompt_content=text)
    promptList.append(prompt)

#promptList = list(map(lambda x: ResPromptMain(prompt_title=x, prompt_content=x), contents))

engine = create_engine('mysql+pymysql://ics:ics1qazxsw2@test.zyys.tech:31601/ics_res?charset=utf8')
Session = sessionmaker(bind=engine)

session = Session()

session.add_all(promptList)
session.commit()
session.close()