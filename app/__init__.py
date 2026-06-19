import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

nav_pages = [
    {"name": "Home", "url": "/"},
    {"name": "Mahashri", "url": "/maha"},
    {"name": "Narottam", "url": "/naro"},
    {"name": "Jordan", "url": "/jordan"},
    {"name": "Hobbies", "url": "/hobbies"},
]

@app.context_processor
def inject_globals():
    return {
        "nav_pages": nav_pages,
        "url": os.getenv("URL"),
        "request": request,
    }

# ── Maha's data ──────────────────────────────────────────
maha_work = [
    {
        "title": "Production Engineering Fellow",
        "company": "Meta",
        "duration": "June 2026 – Present",
        "bullets": [
            "Selected for the highly competitive Meta–MLH Production Engineering Fellowship (2% acceptance rate), working on systems development and engineering collaboration.",
        ],
    },
    {
        "title": "Software Engineer (Platform)",
        "company": "Regen Network Development",
        "duration": "June 2026 – Present",
        "bullets": [
            "Built a production-grade Python SDK and CLI for ingesting multi-source data into Regen's claims pipeline; designed the Output Record contract (JSON-LD + RDF) integrating with the KOI Claims Engine; shipped CI-tested ingestion pipelines (≥80% coverage) with reproducible local-first developer workflows.",
        ],
    },
    {
        "title": "AI Perception Team Lead",
        "company": "Leeds Gryphon Racing",
        "duration": "November 2025 – Present",
        "bullets": [
            "Leading a multi-disciplinary AI-perception team, coordinating model development, system integration and testing cycles within a competitive Formula Student engineering programme.",
            "Implementing LiDAR–camera sensor fusion pipelines using ROS2 to enhance spatial awareness and perception reliability under variable lighting and environmental conditions.",
        ],
    },
    {
        "title": "Research Intern",
        "company": "University of Leeds – Engineering and Physical Sciences Faculty",
        "duration": "December 2025 – January 2026",
        "bullets": [
            "Implemented the Condense & Distil summation algorithm in C++ under academic supervision, designing a drop-in API for seamless integration with existing numerical software and documenting outcomes to support future academic publication.",
        ],
    },
]

maha_education = [
    {
        "degree": "Bachelor of Engineering, Electronics and Computer Engineering",
        "school": "University of Leeds",
        "year": "2025 – 2028",
    },
]

maha_travel = [
    {"name": "India", "lat": 20.5937, "lng": 78.9629},
    {"name": "United Kingdom", "lat": 53.8008, "lng": -1.5491},
]

# ── Naro's data ──────────────────────────────────────────
naro_work = [
    {
        "title": "Production Engineering Fellow",
        "company": "Meta",
        "duration": "June 2026 – Present",
        "bullets": [
            "It is a 12 Week collaborative Production Engineering Fellowship partnered with Meta which focuses on working in Site Reliability Engineering and DevOps. This includes:",
            "Working on projects whilst collaborating in a pod of engineers under direct mentorship from Meta Production Engineers.",
            "Applying CI/CD practices including automated testing and automated deployments across microservices and serverless architectures.",
        ],
    },
]

naro_education = [
    {
        "degree": "Integrated Masters in Computer Science",
        "school": "Trinity College Dublin",
        "year": "2024 - 2029",
    },
]

naro_travel = [
    {"name": "Ireland", "lat": 53.1424, "lng": -7.6921},
    {"name": "United Kingdom", "lat": 55.3781, "lng": -3.4360},
    {"name": "India", "lat": 20.5937, "lng": 78.9629},
    {"name": "Germany", "lat": 51.1657, "lng": 10.4515},
    {"name": "Poland", "lat": 51.9194, "lng": 19.1451},
    {"name": "Portugal", "lat": 39.3999, "lng": -8.2245},
    {"name": "Italy", "lat": 41.8719, "lng": 12.5674},
    {"name": "Switzerland", "lat": 46.8182, "lng": 8.2275},
    {"name": "Netherlands", "lat": 52.1326, "lng": 5.2913},
]

# ── Jordan's data ────────────────────────────────────────
jordan_work = [
    {
        "title": "Job Title",
        "company": "Company",
        "duration": "Month Year – Month Year",
        "description": "Description.",
    },
]

jordan_education = [
    {
        "degree": "Degree",
        "school": "University",
        "year": "Year",
    },
]

jordan_travel = [
    {"name": "Home Country", "lat": 0, "lng": 0},
]

# ── Hobbies data ─────────────────────────────────────────
hobbies_data = [
    {
        "name": ["Music","Movies","Hiking"], "people": ["Maha", "Naro"]
    },
    {
        "name": ["Cooking"], "people": ["Maha", "Jordan"]
    },
    {
        "name": ["Running","Football"], "people": ["Jordan"]
    },
    {
        "name": ["Reading","Cycling"], "people": ["Maha"]
    },
    {
        "name": ["Gaming"], "people": ["Naro"]
    },
]

# ── Routes ───────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/maha')
def maha():
    return render_template(
        'maha.html',
        work_experience=maha_work,
        education=maha_education,
        travel_places=maha_travel,
    )

@app.route('/naro')
def naro():
    return render_template(
        'naro.html',
        work_experience=naro_work,
        education=naro_education,
        travel_places=naro_travel,
    )

@app.route('/jordan')
def jordan():
    return render_template(
        'jordan.html',
        work_experience=jordan_work,
        education=jordan_education,
        travel_places=jordan_travel,
    )

@app.route('/hobbies')
def hobbies():
    circle_positions = {
        frozenset(["Maha"]): (155, 120),
        frozenset(["Naro"]): (345, 120),
        frozenset(["Jordan"]): (250, 255),

        frozenset(["Maha", "Naro"]): (250, 120),
        frozenset(["Maha", "Jordan"]): (210, 190),
        frozenset(["Naro", "Jordan"]): (290, 190),

        frozenset(["Maha", "Naro", "Jordan"]): (250, 160),
    }
    for hobby in hobbies_data:
        key = frozenset(hobby["people"])
        hobby["pos"] = circle_positions.get(key, (250, 175))
    
    return render_template('hobbies.html', hobbies=hobbies_data)
