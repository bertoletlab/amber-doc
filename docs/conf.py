import os
import sys
from datetime import datetime

# Add project root to path so autodoc finds the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '_ext')))

project = 'AMBER'
author = 'Bertolet Lab'
current_year = datetime.now().year
copyright = f'{current_year}, Bertolet Lab'

# General config
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_autodoc_typehints',
    'myst_parser',
    'nbsphinx',
]

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_rtype = True

autosummary_generate = True
autodoc_typehints = 'description'
autodoc_member_order = 'bysource'

# MyST (Markdown) config
myst_enable_extensions = [
    'dollarmath',
    'amsmath',
]

# nbsphinx
nbsphinx_allow_errors = False
nbsphinx_execute = 'never'  # start with non-execution; flip to 'auto' if notebooks are lightweight

# HTML theme
html_theme = 'sphinx_rtd_theme'
html_static_path = []
html_logo = None
html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 3,
}

# Intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# If you keep the notebook under docs/tutorials/
# nbsphinx needs a kernel only if you execute; otherwise fine.
# --- Autogenerate CONFIG schema ---------------------------------------------
try:
    from _ext.config_schema import generate_config_schema
    generate_config_schema()
except Exception as e:  # keep docs builds robust
    print("[docs] config_schema skipped:", e)