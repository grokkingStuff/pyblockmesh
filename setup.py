import setuptools


setuptools.setup(name='pyblockMesh',
                 version='0.0.1',
                 description='Python wrapper around blockMeshDict creation',
                 long_description=open('README.md').read().strip(),
                 author='Vishakh Kumar',
                 author_email='grokkingStuff@gmail.com',
                 url='https://github.com/grokkingStuff/pyblockmesh',
                 py_modules=['pyblockmesh'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 python_requires='>=3',
                 keywords='blockmesh blockmeshdict openfoam pyfoam',
                 classifiers=[
                             # How mature is this project? Common values are
                             #   3 - Alpha
                             #   4 - Beta
                             #   5 - Production/Stable
                             'Development Status :: 3 - Alpha',

                             # Indicate who your project is intended for
                             'Intended Audience :: Developers',

                             # Pick your license as you wish (should match "license" above)
                             'License :: OSI Approved :: MIT License',

                             # Specify the Python versions you support here. In particular, ensure
                             # that you indicate whether you support Python 2, Python 3 or both.
                             'Programming Language :: Python :: 3',
                             'Programming Language :: Python :: 3.2',
                             'Programming Language :: Python :: 3.2',
                             'Programming Language :: Python :: 3.3',
                             'Programming Language :: Python :: 3.4',
                             ])
