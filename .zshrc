alias build_dc='docker build -t minisedric . '
alias run_dc='docker run -d --name minisedric -p 8000:8000 minisedric'
alias run_ptr='poetry run uvicorn main:app --reload --app-dir src '