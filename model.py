from database import target_engine, SessionLocal
from models.user import  User
from sqlalchemy.ext.declarative import declarative_base

# 创建 ORM 的基类
Base = declarative_base()
# 初始化数据库表
def init_db():
    """
    如果数据库中没有表，自动创建表
    """
    Base.metadata.create_all(bind=target_engine)
    print("数据库表初始化完成")

# 主函数
if __name__ == "__main__":
    init_db()
    session = SessionLocal()

    # 示例：添加一个用户
    try:
        new_user = User(name="Alice", email="alice@example.com")
        session.add(new_user)
        session.commit()
        print("用户已添加:", new_user)
    except Exception as e:
        session.rollback()
        print("发生错误:", e)
    finally:
        session.close()
