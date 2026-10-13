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
└── public/
    └── static/
        ├── css/styles.css
        └── images/
            ├── liezel-execom.jpg
            ├── liezel-formal-cutout.png
            └── liezel-formal.jpg
```

---

## 3) Starter code overview

- `app.py`: Flask app with the `/` route that renders your portfolio page.
- `templates/base.html`: Base template with Bootstrap CDN and stylesheet link.
- `templates/index.html`: Hero, About Me, Tech Stack, Projects Gallery, and Contact sections.
- `public/static/`: CSS and image assets served by Vercel's CDN.

## Customize the portfolio

- Update the GitHub URL and contact details in `templates/index.html`.
- Add a resume link when `public/static/resume.pdf` is available.
- Edit project descriptions in `app.py`.

## Deploy to Vercel

This Flask app is detected by Vercel from `app.py` and `requirements.txt`. Static files live under `public/static/`, so Vercel serves them from its CDN while the configured Flask static folder keeps local development working.

For a preview deployment, install the Vercel CLI and run:

```bash
vercel
```

After reviewing the preview, publish to production with:

```bash
vercel --prod
```

You can also import the Git repository at [vercel.com/new](https://vercel.com/new); Vercel will deploy on pushes to the configured production branch.
