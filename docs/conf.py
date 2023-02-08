"""Sphinx configuration."""
project = "Budget App"
author = "Juan Henao"
copyright = "2023, Juan Henao"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
