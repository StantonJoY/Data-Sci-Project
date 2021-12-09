Module(
    body=[
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            name='IrHttp',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.http', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_utm_domain_cookies',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='httprequest',
                                    ctx=Load(),
                                ),
                                attr='host',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_utm',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='response', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Name(id='Exception', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Name(id='response', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='db',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Name(id='response', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='get_utm_domain_cookies',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='var', ctx=Store()),
                                    Name(id='dummy', ctx=Store()),
                                    Name(id='cook', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='utm.mixin', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='tracking_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='var', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='params',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='httprequest',
                                                                ctx=Load(),
                                                            ),
                                                            attr='cookies',
                                                            ctx=Load(),
                                                        ),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='var', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='params',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='var', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='set_cookie',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='cook', ctx=Load()),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='params',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='var', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='domain',
                                                        value=Name(id='domain', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_dispatch',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrHttp', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_dispatch',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_set_utm',
                                    ctx=Load(),
                                ),
                                args=[Name(id='response', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_handle_exception',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='exc', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrHttp', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_handle_exception',
                                    ctx=Load(),
                                ),
                                args=[Name(id='exc', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_set_utm',
                                    ctx=Load(),
                                ),
                                args=[Name(id='response', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
