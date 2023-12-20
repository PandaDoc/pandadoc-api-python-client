"""
    PandaDoc Public API

    PandaDoc Public API documentation  # noqa: E501

    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301
from pathlib import Path
full_description = (Path(__file__).parent/"README.md").read_text()
description = ""
from_index = full_description.find("### Documentation for API Endpoints")
to_index = full_description.find("## License")
if from_index and to_index:
    description = full_description[0:from_index] + full_description[to_index::]

NAME = "pandadoc-python-client"
VERSION = "6.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="PandaDoc Public API",
    author="PandaDoc",
    author_email="",
    url="https://github.com/PandaDoc/pandadoc-api-python-client",
    keywords=["OpenAPI", "PandaDoc Public API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests", "examples"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type='text/markdown',
    long_description=f"""\
    {description}
    """  # noqa: E501
)
