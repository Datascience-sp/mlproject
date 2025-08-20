from setuptools import find_packages, setup
from typing import List


#this function reads the requirements from the requirements.txt file
HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements if req.strip() != HYPEN_E_DOT]
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Snehasis Pradhan',
    author_email = 'pradhan.snehasis@gmail.com',
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')
)
