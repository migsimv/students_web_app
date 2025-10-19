import os

class Config:
    on_vercel = os.getenv("VERCEL") is not None
    on_aws = "RDS_HOSTNAME" in os.environ

    if on_aws:
        SQLALCHEMY_DATABASE_URI = (
            "postgresql://{user}:{password}@{host}:{port}/{db}".format(
                user=os.environ["RDS_USERNAME"],
                password=os.environ["RDS_PASSWORD"],
                host=os.environ["RDS_HOSTNAME"],
                port=os.environ["RDS_PORT"],
                db=os.environ["RDS_DB_NAME"],
            )
        )
        
    elif on_vercel:
        database_url = os.getenv("DATABASE_URL")
        if database_url and database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        SQLALCHEMY_DATABASE_URI = database_url
    else:
        SQLALCHEMY_DATABASE_URI = os.getenv(
            "DATABASE_URL",
            "postgresql://postgres:password@localhost:5432/studentsdb"
        )
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")