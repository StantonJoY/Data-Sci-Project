Module(
    body=[
        Import(
            names=[alias(name='os.path', asname=None)],
        ),
        Try(
            body=[
                Import(
                    names=[alias(name='GeoIP', asname=None)],
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='GeoIP', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        Try(
            body=[
                Import(
                    names=[alias(name='geoip2', asname=None)],
                ),
                Import(
                    names=[alias(name='geoip2.database', asname=None)],
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='geoip2', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        ClassDef(
            name='GeoIPResolver',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fname', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='fname',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='fname', ctx=Load()),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_db',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='geoip2', ctx=Load()),
                                                attr='database',
                                                ctx=Load(),
                                            ),
                                            attr='Reader',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='fname', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='version',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=2, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_db',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='GeoIP', ctx=Load()),
                                                            attr='open',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='fname', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='GeoIP', ctx=Load()),
                                                                attr='GEOIP_STANDARD',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='version',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=1, kind=None),
                                                    type_comment=None,
                                                ),
                                                Assert(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_db',
                                                                ctx=Load(),
                                                            ),
                                                            attr='database_info',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[IsNot()],
                                                        comparators=[Constant(value=None, kind=None)],
                                                    ),
                                                    msg=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='Exception', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='ValueError', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Constant(value='Invalid GeoIP database: %r', kind=None),
                                                                        op=Mod(),
                                                                        right=Name(id='fname', ctx=Load()),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            cause=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__del__',
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
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='version',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=2, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_db',
                                                ctx=Load(),
                                            ),
                                            attr='close',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='open',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='fname', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='GeoIP', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='geoip2', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='exists',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='fname', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='GeoIPResolver', ctx=Load()),
                                args=[Name(id='fname', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='resolve',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='ip', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='version',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_db',
                                                        ctx=Load(),
                                                    ),
                                                    attr='record_by_addr',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='ip', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='version',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='r', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_db',
                                                                ctx=Load(),
                                                            ),
                                                            attr='city',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='ip', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Tuple(
                                                        elts=[
                                                            Name(id='ValueError', ctx=Load()),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='geoip2', ctx=Load()),
                                                                    attr='errors',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='AddressNotFoundError',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    name=None,
                                                    body=[
                                                        Return(
                                                            value=Dict(keys=[], values=[]),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='country', ctx=Store()),
                                                        Name(id='attr', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=IfExp(
                                                test=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='r', ctx=Load()),
                                                        attr='country',
                                                        ctx=Load(),
                                                    ),
                                                    attr='geoname_id',
                                                    ctx=Load(),
                                                ),
                                                body=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='country',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value='iso_code', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                orelse=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='continent',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value='code', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Dict(
                                                keys=[
                                                    Constant(value='city', kind=None),
                                                    Constant(value='country_code', kind=None),
                                                    Constant(value='country_name', kind=None),
                                                    Constant(value='latitude', kind=None),
                                                    Constant(value='longitude', kind=None),
                                                    Constant(value='region', kind=None),
                                                    Constant(value='time_zone', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='city',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='getattr', ctx=Load()),
                                                        args=[
                                                            Name(id='country', ctx=Load()),
                                                            Name(id='attr', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='country', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='location',
                                                            ctx=Load(),
                                                        ),
                                                        attr='latitude',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='location',
                                                            ctx=Load(),
                                                        ),
                                                        attr='longitude',
                                                        ctx=Load(),
                                                    ),
                                                    IfExp(
                                                        test=Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='subdivisions',
                                                            ctx=Load(),
                                                        ),
                                                        body=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='r', ctx=Load()),
                                                                    attr='subdivisions',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='iso_code',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Constant(value=None, kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='location',
                                                            ctx=Load(),
                                                        ),
                                                        attr='time_zone',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='record_by_addr',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='addr', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='resolve',
                                    ctx=Load(),
                                ),
                                args=[Name(id='addr', ctx=Load())],
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
