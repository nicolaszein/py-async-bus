import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-async-bus",
    version="0.0.1",
    author="Nícolas Zein",
    author_email="niczein@gmail.com",
    description="A simple async event bus in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nicolaszein/py-async-bus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
