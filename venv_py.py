sudo apt-get -y update
sudo apt-get -y install python3-virtualenv
sudo apt -y install python3.10-venv
virtualenv --python=/usr/bin/python3.10 .venv
python3.10 -m venv .venv
source .venv/bin/activate
pip3 install Django
