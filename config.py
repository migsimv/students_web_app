import os

class Config:
   # print(os.environ)
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
        SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    else:
        SQLALCHEMY_DATABASE_URI = os.getenv(
            "DATABASE_URL",
            "postgresql://postgres:password@localhost:5432/studentsdb"
        )
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")