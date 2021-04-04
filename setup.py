from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='grand-piano',
    url='https://github.com/D-T-666/grand-piano',
    author='Dimitri Tabatadze',
    author_email='tabatadzedima20@gmail.com',
    # Needed to actually package something
    packages=['grand-piano', 'grand-piano.barchart'],
    # Needed for dependencies
    install_requires=['rich'],
    # *strongly* suggested for sharing
    version='0.0.1',
    # The license can be anything you like
    license='MIT',
    description='Library for plotting stuff to the terminal',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)