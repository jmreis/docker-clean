import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="docker-clean",
    version="0.0.1",
    author="Jair Reis",
    author_email="jmsreis@protonmail.com",
    description="Script para limpar imagens, container e volumes docker.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmreis/docker-clean",
    project_urls={
        "Bug Tracker": "https://github.com/jmreis/docker-clean/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
