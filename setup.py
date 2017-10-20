"""Our setup.py for future users to know what/who we are."""


from setuptools import setup

setup(
    name="trigram",
    description="A Python implementation of a trigram parser.",
    version=0.1,
    author="Zach Taylor & Michael Shinners",
    author_email="zacharymtaylor3@gmail.com & michaelshinners@gmail.com",
    license='MIT',
    py_modules=['trigram'],
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov']}
)
