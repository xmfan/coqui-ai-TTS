#!/usr/bin/env python
#                   ,*++++++*,                ,*++++++*,
#                *++.        .+++          *++.        .++*
#              *+*     ,++++*   *+*      *+*   ,++++,     *+*
#             ,+,   .++++++++++* ,++,,,,*+, ,++++++++++.   *+,
#             *+.  .++++++++++++..++    *+.,++++++++++++.  .+*
#             .+*   ++++++++++++.*+,    .+*.++++++++++++   *+,
#              .++   *++++++++* ++,      .++.*++++++++*   ++,
#               ,+++*.    . .*++,          ,++*.      .*+++*
#              *+,   .,*++**.                  .**++**.   ,+*
#             .+*                                          *+,
#             *+.                   Coqui                  .+*
#             *+*              +++   TTS  +++              *+*
#             .+++*.            .          .             *+++.
#              ,+* *+++*...                       ...*+++* *+,
#               .++.    .""""+++++++****+++++++"""".     ++.
#                 ,++.                                .++,
#                   .++*                            *++.
#                       *+++,                  ,+++*
#                           .,*++++::::::++++*,.
#                                  ``````

import os

import numpy
from Cython.Build import cythonize
from setuptools import Extension, setup

cwd = os.path.dirname(os.path.abspath(__file__))

requirements = open(os.path.join(cwd, "requirements.txt"), "r").readlines()
with open(os.path.join(cwd, "requirements.notebooks.txt"), "r") as f:
    requirements_notebooks = f.readlines()
with open(os.path.join(cwd, "requirements.dev.txt"), "r") as f:
    requirements_dev = f.readlines()
with open(os.path.join(cwd, "requirements.ja.txt"), "r") as f:
    requirements_ja = f.readlines()
requirements_server = ["flask>=2.0.1"]
requirements_all = requirements_dev + requirements_notebooks + requirements_ja + requirements_server

exts = [
    Extension(
        name="TTS.tts.utils.monotonic_align.core",
        sources=["TTS/tts/utils/monotonic_align/core.pyx"],
    )
]
setup(
    include_dirs=numpy.get_include(),
    ext_modules=cythonize(exts, language_level=3),
    install_requires=requirements,
    extras_require={
        "all": requirements_all,
        "dev": requirements_dev,
        "notebooks": requirements_notebooks,
        "server": requirements_server,
        "ja": requirements_ja,
    },
    zip_safe=False,
)
