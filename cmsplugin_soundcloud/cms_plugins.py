from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import SoundCloud, COLORS

from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

# use CMSPLUGIN_SOUNDCLOUD_PARAMS to override PARAMS
PARAMS = getattr(settings, 'CMSPLUGIN_SOUNDCLOUD_PARAMS',
                 'width="100%" height="166" scrolling="no" frameborder="no"')


class SoundCloudPlugin(CMSPluginBase):
    model = SoundCloud
    name = _('SoundCloud')
    text_enabled = True
    render_template = 'cmsplugin_soundcloud/cmsplugin_soundcloud.html'

    def render(self, context, instance, placeholder):
        context.update({'plugin_soundcloud': instance})
        return context

    def icon_src(self, instance):
        return instance.thumbnail_url

    #def get_form(self, request, obj=None, **kwargs):
    #    if obj:
    #        kwargs['exclude'] = ['url']
    #    else:
    #        kwargs['exclude'] = ['title', 'description', 'thumbnail_url']
    #    return super(SoundCloudPlugin, self).get_form(request, obj, **kwargs)


plugin_pool.register_plugin(SoundCloudPlugin)

