"""Setup module."""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mini-civ",
    version="0.0.1",
    author="Placeholder",
    author_email="author@example.com",
    description="A primitive 4X strategy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TrickyFox371/MiniCiv",
    project_urls={
        "Bug Tracker": "https://github.com/TrickyFox371/MiniCiv/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "mini_civ"},
    package_data={"": ["res/*", "*.png"]},
    packages=setuptools.find_packages(where="mini_civ"),
    python_requires=">=3.6",
    install_requires="pygame",
    install_package_data=True
)
