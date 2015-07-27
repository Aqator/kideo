from gallery import specs
from feincms.module.page.models import Page
from django.utils.translation import ugettext_lazy as _
from feincms.content.richtext.models import RichTextContent
from gallery.models import GalleryContent

Page.register_templates({
    'title': _('General FeinCMS Template Example'),
    'path': 'template1.html',
    'regions': (
        ('header', _('Page header.')),
        ('main', _('Main content area.')),
        ('sidebar', _('Sidebar'), 'inherited'),
        ('footer', _('Page footer.')),
    ),
})

GALLERY_TYPES = [
    specs.ClassicLightbox(),  # standard type
    specs.Type(
        verbose_name=_('Fancy paginated gallery'),
        paginated=True,
        paginate_by=12,
        orphans=4,
        template_name='slideshow.html',
        media={'css' : {'all' :
                    ('gallery/slideshow.css',
                     'lib/fancybox/jquery.fancybox-1.3.1.css'),},
                'js' :
                    ('gallery/slideshow.js',
                     'lib/fancybox/jquery.fancybox-1.3.1.pack.js')
        }
    )
]

Page.create_content_type(RichTextContent)
Page.create_content_type(GalleryContent, reqions=('main'),types=GALLERY_TYPES)