Module(
    body=[
        ImportFrom(
            module='odoo.addons.base.tests.common',
            names=[
                alias(name='HttpCaseWithUserDemo', asname=None),
                alias(name='HttpCaseWithUserPortal', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestWEventBoothExhibitorCommon',
            bases=[
                Name(id='HttpCaseWithUserDemo', ctx=Load()),
                Name(id='HttpCaseWithUserPortal', ctx=Load()),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_register',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browser_js',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/event', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].run("webooth_exhibitor_register")', kind=None),
                                    Constant(value='odoo.__DEBUG__.services["web_tour.tour"].tours.webooth_exhibitor_register.ready', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='admin', kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
