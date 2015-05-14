"""Setup for ratingvideo XBlock. v1.50"""

import os
from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='ratingvideo-xblock',
    version='1.2',
    description='XBlock wich shows a rating method for video',
    packages=[
        'ratingvideo',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': 'ratingvideo = ratingvideo:ratingXBlock'
    },
    package_data=package_data("ratingvideo", "static"),
)