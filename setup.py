from setuptools import setup, find_packages

setup(
    name="mac_text_to_image_app",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "PyQt5==5.15.6",
        "requests==2.26.0",
        "pyobjc-framework-Cocoa==8.2",
    ],
    entry_points={
        "console_scripts": [
            "mac_text_to_image=src.app:App().run",
        ],
    },
)
