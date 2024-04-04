if [ -f requirements.txt ]; then
  python -m pip install --user -r requirements.txt
fi

virtualenv -p /usr/bin/pypy3 ~/pypy-env
~/pypy-env/bin/pypy3 -m pip install ipython
