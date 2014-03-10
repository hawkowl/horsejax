from setuptools import setup

setup(
    name="horsejax",
    version="0.1",
    description="Secure password generator via not so secure JSON.",
    long_description=(
        "Like http://correcthorsebatterystaple.net/ except it is a HTTP API"
        " which is logging your passwords and sending them all to the NSA."
    ),
    author="HawkOwl",
    author_email="hawkowl@atleastfornow.net",
    maintainer="HawkOwl",
    maintainer_email="hawkowl@atleastfornow.net",
    url="https://github.com/hawkowl/horsejax/",
    packages=["horsejax"],
    package_data=dict(
        horsejax=["*.json"],
    ),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
)