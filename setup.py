from setuptools import setup, find_packages

setup(
    name="trackgen",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "trackgen=CLI_trackGenerator.main:main",
        ],
    },
)
