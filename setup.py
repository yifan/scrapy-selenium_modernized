"""This module contains the packaging routine for the pybook package"""

from setuptools import setup, find_packages

def get_requirements(source):
    """Get the requirements from the given ``source``

    Parameters
    ----------
    source: stlarger
        The filename containing the requirements

    """
    with open(source) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    packages=find_packages(),
    install_requires=get_requirements('requirements/requirements.txt')
)


