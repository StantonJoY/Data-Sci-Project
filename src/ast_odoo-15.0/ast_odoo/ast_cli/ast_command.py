Module(
    body=[
        ImportFrom(
            module='__future__',
            names=[alias(name='print_function', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        ImportFrom(
            module='os.path',
            names=[
                alias(name='join', asname='joinpath'),
                alias(name='isdir', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo.modules',
            names=[
                alias(name='get_modules', asname=None),
                alias(name='get_module_path', asname=None),
                alias(name='initialize_sys_path', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='commands', ctx=Store())],
            value=Dict(keys=[], values=[]),
            type_comment=None,
        ),
        ClassDef(
            name='CommandType',
            bases=[Name(id='type', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='bases', annotation=None, type_comment=None),
                            arg(arg='attrs', annotation=None, type_comment=None),
                        ],
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
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='CommandType', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='name', ctx=Load()),
                                    Name(id='bases', ctx=Load()),
                                    Name(id='attrs', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='cls', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='__name__',
                                                ctx=Load(),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='name', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='name', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='command', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='commands', ctx=Load()),
                                            slice=Name(id='name', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='cls', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
            targets=[Name(id='Command', ctx=Store())],
            value=Call(
                func=Name(id='CommandType', ctx=Load()),
                args=[
                    Constant(value='Command', kind=None),
                    Tuple(
                        elts=[Name(id='object', ctx=Load())],
                        ctx=Load(),
                    ),
                    Dict(
                        keys=[Constant(value='run', kind=None)],
                        values=[
                            Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[
                                        arg(arg='self', annotation=None, type_comment=None),
                                        arg(arg='args', annotation=None, type_comment=None),
                                    ],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=Constant(value=None, kind=None),
                            ),
                        ],
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='Help',
            bases=[Name(id='Command', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Display the list of available commands', kind=None),
                ),
                FunctionDef(
                    name='run',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='print', ctx=Load()),
                                args=[Constant(value='Available commands:\n', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='names', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[Name(id='commands', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='padding', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Name(id='max', ctx=Load()),
                                    args=[
                                        ListComp(
                                            elt=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='k', ctx=Load())],
                                                keywords=[],
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='k', ctx=Store()),
                                                    iter=Name(id='names', ctx=Load()),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Constant(value=2, kind=None),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='k', ctx=Store()),
                            iter=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[Name(id='names', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='k', ctx=Load()),
                                            attr='ljust',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='padding', ctx=Load()),
                                            Constant(value=' ', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='doc', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='commands', ctx=Load()),
                                                            slice=Name(id='k', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        attr='__doc__',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='print', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='    %s%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='name', ctx=Load()),
                                                        Name(id='doc', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='print', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value="\nUse '%s <command> --help' for individual command help.", kind=None),
                                        op=Mod(),
                                        right=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='sys', ctx=Load()),
                                                            attr='argv',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='path',
                                                            ctx=Load(),
                                                        ),
                                                        attr='sep',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            slice=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            ctx=Load(),
                                        ),
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
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='main',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='args', ctx=Store())],
                    value=Subscript(
                        value=Attribute(
                            value=Name(id='sys', ctx=Load()),
                            attr='argv',
                            ctx=Load(),
                        ),
                        slice=Slice(
                            lower=Constant(value=1, kind=None),
                            upper=None,
                            step=None,
                        ),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='args', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='args', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='startswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--addons-path=', kind=None)],
                                keywords=[],
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Name(id='args', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='startswith',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='-', kind=None)],
                                    keywords=[],
                                ),
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='tools',
                                            ctx=Load(),
                                        ),
                                        attr='config',
                                        ctx=Load(),
                                    ),
                                    attr='_parse_config',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Subscript(
                                                value=Name(id='args', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=Subscript(
                                value=Name(id='args', ctx=Load()),
                                slice=Slice(
                                    lower=Constant(value=1, kind=None),
                                    upper=None,
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='command', ctx=Store())],
                    value=Constant(value='server', kind=None),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[],
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Name(id='args', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='startswith',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='-', kind=None)],
                                    keywords=[],
                                ),
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='disable',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='CRITICAL',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='initialize_sys_path', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='module', ctx=Store()),
                            iter=Call(
                                func=Name(id='get_modules', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isdir', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='joinpath', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='get_module_path', ctx=Load()),
                                                        args=[Name(id='module', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='cli', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='__import__', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='odoo.addons.', kind=None),
                                                        op=Add(),
                                                        right=Name(id='module', ctx=Load()),
                                                    ),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='disable',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='NOTSET',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='command', ctx=Store())],
                            value=Subscript(
                                value=Name(id='args', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=Subscript(
                                value=Name(id='args', ctx=Load()),
                                slice=Slice(
                                    lower=Constant(value=1, kind=None),
                                    upper=None,
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Name(id='command', ctx=Load()),
                        ops=[In()],
                        comparators=[Name(id='commands', ctx=Load())],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='o', ctx=Store())],
                            value=Call(
                                func=Subscript(
                                    value=Name(id='commands', ctx=Load()),
                                    slice=Name(id='command', ctx=Load()),
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='o', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='exit',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='Unknown command %r', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[Name(id='command', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
