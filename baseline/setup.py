from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
  name = 'gr',
  ext_modules = cythonize(
    "gr.pyx",
    language="c++",
  ),
  include_dirs=[numpy.get_include()]
)