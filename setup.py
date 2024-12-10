from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:

    requirement_lst = []
    try:
        with open('requirements.txt', 'r') as file:
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("reuirements.txt file not Found")

    return requirement_lst


setup(
    name="NetworkSecurity",
    version='0.0.1',
    author='Sai',
    author_email='saiseven@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements()
)