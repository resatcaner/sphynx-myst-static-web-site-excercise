import os
import sys
sys.path.insert(0, os.path.abspath("."))

project = 'Schlockchain'
copyright = '2022, Caner Bas <caner.bas>'
author = 'Caner Bas <caner.bas>'
extensions = [
    'myst_parser',
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'alabaster'
html_static_path = ['_static']
myst_enable_extensions = [
    "colon_fence",
]

intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

myst_url_schemes = ["http", "https", ]