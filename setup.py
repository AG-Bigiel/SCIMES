#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

import os
import glob
from pathlib import Path
from setuptools import setup, find_packages

# ---- Core project metadata (adjust as needed) ----
NAME = "scimes"
PACKAGE = "scimes"  # change if your top-level package folder is different
VERSION = "0.4.0"   # bumped
DESCRIPTION = "Spectral Clustering for Molecular Interstellar Emission Segmentation"
AUTHOR = "Dario Colombo, Erik Rosolowsky, Adam Ginsburg, Ana Duarte-Cabral, Annie Hughes, and Zein Bazzi"
AUTHOR_EMAIL = "dario.colombo222@gmail.com"
LICENSE = "BSD-3-Clause"
URL = "http://scimes.readthedocs.org"
REPO_URL = "https://github.com/zeinbazzi/scimes_new"  # update if different

# ---- Long description from README (no runtime imports) ----
long_desc = ""
readme = None
for cand in ("README.md", "README.rst", "README.txt"):
    p = Path(cand)
    if p.exists():
        long_desc = p.read_text(encoding="utf-8")
        readme = cand
        break
long_desc_type = "text/markdown" if (readme and readme.endswith(".md")) else "text/x-rst"

# ---- Scripts (keep any real scripts, skip README) ----
scripts = [
    s for s in glob.glob(os.path.join("scripts", "*"))
    if os.path.basename(s).lower() not in {"readme.rst", "readme.md", "readme.txt"}
] if Path("scripts").exists() else []

# ---- Package data (ship data/* inside the package if present) ----
package_data = {PACKAGE: ["data/*"]} if Path(PACKAGE, "data").exists() else {}

# ---- Modern dependencies (pin floors; sklearn -> scikit-learn) ----
install_requires = [
    "astropy>=6",
    "astrodendro>=0.3",
    "numpy>=1.22",
    "matplotlib>=3.6",
    "scikit-learn>=1.5,<2",
    "tqdm>=4.66",
    "joblib>=1.4",
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_desc,
    long_description_content_type=long_desc_type,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    url=URL,
    project_urls={
        "Source": REPO_URL,
        "Documentation": URL,
    },
    packages=find_packages(exclude=("tests", "docs", "examples")),
    include_package_data=True,
    package_data=package_data,
    scripts=scripts,
    python_requires=">=3.9",
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
    zip_safe=False,
)
