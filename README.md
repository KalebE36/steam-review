# Install Requirements (manual)
1) Create a python virtual environment in the root directory (`steam-review/`)
```
python -m venv .venv
```
2. Activate the virtual environment 
```
source .venv/bin/activate
```
3. Install requirements
```
pip install -r requirements.txt
```

# Install Requirements (script)
### UNIX (Mac or Linux)
```
cd scripts/
chmod +x unix_env.sh
./unix_env.sh
```

### Windows
```
Double click on "dos_env.bat"
```


MAKE SURE YOU HAVE THE RIGHT DATASETS DOWNLOADED. THE IMPORTANT ONES ARE weighted_score_above_08.csv and processed_text.csv