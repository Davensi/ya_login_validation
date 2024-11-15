from sqlalchemy import Column,Integer,String,DateTime
from model import Base
# 定义模型:
class LoginUser(Base):
    # 表的名字:
    __tablename__ = "ya_login_user"

    # 表的结构:
    id = Column(Integer(10), unique=True, nullable=False)
    phone = Column(String(32), unique=True, nullable=False)
    invite_code = Column(String(32),  nullable=False)
    ctime = Column(DateTime, default=datetime.datetime.now)

    # 建立索引,指定字符集和引擎
    __table_args__ = (
       
    )