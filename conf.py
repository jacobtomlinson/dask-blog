# -- Project information
project = "Dask Blog"
author = "Dask Contributors"
copyright = "2014-2026, Dask Contributors"

# -- General configuration
extensions = [
    "ablog",
    "myst_parser",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",  # creates .nojekyll in output
]

# Source file handling
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

exclude_patterns = [
    "_build", "_website", ".doctrees",
    "node_modules", "public", ".github",
    "README.md", "CONTRIBUTING.md", "plans",
    "drafts", "_extra",
]

# -- MyST-Parser configuration
myst_enable_extensions = [
    "dollarmath",       # $...$ and $$...$$ math
    "colon_fence",      # ::: directive syntax alternative
]
myst_update_mathjax = False  # Don't let MyST override MathJax config

# -- ABlog configuration
blog_baseurl = "https://blog.dask.org"
blog_title = "Dask Working Notes"
blog_path = "blog"                       # Archive pages at /blog/
blog_post_pattern = "20*/*/*/*"          # Match YYYY/MM/DD/slug.md at root
post_date_format = "%b %d, %Y"          # e.g. "Jan 15, 2024"
post_date_format_short = "%b %d, %Y"
post_auto_excerpt = 1
post_show_prev_next = True
blog_feed_fulltext = True
blog_feed_archives = True                # Per-tag feeds
blog_feed_length = None                  # All posts in main feed
disqus_shortname = "dask-blog"

# ABlog builder
ablog_builder = "dirhtml"                # /post/ not /post.html
ablog_website = "_website"

# -- HTML output
html_theme = "pydata_sphinx_theme"
html_title = "Dask Working Notes"
html_favicon = "_static/favicon.svg"
html_static_path = ["_static"]
html_extra_path = [
    "_extra",           # Contains images/ and storage/ symlinks — preserves /images/... and /storage/... URLs
    "CNAME",
    "extras",           # Redirect pages (atom.xml, feed.*.xml, etc.)
]
html_css_files = ["css/custom.css"]

html_theme_options = {
    "logo": {
        "image_light": "_static/dask-logo.svg",
        "image_dark": "_static/dask-logo-white.svg",
        "text": "Dask Blog",
    },
    "github_url": "https://github.com/dask/dask-blog",
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "external_links": [
        {"name": "dask.org", "url": "https://dask.org"},
        {"name": "Docs", "url": "https://docs.dask.org"},
    ],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/dask/dask-blog",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
    ],
    "pygments_light_style": "tango",
    "pygments_dark_style": "monokai",
    "footer_start": ["copyright"],
    "footer_end": ["last-updated"],
    "secondary_sidebar_items": [],       # No right sidebar on posts
}

html_sidebars = {
    "index": [],                                             # No sidebar on homepage
    "20*/*/*/*": ["ablog/postcard.html"],                    # Post metadata sidebar
    "blog": ["ablog/tagcloud.html", "ablog/archives.html"], # Blog archive sidebar
    "blog/**": ["ablog/tagcloud.html", "ablog/archives.html"],
}

# -- MathJax
mathjax3_config = {
    "tex": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "displayMath": [["$$", "$$"], ["\\[", "\\]"]],
    },
}

# -- Analytics (injected via custom template override)
html_context = {
    "gtm_id": "GTM-P4GQM59",
}
