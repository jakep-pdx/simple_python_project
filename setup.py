""" packaging config file """
import os
from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

PKG_VERSION = "0.0.0"
try:
    new_ver = os.environ["new_ver"]
    if new_ver:
        PKG_VERSION = new_ver
    else:
        print("new_ver not found, using PKG_VERSION default:", PKG_VERSION)
except KeyError:
    print("new_ver not found, using PKG_VERSION default:", PKG_VERSION)

setup(
    name = "simple_py_proj",
    version = PKG_VERSION,
    python_requires = ">=3.10",
    install_requires = "", #requirements.txt,
    description = "simple test project",
    pakckages = find_packages(include=["simple_py_proj", "simple_py_proj.*"]),
    entry_points = {
        'console_scripts': ['do_every_thing=simple_py_proj.some_thing:main']
    }
)
