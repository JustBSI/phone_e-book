import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name='phone_e-book',
    version='1.0',
    author="Sergey Bobrov",
    author_email="just.b.sergey@gmail.com",
    description="Console application, which allows to interact with phone book.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JustBSI/phone_e-book",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    py_modules=[
        'main',
        'cli',
        'funcs',
        'config'
    ],
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        phone_e-book=main:main
    ''',
)
