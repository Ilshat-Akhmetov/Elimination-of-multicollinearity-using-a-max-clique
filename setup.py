from setuptools import setup

setup(
    name='multicollinearityElimination',
    version='0.1',
    description='Elimination multicollinearity in data using Bron-Kerbosch algorythm',
    url='https://github.com/Ilshat-Akhmetov/Elimination-of-multicollinearity-using-a-max-clique',
    author='Akhmetov Ilshat',
    author_email='ilshat.achmetov@gmail.com',
    license='MIT',
    packages=['multicollinearityElimination'],
    classifiers=[],
    keywords='multicollinearity elimination',
    install_requires=['pandas', 'numpy', 'scipy', 'graphviz '],
)