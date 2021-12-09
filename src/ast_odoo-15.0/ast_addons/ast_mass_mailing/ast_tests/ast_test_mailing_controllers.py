Module(
    body=[
        Import(
            names=[alias(name='werkzeug', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.mass_mailing.tests.common',
            names=[alias(name='MassMailCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='HttpCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestMassMailingControllers',
            bases=[
                Name(id='MassMailCommon', ctx=Load()),
                Name(id='HttpCase', ctx=Load()),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_tracking_url_token',
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
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='web.base.url', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_web_base_url',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mail_mail', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.mail', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Dict(keys=[], values=[])],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='mail_mail', ctx=Load()),
                                            attr='_get_tracking_url',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='status_code',
                                        ctx=Load(),
                                    ),
                                    Constant(value=200, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='base_url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mail_mail', ctx=Load()),
                                    attr='get_base_url',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='werkzeug', ctx=Load()),
                                        attr='urls',
                                        ctx=Load(),
                                    ),
                                    attr='url_join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='base_url', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='mail/track/%s/fake_token/blank.gif', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='mail_mail', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Name(id='url', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='status_code',
                                        ctx=Load(),
                                    ),
                                    Constant(value=400, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
