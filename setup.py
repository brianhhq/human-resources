from setuptools import setup, find_packages

with open('README.MD', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='manage users on a server based on an "inventory" JSON file',
    long_description=readme,
    author='Brian Huang',
    author_email='bran_hhq@hotmail.com',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=[],
    entry_points={
        'console_scripts': 'hr=hr.cli:main',
    },
)
