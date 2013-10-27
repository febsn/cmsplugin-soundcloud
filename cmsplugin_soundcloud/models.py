import re
from django.db import models
from django.conf import settings
from django.template import Template
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from json import load
from urllib2 import urlopen



# use CMSPLUGIN_SOUNDCLOUD_COLORS to override COLORS
COLORS = getattr(settings, 'CMSPLUGIN_SOUNDCLOUD_COLORS', (
    ('ff6600', _('default')),
))


OEMBED_URL_FORMAT = 'http://soundcloud.com/oembed?url=%s&amp;format=json'


def get_sound_properties(url):
    return load(urlopen(OEMBED_URL_FORMAT % url))


class SoundCloud(CMSPlugin):
    url           = models.CharField(_('Sound Cloud URL'), max_length=255,
                        help_text=_('(i. e. https://soundcloud.com/band/song)'))
    author_name   = models.CharField(max_length=255, editable=False)
    author_url    = models.CharField(max_length=255, editable=False)
    title         = models.CharField(max_length=255, editable=False)
    description   = models.CharField(max_length=255, editable=False)
    thumbnail_url = models.CharField(max_length=255, editable=False)
    color         = models.CharField(_('Color'), max_length=6, choices=COLORS,
                        default=COLORS[0][0],
                        help_text=_('Main color of the widget.'))
    auto_play     = models.BooleanField(_('Play automatically'))
    show_artwork  = models.BooleanField(_('Show artwork'))
    params        = models.TextField(editable=False)

    render_template = 'cmsplugin_soundcloud.html'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        properties         = get_sound_properties(self.url)
        self.author_name   = properties['author_name']
        self.author_url    = properties['author_url']
        self.title         = properties['title']
        self.description   = properties['description']
        self.thumbnail_url = properties['thumbnail_url']
        params = []
        # read only some particular attributes from html
        # (no need to trust the content we get)
        for (param, name) in re.findall(r'((width|height|src)="[^"]*")', properties['html']):
            if name == 'src':
                params.append(re.sub(
                    r'&.*"',
                    '&amp;color=%s&amp;auto_play=%s&amp;show_artwork=%s"' % (
                        self.color,
                        self.auto_play    and 'true' or 'false',
                        self.show_artwork and 'true' or 'false',
                    ),
                    param))
            else:
                params.append(param)
        self.params        = ' '.join(params)
        super(SoundCloud, self).save(*args, **kwargs)

