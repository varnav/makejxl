import setuptools
import os
import shutil
import makejxl

if not os.path.exists('makejxl'):
    os.mkdir('makejxl')
shutil.copyfile('makejxl.py', 'makejxl/__init__.py')

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    'click>=7.1.2'
]

setuptools.setup(
    name="makejxl",
    version=makejxl.__version__,
    author="Evgeny Varnavskiy",
    author_email="varnavruz@gmail.com",
    description="This tool will bulk encode image files in given directory to JPEG-XL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/varnav/makejxl",
    keywords=["jpeg", "jpeg-xl", "transcoder"],
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Utilities",
        "Topic :: Multimedia :: Graphics",
        "Environment :: Console",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "makejxl = makejxl:main",
        ]
    }
)
