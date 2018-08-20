import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pataroomie",
    version="0.0.1",
    author="Pataroomie",
    author_email="pataroomie@roomie.me",
    description="Roommate Searching App.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PataRoomie/PataRoomie-api",
    packages=setuptools.find_packages(),
    install_requires=[
        'Django >= 2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3", "Framework :: Django :: 2"
    ],
)
