Module(
    body=[
        ImportFrom(
            module='__future__',
            names=[alias(name='print_function', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Assign(
            targets=[Name(id='component_re', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='(\\d+ | [a-z]+ | \\.| -)', kind=None),
                    Attribute(
                        value=Name(id='re', ctx=Load()),
                        attr='VERBOSE',
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='replace', ctx=Store())],
            value=Attribute(
                value=Dict(
                    keys=[
                        Constant(value='pre', kind=None),
                        Constant(value='preview', kind=None),
                        Constant(value='-', kind=None),
                        Constant(value='_', kind=None),
                        Constant(value='rc', kind=None),
                        Constant(value='dev', kind=None),
                        Constant(value='saas', kind=None),
                        Constant(value='~', kind=None),
                    ],
                    values=[
                        Constant(value='c', kind=None),
                        Constant(value='c', kind=None),
                        Constant(value='final-', kind=None),
                        Constant(value='final-', kind=None),
                        Constant(value='c', kind=None),
                        Constant(value='@', kind=None),
                        Constant(value='', kind=None),
                        Constant(value='', kind=None),
                    ],
                ),
                attr='get',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='_parse_version_parts',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='s', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                For(
                    target=Name(id='part', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='component_re', ctx=Load()),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Name(id='s', ctx=Load())],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='part', ctx=Store())],
                            value=Call(
                                func=Name(id='replace', ctx=Load()),
                                args=[
                                    Name(id='part', ctx=Load()),
                                    Name(id='part', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='part', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Name(id='part', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='.', kind=None)],
                                    ),
                                ],
                            ),
                            body=[Continue()],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='part', ctx=Load()),
                                    slice=Slice(
                                        lower=None,
                                        upper=Constant(value=1, kind=None),
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[Constant(value='0123456789', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='part', ctx=Load()),
                                                attr='zfill',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=8, kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Yield(
                                        value=BinOp(
                                            left=Constant(value='*', kind=None),
                                            op=Add(),
                                            right=Name(id='part', ctx=Load()),
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Expr(
                    value=Yield(
                        value=Constant(value='*final', kind=None),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='parse_version',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='s', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Convert a version string to a chronologically-sortable key\n\n    This is a rough cross between distutils\' StrictVersion and LooseVersion;\n    if you give it versions that would work with StrictVersion, then it behaves\n    the same; otherwise it acts like a slightly-smarter LooseVersion. It is\n    *possible* to create pathological version coding schemes that will fool\n    this parser, but they should be very rare in practice.\n\n    The returned value will be a tuple of strings.  Numeric portions of the\n    version are padded to 8 digits so they will compare numerically, but\n    without relying on how numbers compare relative to strings.  Dots are\n    dropped, but dashes are retained.  Trailing zeros between alpha segments\n    or dashes are suppressed, so that e.g. "2.4.0" is considered the same as\n    "2.4". Alphanumeric parts are lower-cased.\n\n    The algorithm assumes that strings like "-" and any alpha string that\n    alphabetically follows "final"  represents a "patch level".  So, "2.4-1"\n    is assumed to be a branch or patch of "2.4", and therefore "2.4.1" is\n    considered newer than "2.4-1", which in turn is newer than "2.4".\n\n    Strings like "a", "b", "c", "alpha", "beta", "candidate" and so on (that\n    come before "final" alphabetically) are assumed to be pre-release versions,\n    so that the version "2.4" is considered newer than "2.4a1".\n\n    Finally, to handle miscellaneous cases, the strings "pre", "preview", and\n    "rc" are treated as if they were "c", i.e. as though they were release\n    candidates, and therefore are not as new as a version string that does not\n    contain them.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='parts', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Name(id='part', ctx=Store()),
                    iter=Call(
                        func=Name(id='_parse_version_parts', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='s', ctx=Load()),
                                            Constant(value='0.1', kind=None),
                                        ],
                                    ),
                                    attr='lower',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='part', ctx=Load()),
                                    attr='startswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='*', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='part', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[Constant(value='*final', kind=None)],
                                    ),
                                    body=[
                                        While(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='parts', ctx=Load()),
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='parts', ctx=Load()),
                                                            slice=UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=1, kind=None),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='*final-', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='parts', ctx=Load()),
                                                            attr='pop',
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
                                    orelse=[],
                                ),
                                While(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='parts', ctx=Load()),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='parts', ctx=Load()),
                                                    slice=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='00000000', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='parts', ctx=Load()),
                                                    attr='pop',
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
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parts', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='part', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='tuple', ctx=Load()),
                        args=[Name(id='parts', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        If(
            test=Compare(
                left=Name(id='__name__', ctx=Load()),
                ops=[Eq()],
                comparators=[Constant(value='__main__', kind=None)],
            ),
            body=[
                FunctionDef(
                    name='chk',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='lst', annotation=None, type_comment=None),
                            arg(arg='verbose', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='pvs', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='v', ctx=Store()),
                            iter=Name(id='lst', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='pv', ctx=Store())],
                                    value=Call(
                                        func=Name(id='parse_version', ctx=Load()),
                                        args=[Name(id='v', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='pvs', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='pv', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Name(id='verbose', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='print', ctx=Load()),
                                                args=[
                                                    Name(id='v', ctx=Load()),
                                                    Name(id='pv', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='a', ctx=Store()),
                                    Name(id='b', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='pvs', ctx=Load()),
                                    Subscript(
                                        value=Name(id='pvs', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=1, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assert(
                                    test=Compare(
                                        left=Name(id='a', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[Name(id='b', ctx=Load())],
                                    ),
                                    msg=BinOp(
                                        left=Constant(value='%s < %s == %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='a', ctx=Load()),
                                                Name(id='b', ctx=Load()),
                                                Compare(
                                                    left=Name(id='a', ctx=Load()),
                                                    ops=[Lt()],
                                                    comparators=[Name(id='b', ctx=Load())],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='chk', ctx=Load()),
                        args=[
                            Tuple(
                                elts=[
                                    Constant(value='0', kind=None),
                                    Constant(value='4.2', kind=None),
                                    Constant(value='4.2.3.4', kind=None),
                                    Constant(value='5.0.0-alpha', kind=None),
                                    Constant(value='5.0.0-rc1', kind=None),
                                    Constant(value='5.0.0-rc1.1', kind=None),
                                    Constant(value='5.0.0_rc2', kind=None),
                                    Constant(value='5.0.0_rc3', kind=None),
                                    Constant(value='5.0.0', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            Constant(value=False, kind=None),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='chk', ctx=Load()),
                        args=[
                            Tuple(
                                elts=[
                                    Constant(value='5.0.0-0_rc3', kind=None),
                                    Constant(value='5.0.0-1dev', kind=None),
                                    Constant(value='5.0.0-1', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            Constant(value=False, kind=None),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            orelse=[],
        ),
    ],
    type_ignores=[],
)
