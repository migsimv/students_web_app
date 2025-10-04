import os

class Config:
    if 'RDS_HOSTNAME' in os.environ:
        SQLALCHEMY_DATABASE_URI = \
            f"postgresql://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}" \
            f"@{os.environ['RDS_HOSTNAME']}:{os.environ['RDS_PORT']}/{os.environ['RDS_DB_NAME']}"
    else:
        SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or \
            "postgresql://postgres:password@localhost:5432/studentsdb"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")