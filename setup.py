import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="appscanner",
    version="1.0.1",
    author="Thijs van Ede",
    author_email="t.s.vanede@utwente.nl",
    description="AppScanner: Automatic Fingerprinting of Smartphone Apps from "
                "Encrypted Network Traffic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Thijsvanede/AppScanner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
