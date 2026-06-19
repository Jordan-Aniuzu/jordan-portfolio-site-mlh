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
            "Build and deploy an open-source Flask web application, setting up a VPS (DigitalOcean + DuckDNS) and replacing tmux-based deployment with a systemd-managed service with custom bash scripts for uptime and auto-restarts.",
            "Write 20+ unit and integration tests (unittest, Peewee ORM), increasing API and database test coverage by 90% with sub-2ms test execution.",
        ],
    },
    {
        "title": "Software Engineer (Platform)",
        "company": "Regen Network Development",
        "duration": "June 2026 – Present",
        "bullets": [
            "Build a production-grade Python SDK ('regen-network/sensor-sdk') and CLI for ingesting multi-source data (transcripts, RSS, APIs) into Regen's claims pipeline, enabling developers to publish structured evidence in <20 lines of code.",
            "Design and implement the Output Record contract (JSON-LD + RDF), including consent-envelope handling and RID-based identifiers, integrating end-to-end with the KOI Claims Engine to generate on-chain attestations.",
            "Develop and deploy ingestion pipelines with polling, parsing, and idempotent retries; ship CI-tested package (≥80% coverage) and reproducible local-first workflows for external developer adoption.",
        ],
    },
    {
        "title": "AI Perception Team Lead",
        "company": "Leeds Gryphon Racing",
        "duration": "November 2025 – Present",
        "bullets": [
            "Developing a real-time computer vision and object detection pipeline for an autonomous Formula Student vehicle, enabling reliable identification of track boundaries and dynamic obstacles at high-speed.",
            "Implementing LiDAR–camera sensor fusion pipelines using ROS2 to enhance spatial awareness and perception reliability under variable lighting and environmental conditions.",
            "Leading a multi-disciplinary AI-perception team, coordinating model development, system integration and testing cycles within a competitive Formula Student engineering programme.",
        ],
    },
    {
        "title": "Research Intern",
        "company": "University of Leeds – Engineering and Physical Sciences Faculty",
        "duration": "December 2025 – January 2026",
        "bullets": [
            "Implemented the Condense & Distil summation algorithm in C++ under academic supervision, producing a performance-oriented library designed to improve numerical accuracy without sacrificing computational efficiency.",
            "Designed a user-friendly API to minimise integration effort with existing numerical software, enabling the library to function as a drop-in component for scientific computing workflows.",
            "Documented the algorithm's design and implementation outcomes, contributing to a foundation that could support future academic publication or open-source release.",
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
        "title": "Job Title",
        "company": "Company",
        "duration": "Month Year – Month Year",
        "description": "Description.",
    },
]

naro_education = [
    {
        "degree": "Degree",
        "school": "University",
        "year": "Year",
    },
]

naro_travel = [
    {"name": "Home Country", "lat": 0, "lng": 0},
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
        "name": "Maha",
        "items": [
            {"name": "Hobby 1", "description": "Short description.", "image": ""},
        ],
    },
    {
        "name": "Naro",
        "items": [
            {"name": "Hobby 1", "description": "Short description.", "image": ""},
        ],
    },
    {
        "name": "Jordan",
        "items": [
            {"name": "Hobby 1", "description": "Short description.", "image": ""},
        ],
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
    return render_template('hobbies.html', hobbies=hobbies_data)
