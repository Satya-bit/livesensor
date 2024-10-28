from setuptools import find_packages, setup
from typing import List  # Import List from typing

def get_requirements() -> List[str]:  # Use List instead of list[str]
    requirement_list:List[str]=[]
    return requirement_list

setup(
    name='sensor',
    version="0.0.1",
    author="Satya-bit",
    author_email="satya.s@ahduni.edu.in",
    packages=find_packages(),
    install_requires=get_requirements()
)
