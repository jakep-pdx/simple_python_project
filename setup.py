import os
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

pkg_version = "0.0.0"
try:
    new_ver = os.environ["new_ver"]
    if new_ver:
        pkg_version = new_ver
    else:
        print("new_ver not found, using pkg_version default:", pkg_version)
except KeyError:
    print("new_ver not found, using pkg_version default:", pkg_version)

setup(
    name = "simple_py_proj",
    version = pkg_version,
    python_requires = ">=3.10",
    install_requires = "", #requirements,
    description = "simple test project",
    pakckages = find_packages(include=["simple_py_proj", "simple_py_proj.*"]),
    entry_points = {
        'console_scripts': ['do_every_thing=simple_py_proj.some_thing:main']
    }
)