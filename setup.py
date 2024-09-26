from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A simple package to perform basic proteomic analysis in Python'

with open('Proteomagic/README.md', 'r') as file:
    LONG_DESCRIPTION = file.read()

# Setting up
setup(
    name='proteomagic',
    version=VERSION,
    author='Andrew Garven',
    author_email='15ajg6@queensu.ca',
    description=DESCRIPTION,
    package_dir={'': 'proteomagic'},
    packages=find_packages(where='proteomagic'),
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(where='proteomagic'),
    install_requires=['pandas==2.2.1'],
    keywords=['python', 'proteomics', 'bioinformatics', 'mass spectrometry', 'data analysis'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Scientists/Bioinformaticians",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
