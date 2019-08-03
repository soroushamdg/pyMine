import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymine",
    version="1.0.3",
    author="Soroush M Pour",
    author_email="soroushmpour@gmail.com",
    description="pyMine is open-source module for Python, helps you to create or play old classic Windows Mine game in Python Terminal enviorment.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soroushmpour/pyMine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
)
