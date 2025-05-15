from setuptools import setup
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True

setup(
    name='opencv_python_gstreamer',
    version='4.12.0.dev0',
    description='Custom OpenCV build with GStreamer for Jetson',
    packages=['cv2'],
    package_dir={'cv2': 'cv2'},
    package_data={'cv2': ['cv2.cpython-310-aarch64-linux-gnu.so']},
    distclass=BinaryDistribution,
    zip_safe=False,
)
