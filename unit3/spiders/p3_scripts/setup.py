from setuptools import setup, find_packages


setup(
    name='p3_scripts',
    version='1.0',
    packages=find_packages(),
    scripts=[
        'bin/check_jobs.py',
    ],
    entry_points={
        'scrapy': ['settings = p3_scripts.settings'],
    },
)
