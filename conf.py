# -*- encoding: utf-8 -*-
# This is your configuration file.  Please write valid python!
# See http://posativ.org/acrylamid/conf.py.html

SITENAME = 'Press-releases'
WWW_ROOT = 'http://anker.ru/'

AUTHOR = 'Venom'
EMAIL = 'venom@anker.ru'

ENCODING = 'utf-8'

#FILTERS = ['Markdown', 'markdown+codehilite(css_class=highlight)', 'hyphenate', 'h1']
FILTERS = ['Markdown', ]



VIEWS = {

    '/pr_eng/': {'view': 'index',
          'pagination': '/pr_eng/page/:num/', 'items_per_page': 1},



    '/pr_eng/:year/:slug/': {'views': ['entry', 'draft']},


    '/pr_eng/tag/:name/': {'filters': 'summarize', 'view':'tag',
                    'pagination': '/pr_eng/tag/:name/:num/'},

    # # per tag Atom or RSS feed. Just uncomment to generate them.
    # '/tag/:name/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atompertag'},
    # '/tag/:name/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rsspertag'},

    '/pr_eng/articles/': {'view': 'archive', 'template': 'articles.html'},

    '/pr_eng/sitemap.xml': {'view': 'sitemap'},



    # # Here are some more examples

    # # '/:slug/' is a slugified url of your static page's title
    # '/:slug/': {'view': 'page'}

    # # '/atom/full/' will give you a _complete_ feed of all your entries
    # '/atom/full/': {'filters': 'h2', 'view': 'atom', 'num_entries': 1000},

    # # a feed containing all entries tagges with 'python'
    # '/rss/python/': {'filters': 'h2', 'view': 'rss',
    #                  'if': lambda e: 'python' in e.tags}

    # # a full typography features entry including MathML and Footnotes
    # '/:year/:slug': {'filters': ['typography', 'Markdown+Footnotes+MathML'],
    #                  'view': 'entry'}

    # # translations!
    # '/:year/:slug/:lang/': {'view': 'translation'}
}

THEME = 'theme'
ENGINE = 'acrylamid.templates.jinja2.Environment'
LANG = "en_US.UTF-8"
DATE_FORMAT = '%d.%m.%Y'
