from setuptools import setup, find_packages

setup(
    name="uber-price-predict",
    version="1.0.0",
    description="ML web app that predicts rideshare prices",
    author="Your Name",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "Flask>=3.0.0",
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "gunicorn>=21.2.0",
    ],
)
