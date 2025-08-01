from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements from a given file.
    '''
    HYPEN_E_DOT = '-e .'
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # strip removes \n and extra spaces
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='bala',
    author_email='balavenkateswarlu0204@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
