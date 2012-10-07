AUTHOR = u'Marco Chomut'
SITENAME = u'Marco\'s Modern Life'
SITEURL = 'http://marcosmodernlife.com'
TIMEZONE = "America/New_York"

OUTPUT_PATH = '../bin/'
ARTICLE_PERMALINK_STRUCTURE = '/blog/%Y/%m/%d/'
PDF_GENERATOR = False
REVERSE_ARCHIVE_ORDER = True
REVERSE_CATEGORY_ORDER = True
LOCALE = ''
DEFAULT_PAGINATION = 5
# DISPLAY_PAGES_ON_MENU = True

# global metadata to all the contents
# DEFAULT_METADATA = (('yeah', 'it is'),)

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_RSS = 'feeds/tag_%s.rss.xml'
FEED_MAX_ITEMS = 100

# THEME = 'res/'
# THEME_STATIC_PATHS = [
    # 'static',
# ]
# CSS_FILE = 'mml.css'

# static paths will be copied under the same name
# STATIC_PATHS = [
#     '../res/static'
# ]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (
    ('../res/robots.txt', 'robots.txt'),
    ('../res/humans.txt', 'humans.txt'),
    ('../res/favicon.ico', 'favicon.ico'),
    ('../res/CNAME', 'CNAME'),
)

# Custom context variables, used optionally in each theme

LINKS = (
    ('Google', 'http://google.com'),
)

SOCIAL = (
    ('twitter', 'http://twitter.com/pewpewarrows'),
    ('github', 'http://github.com/Pewpewarrows'),
)

MENUITEMS = ()

DISQUS_SITENAME = 'marcosmodernlife'
GITHUB_URL = 'https://github.com/Pewpewarrows/MyModernLife-Redux'
GOOGLE_ANALYTICS = ''
TWITTER_USERNAME = 'pewpewarrows'
