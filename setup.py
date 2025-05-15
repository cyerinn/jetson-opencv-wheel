from setuptools import setup
from setuptools.dist import Distribution
import os

class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True

setup(
    name='opencv-python-gstreamer',
    version='4.12.0.dev0',
    packages=['cv2'],
    package_dir={'cv2': 'cv2'},
    package_data={'cv2': ['*.so']},
    include_package_data=True,
    zip_safe=False,
    distclass=BinaryDistribution,
)
