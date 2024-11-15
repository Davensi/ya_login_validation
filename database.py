from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import ProgrammingError

# 数据库连接配置
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'root'
HOST = 'localhost'
PORT = '3306'
DATABASE_NAME = 'ya_work'

# 不带数据库名的初始连接 URL
initial_database_url = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{HOST}:{PORT}/'
# 带数据库名的目标 URL
target_database_url = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}'

# 创建初始和目标引擎
initial_engine = create_engine(initial_database_url, echo=True)
target_engine = create_engine(target_database_url, echo=True)

# 创建数据库的函数
def create_database_if_not_exists(engine, database_name):
    """
    检查数据库是否存在，如果不存在则创建
    """
    with engine.connect() as connection:
        # 获取所有现有数据库
        existing_databases = connection.execute("SHOW DATABASES;")
        databases = [row[0] for row in existing_databases]
        
        # 如果目标数据库不存在，创建它
        if database_name not in databases:
            connection.execute(f"CREATE DATABASE {database_name};")
            print(f"db '{database_name}' 不存在已创建")
        else:
            print(f"db '{database_name}' OK")

# 确保目标数据库存在
create_database_if_not_exists(initial_engine, DATABASE_NAME)

# 创建全局会话工厂和线程安全会话
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=target_engine))

# 测试数据库连接是否正常
try:
    print("已成功连接到数据库")
except ProgrammingError as e:
    print(f"数据库连接失败: {e}")
