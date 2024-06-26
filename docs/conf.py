# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "IHSetDocs"
copyright = "2024, Lim, Changbin"
author = "Lim, Changbin"

html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "ihcantabria",  # Username
    "github_repo": "IHSetDocs",  # Repo name
    "github_version": "main",  # Version
    "conf_py_path": "/docs/",
}

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
    "myst_nb",
    "sphinx.ext.autosummary",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
mathjax_config = {
    'tex2jax': {
        'inlineMath': [['$', '$'], ['\\(', '\\)']],
        'displayMath': [['$$', '$$'], ['\\[', '\\]']],
        'processEscapes': True,
        'ignoreClass': 'document',
        'processClass': 'math|output_area',
    },
    'TeX': {
        'extensions': ['AMSmath.js', 'AMSsymbols.js'],
    },
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "display_version": True,
    "style_external_links": False,
}
html_sidebars = {
    '**': [
        'sidebar.html',  # Default sidebar content
        'localtoc.html',  # Table of contents for the current page
        'sourcelink.html',  # Link to the source code
        'searchbox.html',  # Search box
    ],
}
# html_theme = 'furo'
# html_theme = 'sphinx_book_theme'

html_static_path = ["_static"]
html_logo = ""
html_title = " v"
myst_heading_anchors = 3