#Desde Windows
#.\.venv\Scripts\activate
#Desde Linux Mac o Gitbash
#source .venv/bin/activate
source .venv/Scripts/activate

pip install --upgrade pip
#".\.venv\Scripts\python.exe" -m pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
API_URL=https://rtocast-web.up.railway.app reflex export --frontend-only
#reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip

#Para Windows
#.\.venv\Scripts\deactivate
#Para Linux, Mac o Git Bash
deactivate
