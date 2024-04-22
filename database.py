import pymysql
import os
from flask import g

timeout = 10

# Function to establish a database connection
def get_database_connection():
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
    return connection

# Function to get a database connection within the Flask application context
def get_db_connection():
    if not hasattr(g, 'db_connection'):
        g.db_connection = get_database_connection()
    return g.db_connection

# Function to load all jobs from the database
def load_jobs_from_db():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM jobs")
        jobs = cursor.fetchall()
    return jobs

# Function to load a single job from the database based on its ID
def load_job_from_db(id):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM jobs WHERE id=%s", (id))
        job = cursor.fetchone()
    return job

def add_application_to_db(job_id, data):
  connection = get_db_connection()
  with connection.cursor() as cursor:
      cursor.execute("INSERT INTO applications(job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (%s, %s, %s, %s, %s, %s, %s)",(job_id, data['full_name'], data['email'], data['linkedin_url'], data['education'], data['work_experience'], data['resume_url']))
  connection.commit()
