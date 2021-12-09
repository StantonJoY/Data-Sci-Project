Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[
                alias(name='Controller', asname=None),
                alias(name='request', asname=None),
                alias(name='Response', asname=None),
                alias(name='route', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='Profiling',
            bases=[Name(id='Controller', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='profile',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='profile', annotation=None, type_comment=None),
                            arg(arg='collectors', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='params', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='collectors', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='collectors', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='collectors', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=',', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='collectors', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Constant(value='sql', kind=None),
                                            Constant(value='traces_async', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='profile', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='profile', ctx=Load()),
                                    Compare(
                                        left=Name(id='profile', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='0', kind=None)],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='state', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.profile', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='set_profiling',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='profile', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='collectors',
                                                value=Name(id='collectors', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='params',
                                                value=Name(id='params', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='state', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='UserError', ctx=Load()),
                                    name='e',
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='Response', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='response',
                                                        value=BinOp(
                                                            left=Constant(value='error: %s', kind=None),
                                                            op=Mod(),
                                                            right=Name(id='e', ctx=Load()),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='status',
                                                        value=Constant(value=500, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[Constant(value='/web/set_profiling', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='speedscope',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='profile', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='ir.profile', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='_enabled_until',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='not_found',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='icp', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.config_parameter', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='profile', kind=None),
                                    Constant(value='url_root', kind=None),
                                    Constant(value='cdn', kind=None),
                                ],
                                values=[
                                    Name(id='profile', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='url_root',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='icp', ctx=Load()),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='speedscope_cdn', kind=None),
                                            Constant(value='https://cdn.jsdelivr.net/npm/speedscope@1.13.0/dist/release/', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='web.view_speedscope_index', kind=None),
                                    Name(id='context', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[
                                List(
                                    elts=[
                                        Constant(value='/web/speedscope/', kind=None),
                                        Constant(value='/web/speedscope/<model("ir.profile"):profile>', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=False, kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
