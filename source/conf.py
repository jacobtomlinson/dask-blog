# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import datetime

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "dask-blog"
copyright = f"{datetime.date.today().year}, Dask Developers"
author = "Dask Developers"
html_title = "Dask Blog"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "IPython.sphinxext.ipython_console_highlighting",
    "sphinx.ext.intersphinx",
    "myst_nb",
    "sphinxcontrib.mermaid",
    "sphinx_design",
    "sphinx_copybutton",
    "yasfb",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_sidebars = {"**": []}
html_theme_options = {
    # Top nav config
    "navbar_start": ["navbar-logo"],
    "navbar_center": [],
    "navbar_end": ["navbar-nav", "navbar-icon-links"],
    "navbar_persistent": [],
    "external_links": [
        {
            "name": "Docs",
            "url": "https://docs.dask.org/en/stable/",
        },
    ],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/dask",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        }
    ],
    # Page buttons config
    "use_download_button": False,
    "repository_url": "https://github.com/dask/dask-blog",
    "repository_branch": "gh-pages",
    "path_to_docs": "source",
    "use_edit_page_button": True,
    "use_sidenotes": True,
    "use_fullscreen_button": False,
}
