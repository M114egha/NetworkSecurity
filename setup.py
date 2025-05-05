
from setuptools import setup, find_packages
from typing import List


def get_requirements()->List[str]:
    """
    This function returns a list of requirements for the project.
    """
    requirement_lst:List[str] = [] # create an empty list to store requirements
    try:
        with open('requirements.txt') as file:
            lines=file.readlines()  # read all lines from the file
            for line in lines:
                requirement=line.strip()# remove leading and trailing whitespace
                if requirement and requirement != "-e .":
                    # if the line is not empty and not equal to "-e ."
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please make sure it exists.")

    return requirement_lst


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Meghana Bhairi",
    author_email="meghabhairi114@gmail.com",
    packages=find_packages(),  # Automatically find and include all packages in the project
    install_requires=get_requirements(),  # Install the required packages from requirements.txt
)