from setuptools import setup, find_packages

setup(
    name="tiktokexe",
    version="0.1.0",
    author="TTDOTEXE",
    author_email="TIKTOKDOTEXE@TIKTOKEXE.COM",
    license='MIT',
    description="ASCII GIF and Solana Token Project",
    long_description="TIKTOKEXE: A project combining ASCII art animations and Solana blockchain integration.",
    url="https://github.com/ttdotexe/tiktokexe",
    project_urls={
        'Source': 'https://github.com/ttdotexe/tiktokexe',
        'Tracker': 'https://github.com/ttdotexe/tiktokexe/issues'
    },
    packages=find_packages(where="src"),  # Include only the src directory
    package_dir={"": "src"},  # Root is the "src" folder
    py_modules=['fetch_wallet'],  # Add fetch_wallet.py as a standalone module
    include_package_data=True,
    install_requires=[
        'Pillow',
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='ascii art gif solana blockchain',
    entry_points={
        "console_scripts": [
            'tiktokexe=src.TIKTOKEXE:main',
            'fetch-wallet=fetch_wallet:main'
        ]
    }
)

