from setuptools import setup, find_packages

setup(
    name="Sourcetree Assets Plugin",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Pillow"
    ],
    entry_points={
        "console_scripts": [
            "sourcetree-assets-plugin = src.main:main"
        ]
    },
    include_package_data=True,
    package_data={
        "": ["assets/*"]
    }
)
