# Outdated packages now require special setup at start of script
import sys
import jinja2
import markupsafe
# workaround for setup
jinja2.Markup = markupsafe.Markup
jinja2.evalcontextfilter = jinja2.pass_context

from secretary import Renderer


# Basic definitions
template = sys.argv[1]


engine = Renderer()
engine.environment.variable_start_string  = '[['
engine.environment.variable_end_string = ']]'
engine.environment.block_start_string = '{{'
engine.environment.block_end_string = '}}'

result = engine.render(template, test="foo", test1="bar")

output = open('rendered_document.odt', 'wb')
output.write(result)
