#Si fue creado desde Linux Mac o Gitbash
#source .venv/bin/activate

#Si fue creado desde Windows
source .venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate
