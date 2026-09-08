from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    profile = {
        "name": "Liezel A. Ybañez",
        "short_name": "Liezel",
        "role": "Project Manager | Frontend Developer",
        "location": "Cebu City, Philippines",
        "email": "liezellalay@gmail.com",
        "school_email": "liezel.ybanez@cit.edu",
        "phone": "+63 993 905 7350",
        "linkedin": "https://www.linkedin.com/in/liezel-a-yba%C3%B1ez-b1571a3b0",
        "summary": "Detail-oriented Information Technology student with a strong foundation in full-stack development and agile methodologies. Proven track record in leadership, document control, and student governance, having authored and co-authored legislative frameworks to support university initiatives. Skilled in coordinating complex team environments as a Scrum Master and leading community-focused committees. Passionate about software testing, quality assurance, and delivering robust, user-centric technology solutions.",
    }

    skills = {
        "Programming": ["Python", "JavaScript", "Java", "SQL"],
        "Frameworks": ["React", "Node.js", "Django", "Spring Boot"],
        "Tools & Platforms": ["Git", "Docker", "AWS", "Figma"],
        "Soft Skills": ["Leadership", "Communication", "Problem-Solving"],
        "Languages": ["English (Fluent)", "Filipino (Native)"],
    }

    education = [
        {"degree": "Bachelor of Science in Information Technology", "school": "Cebu Institute of Technology University", "years": "2023 – 2027", "location": "Cebu City, Philippines"},
        {"degree": "Secondary Education: Senior High School", "school": "Cebu Institute of Technology University", "years": "2021 – 2023", "location": "Cebu City, Philippines"},
        {"degree": "Secondary Education: Junior High School", "school": "Cebu Institute of Technology University", "years": "2017 – 2021", "location": "Cebu City, Philippines"},
        {"degree": "Elementary Education", "school": "San Nicolas Elementary School", "years": "2011 – 2017", "location": "Cebu City, Philippines"},
    ]

    projects = [
        {
            "name": "UniGear Tracker",
            "category": "Project management & QA",
            "description": "Served as Scrum Master and Documentation Lead, guiding sprint iterations, test plans, acceptance criteria, and final regression reporting.",
            "details": "UniGear Tracker helps organize equipment requests and borrowing workflows for a university setting. I kept delivery focused through clear acceptance criteria, QA checkpoints, and sprint documentation.",
            "stack": ["Scrum", "QA", "Documentation"],
        },
        {
            "name": "StuNotes",
            "category": "Academic collaboration tool",
            "description": "Led documentation and agile pipeline management, formulating software requirements and coordinating development tracking through Scrum.",
            "details": "StuNotes is an academic collaboration concept that brings shared notes and coordinated study work into one focused experience. I mapped requirements and kept the team aligned through an agile workflow.",
            "stack": ["Scrum", "SRS", "Collaboration"],
        },
        {
            "name": "DEPTH",
            "category": "ServiceNow application",
            "description": "Automated enrollment adjustment and tuition re-computation workflows with database schemas, approval flows, and intuitive student portals.",
            "details": "DEPTH streamlines enrollment adjustments by connecting approval flows, tuition re-computation, and student-facing forms in a single ServiceNow application.",
            "stack": ["ServiceNow", "Workflows", "Database design"],
        },
        {
            "name": "LaunchUp Capstone Project",
            "category": "System architecture & agile delivery",
            "description": "Orchestrated database schema design, system architecture, backlog grooming, SRS documentation, and sprint reporting.",
            "details": "LaunchUp is a capstone delivery project where I supported the work from system planning through sprint reporting, with a particular focus on traceable requirements and a practical architecture.",
            "stack": ["Architecture", "Backlog planning", "SRS"],
        },
        {
            "name": "Clawendar",
            "category": "Frontend scheduling application",
            "description": "Built an interactive scheduling app with modern UI components, structured test cases, responsive event rendering, and state persistence.",
            "details": "Clawendar is a responsive scheduling experience designed for quick event planning. It pairs persistent client-side state with structured test cases and a clear, easy-to-scan interface.",
            "stack": ["JavaScript", "Responsive UI", "Testing"],
        },
    ]

    involvement = [
        {"role": "Head of Committee on Community Engagement", "organization": "Wildcats Esports League", "period": "May 2026 – Present", "description": "Spearhead strategic community initiatives and outreach programs for an inclusive campus esports ecosystem."},
        {"role": "Auditor", "organization": "CIT University Computer Students' Society", "period": "June 2026 – Present", "description": "Manage internal financial reviews, audit expenditures, and maintain fiscal transparency across events."},
        {"role": "Assistant Director, Internal Coordination Department", "organization": "AWS Cloud", "period": "2026 – Present", "description": "Oversee operational alignment and communication across cloud-focused student projects."},
        {"role": "Project Management Officer, Operations Department", "organization": "Google Developer Group on Campus, CIT-U GDGoC Administration", "period": "A.Y. 2026 – 2027 · Present", "description": "Coordinate project planning, operational workflows, and delivery support for campus developer community initiatives."},
        {"role": "Head of Committee on Community and Social Responsibility", "organization": "CIT University Computer Students' Society", "period": "July 2025 – June 2026", "description": "Directed CSR initiatives, committee coordination, and community-focused student development plans."},
        {"role": "Resource Manager, Commission on Social Responsibility", "organization": "CIT University Supreme Student Government", "period": "June 2025 – June 2026", "description": "Controlled asset distribution, organized supply logistics, and optimized resources for university projects."},
        {"role": "IT Representative, Legislative Department", "organization": "CIT University Supreme Student Government", "period": "A.Y. 2026 – 2027 · Present", "description": "Represent the Information Technology student body within the legislative department and support initiatives for student welfare and technical development."},
        {"role": "Speaker Pro Tempore", "organization": "CIT University Supreme Student Government, Legislative Department", "period": "A.Y. 2026 – 2027 · Present", "description": "Support legislative session leadership, maintain procedural order, and help facilitate productive deliberations within the student government."},
        {"role": "IT Representative & Legislator", "organization": "CIT University Supreme Student Government", "period": "June 2024 – 2025", "description": "Authored and co-authored 8+ legislative resolutions focused on student welfare, infrastructure, and IT certification subsidies."},
    ]

    return render_template("index.html", profile=profile, skills=skills, education=education, projects=projects, involvement=involvement)


if __name__ == "__main__":
    app.run()
