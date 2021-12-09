Module(
    body=[
        ImportFrom(
            module='http',
            names=[alias(name='HTTPStatus', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo.tools', asname=None)],
        ),
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='HttpCase', asname=None),
                alias(name='HOST', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestCustomAuth',
            bases=[Name(id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_json',
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
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/test_auth_custom/json', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='headers',
                                        value=Dict(
                                            keys=[Constant(value='Content-Type', kind=None)],
                                            values=[Constant(value='application/json', kind=None)],
                                        ),
                                    ),
                                    keyword(
                                        arg='data',
                                        value=Constant(value='{}', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='e', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='r', ctx=Load()),
                                        attr='json',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value='error', kind=None),
                                ctx=Load(),
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='data', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='name', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='odoo.exceptions.AccessDenied', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='http://%s:%s/test_auth_custom/json', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='HOST', ctx=Load()),
                                        Subscript(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='tools',
                                                    ctx=Load(),
                                                ),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='http_port', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='opener',
                                        ctx=Load(),
                                    ),
                                    attr='options',
                                    ctx=Load(),
                                ),
                                args=[Name(id='url', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='headers',
                                        value=Dict(
                                            keys=[
                                                Constant(value='Origin', kind=None),
                                                Constant(value='Access-Control-Request-Method', kind=None),
                                                Constant(value='Access-Control-Request-Headers', kind=None),
                                            ],
                                            values=[
                                                Constant(value='localhost', kind=None),
                                                Constant(value='QUX', kind=None),
                                                Constant(value='XYZ', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='r', ctx=Load()),
                                        attr='ok',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='headers',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='Access-Control-Allow-Origin', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='*', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='headers',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='Access-Control-Allow-Methods', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='POST', kind=None),
                                    Constant(value='json is always POST', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='XYZ', kind=None),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='headers',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='Access-Control-Allow-Headers', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='headers are ignored', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='tools',
                                    ctx=Load(),
                                ),
                                attr='mute_logger',
                                ctx=Load(),
                            ),
                            args=[Constant(value='odoo.http', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_http',
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
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/test_auth_custom/http', kind=None)],
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
                                        value=Name(id='r', ctx=Load()),
                                        attr='status_code',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='HTTPStatus', ctx=Load()),
                                        attr='FORBIDDEN',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='http://%s:%s/test_auth_custom/http', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='HOST', ctx=Load()),
                                        Subscript(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='tools',
                                                    ctx=Load(),
                                                ),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='http_port', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='opener',
                                        ctx=Load(),
                                    ),
                                    attr='options',
                                    ctx=Load(),
                                ),
                                args=[Name(id='url', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='headers',
                                        value=Dict(
                                            keys=[
                                                Constant(value='Origin', kind=None),
                                                Constant(value='Access-Control-Request-Method', kind=None),
                                                Constant(value='Access-Control-Request-Headers', kind=None),
                                            ],
                                            values=[
                                                Constant(value='localhost', kind=None),
                                                Constant(value='QUX', kind=None),
                                                Constant(value='XYZ', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='r', ctx=Load()),
                                        attr='ok',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='r', ctx=Load()),
                                        attr='text',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='headers',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='Access-Control-Allow-Origin', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='*', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='headers',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='Access-Control-Allow-Methods', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='GET, OPTIONS', kind=None),
                                    Constant(value="http is whatever's on the endpoint", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='XYZ', kind=None),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='headers',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='Access-Control-Allow-Headers', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='headers are ignored', kind=None),
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
