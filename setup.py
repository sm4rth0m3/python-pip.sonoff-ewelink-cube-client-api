"""Setup file for installing and configuring the sonoff-ewelink-cube-client-api package."""
from setuptools import setup, find_packages

VERSION = "0.0.2"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sonoff-ewelink-cube-client-api",
    version=VERSION,
    author="sipimokus",
    author_email="sipimokus@gmail.com",
    description="SONOFF eWelink CUBE API communication library (unofficial)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sm4rth0m3/python-pip.sonoff-ewelink-cube-client-api",
    project_urls={
        "Bug Tracker": "https://github.com/sm4rth0m3/python-pip.sonoff-ewelink-cube-client-api/issues",
        "Documentation": "https://github.com/sm4rth0m3/python-pip.sonoff-ewelink-cube-client-api",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        # Need cross OS and python tests
        # "Programming Language :: Python :: 3.6",
        # "Programming Language :: Python :: 3.7",
        # "Programming Language :: Python :: 3.8",
        # "Programming Language :: Python :: 3.9",
        # "Programming Language :: Python :: 3.10",
        # "Programming Language :: Python :: 3.11",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
        "Topic :: Utilities",
    ],
    keywords="sonoff ewelink cube api openapi ihost nspanel library asyncio",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=[
        "aiohttp>=3.0.0",
        "asyncio>=3.4.3",
        "setuptools",
    ],
)
