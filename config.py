import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRAT_KEY') or b'4\x13\x8e\x0fp\xa3\x9c"T\\\xa1\x16\x83\x8e\n\xc6'
