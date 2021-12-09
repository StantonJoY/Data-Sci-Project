Module(
    body=[
        Expr(
            value=Constant(value='\nOpenERP - Server\nOpenERP is an ERP+CRM program for small and medium businesses.\n\nThe whole source code is distributed under the terms of the\nGNU Public Licence.\n\n(c) 2003-TODAY, Fabien Pinckaers - OpenERP SA\n', kind=None),
        ),
        Import(
            names=[alias(name='atexit', asname=None)],
        ),
        Import(
            names=[alias(name='csv', asname=None)],
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
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='traceback', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='psycopg2',
            names=[
                alias(name='ProgrammingError', asname=None),
                alias(name='errorcodes', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module=None,
            names=[alias(name='Command', asname=None)],
            level=1,
        ),
        Assign(
            targets=[Name(id='__author__', ctx=Store())],
            value=Attribute(
                value=Attribute(
                    value=Name(id='odoo', ctx=Load()),
                    attr='release',
                    ctx=Load(),
                ),
                attr='author',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='__version__', ctx=Store())],
            value=Attribute(
                value=Attribute(
                    value=Name(id='odoo', ctx=Load()),
                    attr='release',
                    ctx=Load(),
                ),
                attr='version',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Constant(value='odoo', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='check_root_user',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value="Warn if the process's user is 'root' (on POSIX system).", kind=None),
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='os', ctx=Load()),
                            attr='name',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='posix', kind=None)],
                    ),
                    body=[
                        Import(
                            names=[alias(name='getpass', asname=None)],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='getpass', ctx=Load()),
                                        attr='getuser',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='root', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='sys', ctx=Load()),
                                                attr='stderr',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value="Running as user 'root' is a security risk.\n", kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
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
            name='check_postgres_user',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value=" Exit if the configured database user is 'postgres'.\n\n    This function assumes the configuration has been initialized.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='config', ctx=Store())],
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tools',
                            ctx=Load(),
                        ),
                        attr='config',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=BoolOp(
                            op=Or(),
                            values=[
                                Subscript(
                                    value=Name(id='config', ctx=Load()),
                                    slice=Constant(value='db_user', kind=None),
                                    ctx=Load(),
                                ),
                                Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='environ',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='PGUSER', kind=None)],
                                    keywords=[],
                                ),
                            ],
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='postgres', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='sys', ctx=Load()),
                                        attr='stderr',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="Using the database user 'postgres' is a security risk, aborting.", kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='exit',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=1, kind=None)],
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
            name='report_configuration',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value=' Log the server version and some configuration values.\n\n    This function assumes the configuration has been initialized.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='config', ctx=Store())],
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tools',
                            ctx=Load(),
                        ),
                        attr='config',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Odoo version %s', kind=None),
                            Name(id='__version__', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='isfile',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='config', ctx=Load()),
                                attr='rcfile',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='Using configuration file at ', kind=None),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='config', ctx=Load()),
                                            attr='rcfile',
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
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='addons paths: %s', kind=None),
                            Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='addons',
                                    ctx=Load(),
                                ),
                                attr='__path__',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=Name(id='config', ctx=Load()),
                            attr='get',
                            ctx=Load(),
                        ),
                        args=[Constant(value='upgrade_path', kind=None)],
                        keywords=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='upgrade path: %s', kind=None),
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='upgrade_path', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='host', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='db_host', kind=None),
                                ctx=Load(),
                            ),
                            Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='environ',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='PGHOST', kind=None),
                                    Constant(value='default', kind=None),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='port', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='db_port', kind=None),
                                ctx=Load(),
                            ),
                            Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='environ',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='PGPORT', kind=None),
                                    Constant(value='default', kind=None),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='db_user', kind=None),
                                ctx=Load(),
                            ),
                            Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='environ',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='PGUSER', kind=None),
                                    Constant(value='default', kind=None),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='database: %s@%s:%s', kind=None),
                            Name(id='user', ctx=Load()),
                            Name(id='host', ctx=Load()),
                            Name(id='port', ctx=Load()),
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
            name='rm_pid_file',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='main_pid', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='config', ctx=Store())],
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tools',
                            ctx=Load(),
                        ),
                        attr='config',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='pidfile', kind=None),
                                ctx=Load(),
                            ),
                            Compare(
                                left=Name(id='main_pid', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='getpid',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='pidfile', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='OSError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
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
            name='setup_pid_file',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value=' Create a file with the process id written in it.\n\n    This function assumes the configuration has been initialized.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='config', ctx=Store())],
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tools',
                            ctx=Load(),
                        ),
                        attr='config',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='evented',
                                    ctx=Load(),
                                ),
                            ),
                            Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='pidfile', kind=None),
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='pid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='getpid',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='pidfile', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value='w', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='fd', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fd', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='pid', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='atexit', ctx=Load()),
                                    attr='register',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='rm_pid_file', ctx=Load()),
                                    Name(id='pid', ctx=Load()),
                                ],
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
            name='export_translation',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='config', ctx=Store())],
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tools',
                            ctx=Load(),
                        ),
                        attr='config',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='dbname', ctx=Store())],
                    value=Subscript(
                        value=Name(id='config', ctx=Load()),
                        slice=Constant(value='db_name', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Subscript(
                        value=Name(id='config', ctx=Load()),
                        slice=Constant(value='language', kind=None),
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='language %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='config', ctx=Load()),
                                            slice=Constant(value='language', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=Constant(value='new language', kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='writing translation file for %s to %s', kind=None),
                            Name(id='msg', ctx=Load()),
                            Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='translate_out', kind=None),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='fileformat', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Subscript(
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
                                        args=[
                                            Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='translate_out', kind=None),
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
                                slice=Slice(
                                    lower=Constant(value=1, kind=None),
                                    upper=None,
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            attr='lower',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Name(id='open', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='translate_out', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='wb', kind=None),
                                ],
                                keywords=[],
                            ),
                            optional_vars=Name(id='buf', ctx=Store()),
                        ),
                    ],
                    body=[
                        Assign(
                            targets=[Name(id='registry', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='modules',
                                                ctx=Load(),
                                            ),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        attr='Registry',
                                        ctx=Load(),
                                    ),
                                    attr='new',
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='tools',
                                                ctx=Load(),
                                            ),
                                            attr='trans_export',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='language', kind=None),
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='config', ctx=Load()),
                                                        slice=Constant(value='translate_modules', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[Constant(value='all', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Name(id='buf', ctx=Load()),
                                            Name(id='fileformat', ctx=Load()),
                                            Name(id='cr', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[Constant(value='translation file written successfully', kind=None)],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='import_translation',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='config', ctx=Store())],
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tools',
                            ctx=Load(),
                        ),
                        attr='config',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='overwrite', ctx=Store())],
                    value=Subscript(
                        value=Name(id='config', ctx=Load()),
                        slice=Constant(value='overwrite_existing_translations', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='dbname', ctx=Store())],
                    value=Subscript(
                        value=Name(id='config', ctx=Load()),
                        slice=Constant(value='db_name', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='registry', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                    attr='registry',
                                    ctx=Load(),
                                ),
                                attr='Registry',
                                ctx=Load(),
                            ),
                            attr='new',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='tools',
                                        ctx=Load(),
                                    ),
                                    attr='trans_load',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='translate_in', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='language', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='overwrite',
                                        value=Name(id='overwrite', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='main',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='args', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Name(id='check_root_user', ctx=Load()),
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
                                    attr='tools',
                                    ctx=Load(),
                                ),
                                attr='config',
                                ctx=Load(),
                            ),
                            attr='parse_config',
                            ctx=Load(),
                        ),
                        args=[Name(id='args', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='check_postgres_user', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='report_configuration', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='config', ctx=Store())],
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tools',
                            ctx=Load(),
                        ),
                        attr='config',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='csv', ctx=Load()),
                            attr='field_size_limit',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=BinOp(
                                    left=Constant(value=500, kind=None),
                                    op=Mult(),
                                    right=Constant(value=1024, kind=None),
                                ),
                                op=Mult(),
                                right=Constant(value=1024, kind=None),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='preload', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                If(
                    test=Subscript(
                        value=Name(id='config', ctx=Load()),
                        slice=Constant(value='db_name', kind=None),
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='preload', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='db_name', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=',', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='db_name', ctx=Store()),
                            iter=Name(id='preload', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='odoo', ctx=Load()),
                                                            attr='service',
                                                            ctx=Load(),
                                                        ),
                                                        attr='db',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_create_empty_database',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='db_name', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='config', ctx=Load()),
                                                        slice=Constant(value='init', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='base', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ProgrammingError', ctx=Load()),
                                            name='err',
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='err', ctx=Load()),
                                                            attr='pgcode',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='errorcodes', ctx=Load()),
                                                                attr='INSUFFICIENT_PRIVILEGE',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='info',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='Could not determine if database %s exists, skipping auto-creation: %s', kind=None),
                                                                    Name(id='db_name', ctx=Load()),
                                                                    Name(id='err', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Raise(
                                                            exc=Name(id='err', ctx=Load()),
                                                            cause=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='service',
                                                        ctx=Load(),
                                                    ),
                                                    attr='db',
                                                    ctx=Load(),
                                                ),
                                                attr='DatabaseExists',
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[Pass()],
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
                    orelse=[],
                ),
                If(
                    test=Subscript(
                        value=Name(id='config', ctx=Load()),
                        slice=Constant(value='translate_out', kind=None),
                        ctx=Load(),
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='export_translation', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='exit',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=0, kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Subscript(
                        value=Name(id='config', ctx=Load()),
                        slice=Constant(value='translate_in', kind=None),
                        ctx=Load(),
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='import_translation', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='exit',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=0, kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Subscript(
                        value=Name(id='config', ctx=Load()),
                        slice=Constant(value='workers', kind=None),
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='multi_process',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='stop', ctx=Store())],
                    value=Subscript(
                        value=Name(id='config', ctx=Load()),
                        slice=Constant(value='stop_after_init', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='setup_pid_file', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='rc', ctx=Store())],
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
                                value=Name(id='preload', ctx=Load()),
                            ),
                            keyword(
                                arg='stop',
                                value=Name(id='stop', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='sys', ctx=Load()),
                            attr='exit',
                            ctx=Load(),
                        ),
                        args=[Name(id='rc', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='Server',
            bases=[Name(id='Command', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Start the odoo server (default command)', kind=None),
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
                                func=Name(id='main', ctx=Load()),
                                args=[Name(id='args', ctx=Load())],
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
