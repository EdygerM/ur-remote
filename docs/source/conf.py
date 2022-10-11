# -- Path setup ----------------------------------------
import os
import sys
sys.path.append(os.path.abspath('../..'))
sys.path.append(os.path.abspath(''))

# -- Project information -------------------------------
project = 'ur_remote'
copyright = '2022, Edy Mariano'
author = 'Edy Mariano'

# -- General configuration -----------------------------
extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output ---------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']