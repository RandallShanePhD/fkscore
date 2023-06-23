import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fkscore",
    version="1.1.7",

    description="Flesch Kincaid readability scoring algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RandallShanePhD/fkscore",

    # Author Info
    author="Randall Shane PhD <Randall@NumbersAndTech.com>",
    author_email="Randall@NumbersAndTech.com",


    # License
    license='MIT',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Indexing',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Operating System :: OS Independent",
    ],

    keywords=["nlp", 'linguistics', 'nltk', 'text processing'],
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
)
