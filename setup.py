import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='template',
    version='0.0.3',
    author='IJAS',
    author_email='ijas.ahammed@scrapehero.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/firedrak-e/spider',
    license='MIT',
    packages=['spider'],
    install_requires=[],
)
