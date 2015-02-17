from setuptools import setup

setup(name='cs136-bunny',
      version ='1.0',
      description='An automated I/O testing tool for CS 136',
      url='https://github.com/Gibstick/cs136-bunny',
      author='Charlie (Gibstick) Wang',
      author_email='charlie.wang@uwaterloo.ca',
      license='MIT',
      packages=['bunny'],
      install_requires = ['envoy'],
      entry_points= {
        'console_scripts': ['bunny = bunny:main'],
      },
    )