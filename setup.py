from setuptools import setup, find_packages

setup(
    name="trackgen",
    version="0.1.0",
    packages=find_packages(),

    install_requires=[
        "requests",
        "colorama",
        "prompt_toolkit"
    ],

    entry_points={
        "console_scripts": [
            "trackgen=CLI_trackGenerator.main:main",
        ],
    },

    author="Your Name",
    description="CLI music discovery tool using MusicBrainz API",
    python_requires=">=3.8",
)
