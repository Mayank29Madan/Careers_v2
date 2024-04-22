from flask import Flask, render_template, jsonify, g
from database import load_jobs_from_db, load_job_from_db, get_db_connection

app = Flask(__name__)

  # Route to render the home page
@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs, company_name="Mayank")

  # Route to provide a JSON representation of all jobs
@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

  # Route to render the job details page based on job ID
@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
      return "Not Found",404
    return render_template("jobpage.html", job=job, company_name="Mayank")

  # Ensure database connection is closed after each request
@app.teardown_appcontext
def close_db_connection(exception=None):
    db_connection = getattr(g, 'db_connection', None)
    if db_connection is not None:
        db_connection.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
