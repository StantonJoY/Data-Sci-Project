Module(
    body=[
        ImportFrom(
            module='__future__',
            names=[alias(name='print_function', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='argparse', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='jinja2', asname=None)],
        ),
        ImportFrom(
            module=None,
            names=[alias(name='Command', asname=None)],
            level=1,
        ),
        ClassDef(
            name='Scaffold',
            bases=[Name(id='Command', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Generates an Odoo module skeleton. ', kind=None),
                ),
                FunctionDef(
                    name='run',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cmdargs', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='parser', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='argparse', ctx=Load()),
                                    attr='ArgumentParser',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='prog',
                                        value=BinOp(
                                            left=Constant(value='%s scaffold', kind=None),
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
                                    ),
                                    keyword(
                                        arg='description',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='__doc__',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='epilog',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='epilog',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_argument',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-t', kind=None),
                                    Constant(value='--template', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='type',
                                        value=Name(id='template', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='default',
                                        value=Call(
                                            func=Name(id='template', ctx=Load()),
                                            args=[Constant(value='default', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Use a custom module template, can be a template name or the path to a module template (default: %(default)s)', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_argument',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='name', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Name of the module to create', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_argument',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='dest', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value='.', kind=None),
                                    ),
                                    keyword(
                                        arg='nargs',
                                        value=Constant(value='?', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Directory to create the module in (default: %(default)s)', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='cmdargs', ctx=Load()),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sys', ctx=Load()),
                                            attr='exit',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='parser', ctx=Load()),
                                                    attr='print_help',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='parse_args',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='args',
                                        value=Name(id='cmdargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='args', ctx=Load()),
                                        attr='template',
                                        ctx=Load(),
                                    ),
                                    attr='render_to',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='snake', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='directory', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='dest',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='create',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='epilog',
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
                        Return(
                            value=BinOp(
                                left=Constant(value='Built-in templates available are: %s', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Attribute(
                                        value=Constant(value=', ', kind=None),
                                        attr='join',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        GeneratorExp(
                                            elt=Name(id='d', ctx=Load()),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='d', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='listdir',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='builtins', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    ifs=[
                                                        Compare(
                                                            left=Name(id='d', ctx=Load()),
                                                            ops=[NotEq()],
                                                            comparators=[Constant(value='base', kind=None)],
                                                        ),
                                                    ],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
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
            targets=[Name(id='builtins', ctx=Store())],
            value=Lambda(
                args=arguments(
                    posonlyargs=[],
                    args=[],
                    vararg=arg(arg='args', annotation=None, type_comment=None),
                    kwonlyargs=[],
                    kw_defaults=[],
                    kwarg=None,
                    defaults=[],
                ),
                body=Call(
                    func=Attribute(
                        value=Attribute(
                            value=Name(id='os', ctx=Load()),
                            attr='path',
                            ctx=Load(),
                        ),
                        attr='join',
                        ctx=Load(),
                    ),
                    args=[
                        Call(
                            func=Attribute(
                                value=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='path',
                                    ctx=Load(),
                                ),
                                attr='abspath',
                                ctx=Load(),
                            ),
                            args=[
                                Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='dirname',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='__file__', ctx=Load())],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                        Constant(value='templates', kind=None),
                        Starred(
                            value=Name(id='args', ctx=Load()),
                            ctx=Load(),
                        ),
                    ],
                    keywords=[],
                ),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='snake',
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
                    value=Constant(value=' snake cases ``s``\n\n    :param str s:\n    :return: str\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='s', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='(?<=[^A-Z])\\B([A-Z])', kind=None),
                            Constant(value=' \\1', kind=None),
                            Name(id='s', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Constant(value='_', kind=None),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='s', ctx=Load()),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
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
            name='pascal',
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
                Return(
                    value=Call(
                        func=Attribute(
                            value=Constant(value='', kind=None),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[
                            GeneratorExp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='ss', ctx=Load()),
                                        attr='capitalize',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='ss', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='re', ctx=Load()),
                                                        attr='sub',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='[_\\s]+', kind=None),
                                                        Constant(value=' ', kind=None),
                                                        Name(id='s', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
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
            name='directory',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='p', annotation=None, type_comment=None),
                    arg(arg='create', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='expanded', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='abspath',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='expanduser',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='expandvars',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='p', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
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
                            Name(id='create', ctx=Load()),
                            UnaryOp(
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
                                    args=[Name(id='expanded', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='makedirs',
                                    ctx=Load(),
                                ),
                                args=[Name(id='expanded', ctx=Load())],
                                keywords=[],
                            ),
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
                                attr='isdir',
                                ctx=Load(),
                            ),
                            args=[Name(id='expanded', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='die', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='%s is not a directory', kind=None),
                                        op=Mod(),
                                        right=Name(id='p', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='expanded', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='env', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='jinja2', ctx=Load()),
                    attr='Environment',
                    ctx=Load(),
                ),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Subscript(
                    value=Attribute(
                        value=Name(id='env', ctx=Load()),
                        attr='filters',
                        ctx=Load(),
                    ),
                    slice=Constant(value='snake', kind=None),
                    ctx=Store(),
                ),
            ],
            value=Name(id='snake', ctx=Load()),
            type_comment=None,
        ),
        Assign(
            targets=[
                Subscript(
                    value=Attribute(
                        value=Name(id='env', ctx=Load()),
                        attr='filters',
                        ctx=Load(),
                    ),
                    slice=Constant(value='pascal', kind=None),
                    ctx=Store(),
                ),
            ],
            value=Name(id='pascal', ctx=Load()),
            type_comment=None,
        ),
        ClassDef(
            name='template',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='identifier', annotation=None, type_comment=None),
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
                                    attr='id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='identifier', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='path',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='builtins', ctx=Load()),
                                args=[Name(id='identifier', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='isdir',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='path',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='identifier', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='isdir',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='die', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='{} is not a valid module template', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='identifier', ctx=Load())],
                                        keywords=[],
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
                    name='__str__',
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
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='files',
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
                            value=Constant(value=' Lists the (local) path and content of all files in the template\n        ', kind=None),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='root', ctx=Store()),
                                    Name(id='_', ctx=Store()),
                                    Name(id='files', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='walk',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='f', ctx=Store()),
                                    iter=Name(id='files', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='root', ctx=Load()),
                                                    Name(id='f', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Yield(
                                                value=Tuple(
                                                    elts=[
                                                        Name(id='path', ctx=Load()),
                                                        Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Name(id='open', ctx=Load()),
                                                                    args=[
                                                                        Name(id='path', ctx=Load()),
                                                                        Constant(value='rb', kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='read',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
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
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='render_to',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='modname', annotation=None, type_comment=None),
                            arg(arg='directory', annotation=None, type_comment=None),
                            arg(arg='params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Render this module template to ``dest`` with the provided\n         rendering parameters\n        ', kind=None),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='path', ctx=Store()),
                                    Name(id='content', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='files',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='local', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='relpath',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='path', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='root', ctx=Store()),
                                                Name(id='ext', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='splitext',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='local', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='ext', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='.template', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='local', ctx=Store())],
                                            value=Name(id='root', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='dest', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='directory', ctx=Load()),
                                            Name(id='modname', ctx=Load()),
                                            Name(id='local', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='destdir', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='dirname',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='dest', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
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
                                            args=[Name(id='destdir', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='makedirs',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='destdir', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='open', ctx=Load()),
                                                args=[
                                                    Name(id='dest', ctx=Load()),
                                                    Constant(value='wb', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='f', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='ext', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='.py', kind=None),
                                                            Constant(value='.xml', kind=None),
                                                            Constant(value='.csv', kind=None),
                                                            Constant(value='.js', kind=None),
                                                            Constant(value='.rst', kind=None),
                                                            Constant(value='.html', kind=None),
                                                            Constant(value='.template', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='f', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='content', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='env', ctx=Load()),
                                                                            attr='from_string',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='content', ctx=Load()),
                                                                                    attr='decode',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='utf-8', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='stream',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Name(id='params', ctx=Load()),
                                                                            Dict(keys=[], values=[]),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='dump',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='f', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='encoding',
                                                                value=Constant(value='utf-8', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    type_comment=None,
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
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='die',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='message', annotation=None, type_comment=None),
                    arg(arg='code', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=1, kind=None)],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[Name(id='message', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='file',
                                value=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='stderr',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='sys', ctx=Load()),
                            attr='exit',
                            ctx=Load(),
                        ),
                        args=[Name(id='code', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='warn',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='message', annotation=None, type_comment=None)],
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
                        args=[
                            Constant(value='WARNING:', kind=None),
                            Name(id='message', ctx=Load()),
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
    type_ignores=[],
)
