# Deploy Django to Vercel

## 1) Push the project
Push your latest code (including `api/index.py` and `vercel.json`) to GitHub.

## 2) Import into Vercel
1. Open Vercel dashboard.
2. Click **Add New...** -> **Project**.
3. Import this repository.
4. Keep the default framework as **Other**.

## 3) Configure Environment Variables
In Vercel project settings, add:

- `SECRET_KEY`
- `DEBUG` = `False`
- `DATABASE_URL` = your hosted PostgreSQL connection string
- `ALLOWED_HOSTS` = `.vercel.app,your-domain.com`
- `CSRF_TRUSTED_ORIGINS` = `https://your-project-name.vercel.app,https://your-domain.com`

## 4) Deploy
Trigger deployment from Vercel.

## 5) Run migrations
After deployment, run:

```bash
python manage.py migrate
```

## 6) Optional: create admin user

```bash
python manage.py createsuperuser
```

## Notes
- SQLite is not suitable for production on Vercel serverless.
- Use PostgreSQL in production.
- Static assets are collected during build via `vercel.json`.
