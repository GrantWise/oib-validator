from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="oib-validator",
    version="0.1.0",
    author="OIB Validator Contributors",
    author_email="your.email@example.com",  # TODO: Update with your email before publishing
    description="A validator for Croatian Personal Identification Numbers (OIB)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GrantWise/oib-validator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "oib-validator=oib_validator.validator:main",
        ],
    },
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "mypy>=0.930",
            "flake8>=4.0.0",
            "tox>=3.24.0",
            "twine>=4.0.0",
        ],
    },
)
