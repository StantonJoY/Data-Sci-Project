Module(
    body=[
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='odoo', ctx=Load()),
                    attr='multi_process',
                    ctx=Store(),
                ),
            ],
            value=Constant(value=True, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Attribute(
                        value=Name(id='odoo', ctx=Load()),
                        attr='conf',
                        ctx=Load(),
                    ),
                    attr='server_wide_modules',
                    ctx=Store(),
                ),
            ],
            value=List(
                elts=[
                    Constant(value='base', kind=None),
                    Constant(value='web', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='conf', ctx=Store())],
            value=Attribute(
                value=Attribute(
                    value=Name(id='odoo', ctx=Load()),
                    attr='tools',
                    ctx=Load(),
                ),
                attr='config',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Subscript(
                    value=Name(id='conf', ctx=Load()),
                    slice=Constant(value='addons_path', kind=None),
                    ctx=Store(),
                ),
            ],
            value=Constant(value='../../addons/trunk,../../web/trunk/addons', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='application', ctx=Store())],
            value=Attribute(
                value=Attribute(
                    value=Attribute(
                        value=Name(id='odoo', ctx=Load()),
                        attr='service',
                        ctx=Load(),
                    ),
                    attr='wsgi_server',
                    ctx=Load(),
                ),
                attr='application',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Expr(
            value=Call(
                func=Attribute(
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='service',
                            ctx=Load(),
                        ),
                        attr='server',
                        ctx=Load(),
                    ),
                    attr='load_server_wide_modules',
                    ctx=Load(),
                ),
                args=[],
                keywords=[],
            ),
        ),
        Assign(
            targets=[Name(id='bind', ctx=Store())],
            value=Constant(value='127.0.0.1:8069', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='pidfile', ctx=Store())],
            value=Constant(value='.gunicorn.pid', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='workers', ctx=Store())],
            value=Constant(value=4, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='timeout', ctx=Store())],
            value=Constant(value=240, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='max_requests', ctx=Store())],
            value=Constant(value=2000, kind=None),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
