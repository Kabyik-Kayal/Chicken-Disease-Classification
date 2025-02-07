import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "CHICKEN-DISEASE-CLASSIFICATION"
AUTHOR_USER_NAME = 'Kabyik-Kayal'
SRC_REPO_NAME = f"{AUTHOR_USER_NAME}/{REPO_NAME}"
AUTHOR_EMAIL = "scientistk001@gmail.com"

setuptools.setup(
    name= SRC_REPO_NAME,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "Chicken Disease Classification",
    long_description= long_description,
    long_description_content_type= "text/markdown",
    url=f"https://github.com/{SRC_REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{SRC_REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)