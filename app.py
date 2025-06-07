from flask import Flask, render_template, request, g, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'jobs.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    db = get_db()
    featured_jobs = db.execute("SELECT * FROM jobs LIMIT 3").fetchall()
    featured_candidates = db.execute("SELECT * FROM candidates LIMIT 3").fetchall()
    testimonials = [
        {"name": "Aakash", "text": "Found my dream team with Buddy Jobs!", "pic": "/static/buddies/aakash.jpg"},
        {"name": "Meera", "text": "Easy and fast! Hired a great developer.", "pic": "/static/buddies/meera.jpg"},
        {"name": "Vikram", "text": "This portal is a game changer for job seekers.", "pic": "/static/buddies/vikram.jpg"}
    ]
    return render_template('index.html', jobs=featured_jobs, candidates=featured_candidates, testimonials=testimonials)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message = ""
    if request.method == 'POST':
        # Dummy contact handler
        message = "Thanks for reaching out! We'll get back soon."
    return render_template('contact.html', message=message)

@app.route('/buddies')
def buddies():
    buddies = [
        {"name": "Aakash", "role": "Software Engineer", "story": "Matched with a dream company in 2 weeks!", "pic": "/static/buddies/aakash.jpg"},
        {"name": "Meera", "role": "Recruiter", "story": "Found top talent for my startup!", "pic": "/static/buddies/meera.jpg"},
        {"name": "Vikram", "role": "Designer", "story": "Got my first remote UI/UX role here.", "pic": "/static/buddies/vikram.jpg"}
    ]
    return render_template('buddies.html', buddies=buddies)

@app.route('/job-search', methods=['GET', 'POST'])
def job_search():
    db = get_db()
    if request.method == 'POST':
        role = request.form.get('role', '').strip()
        skill = request.form.get('skill', '').strip()
        salary = request.form.get('salary', '').strip()
        location = request.form.get('location', '').strip()

        query = "SELECT * FROM jobs WHERE 1=1"
        params = []

        if role:
            query += " AND role LIKE ?"
            params.append(f"%{role}%")
        if skill:
            query += " AND skill LIKE ?"
            params.append(f"%{skill}%")
        if salary:
            query += " AND salary >= ?"
            params.append(salary)
        if location:
            query += " AND location LIKE ?"
            params.append(f"%{location}%")

        results = db.execute(query, params).fetchall()
    else:
        results = db.execute("SELECT * FROM jobs").fetchall()
    return render_template('job_search.html', results=results)

@app.route('/candidate-search', methods=['GET', 'POST'])
def candidate_search():
    db = get_db()
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        skill = request.form.get('skill', '').strip()
        location = request.form.get('location', '').strip()
        experience = request.form.get('experience', '').strip()
        certification = request.form.get('certification', '').strip()

        query = "SELECT * FROM candidates WHERE 1=1"
        params = []

        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")
        if skill:
            query += " AND skill LIKE ?"
            params.append(f"%{skill}%")
        if location:
            query += " AND location LIKE ?"
            params.append(f"%{location}%")
        if experience:
            query += " AND experience >= ?"
            params.append(experience)
        if certification:
            query += " AND certification LIKE ?"
            params.append(f"%{certification}%")

        results = db.execute(query, params).fetchall()
    else:
        results = db.execute("SELECT * FROM candidates").fetchall()
    return render_template('candidate_search.html', results=results)

@app.route('/job/<int:job_id>')
def job_detail(job_id):
    db = get_db()
    job = db.execute("SELECT * FROM jobs WHERE id = ?", (job_id,)).fetchone()
    if not job:
        return redirect(url_for('job_search'))
    return render_template('job_detail.html', job=job)

@app.route('/candidate/<int:cand_id>')
def candidate_detail(cand_id):
    db = get_db()
    candidate = db.execute("SELECT * FROM candidates WHERE id = ?", (cand_id,)).fetchone()
    if not candidate:
        return redirect(url_for('candidate_search'))
    return render_template('candidate_detail.html', candidate=candidate)

if __name__ == '__main__':
    app.run(debug=True)