from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STR']

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


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs
  
