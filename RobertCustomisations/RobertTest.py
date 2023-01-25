# Outdated packages now require special setup at start of script

    import jinja2
    import markupsafe
    jinja2.Markup = markupsafe.Markup
    jinja2.evalcontextfilter = jinja2.pass_context
    import secretary
