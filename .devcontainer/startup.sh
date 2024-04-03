if [ -f requirements.txt ]; then
  pip install --user -r requirements.txt
fi


/usr/bin/pypy3 -m venv ~/.pypyenv
~/.pypyenv/bin/python -m pip install ipython
