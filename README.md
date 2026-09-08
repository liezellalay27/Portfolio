# Portfolio Website (Flask)

A modern, responsive personal portfolio built with Flask + Bootstrap.

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

## Customize the portfolio

- Update the GitHub URL and contact details in `templates/index.html`.
- Add a resume link when `static/resume.pdf` is available.
- Edit project descriptions in `app.py`.
