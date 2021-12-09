Module(
    body=[
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='tagged', asname=None),
                alias(name='HttpCase', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='Command', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestMailFullComposer',
            bases=[Name(id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_full_composer_tour',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='partner_to', kind=None),
                                            Constant(value='lang', kind=None),
                                            Constant(value='auto_delete', kind=None),
                                            Constant(value='model_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test template', kind=None),
                                            Constant(value='{{ object.id }}', kind=None),
                                            Constant(value='{{ object.lang }}', kind=None),
                                            Constant(value=True, kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='base.model_res_partner', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='testuser', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='email', kind=None),
                                            Constant(value='groups_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='password', kind=None),
                                        ],
                                        values=[
                                            Constant(value='testuser@testuser.com', kind=None),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='set',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='ref',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='base.group_user', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='ref',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='base.group_partner_manager', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='Test User', kind=None),
                                            Constant(value='testuser', kind=None),
                                            Constant(value='testuser', kind=None),
                                        ],
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
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/web#id=%d&model=res.partner', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='testuser', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='mail/static/tests/tours/mail_full_composer_test_tour.js', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='testuser', kind=None),
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
                        Constant(value='-at_install', kind=None),
                        Constant(value='post_install', kind=None),
                        Constant(value='mail_composer', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
