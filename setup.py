from setuptools import setup
import re

version = ''
with open('bloxlink/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

DESCRIPTION = "An API wrapper for the Bloxlink API."

long_desc = ""
with open(".github/README.md") as f:
    long_desc = f.read()

setup(
    name="pybloxlink",
    version=version,
    author="acatiadroid",
    license="The MIT License (MIT)",
    author_email="<acatia@mail.com>",
    url="https://github.com/acatiadroid/pybloxlink",
    project_urls={
        "Issues": "https://github.com/acatiadroid/pybloxlink/issues"
    },
    description=DESCRIPTION,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    install_requires=["aiohttp"],
    keywords=["python", "bloxlink", "api wrapper"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)