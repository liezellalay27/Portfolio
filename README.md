# Portfolio Website (Flask)

A clean, modern, responsive personal portfolio starter built with Flask + Bootstrap.

## 1) Terminal setup commands

```bash
# from the repository root
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Run locally:

```bash
flask --app app run --debug
```

Open: `http://127.0.0.1:5000`

---

## 2) Folder structure

```text
Portfolio/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   └── index.html
└── static/
    ├── css/
    │   └── styles.css
    └── resume.pdf   # add your actual resume file here
```

---

## 3) Starter code overview

- `app.py`: Flask app with the `/` route that renders your portfolio page.
- `templates/base.html`: Base template with Bootstrap CDN and stylesheet link.
- `templates/index.html`: Hero, About Me, Tech Stack, Projects Gallery, and Contact sections.
- `static/css/styles.css`: Custom styling for a polished UI.

## Customize placeholders

- Update GitHub/LinkedIn URLs in `/home/runner/work/Portfolio/Portfolio/templates/index.html`.
- Add your resume as `/home/runner/work/Portfolio/Portfolio/static/resume.pdf`.
- Edit project descriptions in `/home/runner/work/Portfolio/Portfolio/app.py`.
