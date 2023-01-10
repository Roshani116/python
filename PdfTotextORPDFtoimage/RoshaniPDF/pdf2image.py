import setuptools

setuptools.setup(
    name = "RoshaniPDF",
    version=1.0,
    long_description = "",
    # find_package method discover the project and find packages if any.
    packages=setuptools.find_packages(["tests", "data"])
)