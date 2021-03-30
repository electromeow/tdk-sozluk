import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tdk-sozluk",
    version="1.0.4",
    author="Berat Gökgöz",
    author_email="gokgoz.berat123@gmail.com",
    description="En iyi TDK sözlük arama kütüphanesi. Best TDK dict. search library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/electromeow/tdk-sozluk",
    project_urls={
        "Bug Tracker": "https://github.com/electromeow/tdk-sozluk/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.3",
)
