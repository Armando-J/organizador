from setuptools import setup

with open ( "README.md" , "r" ) as fh :
    long_description = fh . read ()

setup(
    name="organizador",
    version="0.1.3",
    description="Organiza archivos en carpetas teniendo como referencia las similitudes en sus nombres.",
    long_description = long_description ,
    long_description_content_type = "text/markdown" ,
    author="Armando J",
    url="https://github.com/Armando-J/organizador",
    packages=['organizador',],
    )