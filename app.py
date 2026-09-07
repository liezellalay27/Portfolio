from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    tech_stack = [
        "Python",
        "Django",
        "Java",
        "Spring Boot",
        "JavaScript",
        "Android Studio",
    ]

    projects = [
        {
            "name": "Snapfolio",
            "category": "App development",
            "description": "A mobile-focused portfolio and content experience with a clean social-style interface.",
        },
        {
            "name": "UniGear Tracker",
            "category": "University inventory & equipment borrowing system",
            "description": "A system for tracking equipment availability, requests, and borrowing workflows across campus.",
        },
        {
            "name": "Smart Campus Navigation System",
            "category": "Interactive indoor navigation capstone",
            "description": "A capstone project that helps students and staff navigate buildings with interactive mapping and directions.",
        },
        {
            "name": "DEPTH",
            "category": "Automated enrollment adjustment application",
            "description": "An application that streamlines enrollment adjustments and reduces manual processing overhead.",
        },
    ]

    return render_template("index.html", tech_stack=tech_stack, projects=projects)


if __name__ == "__main__":
    app.run()
