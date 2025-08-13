from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    author="anouri",
    author_email="anouri@42.fr",
    description="A sample test package",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AhlemNG/ft_package",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license="MIT",
)
