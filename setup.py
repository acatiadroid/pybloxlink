from setuptools import setup
import re

version = ''
with open('./bloxlink/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setup(version=version)