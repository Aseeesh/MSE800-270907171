
# Create a venv instead
python3 -m venv venv

# Activate it (this WILL work)
source venv/bin/activate

# Now install
pip install ucimlrepo
pip freeze > requirements.txt

# Check - it will work!
which python  # → ./venv/bin/python ✅
which pip     # → ./venv/bin/pip ✅