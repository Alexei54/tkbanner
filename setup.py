from setuptools import setup, find_packages

setup(
    name="tkbanner",
    version="0.1.0",
    author="Alexei54",
    description="Animated video banner for tkinter",
    long_description=open("pyproject.toml", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "Pillow",
    ],
    python_requires=">=3.8",
)
