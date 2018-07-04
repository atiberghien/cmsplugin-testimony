from setuptools import setup, find_packages

setup(name='cmsplugin_testimony',
      version='0.1',
      description='CMS Plugin for testimony',
      url='https://github.com/atiberghien/cmsplugin_testimony',
      author='Alban Tiberghien',
      author_email='alban.tiberghien@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
           'Django<2.0',
      ],
      zip_safe=False)