if [ -f requirements.txt ]; then
  python -m pip install --user -r requirements.txt
fi

virtualenv ~/pypy-env
~/pypy-env/bin/pypy3 -m pip install ipython
