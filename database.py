import pymysql
import os

timeout = 10
connection = pymysql.connect(
charset="utf8mb4",
connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
          db=os.environ['DATABASE'],
          host=os.environ['HOST'],
          password=os.environ['PASSWORD'],
          read_timeout=timeout,
          port=21772,
          user=os.environ['USER'],
          write_timeout=timeout,
        )

def load_jobs_from_db():
    with connection.cursor() as cursor:
      cursor.execute("select * from jobs")
      jobs=cursor.fetchall()
      return jobs