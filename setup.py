from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from setuptools import setup, Extension
import platform


try:
    from Cython.Build import build_ext
except ImportError:
    from setuptools.command.build_ext import build_ext
    ext = '.c'
else:
    ext = '.pyx'


# from https://stackoverflow.com/a/52466939/3216742
extra_compile_args = ['-O3']
extra_link_args = []

if platform.system() == "Darwin":
    extra_compile_args += ["-mmacosx-version-min=10.9"]
    extra_link_args += ["-mmacosx-version-min=10.9"]


def read_md(path):
    with open(path, 'r') as f:
        f.read()


def set_builtin(name, value):
    if isinstance(__builtins__, dict):
        __builtins__[name] = value
    else:
        setattr(__builtins__, name, value)


# include_dirs adjusted:
class my_build_ext(build_ext):
    def finalize_options(self):
        build_ext.finalize_options(self)

        # prevent numpy from thinking it is still in its setup process:
        set_builtin('__NUMPY_SETUP__', False)
        import numpy as np
        self.include_dirs.append(np.get_include())


setup(
    name='Kaggler',
    version='0.8.2',

    author='Jeong-Yoon Lee',
    author_email='jeongyoon.lee1@gmail.com',

    packages=['kaggler',
              'kaggler.feature_selection',
              'kaggler.ensemble',
              'kaggler.model',
              'kaggler.metrics',
              'kaggler.online_model',
              'kaggler.preprocessing'],
    url='https://github.com/jeongyoonlee/Kaggler',
    license='LICENSE',

    description='Code for Kaggle Data Science Competitions.',
    long_description=read_md('README.md'),
    long_description_content_type='text/markdown',

    install_requires=[
        'setuptools>=41.0.0',
        'cython>=0.29.0',
        'h5py',
        'hyperopt',
        'ml_metrics',
        'numpy',
        'pandas',
        'matplotlib',
        'scipy>=0.14.0',
        'scikit-learn>=0.15.0',
        'statsmodels>=0.5.0',
        'kaggle',
        'tensorflow',
        'keras',
    ],

    setup_requires=['cython>=0.29.0', 'numpy'],

    cmdclass={'build_ext': my_build_ext},
    ext_modules=[Extension('kaggler.online_model.ftrl',
                           ['kaggler/online_model/ftrl' + ext,
                            'kaggler/online_model/murmurhash/MurmurHash3.cpp'],
                           libraries=[],
                           include_dirs=['.'],
                           extra_compile_args=extra_compile_args,
                           extra_link_args=extra_link_args),
                 Extension('kaggler.online_model.sgd',
                           ['kaggler/online_model/sgd' + ext],
                           libraries=[],
                           include_dirs=['.'],
                           extra_compile_args=extra_compile_args,
                           extra_link_args=extra_link_args),
                 Extension('kaggler.online_model.fm',
                           ['kaggler/online_model/fm' + ext],
                           libraries=[],
                           include_dirs=['.'],
                           extra_compile_args=extra_compile_args,
                           extra_link_args=extra_link_args),
                 Extension('kaggler.online_model.nn',
                           ['kaggler/online_model/nn' + ext],
                           libraries=[],
                           include_dirs=['.'],
                           extra_compile_args=extra_compile_args,
                           extra_link_args=extra_link_args),
                 Extension('kaggler.online_model.nn_h2',
                           ['kaggler/online_model/nn_h2' + ext],
                           libraries=[],
                           include_dirs=['.'],
                           extra_compile_args=extra_compile_args,
                           extra_link_args=extra_link_args),
                 Extension('kaggler.online_model._tree',
                           ['kaggler/online_model/_tree' + ext],
                           libraries=[],
                           include_dirs=['.'],
                           extra_compile_args=extra_compile_args,
                           extra_link_args=extra_link_args),
                 Extension('kaggler.util',
                           ['kaggler/util' + ext, 'kaggler/util.pxd'],
                           libraries=[],
                           include_dirs=['.'],
                           extra_compile_args=extra_compile_args,
                           extra_link_args=extra_link_args),
                 ],

    zip_safe=False,
)
