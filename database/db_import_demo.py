import datetime
from xid import XID
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select,update,insert
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from file_reader import read_file


Base = declarative_base()
class PromptMainTmp(Base):
    __tablename__ = 'prompt_main_tmp'

    id = Column(String(20))
    code = Column(String(20),primary_key=True)
    prompt_content = Column(String(200))
    children = Column(String(200))

class ResPromptMain(Base):
    __tablename__ = 'res_prompt_main'

    id = Column(String(20),primary_key=True)
    prompt_title = Column(String(200))
    prompt_content = Column(String(200))
    type = Column(String(10),default='guide')
    created_at = Column(DateTime,default=datetime.datetime.now)
    updated_at = Column(DateTime,default=datetime.datetime.now)
    is_enabled = Column(Integer,default=1)
    is_deleted = Column(Integer,default=0)

class ResPromptRelation(Base):
    __tablename__ = 'res_prompt_relation'

    id = Column(String(20),primary_key=True)
    parent_id = Column(String(20))
    child_id = Column(String(20))
    type = Column(String(10),default='prompt')
    created_at = Column(DateTime,default=datetime.datetime.now)
    updated_at = Column(DateTime,default=datetime.datetime.now)
    is_enabled = Column(Integer,default=1)
    is_deleted = Column(Integer,default=0)        

#标准化prompt_main_tmp表的数据
def standardize_data():
    engine = create_engine('mysql+pymysql://ics:ics1qazxsw2@test.zyys.tech:31601/ics_res?charset=utf8')
    Session = sessionmaker(bind=engine)
    session = Session()
    stmt = select(PromptMainTmp)
    result = session.execute(stmt)
    for prompt in result.scalars():
        stmt = update(PromptMainTmp).where(PromptMainTmp.code == prompt.code).values(id=XID().string())
        result = session.execute(stmt)
    session.commit()
    session.close()

#插入res_prompt_main表和res_prompt_relation表
def gen_prompt():
    engine = create_engine('mysql+pymysql://ics:ics1qazxsw2@test.zyys.tech:31601/ics_res?charset=utf8')
    Session = sessionmaker(bind=engine)
    session = Session()
    stmt = select(PromptMainTmp)
    result = session.execute(stmt)
    for tmp_prompt in result.scalars():
        stmt = insert(ResPromptMain).values(id=tmp_prompt.id,prompt_title=tmp_prompt.prompt_content,prompt_content=tmp_prompt.prompt_content)
        session.execute(stmt)
        if tmp_prompt.children == None: continue
        children = tmp_prompt.children.split(',')
        for child in children:
            prompt = session.get(PromptMainTmp,child)
            #print(prompt.id)
            stmt = insert(ResPromptRelation).values(id=XID().string(),parent_id=tmp_prompt.id,child_id=prompt.id,type='prompt')
            session.execute(stmt)
    session.commit()
    session.close()

gen_prompt()