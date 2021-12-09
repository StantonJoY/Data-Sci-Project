Module(
    body=[
        ImportFrom(
            module='__future__',
            names=[alias(name='print_function', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='code', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='signal', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='config', asname=None)],
            level=0,
        ),
        ImportFrom(
            module=None,
            names=[alias(name='Command', asname=None)],
            level=1,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Expr(
            value=Constant(value='\n    Shell exit behaviors\n    ====================\n\n    Legend:\n        stop = The REPL main loop stop.\n        raise = Exception raised.\n        loop = Stay in REPL.\n\n   Shell  | ^D    | exit() | quit() | sys.exit() | raise SystemExit()\n----------------------------------------------------------------------\n python   | stop  | raise  | raise  | raise      | raise\n ipython  | stop  | stop   | stop   | loop       | loop\n ptpython | stop  | raise  | raise  | raise      | raise\n bpython  | stop  | stop   | stop   | stop       | stop\n\n', kind=None),
        ),
        FunctionDef(
            name='raise_keyboard_interrupt',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=arg(arg='a', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Raise(
                    exc=Call(
                        func=Name(id='KeyboardInterrupt', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    cause=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='Console',
            bases=[
                Attribute(
                    value=Name(id='code', ctx=Load()),
                    attr='InteractiveConsole',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='locals', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='<console>', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='code', ctx=Load()),
                                        attr='InteractiveConsole',
                                        ctx=Load(),
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='locals', ctx=Load()),
                                    Name(id='filename', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Import(
                                    names=[alias(name='readline', asname=None)],
                                ),
                                Import(
                                    names=[alias(name='rlcompleter', asname=None)],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ImportError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='print', ctx=Load()),
                                                args=[Constant(value='readline or rlcompleter not available, autocomplete disabled.', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='readline', ctx=Load()),
                                            attr='set_completer',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='rlcompleter', ctx=Load()),
                                                        attr='Completer',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='locals', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='complete',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='readline', ctx=Load()),
                                            attr='parse_and_bind',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='tab: complete', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            finalbody=[],
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
            name='Shell',
            bases=[Name(id='Command', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Start odoo in an interactive shell', kind=None),
                ),
                Assign(
                    targets=[Name(id='supported_shells', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='ipython', kind=None),
                            Constant(value='ptpython', kind=None),
                            Constant(value='bpython', kind=None),
                            Constant(value='python', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='init',
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
                                func=Attribute(
                                    value=Name(id='config', ctx=Load()),
                                    attr='parse_config',
                                    ctx=Load(),
                                ),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='cli',
                                            ctx=Load(),
                                        ),
                                        attr='server',
                                        ctx=Load(),
                                    ),
                                    attr='report_configuration',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='service',
                                            ctx=Load(),
                                        ),
                                        attr='server',
                                        ctx=Load(),
                                    ),
                                    attr='start',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='preload',
                                        value=List(elts=[], ctx=Load()),
                                    ),
                                    keyword(
                                        arg='stop',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='signal', ctx=Load()),
                                    attr='signal',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='signal', ctx=Load()),
                                        attr='SIGINT',
                                        ctx=Load(),
                                    ),
                                    Name(id='raise_keyboard_interrupt', ctx=Load()),
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
                    name='console',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='local_vars', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='isatty',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='sys', ctx=Load()),
                                                    attr='stdin',
                                                    ctx=Load(),
                                                ),
                                                attr='fileno',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='local_vars', ctx=Load()),
                                            slice=Constant(value='__name__', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='__main__', kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='exec', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='sys', ctx=Load()),
                                                        attr='stdin',
                                                        ctx=Load(),
                                                    ),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Name(id='local_vars', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Constant(value='env', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='local_vars', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='print', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='No environment set, use `%s shell -d dbname` to get one.', kind=None),
                                                        op=Mod(),
                                                        right=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='sys', ctx=Load()),
                                                                attr='argv',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='i', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[Name(id='local_vars', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='print', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='%s: %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='i', ctx=Load()),
                                                                Subscript(
                                                                    value=Name(id='local_vars', ctx=Load()),
                                                                    slice=Name(id='i', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
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
                                Assign(
                                    targets=[Name(id='preferred_interface', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='config', ctx=Load()),
                                                attr='options',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='shell_interface', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='preferred_interface', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='shells_to_try', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Name(id='preferred_interface', ctx=Load()),
                                                    Constant(value='python', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='shells_to_try', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='supported_shells',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                For(
                                    target=Name(id='shell', ctx=Store()),
                                    iter=Name(id='shells_to_try', ctx=Load()),
                                    body=[
                                        Try(
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Call(
                                                            func=Name(id='getattr', ctx=Load()),
                                                            args=[
                                                                Name(id='self', ctx=Load()),
                                                                Name(id='shell', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        args=[Name(id='local_vars', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='ImportError', ctx=Load()),
                                                    name=None,
                                                    body=[Pass()],
                                                ),
                                                ExceptHandler(
                                                    type=Name(id='Exception', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='warning',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Constant(value="Could not start '%s' shell.", kind=None),
                                                                        op=Mod(),
                                                                        right=Name(id='shell', ctx=Load()),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='debug',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='Shell error:', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='exc_info',
                                                                        value=Constant(value=True, kind=None),
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
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='ipython',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='local_vars', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        ImportFrom(
                            module='IPython',
                            names=[alias(name='start_ipython', asname=None)],
                            level=0,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='start_ipython', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='argv',
                                        value=List(elts=[], ctx=Load()),
                                    ),
                                    keyword(
                                        arg='user_ns',
                                        value=Name(id='local_vars', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='ptpython',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='local_vars', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        ImportFrom(
                            module='ptpython.repl',
                            names=[alias(name='embed', asname=None)],
                            level=0,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='embed', ctx=Load()),
                                args=[
                                    Dict(keys=[], values=[]),
                                    Name(id='local_vars', ctx=Load()),
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
                    name='bpython',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='local_vars', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        ImportFrom(
                            module='bpython',
                            names=[alias(name='embed', asname=None)],
                            level=0,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='embed', ctx=Load()),
                                args=[Name(id='local_vars', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='python',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='local_vars', annotation=None, type_comment=None),
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
                                        func=Name(id='Console', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='locals',
                                                value=Name(id='local_vars', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    attr='interact',
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
                FunctionDef(
                    name='shell',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='dbname', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='local_vars', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='openerp', kind=None),
                                    Constant(value='odoo', kind=None),
                                ],
                                values=[
                                    Name(id='odoo', ctx=Load()),
                                    Name(id='odoo', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='dbname', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='registry', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='dbname', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='registry', ctx=Load()),
                                                    attr='cursor',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='cr', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='uid', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='SUPERUSER_ID',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='ctx', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='odoo', ctx=Load()),
                                                                    attr='api',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='Environment',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(id='cr', ctx=Load()),
                                                                Name(id='uid', ctx=Load()),
                                                                Dict(keys=[], values=[]),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value='res.users', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='context_get',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='env', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='api',
                                                        ctx=Load(),
                                                    ),
                                                    attr='Environment',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='cr', ctx=Load()),
                                                    Name(id='uid', ctx=Load()),
                                                    Name(id='ctx', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='local_vars', ctx=Load()),
                                                    slice=Constant(value='env', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='env', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='local_vars', ctx=Load()),
                                                    slice=Constant(value='self', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='env', ctx=Load()),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='console',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='local_vars', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cr', ctx=Load()),
                                                    attr='rollback',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='console',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='local_vars', ctx=Load())],
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
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='init',
                                    ctx=Load(),
                                ),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='shell',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='db_name', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Constant(value=0, kind=None),
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
