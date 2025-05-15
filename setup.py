from setuptools import setup
from setuptools.extension import Extension

setup(
    name='opencv-python-gstreamer',
    version='4.12.0.dev0',
    description='OpenCV with GStreamer for Jetson',
    packages=['cv2'],
    package_dir={'cv2': 'cv2'},
)

