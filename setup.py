from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Shubham Bawiskar',
    author_email='shubhambawiskar10@gmail.com',
    install_requires=['openai', 'langchain', 'pyPDF2', 'streamlit', 'python-dotenv'],
    packages=find_packages()
)