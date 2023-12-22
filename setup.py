# snake_me_please/setup.py
from setuptools import setup, find_packages

setup(
    name="snake_me_please",
    description="Snake Me Please is a Python package and command-line tool designed to convert user-defined variable names to snake_case in Python files while excluding imported variables and keywords from Python libraries.",
    version="0.2",
    author="Aditya Jetely",
    author_email="ajetely@gmail.com",
    license="public",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snake-me-please = snake_me_please.converter:main",
        ],
    },
)
