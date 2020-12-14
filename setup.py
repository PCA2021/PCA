from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'streamlit==0.65.2']

setup(
    name='personality-chat-assistant',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Streamlit App'
)
