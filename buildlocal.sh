git add -A
git commit -m "Update"
git push
python3.9 setup.py sdist
pip3.9 install ./dist/alpezacassette-0.1.6.tar.gz