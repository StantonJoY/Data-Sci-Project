Module(
    body=[
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.exceptions', asname=None)],
        ),
        FunctionDef(
            name='check',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='db', annotation=None, type_comment=None),
                    arg(arg='uid', annotation=None, type_comment=None),
                    arg(arg='passwd', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='res_users', ctx=Store())],
                    value=Subscript(
                        value=Call(
                            func=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='registry',
                                ctx=Load(),
                            ),
                            args=[Name(id='db', ctx=Load())],
                            keywords=[],
                        ),
                        slice=Constant(value='res.users', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='res_users', ctx=Load()),
                            attr='check',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='db', ctx=Load()),
                            Name(id='uid', ctx=Load()),
                            Name(id='passwd', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='compute_session_token',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='session', annotation=None, type_comment=None),
                    arg(arg='env', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='self', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='res.users', kind=None),
                                ctx=Load(),
                            ),
                            attr='browse',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='session', ctx=Load()),
                                attr='uid',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='self', ctx=Load()),
                            attr='_compute_session_token',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='session', ctx=Load()),
                                attr='sid',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='check_session',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='session', annotation=None, type_comment=None),
                    arg(arg='env', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='self', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='res.users', kind=None),
                                ctx=Load(),
                            ),
                            attr='browse',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='session', ctx=Load()),
                                attr='uid',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='expected', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='self', ctx=Load()),
                            attr='_compute_session_token',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='session', ctx=Load()),
                                attr='sid',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='expected', ctx=Load()),
                            Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='tools',
                                            ctx=Load(),
                                        ),
                                        attr='misc',
                                        ctx=Load(),
                                    ),
                                    attr='consteq',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='expected', ctx=Load()),
                                    Attribute(
                                        value=Name(id='session', ctx=Load()),
                                        attr='session_token',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Constant(value=False, kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
