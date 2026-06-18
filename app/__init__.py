import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

pages = [
    {
        "name": "Home",
        "url": "/"
    },
    {
        "name": "Hobbies",
        "url": "/hobbies"
    }
]


@app.route("/")
def index():

    work_experiences = [
        {
            "role": "Software Engineering Intern",
            "company": "Irish Life",
            "description": "Worked with C#, SQL, Agile Scrum teams and enterprise applications."
        },
        {
            "role": "IT Operations Intern",
            "company": "Equinix",
            "description": "Supported data centre operations, monitoring and infrastructure processes."
        },
        {
            "role": "Computer Science Tutor",
            "company": "TU Dublin",
            "description": "Provided programming and networking support to university students."
        }
    ]

    education = [
        {
            "course": "BSc Computing and IT",
            "institution": "Technological University Dublin",
            "year": "2022 - 2026"
        }
    ]

    hobbies = [
        "Gym",
        "Travel",
        "Software Development",
        "Running"
    ]

    return render_template(
        "index.html",
        title="Jordan Aniuzu",
        url=os.getenv("URL"),
        pages=pages,
        work_experiences=work_experiences,
        education=education,
        hobbies=hobbies
    )


@app.route("/hobbies")
def hobbies():

    hobbies_list = [
        {
            "name": "Gym",
            "image": "gym.jpeg"
        },
        {
            "name": "Travel",
            "image": "travel.jpeg"
        },
        {
            "name": "Running",
            "image": "running.jpeg"
        },
        {
            "name": "Software Development",
            "image": "SDE.jpeg"
        }
    ]

    return render_template(
        "hobbies.html",
        title="My Hobbies",
        pages=pages,
        hobbies=hobbies_list
    )