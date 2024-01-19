import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fkscore",
    version="2.0.1",

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
        # Development Status
        'Development Status :: 5 - Production/Stable',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Environments
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: OpenStack',
        'Environment :: Web Environment',

        # Frameworks
        'Framework :: IPython',
        'Framework :: Jupyter',

        # Audience
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',

        # Language
        'Natural Language :: English',

        # OS
        'Operating System :: OS Independent',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',

        # Python Version
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',

        # Topics
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules',

    ],

    keywords=["nlp", 'linguistics', 'nltk', 'text processing', 'flesch-kincaid readability'],
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
)
