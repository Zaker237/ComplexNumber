from setuptools import setup, find_packages
import cnumber

setup(
    name="cnumber",
    version=cnumber.__version__,
    description="A library to handel operations with complex number",
    long_description="",
    license="MIT",
    author="Alex Mboutchouang",
    author_email="mboutchouangalex@gmail.com",
    url="https://github.com/Zaker237/ComplexNumber",
    packages=find_packages(exclude=("tests",))
)
