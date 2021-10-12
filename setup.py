from setuptools import setup, find_packages

setup(
    name="VeronikaPotseichukSerializer",
    version="1.0.0",
    description="Lib for serialize and deserialize objects",
    author="Veronika Potseichuk",
    url="https://github.com/VeronikaPotseichuk/Lab2",
    setup_requires=["wheel"],
    install_requires=["wheel"],
    packages= find_packages(),
    entry_points={"console_scripts": "cu=console_interface:main"},
)