Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ClassDef(
            name='IoTBoxHttpRequest',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='HttpRequest',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='dispatch',
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_cors_preflight',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='http', ctx=Load()),
                                            attr='request',
                                            ctx=Load(),
                                        ),
                                        attr='endpoint',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='headers', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='Access-Control-Max-Age', kind=None),
                                            Constant(value='Access-Control-Allow-Headers', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value=60, kind=None),
                                                    op=Mult(),
                                                    right=Constant(value=60, kind=None),
                                                ),
                                                op=Mult(),
                                                right=Constant(value=24, kind=None),
                                            ),
                                            Constant(value='Origin, X-Requested-With, Content-Type, Accept, Authorization, X-Debug-Mode', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='http', ctx=Load()),
                                            attr='Response',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='status',
                                                value=Constant(value=200, kind=None),
                                            ),
                                            keyword(
                                                arg='headers',
                                                value=Name(id='headers', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IoTBoxHttpRequest', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='dispatch',
                                    ctx=Load(),
                                ),
                                args=[],
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
        ClassDef(
            name='IoTBoxRoot',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Root',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='setup_db',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='httprequest', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[Pass()],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='httprequest', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='httprequest', ctx=Load()),
                                    attr='mimetype',
                                    ctx=Load(),
                                ),
                                ops=[NotIn()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='application/json', kind=None),
                                            Constant(value='application/json-rpc', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='IoTBoxHttpRequest', ctx=Load()),
                                        args=[Name(id='httprequest', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IoTBoxRoot', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_request',
                                    ctx=Load(),
                                ),
                                args=[Name(id='httprequest', ctx=Load())],
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
        Assign(
            targets=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Root',
                    ctx=Store(),
                ),
            ],
            value=Name(id='IoTBoxRoot', ctx=Load()),
            type_comment=None,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='root',
                    ctx=Store(),
                ),
            ],
            value=Call(
                func=Name(id='IoTBoxRoot', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
