#Si fue creado desde Linux Mac o Gitbash
#source .venv/bin/activate
#Si fue creado desde Windows
#source .venv/Scripts/activate

python -m venv .venv
source .venv/bin/activate #Usa la máquina virtual de Ubuntu(Linux)
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
API_URL=https://rtocast-web.up.railway.app reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate
