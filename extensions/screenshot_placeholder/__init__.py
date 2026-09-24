"""``.. screenshot::`` directive — a placeholder for a screenshot still to be made.

The spec (what the screenshot must show) lives in the source so nobody has to
rethink it when taking the picture. Options are NOT extracted for translation
(internal spec, English only). Rendered as a faint, low-contrast box.

Usage::

    .. screenshot:: invoicing-settings-default-taxes
       :menu: Invoicing ‣ Configuration ‣ Settings
       :shows: Settings page, Taxes section, "Default Taxes" field set to 27%.
       :highlight: The "Default Taxes" field.
       :data: Company: YourCompany (HU); sales tax "27%"; purchase tax "27%".
       :module: account
       :notes: Light theme, 1440px wide, English UI.

Set ``screenshot_placeholders_hidden = True`` in conf.py to hide them all.
"""
from docutils import nodes
from docutils.parsers.rst import Directive, directives

FIELDS = ('menu', 'shows', 'highlight', 'data', 'module', 'notes')


class screenshot_placeholder(nodes.General, nodes.Element):
    pass


class ScreenshotDirective(Directive):
    required_arguments = 1  # unique id (kebab-case), also the future image file name
    has_content = False
    option_spec = {f: directives.unchanged for f in FIELDS}

    def run(self):
        node = screenshot_placeholder()
        node['sid'] = self.arguments[0]
        for f in FIELDS:
            node[f] = self.options.get(f, '')
        if not node['shows']:
            return [self.state.document.reporter.warning(
                'screenshot placeholder %r has no :shows: option' % node['sid'], line=self.lineno)]
        return [node]


def visit_html(self, node):
    if self.builder.config.screenshot_placeholders_hidden:
        raise nodes.SkipNode
    esc = self.encode
    rows = ''.join(
        '<dt>%s</dt><dd>%s</dd>' % (f, esc(node[f])) for f in FIELDS if node[f])
    self.body.append(
        '<div class="o-screenshot-placeholder" data-screenshot-id="%s">'
        '<span class="o-screenshot-placeholder-title">screenshot: %s</span><dl>%s</dl></div>'
        % (esc(node['sid']), esc(node['sid']), rows))
    raise nodes.SkipNode


def skip(self, node):
    raise nodes.SkipNode


def setup(app):
    app.add_config_value('screenshot_placeholders_hidden', False, 'html')
    app.add_node(screenshot_placeholder, html=(visit_html, None),
                 latex=(skip, None), text=(skip, None), gettext=(skip, None))
    app.add_directive('screenshot', ScreenshotDirective)
    app.add_css_file('css/screenshot_placeholder.css')
    return {'parallel_read_safe': True, 'parallel_write_safe': True}
