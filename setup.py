"""
setup.py - Project metadata for suleimanAlQusaimi Python Course

This file documents the course project metadata.
The course materials consist of standalone Python scripts (no installable package).
"""

from setuptools import setup

setup(
    name="suleiman-alqusaimi-python-course",
    version="1.0.0",
    author="Mahmoud Shaabo",
    author_email="",
    description=(
        "Beginner Python exercises and mini-apps for blind learners, "
        "Level 1 with Suleiman Al-Qusaimi. Standard library only; lectures "
        "2–10 with Arabic instruction and accessibility-focused documentation."
    ),
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mahmoudshaabo1984/suleimanAlQusaimiPythonCourse",
    project_urls={
        "Bug Tracker": (
            "https://github.com/mahmoudshaabo1984/"
            "suleimanAlQusaimiPythonCourse/issues"
        ),
        "Source Code": (
            "https://github.com/mahmoudshaabo1984/"
            "suleimanAlQusaimiPythonCourse"
        ),
    },
    packages=[],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "flake8>=6.0.0",
            "pylint>=3.0.0",
            "autopep8>=2.0.0",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: Arabic",
        "Natural Language :: English",
    ],
    keywords=[
        "python",
        "course",
        "education",
        "accessibility",
        "blind",
        "visually impaired",
        "arabic",
        "beginner",
    ],
)
