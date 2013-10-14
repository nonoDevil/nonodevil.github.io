#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'nonoDevil'
SITENAME = u'中二社'
SITEURL = u'http://nonodevil.com'

GITHUB_URL = 'https://github.com/nonoDevil'
ARCHIVES_URL = 'archives.html'
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS =  (('66ccff', 'http://chxccc.diandian.com'),
          ('刘丹阳', 'http;//rsroad.blog.chinaunix.net'),
          ('李欣',   'http://blog.sina.com.cn/u/1715653890'),
          ('韩伟',   'htpp://bsehw.blog.chinaunix.net'),
          ('何宇航', 'http://hookup.sinaapp.com/views/'),
          ('高家升', 'http://gaojiasheng.him.blog.163.com/'),
          ('王韬',   'http://hi.baidu.com/0xc0000000'),
          ('杨帆',   'http://blog.163.com/yangfan876@126/'),
          ('杜斌',   'http://blog.db89.org'),
          ('李文苹', 'http://lwplinux.blog.chinaunix.net'),
          ('刘欢',   'http://www.0xffffff.org'),
          ('林达意', 'http://www.lindayi.tk'),
          ('刘永康', 'http://liuyongkang.blog.chinaunix.net'),
          ('李力',   'http://tioo.sinaapp.com/'),
          ('沈昭萌', 'http://blog.csdn.net/sim_szm'),
          ('张瑞',   'http://through-my-eyes.diandian.com/'),
          ('陈露纹', 'http://blog.sina.com.cn/eallychen'),
          ('雷雨',   'http://blog.sina.com.cn/u/2657346022'),
          ('武特',   'http://edsionte.com/techblog/'),
          ('赵桥',   'http://www.linuxqiao.org/'),
          ('吴云',   'http://wykitty.blog.chinaunix.net'),
          ('Pelican', 'http://getpelican.com'),
          )

# Social widget
SOCIAL = (('Github', 'https://github.com/nonoDevil'),
          (u'微博', 'http://weibo.com/nonodevil'),
          (u'知乎', 'http://www.zhihu.com/people/nonodevil'),)

# pagination
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#Theme   usually use: tuxlite_tbs pelican-bootstrap3
THEME = 'tuxlite_tbs'
#THEME = 'pelican-bootstrap3'

#pelican-bootstrap theme setting
#BOOTSTRAP_THEME = 'flatly'

#DISQUS
DISQUS_SITENAME = 'nonodevil'

#Google Analytics
GOOGLE_ANALYTICS = 'UA-44575590-1'

#pelican-plugin setting
PLUGIN_PATH = u"pelican-plugins"

#pelican-plugin in use
PLUGINS = ["sitemap", "neighbors", "related_posts"]

#plugins setting
#相关文章推荐
RELATED_POST_MAX = 10

#configure sitemap
SITEMAP =  {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes":  0.5,
        "pages":    0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes":  "daily",
        "pages":    "monthly",
    }
}

#static directory
STATIC_PATHS = [
        'extra/robots.txt',
        '../pelicanconf.py',
        ]

#static page
EXTRA_PATH_METADATA = {
        'extra/robots.txt': {'path': 'robots.txt'},
        '../pelicanconf.py': {'path': 'pelicanconf.py'},
        }

