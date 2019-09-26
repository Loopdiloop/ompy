# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
import sys

# sys.path.insert(0, os.path.abspath('../sphinxext'))
# only for local build if the package was installed such that the compiles
# cython libraries are in the ../../package folder
# sys.path.insert(0, os.path.abspath('../..'))

# if autodoc or autosummary is not called, we cannot use their rutine
import mock
MOCK_MODULES = ['pymultinest']
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()


# -- Project information -----------------------------------------------------
from ompy import __version__
from ompy import __full_version__

project = 'OMpy'
copyright = '2019, Jørgen Eriksson Midtbø, Fabio Zeiser, Erlend Lima'
author = 'Jørgen Eriksson Midtbø, Fabio Zeiser, Erlend Lima'
version = __version__
release = __full_version__

# exec(compile(open('../../ipywidgets/_version.py').read(), '../../ipywidgets/_version.py', 'exec'), _release)
# version = '.'.join(map(str, _release['version_info'][:2]))
# release = _release['__version__']


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.autosummary',
              'sphinx.ext.intersphinx',
              'sphinx.ext.viewcode',
              'sphinx.ext.todo',
              'sphinx_automodapi.automodapi',
              'sphinx_automodapi.smart_resolver',
              'sphinx.ext.autosectionlabel',
              'recommonmark',
              # 'sphinxcontrib.katex',
              # 'sphinx_numfig',
              # 'notebook_sphinxext']
              ]

# autodoc_mock_imports = ["pymultinest"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "**.ipynb_checkpoints"]

# The master toctree document.
master_doc = 'index'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = [".rst", ".md"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'classic'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Misc -------------------------------------------------------------------

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'
# pygments_style = 'fruity'
# pygments_style = 'manni'
# pygments_style = 'tango'
pygments_style = 'friendly'
# pygments_style = 'bw'

# Prefix document path to section labels, otherwise autogenerated labels would
# look like 'heading' rather than 'path/to/file:heading'
autosectionlabel_prefix_document = True

# autodoc_default_flags = ["members"]
autosummary_generate = True
autosummary_imported_members = False

# remove typehints in signature
# autodoc_typehints = "none"

# Show the documentation of __init__ and the class docstring
autoclass_content = "both"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Don't auto-generate summary for class members.
numpydoc_show_class_members = False

napoleon_use_ivar = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference/', None)
}
