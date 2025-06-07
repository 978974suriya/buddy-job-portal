import sqlite3
import random

roles = [
    "Software Engineer", "Frontend Developer", "Data Analyst", "UI/UX Designer", "DevOps Engineer",
    "QA Tester", "Mobile App Developer", "Project Manager", "Backend Developer", "Cloud Architect",
    "Full Stack Developer", "System Administrator", "Business Analyst", "Support Engineer", "AI Engineer",
    "ML Engineer", "Product Manager", "Network Engineer", "Game Developer", "Security Analyst"
]

skills = [
    "Python", "JavaScript", "React", "Node.js", "Flask", "Django", "Java", "AWS", "Docker", "SQL",
    "C#", "Kotlin", "Swift", "Angular", "Vue.js", "Figma", "Sketch", "Linux", "GCP", "Azure"
]

cities = [
    "Bangalore", "Delhi", "Mumbai", "Pune", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad", "Jaipur", "Lucknow",
    "Indore", "Bhopal", "Surat", "Nagpur", "Patna", "Chandigarh", "Cochin", "Noida", "Gurgaon", "Vizag"
]

companies = [
    "TechNova", "CloudNest", "PixelCraft", "DataMinds", "WebGenix", "InfoVerse", "BrightApps", "SoftZen", "NextGen", "InnoSpark",
    "QuantumLeap", "Appify", "ByteWorks", "CyberShift", "MetaCore", "SkyNet", "LogiTech", "NexSoft", "DreamLabs", "AlphaWare"
]

candidate_names = [
    "Aarav", "Vihaan", "Vivaan", "Ananya", "Ishaan", "Aadhya", "Advika", "Reyansh", "Siya", "Prisha",
    "Arjun", "Aanya", "Riya", "Dhruv", "Myra", "Krishna", "Tara", "Ira", "Aarohi", "Anvi",
    "Saanvi", "Kabir", "Navya", "Ishika", "Pari", "Shaurya", "Samaira", "Ayaan", "Kiara", "Ishita",
    "Advait", "Vanya", "Aarush", "Meera", "Aryan", "Jiya", "Arnav", "Amaira", "Anika", "Viha",
    "Advik", "Aarohi", "Shaan", "Mira", "Aarushi", "Rehaan", "Eva", "Ahaan", "Anaya", "Aanya"
]

certifications = [
    "AWS Certified", "Azure Certified", "GCP Professional", "Scrum Master", "PMP", "OCJP", "None", "ISTQB", "RHCE", "CCNA"
]

bios = [
    "Passionate developer with a love for technology.",
    "Detail-oriented and a strong team player.",
    "Experienced in fast-paced startup environments.",
    "Focused on delivering high-quality software.",
    "Eager to learn new technologies.",
    "Strong background in cloud and DevOps.",
    "Creative thinker with UI/UX expertise.",
    "Problem solver and innovator.",
    "Enjoys tackling challenging problems.",
    "Excellent communicator and leader."
]

descriptions = [
    "Work with a talented team to build scalable products.",
    "Responsible for designing and developing robust applications.",
    "Opportunity to learn new technologies in a supportive environment.",
    "Drive innovation and help automate key business processes.",
    "Engage with cross-functional teams for project delivery.",
    "Focus on code quality, best practices, and continuous improvement.",
    "Hands-on role with opportunities for growth.",
    "Work on impactful projects that reach millions.",
    "Contribute to open-source and in-house platforms.",
    "Flexible work environment with remote options."
]

logo_urls = [
    "/static/logos/technova.png", "/static/logos/cloudnest.png", "/static/logos/pixelcraft.png",
    "/static/logos/dataminds.png", "/static/logos/webgenix.png", "/static/logos/infoverse.png",
    "/static/logos/brightapps.png", "/static/logos/softzen.png", "/static/logos/nextgen.png", "/static/logos/innospark.png"
]

profile_pics = [
    "/static/profiles/1.jpg", "/static/profiles/2.jpg", "/static/profiles/3.jpg", "/static/profiles/4.jpg", "/static/profiles/5.jpg",
    "/static/profiles/6.jpg", "/static/profiles/7.jpg", "/static/profiles/8.jpg", "/static/profiles/9.jpg", "/static/profiles/10.jpg"
]

conn = sqlite3.connect('jobs.db')
c = conn.cursor()

# Drop tables if they exist for clean re-creation
c.execute('DROP TABLE IF EXISTS jobs')
c.execute('DROP TABLE IF EXISTS candidates')

# Create jobs table
c.execute('''
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    skill TEXT NOT NULL,
    salary INTEGER NOT NULL,
    location TEXT NOT NULL,
    company TEXT,
    description TEXT,
    logo_url TEXT
)
''')

# Create candidates table
c.execute('''
CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    skill TEXT NOT NULL,
    experience INTEGER NOT NULL,
    certification TEXT,
    location TEXT NOT NULL,
    bio TEXT,
    profile_pic TEXT
)
''')

# Insert 100 jobs
job_records = []
for i in range(100):
    role = random.choice(roles)
    skill = ", ".join(random.sample(skills, k=random.randint(1,3)))
    salary = random.randint(30000, 150000)
    location = random.choice(cities)
    company = random.choice(companies)
    description = random.choice(descriptions)
    logo_url = random.choice(logo_urls)
    job_records.append((role, skill, salary, location, company, description, logo_url))

c.executemany('INSERT INTO jobs (role, skill, salary, location, company, description, logo_url) VALUES (?, ?, ?, ?, ?, ?, ?)', job_records)

# Insert 100 candidates
candidate_records = []
for i in range(100):
    name = random.choice(candidate_names) + " " + random.choice(['Sharma','Patel','Singh','Mehra','Kumar','Rao','Das','Nair','Kaur','Gupta'])
    skill = ", ".join(random.sample(skills, k=random.randint(1,3)))
    experience = random.randint(1, 10)
    certification = random.choice(certifications)
    location = random.choice(cities)
    bio = random.choice(bios)
    profile_pic = random.choice(profile_pics)
    candidate_records.append((name, skill, experience, certification, location, bio, profile_pic))

c.executemany('INSERT INTO candidates (name, skill, experience, certification, location, bio, profile_pic) VALUES (?, ?, ?, ?, ?, ?, ?)', candidate_records)

conn.commit()
conn.close()
print("Database initialized with 100 jobs and 100 candidates.")