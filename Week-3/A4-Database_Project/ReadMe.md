# Create a venv instead
python3 -m venv .venv

# Activate it (this WILL work)
source .venv/bin/activate

# Now install
pip install SQLAlchemy
pip install python-dotenv
pip install alembic

pip freeze > requirements.txt