import sqlalchemy, text
from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://sj9w2rsc04a2p94nukju:pscale_pw_rwZTJYd18oer1Qnuavu99p0B7a1FKrFhzHh0ALhk7ZS@us-west.connect.psdb.cloud/wycliffecareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem",
            # "cert": "/home/gord/client-ssl/client-cert.pem",
            # "key": "/home/gord/client-ssl/client-key.pem"
        }
    }
)
with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())