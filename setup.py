from setuptools import setup, find_packages

setup(
    name="india_housing_datasets",
    version="0.1.0",
    author="Vishal Baghel",
    author_email="your_email@example.com",
    description="A collection of clean Indian city housing datasets (Ahmedabad, Gurugram, Mumbai).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vishalbaghel/india_housing_datasets",  # change later if you upload to GitHub
    packages=find_packages(),
    include_package_data=True,
    package_data={"india_housing_datasets": ["data/*.csv"]},
    install_requires=[
        "pandas>=1.3.0",
    ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
