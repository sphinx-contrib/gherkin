from setuptools import find_namespace_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sphinxcontrib-gherkin",
    version="1.0.0",
    author="Martin Hasoň",
    author_email="martin.hason@gmail.com",
    description="Sphinx parser for Gherkin BDD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sphinx-contrib/kroki",
    packages=find_namespace_packages(include=["sphinxcontrib.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "sphinx",
        "behave",
    ],
    extras_require={
        "code": ["black", "flake8", "mypy", "isort"],
        "test": [
            "coverage",
            "pytest",
            "pytest-cov",
        ],
        "extra": [
        ],
    },
)
