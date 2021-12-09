Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ResConfigSettings',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.config.settings', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='jitsi_server_domain', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Jitsi Server Domain', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='meet.jit.si', kind=None),
                            ),
                            keyword(
                                arg='config_parameter',
                                value=Constant(value='website_jitsi.jitsi_server_domain', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The Jitsi server domain can be customized through the settings to use a different server than the default "meet.jit.si"', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
