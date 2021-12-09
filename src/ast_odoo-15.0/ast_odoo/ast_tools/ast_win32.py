Module(
    body=[
        Import(
            names=[alias(name='locale', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        If(
            test=UnaryOp(
                op=Not(),
                operand=Call(
                    func=Name(id='hasattr', ctx=Load()),
                    args=[
                        Name(id='locale', ctx=Load()),
                        Constant(value='D_FMT', kind=None),
                    ],
                    keywords=[],
                ),
            ),
            body=[
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='locale', ctx=Load()),
                            attr='D_FMT',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(value=1, kind=None),
                    type_comment=None,
                ),
            ],
            orelse=[],
        ),
        If(
            test=UnaryOp(
                op=Not(),
                operand=Call(
                    func=Name(id='hasattr', ctx=Load()),
                    args=[
                        Name(id='locale', ctx=Load()),
                        Constant(value='T_FMT', kind=None),
                    ],
                    keywords=[],
                ),
            ),
            body=[
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='locale', ctx=Load()),
                            attr='T_FMT',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(value=2, kind=None),
                    type_comment=None,
                ),
            ],
            orelse=[],
        ),
        If(
            test=UnaryOp(
                op=Not(),
                operand=Call(
                    func=Name(id='hasattr', ctx=Load()),
                    args=[
                        Name(id='locale', ctx=Load()),
                        Constant(value='nl_langinfo', kind=None),
                    ],
                    keywords=[],
                ),
            ),
            body=[
                FunctionDef(
                    name='nl_langinfo',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='param', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='param', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='locale', ctx=Load()),
                                        attr='D_FMT',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='val', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='30/12/2004', kind=None),
                                            Constant(value='%d/%m/%Y', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='dt', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Subscript(
                                                    value=Name(id='val', ctx=Load()),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=2, kind=None),
                                                        ),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='format_date', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dt', ctx=Load()),
                                            attr='strftime',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='%x', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='x', ctx=Store()),
                                            Name(id='y', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='30', kind=None),
                                                    Constant(value='%d', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='12', kind=None),
                                                    Constant(value='%m', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='2004', kind=None),
                                                    Constant(value='%Y', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='04', kind=None),
                                                    Constant(value='%Y', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='format_date', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='format_date', ctx=Load()),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='x', ctx=Load()),
                                                    Name(id='y', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='format_date', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='param', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='locale', ctx=Load()),
                                        attr='T_FMT',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='val', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='13:24:56', kind=None),
                                            Constant(value='%H:%M:%S', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='dt', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Subscript(
                                                    value=Name(id='val', ctx=Load()),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=2, kind=None),
                                                        ),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='format_time', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dt', ctx=Load()),
                                            attr='strftime',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='%X', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='x', ctx=Store()),
                                            Name(id='y', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='13', kind=None),
                                                    Constant(value='%H', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='24', kind=None),
                                                    Constant(value='%M', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='56', kind=None),
                                                    Constant(value='%S', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='format_time', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='format_time', ctx=Load()),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='x', ctx=Load()),
                                                    Name(id='y', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='format_time', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='locale', ctx=Load()),
                            attr='nl_langinfo',
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='nl_langinfo', ctx=Load()),
                    type_comment=None,
                ),
            ],
            orelse=[],
        ),
    ],
    type_ignores=[],
)
