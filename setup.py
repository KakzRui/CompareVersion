import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='CompareVersion',
    version='0.1',
    author='Manoj',
    author_email='manoj.chary@gmail.com',
    description='Comparing two version',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KakzRui/CompareVersion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)