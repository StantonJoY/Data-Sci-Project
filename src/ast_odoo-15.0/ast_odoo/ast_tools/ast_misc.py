Module(
    body=[
        Expr(
            value=Constant(value='\nMiscellaneous tools used by OpenERP.\n', kind=None),
        ),
        Import(
            names=[alias(name='cProfile', asname=None)],
        ),
        Import(
            names=[alias(name='collections', asname=None)],
        ),
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='hmac', asname='hmac_lib')],
        ),
        Import(
            names=[alias(name='hashlib', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='pickle', asname='pickle_')],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='socket', asname=None)],
        ),
        Import(
            names=[alias(name='subprocess', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='traceback', asname=None)],
        ),
        Import(
            names=[alias(name='types', asname=None)],
        ),
        Import(
            names=[alias(name='unicodedata', asname=None)],
        ),
        Import(
            names=[alias(name='zipfile', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='OrderedDict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='collections.abc',
            names=[
                alias(name='Iterable', asname=None),
                alias(name='Mapping', asname=None),
                alias(name='MutableMapping', asname=None),
                alias(name='MutableSet', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='contextlib',
            names=[alias(name='contextmanager', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='difflib',
            names=[alias(name='HtmlDiff', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='functools',
            names=[alias(name='wraps', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='itertools',
            names=[
                alias(name='islice', asname=None),
                alias(name='groupby', asname='itergroupby'),
            ],
            level=0,
        ),
        ImportFrom(
            module='operator',
            names=[alias(name='itemgetter', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='babel', asname=None)],
        ),
        Import(
            names=[alias(name='babel.dates', asname=None)],
        ),
        Import(
            names=[alias(name='markupsafe', asname=None)],
        ),
        Import(
            names=[alias(name='passlib.utils', asname=None)],
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.utils', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.addons', asname=None)],
        ),
        ImportFrom(
            module='odoo.loglevels',
            names=[
                alias(name='get_encodings', asname=None),
                alias(name='ustr', asname=None),
                alias(name='exception_to_unicode', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module=None,
            names=[alias(name='pycompat', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='cache',
            names=[alias(name='*', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='config',
            names=[alias(name='config', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='parse_version',
            names=[alias(name='parse_version', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='which',
            names=[alias(name='which', asname=None)],
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
        Assign(
            targets=[Name(id='SKIPPED_ELEMENT_TYPES', ctx=Store())],
            value=Tuple(
                elts=[
                    Attribute(
                        value=Name(id='etree', ctx=Load()),
                        attr='_Comment',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='etree', ctx=Load()),
                        attr='_ProcessingInstruction',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='etree', ctx=Load()),
                        attr='CommentBase',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='etree', ctx=Load()),
                        attr='PIBase',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='etree', ctx=Load()),
                        attr='_Entity',
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='etree', ctx=Load()),
                    attr='set_default_parser',
                    ctx=Load(),
                ),
                args=[
                    Call(
                        func=Attribute(
                            value=Name(id='etree', ctx=Load()),
                            attr='XMLParser',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='resolve_entities',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                ],
                keywords=[],
            ),
        ),
        FunctionDef(
            name='find_in_path',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='name', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='path', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
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
                                    Constant(value='PATH', kind=None),
                                    Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='defpath',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='pathsep',
                                ctx=Load(),
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
                            Call(
                                func=Attribute(
                                    value=Name(id='config', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='bin_path', kind=None)],
                                keywords=[],
                            ),
                            Compare(
                                left=Subscript(
                                    value=Name(id='config', ctx=Load()),
                                    slice=Constant(value='bin_path', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='None', kind=None)],
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='path', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='bin_path', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Name(id='which', ctx=Load()),
                        args=[Name(id='name', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='path',
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='pathsep',
                                            ctx=Load(),
                                        ),
                                        attr='join',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='path', ctx=Load())],
                                    keywords=[],
                                ),
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
            name='_exec_pipe',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='prog', annotation=None, type_comment=None),
                    arg(arg='args', annotation=None, type_comment=None),
                    arg(arg='env', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='cmd', ctx=Store())],
                    value=BinOp(
                        left=Tuple(
                            elts=[Name(id='prog', ctx=Load())],
                            ctx=Load(),
                        ),
                        op=Add(),
                        right=Name(id='args', ctx=Load()),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='close_fds', ctx=Store())],
                    value=Compare(
                        left=Attribute(
                            value=Name(id='os', ctx=Load()),
                            attr='name',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='posix', kind=None)],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='pop', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='subprocess', ctx=Load()),
                            attr='Popen',
                            ctx=Load(),
                        ),
                        args=[Name(id='cmd', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='bufsize',
                                value=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                            ),
                            keyword(
                                arg='stdin',
                                value=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='PIPE',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='stdout',
                                value=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='PIPE',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='close_fds',
                                value=Name(id='close_fds', ctx=Load()),
                            ),
                            keyword(
                                arg='env',
                                value=Name(id='env', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Attribute(
                                value=Name(id='pop', ctx=Load()),
                                attr='stdin',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='pop', ctx=Load()),
                                attr='stdout',
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exec_command_pipe',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='name', annotation=None, type_comment=None)],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='prog', ctx=Store())],
                    value=Call(
                        func=Name(id='find_in_path', ctx=Load()),
                        args=[Name(id='name', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='prog', ctx=Load()),
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='Exception', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='Command `%s` not found.', kind=None),
                                        op=Mod(),
                                        right=Name(id='name', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Name(id='_exec_pipe', ctx=Load()),
                        args=[
                            Name(id='prog', ctx=Load()),
                            Name(id='args', ctx=Load()),
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
            name='find_pg_tool',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='name', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='path', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='pg_path', kind=None),
                                ctx=Load(),
                            ),
                            Compare(
                                left=Subscript(
                                    value=Name(id='config', ctx=Load()),
                                    slice=Constant(value='pg_path', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='None', kind=None)],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='pg_path', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Try(
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='which', ctx=Load()),
                                args=[Name(id='name', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='path',
                                        value=Name(id='path', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='IOError', ctx=Load()),
                            name=None,
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Command `%s` not found.', kind=None),
                                                op=Mod(),
                                                right=Name(id='name', ctx=Load()),
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
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exec_pg_environ',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value='\n    Force the database PostgreSQL environment variables to the database\n    configuration of Odoo.\n\n    Note: On systems where pg_restore/pg_dump require an explicit password\n    (i.e.  on Windows where TCP sockets are used), it is necessary to pass the\n    postgres user password in the PGPASSWORD environment variable or in a\n    special .pgpass file.\n\n    See also http://www.postgresql.org/docs/8.4/static/libpq-envars.html\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='env', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='environ',
                                ctx=Load(),
                            ),
                            attr='copy',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Subscript(
                        value=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='tools',
                                ctx=Load(),
                            ),
                            attr='config',
                            ctx=Load(),
                        ),
                        slice=Constant(value='db_host', kind=None),
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='env', ctx=Load()),
                                    slice=Constant(value='PGHOST', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='tools',
                                        ctx=Load(),
                                    ),
                                    attr='config',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='db_host', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Subscript(
                        value=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='tools',
                                ctx=Load(),
                            ),
                            attr='config',
                            ctx=Load(),
                        ),
                        slice=Constant(value='db_port', kind=None),
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='env', ctx=Load()),
                                    slice=Constant(value='PGPORT', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='str', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='tools',
                                                ctx=Load(),
                                            ),
                                            attr='config',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='db_port', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Subscript(
                        value=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='tools',
                                ctx=Load(),
                            ),
                            attr='config',
                            ctx=Load(),
                        ),
                        slice=Constant(value='db_user', kind=None),
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='env', ctx=Load()),
                                    slice=Constant(value='PGUSER', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='tools',
                                        ctx=Load(),
                                    ),
                                    attr='config',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='db_user', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Subscript(
                        value=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='tools',
                                ctx=Load(),
                            ),
                            attr='config',
                            ctx=Load(),
                        ),
                        slice=Constant(value='db_password', kind=None),
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='env', ctx=Load()),
                                    slice=Constant(value='PGPASSWORD', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='tools',
                                        ctx=Load(),
                                    ),
                                    attr='config',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='db_password', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='env', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exec_pg_command',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='name', annotation=None, type_comment=None)],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='prog', ctx=Store())],
                    value=Call(
                        func=Name(id='find_pg_tool', ctx=Load()),
                        args=[Name(id='name', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='env', ctx=Store())],
                    value=Call(
                        func=Name(id='exec_pg_environ', ctx=Load()),
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
                                    Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='devnull',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            optional_vars=Name(id='dn', ctx=Store()),
                        ),
                    ],
                    body=[
                        Assign(
                            targets=[Name(id='args2', ctx=Store())],
                            value=BinOp(
                                left=Tuple(
                                    elts=[Name(id='prog', ctx=Load())],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Name(id='args', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='call',
                                    ctx=Load(),
                                ),
                                args=[Name(id='args2', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='env',
                                        value=Name(id='env', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='stdout',
                                        value=Name(id='dn', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='stderr',
                                        value=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='STDOUT',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='rc', ctx=Load()),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Postgres subprocess %s error %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='args2', ctx=Load()),
                                                        Name(id='rc', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
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
            name='exec_pg_command_pipe',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='name', annotation=None, type_comment=None)],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='prog', ctx=Store())],
                    value=Call(
                        func=Name(id='find_pg_tool', ctx=Load()),
                        args=[Name(id='name', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='env', ctx=Store())],
                    value=Call(
                        func=Name(id='exec_pg_environ', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='_exec_pipe', ctx=Load()),
                        args=[
                            Name(id='prog', ctx=Load()),
                            Name(id='args', ctx=Load()),
                            Name(id='env', ctx=Load()),
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
            name='file_path',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='file_path', annotation=None, type_comment=None),
                    arg(arg='filter_ext', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Tuple(
                        elts=[Constant(value='', kind=None)],
                        ctx=Load(),
                    ),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value="Verify that a file exists under a known `addons_path` directory and return its full path.\n\n    Examples::\n\n    >>> file_path('hr')\n    >>> file_path('hr/static/description/icon.png')\n    >>> file_path('hr/static/description/icon.png', filter_ext=('.png', '.jpg'))\n\n    :param str file_path: absolute file path, or relative path within any `addons_path` directory\n    :param list[str] filter_ext: optional list of supported extensions (lowercase, with leading dot)\n    :return: the absolute path to the file\n    :raise FileNotFoundError: if the file is not found under the known `addons_path` directories\n    :raise ValueError: if the file doesn't have one of the supported extensions (`filter_ext`)\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='root_path', ctx=Store())],
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
                            Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='root_path', kind=None),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='addons_paths', ctx=Store())],
                    value=BinOp(
                        left=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='addons',
                                ctx=Load(),
                            ),
                            attr='__path__',
                            ctx=Load(),
                        ),
                        op=Add(),
                        right=List(
                            elts=[Name(id='root_path', ctx=Load())],
                            ctx=Load(),
                        ),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_abs', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='isabs',
                            ctx=Load(),
                        ),
                        args=[Name(id='file_path', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='normalized_path', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='normpath',
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
                                    attr='normcase',
                                    ctx=Load(),
                                ),
                                args=[Name(id='file_path', ctx=Load())],
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
                            Name(id='filter_ext', ctx=Load()),
                            UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='normalized_path', ctx=Load()),
                                                attr='lower',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='endswith',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='filter_ext', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValueError', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='Unsupported file: ', kind=None),
                                        op=Add(),
                                        right=Name(id='file_path', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=Name(id='normalized_path', ctx=Load()),
                            attr='startswith',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=Constant(value='addons', kind=None),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='sep',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='normalized_path', ctx=Store())],
                            value=Subscript(
                                value=Name(id='normalized_path', ctx=Load()),
                                slice=Slice(
                                    lower=Constant(value=7, kind=None),
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
                For(
                    target=Name(id='addons_dir', ctx=Store()),
                    iter=Name(id='addons_paths', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='parent_path', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='normpath',
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
                                                attr='normcase',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='addons_dir', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='sep',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fpath', ctx=Store())],
                            value=IfExp(
                                test=Name(id='is_abs', ctx=Load()),
                                body=Name(id='normalized_path', ctx=Load()),
                                orelse=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='normpath',
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
                                                attr='normcase',
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
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='parent_path', ctx=Load()),
                                                        Name(id='normalized_path', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='fpath', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='parent_path', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='fpath', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Name(id='fpath', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Raise(
                    exc=Call(
                        func=Name(id='FileNotFoundError', ctx=Load()),
                        args=[
                            BinOp(
                                left=Constant(value='File not found: ', kind=None),
                                op=Add(),
                                right=Name(id='file_path', ctx=Load()),
                            ),
                        ],
                        keywords=[],
                    ),
                    cause=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='file_open',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='name', annotation=None, type_comment=None),
                    arg(arg='mode', annotation=None, type_comment=None),
                    arg(arg='filter_ext', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value='r', kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value="Open a file from within the addons_path directories, as an absolute or relative path.\n\n    Examples::\n\n    >>> file_open('hr/static/description/icon.png')\n    >>> file_open('hr/static/description/icon.png', filter_ext=('.png', '.jpg'))\n    >>> with file_open('/opt/odoo/addons/hr/static/description/icon.png', 'rb') as f:\n    ...     contents = f.read()\n\n    :param name: absolute or relative path to a file located inside an addon\n    :param mode: file open mode, as for `open()`\n    :param list[str] filter_ext: optional list of supported extensions (lowercase, with leading dot)\n    :return: file object, as returned by `open()`\n    :raise FileNotFoundError: if the file is not found under the known `addons_path` directories\n    :raise ValueError: if the file doesn't have one of the supported extensions (`filter_ext`)\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='path', ctx=Store())],
                    value=Call(
                        func=Name(id='file_path', ctx=Load()),
                        args=[Name(id='name', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='filter_ext',
                                value=Name(id='filter_ext', ctx=Load()),
                            ),
                        ],
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
                            attr='isfile',
                            ctx=Load(),
                        ),
                        args=[Name(id='path', ctx=Load())],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='b', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='mode', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Name(id='path', ctx=Load()),
                                            Name(id='mode', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='encoding',
                                                value=Constant(value='utf-8', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='open', ctx=Load()),
                                args=[
                                    Name(id='path', ctx=Load()),
                                    Name(id='mode', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Raise(
                    exc=Call(
                        func=Name(id='FileNotFoundError', ctx=Load()),
                        args=[
                            BinOp(
                                left=Constant(value='Not a file: ', kind=None),
                                op=Add(),
                                right=Name(id='name', ctx=Load()),
                            ),
                        ],
                        keywords=[],
                    ),
                    cause=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='flatten',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='list', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value="Flatten a list of elements into a unique list\n    Author: Christophe Simonis (christophe@tinyerp.com)\n\n    Examples::\n    >>> flatten(['a'])\n    ['a']\n    >>> flatten('b')\n    ['b']\n    >>> flatten( [] )\n    []\n    >>> flatten( [[], [[]]] )\n    []\n    >>> flatten( [[['a','b'], 'c'], 'd', ['e', [], 'f']] )\n    ['a', 'b', 'c', 'd', 'e', 'f']\n    >>> t = (1,2,(3,), [4, 5, [6, [7], (8, 9), ([10, 11, (12, 13)]), [14, [], (15,)], []]])\n    >>> flatten(t)\n    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='r', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Name(id='e', ctx=Store()),
                    iter=Name(id='list', ctx=Load()),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='e', ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Name(id='bytes', ctx=Load()),
                                                    Name(id='str', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='isinstance', ctx=Load()),
                                            args=[
                                                Name(id='e', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='collections', ctx=Load()),
                                                    attr='Iterable',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='e', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='flatten', ctx=Load()),
                                                args=[Name(id='e', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='r', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='reverse_enumerate',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='l', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Like enumerate but in the other direction\n\n    Usage::\n    >>> a = [\'a\', \'b\', \'c\']\n    >>> it = reverse_enumerate(a)\n    >>> it.next()\n    (2, \'c\')\n    >>> it.next()\n    (1, \'b\')\n    >>> it.next()\n    (0, \'a\')\n    >>> it.next()\n    Traceback (most recent call last):\n      File "<stdin>", line 1, in <module>\n    StopIteration\n    ', kind=None),
                ),
                Return(
                    value=Call(
                        func=Name(id='zip', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='l', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            Call(
                                func=Name(id='reversed', ctx=Load()),
                                args=[Name(id='l', ctx=Load())],
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
            name='partition',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='pred', annotation=None, type_comment=None),
                    arg(arg='elems', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a pair equivalent to:\n        ``filter(pred, elems), filter(lambda x: not pred(x), elems)` ', kind=None),
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='yes', ctx=Store()),
                                Name(id='nos', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Tuple(
                        elts=[
                            List(elts=[], ctx=Load()),
                            List(elts=[], ctx=Load()),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='elem', ctx=Store()),
                    iter=Name(id='elems', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=IfExp(
                                        test=Call(
                                            func=Name(id='pred', ctx=Load()),
                                            args=[Name(id='elem', ctx=Load())],
                                            keywords=[],
                                        ),
                                        body=Name(id='yes', ctx=Load()),
                                        orelse=Name(id='nos', ctx=Load()),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='elem', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Name(id='yes', ctx=Load()),
                            Name(id='nos', ctx=Load()),
                        ],
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='topological_sort',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='elems', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a list of elements sorted so that their dependencies are listed\n    before them in the result.\n\n    :param elems: specifies the elements to sort with their dependencies; it is\n        a dictionary like `{element: dependencies}` where `dependencies` is a\n        collection of elements that must appear before `element`. The elements\n        of `dependencies` are not required to appear in `elems`; they will\n        simply not appear in the result.\n\n    :returns: a list with the keys of `elems` sorted according to their\n        specification.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='visited', ctx=Store())],
                    value=Call(
                        func=Name(id='set', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='visit',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='n', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='n', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[Name(id='visited', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='visited', ctx=Load()),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='n', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='n', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='elems', ctx=Load())],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='it', ctx=Store()),
                                            iter=Subscript(
                                                value=Name(id='elems', ctx=Load()),
                                                slice=Name(id='n', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='visit', ctx=Load()),
                                                        args=[Name(id='it', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='n', ctx=Load())],
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
                For(
                    target=Name(id='el', ctx=Store()),
                    iter=Name(id='elems', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='visit', ctx=Load()),
                                args=[Name(id='el', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='result', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='merge_sequences',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=arg(arg='iterables', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Merge several iterables into a list. The result is the union of the\n        iterables, ordered following the partial order given by the iterables,\n        with a bias towards the end for the last iterable::\n\n            seq = merge_sequences(['A', 'B', 'C'])\n            assert seq == ['A', 'B', 'C']\n\n            seq = merge_sequences(\n                ['A', 'B', 'C'],\n                ['Z'],                  # 'Z' can be anywhere\n                ['Y', 'C'],             # 'Y' must precede 'C';\n                ['A', 'X', 'Y'],        # 'X' must follow 'A' and precede 'Y'\n            )\n            assert seq == ['A', 'B', 'X', 'Y', 'C', 'Z']\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='deps', ctx=Store())],
                    value=Call(
                        func=Name(id='OrderedDict', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='iterable', ctx=Store()),
                    iter=Name(id='iterables', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='prev', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='index', ctx=Store()),
                                    Name(id='item', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='iterable', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='index', ctx=Load()),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='deps', ctx=Load()),
                                                    attr='setdefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='item', ctx=Load()),
                                                    List(elts=[], ctx=Load()),
                                                ],
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
                                                            value=Name(id='deps', ctx=Load()),
                                                            attr='setdefault',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='item', ctx=Load()),
                                                            List(elts=[], ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='prev', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='prev', ctx=Store())],
                                    value=Name(id='item', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='topological_sort', ctx=Load()),
                        args=[Name(id='deps', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Try(
            body=[
                Import(
                    names=[alias(name='xlwt', asname=None)],
                ),
                ClassDef(
                    name='PatchedWorkbook',
                    bases=[
                        Attribute(
                            value=Name(id='xlwt', ctx=Load()),
                            attr='Workbook',
                            ctx=Load(),
                        ),
                    ],
                    keywords=[],
                    body=[
                        FunctionDef(
                            name='add_sheet',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='self', annotation=None, type_comment=None),
                                    arg(arg='name', annotation=None, type_comment=None),
                                    arg(arg='cell_overwrite_ok', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[Constant(value=False, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='[\\[\\]:*?/\\\\]', kind=None),
                                            Constant(value='', kind=None),
                                            Name(id='name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='name', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=31, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='PatchedWorkbook', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='add_sheet',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='name', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='cell_overwrite_ok',
                                                value=Name(id='cell_overwrite_ok', ctx=Load()),
                                            ),
                                        ],
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
                            value=Name(id='xlwt', ctx=Load()),
                            attr='Workbook',
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='PatchedWorkbook', ctx=Load()),
                    type_comment=None,
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='xlwt', ctx=Store())],
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
                    names=[alias(name='xlsxwriter', asname=None)],
                ),
                ClassDef(
                    name='PatchedXlsxWorkbook',
                    bases=[
                        Attribute(
                            value=Name(id='xlsxwriter', ctx=Load()),
                            attr='Workbook',
                            ctx=Load(),
                        ),
                    ],
                    keywords=[],
                    body=[
                        FunctionDef(
                            name='add_worksheet',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='self', annotation=None, type_comment=None),
                                    arg(arg='name', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kw', annotation=None, type_comment=None),
                                defaults=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                If(
                                    test=Name(id='name', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='name', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='sub',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='[\\[\\]:*?/\\\\]', kind=None),
                                                    Constant(value='', kind=None),
                                                    Name(id='name', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='name', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='name', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=31, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
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
                                                    Name(id='PatchedXlsxWorkbook', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='add_worksheet',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='name', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='kw', ctx=Load()),
                                            ),
                                        ],
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
                            value=Name(id='xlsxwriter', ctx=Load()),
                            attr='Workbook',
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='PatchedXlsxWorkbook', ctx=Load()),
                    type_comment=None,
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='xlsxwriter', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        FunctionDef(
            name='to_xml',
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='s', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='&', kind=None),
                                            Constant(value='&amp;', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<', kind=None),
                                    Constant(value='&lt;', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='>', kind=None),
                            Constant(value='&gt;', kind=None),
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
            name='get_iso_codes',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='lang', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Compare(
                        left=Call(
                            func=Attribute(
                                value=Name(id='lang', ctx=Load()),
                                attr='find',
                                ctx=Load(),
                            ),
                            args=[Constant(value='_', kind=None)],
                            keywords=[],
                        ),
                        ops=[NotEq()],
                        comparators=[
                            UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lang', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='_', kind=None)],
                                        keywords=[],
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='_', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='lang', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='lang', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='_', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='lang', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='scan_languages',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value=' Returns all languages supported by OpenERP for translation\n\n    :returns: a list of (lang_code, lang_name) pairs\n    :rtype: [(str, unicode)]\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='csvpath', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='modules',
                                    ctx=Load(),
                                ),
                                attr='module',
                                ctx=Load(),
                            ),
                            attr='get_resource_path',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='base', kind=None),
                            Constant(value='data', kind=None),
                            Constant(value='res.lang.csv', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Name(id='csvpath', ctx=Load()),
                                            Constant(value='rb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='csvfile', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='reader', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='pycompat', ctx=Load()),
                                            attr='csv_reader',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='csvfile', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='delimiter',
                                                value=Constant(value=',', kind=None),
                                            ),
                                            keyword(
                                                arg='quotechar',
                                                value=Constant(value='"', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='fields', ctx=Store())],
                                    value=Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='reader', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='code_index', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fields', ctx=Load()),
                                            attr='index',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='code', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='name_index', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fields', ctx=Load()),
                                            attr='index',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Name(id='code_index', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Name(id='name_index', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='row', ctx=Store()),
                                                iter=Name(id='reader', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name=None,
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Could not read %s', kind=None),
                                            Name(id='csvpath', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
                Return(
                    value=Call(
                        func=Name(id='sorted', ctx=Load()),
                        args=[
                            BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='result', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='en_US', kind=None),
                                                    Constant(value='English', kind='u'),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='key',
                                value=Call(
                                    func=Name(id='itemgetter', ctx=Load()),
                                    args=[Constant(value=1, kind=None)],
                                    keywords=[],
                                ),
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
            name='mod10r',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='number', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Input number : account or invoice number\n    Output return: the same number completed with the recursive mod10\n    key\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='codec', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value=0, kind=None),
                            Constant(value=9, kind=None),
                            Constant(value=4, kind=None),
                            Constant(value=6, kind=None),
                            Constant(value=8, kind=None),
                            Constant(value=2, kind=None),
                            Constant(value=7, kind=None),
                            Constant(value=1, kind=None),
                            Constant(value=3, kind=None),
                            Constant(value=5, kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='report', ctx=Store())],
                    value=Constant(value=0, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=Constant(value='', kind=None),
                    type_comment=None,
                ),
                For(
                    target=Name(id='digit', ctx=Store()),
                    iter=Name(id='number', ctx=Load()),
                    body=[
                        AugAssign(
                            target=Name(id='result', ctx=Store()),
                            op=Add(),
                            value=Name(id='digit', ctx=Load()),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='digit', ctx=Load()),
                                    attr='isdigit',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='report', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='codec', ctx=Load()),
                                        slice=BinOp(
                                            left=BinOp(
                                                left=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[Name(id='digit', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Name(id='report', ctx=Load()),
                                            ),
                                            op=Mod(),
                                            right=Constant(value=10, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=BinOp(
                        left=Name(id='result', ctx=Load()),
                        op=Add(),
                        right=Call(
                            func=Name(id='str', ctx=Load()),
                            args=[
                                BinOp(
                                    left=BinOp(
                                        left=Constant(value=10, kind=None),
                                        op=Sub(),
                                        right=Name(id='report', ctx=Load()),
                                    ),
                                    op=Mod(),
                                    right=Constant(value=10, kind=None),
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
        FunctionDef(
            name='str2bool',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='s', annotation=None, type_comment=None),
                    arg(arg='default', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='s', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Name(id='ustr', ctx=Load()),
                                args=[Name(id='s', ctx=Load())],
                                keywords=[],
                            ),
                            attr='lower',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='y', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Constant(value='y yes 1 true t on', kind=None),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='n', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Constant(value='n no 0 false f off', kind=None),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='s', ctx=Load()),
                        ops=[NotIn()],
                        comparators=[
                            BinOp(
                                left=Name(id='y', ctx=Load()),
                                op=Add(),
                                right=Name(id='n', ctx=Load()),
                            ),
                        ],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='default', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[Constant(value='Use 0/1/yes/no/true/false/on/off', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[Name(id='default', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Compare(
                        left=Name(id='s', ctx=Load()),
                        ops=[In()],
                        comparators=[Name(id='y', ctx=Load())],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='human_size',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='sz', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Return the size in a human readable format\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='sz', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='units', ctx=Store())],
                    value=Tuple(
                        elts=[
                            Constant(value='bytes', kind=None),
                            Constant(value='Kb', kind=None),
                            Constant(value='Mb', kind=None),
                            Constant(value='Gb', kind=None),
                            Constant(value='Tb', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='sz', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='sz', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='sz', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='s', ctx=Store()),
                                Name(id='i', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Tuple(
                        elts=[
                            Call(
                                func=Name(id='float', ctx=Load()),
                                args=[Name(id='sz', ctx=Load())],
                                keywords=[],
                            ),
                            Constant(value=0, kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                While(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Name(id='s', ctx=Load()),
                                ops=[GtE()],
                                comparators=[Constant(value=1024, kind=None)],
                            ),
                            Compare(
                                left=Name(id='i', ctx=Load()),
                                ops=[Lt()],
                                comparators=[
                                    BinOp(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='units', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        AugAssign(
                            target=Name(id='s', ctx=Store()),
                            op=Div(),
                            value=Constant(value=1024, kind=None),
                        ),
                        AugAssign(
                            target=Name(id='i', ctx=Store()),
                            op=Add(),
                            value=Constant(value=1, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=BinOp(
                        left=Constant(value='%0.2f %s', kind=None),
                        op=Mod(),
                        right=Tuple(
                            elts=[
                                Name(id='s', ctx=Load()),
                                Subscript(
                                    value=Name(id='units', ctx=Load()),
                                    slice=Name(id='i', ctx=Load()),
                                    ctx=Load(),
                                ),
                            ],
                            ctx=Load(),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='logged',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='f', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                FunctionDef(
                    name='wrapper',
                    args=arguments(
                        posonlyargs=[],
                        args=[],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        ImportFrom(
                            module='pprint',
                            names=[alias(name='pformat', asname=None)],
                            level=0,
                        ),
                        Assign(
                            targets=[Name(id='vector', ctx=Store())],
                            value=List(
                                elts=[
                                    BinOp(
                                        left=Constant(value='Call -> function: %r', kind=None),
                                        op=Mod(),
                                        right=Name(id='f', ctx=Load()),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='i', ctx=Store()),
                                    Name(id='arg', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='vector', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='  arg %02d: %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='i', ctx=Load()),
                                                        Call(
                                                            func=Name(id='pformat', ctx=Load()),
                                                            args=[Name(id='arg', ctx=Load())],
                                                            keywords=[],
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
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='vector', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='  kwarg %10s: %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='key', ctx=Load()),
                                                        Call(
                                                            func=Name(id='pformat', ctx=Load()),
                                                            args=[Name(id='value', ctx=Load())],
                                                            keywords=[],
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
                            targets=[Name(id='timeb4', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='time',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Name(id='f', ctx=Load()),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='vector', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='  result: %s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='pformat', ctx=Load()),
                                            args=[Name(id='res', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='vector', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='  time delta: %s', kind=None),
                                        op=Mod(),
                                        right=BinOp(
                                            left=Call(
                                                func=Attribute(
                                                    value=Name(id='time', ctx=Load()),
                                                    attr='time',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            op=Sub(),
                                            right=Name(id='timeb4', ctx=Load()),
                                        ),
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
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='\n', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='vector', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='wraps', ctx=Load()),
                            args=[Name(id='f', ctx=Load())],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Name(id='wrapper', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='profile',
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
                        defaults=[Constant(value=None, kind=None)],
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__call__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='f', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='wrapper',
                            args=arguments(
                                posonlyargs=[],
                                args=[],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='profile', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cProfile', ctx=Load()),
                                            attr='Profile',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='profile', ctx=Load()),
                                            attr='runcall',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='f', ctx=Load()),
                                            Starred(
                                                value=Name(id='args', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='kwargs', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='profile', ctx=Load()),
                                            attr='dump_stats',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='fname',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='%s.cprof', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='f', ctx=Load()),
                                                                    attr='__name__',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='result', ctx=Load()),
                                ),
                            ],
                            decorator_list=[
                                Call(
                                    func=Name(id='wraps', ctx=Load()),
                                    args=[Name(id='f', ctx=Load())],
                                    keywords=[],
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='wrapper', ctx=Load()),
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
            name='detect_ip_addr',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value="Try a very crude method to figure out a valid external\n       IP or hostname for the current machine. Don't rely on this\n       for binding to an interface, but it could be used as basis\n       for constructing a remote URL to the server.\n    ", kind=None),
                ),
                FunctionDef(
                    name='_detect_ip_addr',
                    args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                    body=[
                        ImportFrom(
                            module='array',
                            names=[alias(name='array', asname=None)],
                            level=0,
                        ),
                        ImportFrom(
                            module='struct',
                            names=[
                                alias(name='pack', asname=None),
                                alias(name='unpack', asname=None),
                            ],
                            level=0,
                        ),
                        Try(
                            body=[
                                Import(
                                    names=[alias(name='fcntl', asname=None)],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ImportError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='fcntl', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='ip_addr', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='fcntl', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='host', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='socket', ctx=Load()),
                                            attr='gethostname',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ip_addr', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='socket', ctx=Load()),
                                            attr='gethostbyname',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='host', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='nbytes', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value=128, kind=None),
                                        op=Mult(),
                                        right=Constant(value=32, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='s', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='socket', ctx=Load()),
                                            attr='socket',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='socket', ctx=Load()),
                                                attr='AF_INET',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='socket', ctx=Load()),
                                                attr='SOCK_DGRAM',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='names', ctx=Store())],
                                    value=Call(
                                        func=Name(id='array', ctx=Load()),
                                        args=[
                                            Constant(value='B', kind=None),
                                            BinOp(
                                                left=Constant(value='\x00', kind=None),
                                                op=Mult(),
                                                right=Name(id='nbytes', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='outbytes', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Name(id='unpack', ctx=Load()),
                                            args=[
                                                Constant(value='iL', kind=None),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='fcntl', ctx=Load()),
                                                        attr='ioctl',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='s', ctx=Load()),
                                                                attr='fileno',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        Constant(value=35090, kind=None),
                                                        Call(
                                                            func=Name(id='pack', ctx=Load()),
                                                            args=[
                                                                Constant(value='iL', kind=None),
                                                                Name(id='nbytes', ctx=Load()),
                                                                Subscript(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='names', ctx=Load()),
                                                                            attr='buffer_info',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='namestr', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='names', ctx=Load()),
                                            attr='tostring',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='i', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Name(id='outbytes', ctx=Load()),
                                            Constant(value=40, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='name', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='namestr', ctx=Load()),
                                                            slice=Slice(
                                                                lower=Name(id='i', ctx=Load()),
                                                                upper=BinOp(
                                                                    left=Name(id='i', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Constant(value=16, kind=None),
                                                                ),
                                                                step=None,
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='\x00', kind=None),
                                                        Constant(value=1, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='name', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='lo', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='ip_addr', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='socket', ctx=Load()),
                                                            attr='inet_ntoa',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='namestr', ctx=Load()),
                                                                slice=Slice(
                                                                    lower=BinOp(
                                                                        left=Name(id='i', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value=20, kind=None),
                                                                    ),
                                                                    upper=BinOp(
                                                                        left=Name(id='i', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value=24, kind=None),
                                                                    ),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Break(),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='ip_addr', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='ifaces', ctx=Store())],
                                            value=ListComp(
                                                elt=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='namestr', ctx=Load()),
                                                                slice=Slice(
                                                                    lower=Name(id='i', ctx=Load()),
                                                                    upper=BinOp(
                                                                        left=Name(id='i', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value=32, kind=None),
                                                                    ),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='\x00', kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='i', ctx=Store()),
                                                        iter=Call(
                                                            func=Name(id='range', ctx=Load()),
                                                            args=[
                                                                Constant(value=0, kind=None),
                                                                Name(id='outbytes', ctx=Load()),
                                                                Constant(value=32, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='ifname', ctx=Store()),
                                            iter=ListComp(
                                                elt=Name(id='iface', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='iface', ctx=Store()),
                                                        iter=Name(id='ifaces', ctx=Load()),
                                                        ifs=[
                                                            Name(id='iface', ctx=Load()),
                                                            Compare(
                                                                left=Name(id='iface', ctx=Load()),
                                                                ops=[NotEq()],
                                                                comparators=[Constant(value='lo', kind=None)],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='ip_addr', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='socket', ctx=Load()),
                                                            attr='inet_ntoa',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='fcntl', ctx=Load()),
                                                                        attr='ioctl',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='s', ctx=Load()),
                                                                                attr='fileno',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        Constant(value=35093, kind=None),
                                                                        Call(
                                                                            func=Name(id='pack', ctx=Load()),
                                                                            args=[
                                                                                Constant(value='256s', kind=None),
                                                                                Subscript(
                                                                                    value=Name(id='ifname', ctx=Load()),
                                                                                    slice=Slice(
                                                                                        lower=None,
                                                                                        upper=Constant(value=15, kind=None),
                                                                                        step=None,
                                                                                    ),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                slice=Slice(
                                                                    lower=Constant(value=20, kind=None),
                                                                    upper=Constant(value=24, kind=None),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Break(),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='ip_addr', ctx=Load()),
                                    Constant(value='localhost', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='ip_addr', ctx=Store())],
                            value=Call(
                                func=Name(id='_detect_ip_addr', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name=None,
                            body=[
                                Assign(
                                    targets=[Name(id='ip_addr', ctx=Store())],
                                    value=Constant(value='localhost', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
                Return(
                    value=Name(id='ip_addr', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Store())],
            value=Constant(value='%Y-%m-%d', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_SERVER_TIME_FORMAT', ctx=Store())],
            value=Constant(value='%H:%M:%S', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Store())],
            value=BinOp(
                left=Constant(value='%s %s', kind=None),
                op=Mod(),
                right=Tuple(
                    elts=[
                        Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load()),
                        Name(id='DEFAULT_SERVER_TIME_FORMAT', ctx=Load()),
                    ],
                    ctx=Load(),
                ),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DATE_LENGTH', ctx=Store())],
            value=Call(
                func=Name(id='len', ctx=Load()),
                args=[
                    Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
                                        attr='date',
                                        ctx=Load(),
                                    ),
                                    attr='today',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr='strftime',
                            ctx=Load(),
                        ),
                        args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                        keywords=[],
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DATETIME_FORMATS_MAP', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='%C', kind=None),
                    Constant(value='%D', kind=None),
                    Constant(value='%e', kind=None),
                    Constant(value='%E', kind=None),
                    Constant(value='%F', kind=None),
                    Constant(value='%g', kind=None),
                    Constant(value='%G', kind=None),
                    Constant(value='%h', kind=None),
                    Constant(value='%k', kind=None),
                    Constant(value='%l', kind=None),
                    Constant(value='%n', kind=None),
                    Constant(value='%O', kind=None),
                    Constant(value='%P', kind=None),
                    Constant(value='%R', kind=None),
                    Constant(value='%r', kind=None),
                    Constant(value='%s', kind=None),
                    Constant(value='%T', kind=None),
                    Constant(value='%t', kind=None),
                    Constant(value='%u', kind=None),
                    Constant(value='%V', kind=None),
                    Constant(value='%y', kind=None),
                    Constant(value='%+', kind=None),
                    Constant(value='%z', kind=None),
                    Constant(value='%Z', kind=None),
                ],
                values=[
                    Constant(value='', kind=None),
                    Constant(value='%m/%d/%Y', kind=None),
                    Constant(value='%d', kind=None),
                    Constant(value='', kind=None),
                    Constant(value='%Y-%m-%d', kind=None),
                    Constant(value='%Y', kind=None),
                    Constant(value='%Y', kind=None),
                    Constant(value='%b', kind=None),
                    Constant(value='%H', kind=None),
                    Constant(value='%I', kind=None),
                    Constant(value='\n', kind=None),
                    Constant(value='', kind=None),
                    Constant(value='%p', kind=None),
                    Constant(value='%H:%M', kind=None),
                    Constant(value='%I:%M:%S %p', kind=None),
                    Constant(value='', kind=None),
                    Constant(value='%H:%M:%S', kind=None),
                    Constant(value=' ', kind=None),
                    Constant(value=' %w', kind=None),
                    Constant(value='%W', kind=None),
                    Constant(value='%Y', kind=None),
                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
                    Constant(value='', kind=None),
                    Constant(value='', kind=None),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='POSIX_TO_LDML', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='a', kind=None),
                    Constant(value='A', kind=None),
                    Constant(value='b', kind=None),
                    Constant(value='B', kind=None),
                    Constant(value='d', kind=None),
                    Constant(value='H', kind=None),
                    Constant(value='I', kind=None),
                    Constant(value='j', kind=None),
                    Constant(value='m', kind=None),
                    Constant(value='M', kind=None),
                    Constant(value='p', kind=None),
                    Constant(value='S', kind=None),
                    Constant(value='U', kind=None),
                    Constant(value='w', kind=None),
                    Constant(value='W', kind=None),
                    Constant(value='y', kind=None),
                    Constant(value='Y', kind=None),
                ],
                values=[
                    Constant(value='E', kind=None),
                    Constant(value='EEEE', kind=None),
                    Constant(value='MMM', kind=None),
                    Constant(value='MMMM', kind=None),
                    Constant(value='dd', kind=None),
                    Constant(value='HH', kind=None),
                    Constant(value='hh', kind=None),
                    Constant(value='DDD', kind=None),
                    Constant(value='MM', kind=None),
                    Constant(value='mm', kind=None),
                    Constant(value='a', kind=None),
                    Constant(value='ss', kind=None),
                    Constant(value='w', kind=None),
                    Constant(value='e', kind=None),
                    Constant(value='w', kind=None),
                    Constant(value='yy', kind=None),
                    Constant(value='yyyy', kind=None),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='posix_to_ldml',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='fmt', annotation=None, type_comment=None),
                    arg(arg='locale', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Converts a posix/strftime pattern into an LDML date format pattern.\n\n    :param fmt: non-extended C89/C90 strftime pattern\n    :param locale: babel locale used for locale-specific conversions (e.g. %x and %X)\n    :return: unicode\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='buf', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='pc', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='quoted', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Name(id='c', ctx=Store()),
                    iter=Name(id='fmt', ctx=Load()),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='pc', ctx=Load()),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='c', ctx=Load()),
                                            attr='isalpha',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='quoted', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            IfExp(
                                                test=Compare(
                                                    left=Name(id='c', ctx=Load()),
                                                    ops=[NotEq()],
                                                    comparators=[Constant(value="'", kind=None)],
                                                ),
                                                body=Name(id='c', ctx=Load()),
                                                orelse=Constant(value="''", kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Continue(),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='quoted', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='buf', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value="'", kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='buf', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='quoted', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='buf', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value="'", kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='quoted', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='pc', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='c', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='%', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='buf', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='%', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='c', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='x', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='buf', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='locale', ctx=Load()),
                                                                        attr='date_formats',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='short', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='pattern',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='c', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='X', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='buf', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='locale', ctx=Load()),
                                                                                attr='time_formats',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='medium', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='pattern',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='buf', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='POSIX_TO_LDML', ctx=Load()),
                                                                        slice=Name(id='c', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='pc', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='c', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='%', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='pc', ctx=Store())],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='buf', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='c', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                If(
                    test=Name(id='quoted', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='buf', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="'", kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='buf', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='quoted', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='buf', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="'", kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Constant(value='', kind=None),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[Name(id='buf', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='split_every',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='n', annotation=None, type_comment=None),
                    arg(arg='iterable', annotation=None, type_comment=None),
                    arg(arg='piece_maker', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Name(id='tuple', ctx=Load())],
            ),
            body=[
                Expr(
                    value=Constant(value='Splits an iterable into length-n pieces. The last piece will be shorter\n       if ``n`` does not evenly divide the iterable length.\n\n       :param int n: maximum size of each generated chunk\n       :param Iterable iterable: iterable to chunk into pieces\n       :param piece_maker: callable taking an iterable and collecting each\n                           chunk from its slice, *must consume the entire slice*.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='iterator', ctx=Store())],
                    value=Call(
                        func=Name(id='iter', ctx=Load()),
                        args=[Name(id='iterable', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='piece', ctx=Store())],
                    value=Call(
                        func=Name(id='piece_maker', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='islice', ctx=Load()),
                                args=[
                                    Name(id='iterator', ctx=Load()),
                                    Name(id='n', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                While(
                    test=Name(id='piece', ctx=Load()),
                    body=[
                        Expr(
                            value=Yield(
                                value=Name(id='piece', ctx=Load()),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='piece', ctx=Store())],
                            value=Call(
                                func=Name(id='piece_maker', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='islice', ctx=Load()),
                                        args=[
                                            Name(id='iterator', ctx=Load()),
                                            Name(id='n', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
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
        FunctionDef(
            name='get_and_group_by_field',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='uid', annotation=None, type_comment=None),
                    arg(arg='obj', annotation=None, type_comment=None),
                    arg(arg='ids', annotation=None, type_comment=None),
                    arg(arg='field', annotation=None, type_comment=None),
                    arg(arg='context', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Read the values of ``field´´ for the given ``ids´´ and group ids by value.\n\n       :param string field: name of the field we want to read and group by\n       :return: mapping of field values to the list of ids that have it\n       :rtype: dict\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='res', ctx=Store())],
                    value=Dict(keys=[], values=[]),
                    type_comment=None,
                ),
                For(
                    target=Name(id='record', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='obj', ctx=Load()),
                            attr='read',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Name(id='uid', ctx=Load()),
                            Name(id='ids', ctx=Load()),
                            List(
                                elts=[Name(id='field', ctx=Load())],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='context',
                                value=Name(id='context', ctx=Load()),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='key', ctx=Store())],
                            value=Subscript(
                                value=Name(id='record', ctx=Load()),
                                slice=Name(id='field', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            IfExp(
                                                test=Call(
                                                    func=Name(id='isinstance', ctx=Load()),
                                                    args=[
                                                        Name(id='key', ctx=Load()),
                                                        Name(id='tuple', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                body=Subscript(
                                                    value=Name(id='key', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                orelse=Name(id='key', ctx=Load()),
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='record', ctx=Load()),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='res', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_and_group_by_company',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='uid', annotation=None, type_comment=None),
                    arg(arg='obj', annotation=None, type_comment=None),
                    arg(arg='ids', annotation=None, type_comment=None),
                    arg(arg='context', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Return(
                    value=Call(
                        func=Name(id='get_and_group_by_field', ctx=Load()),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Name(id='uid', ctx=Load()),
                            Name(id='obj', ctx=Load()),
                            Name(id='ids', ctx=Load()),
                        ],
                        keywords=[
                            keyword(
                                arg='field',
                                value=Constant(value='company_id', kind=None),
                            ),
                            keyword(
                                arg='context',
                                value=Name(id='context', ctx=Load()),
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
            name='resolve_attr',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='obj', annotation=None, type_comment=None),
                    arg(arg='attr', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                For(
                    target=Name(id='name', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='attr', ctx=Load()),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value='.', kind=None)],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='obj', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='obj', ctx=Load()),
                                    Name(id='name', ctx=Load()),
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
                    value=Name(id='obj', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='attrgetter',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=arg(arg='items', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='items', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value=1, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='attr', ctx=Store())],
                            value=Subscript(
                                value=Name(id='items', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='g',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='obj', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='resolve_attr', ctx=Load()),
                                        args=[
                                            Name(id='obj', ctx=Load()),
                                            Name(id='attr', ctx=Load()),
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
                    orelse=[
                        FunctionDef(
                            name='g',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='obj', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Name(id='resolve_attr', ctx=Load()),
                                                    args=[
                                                        Name(id='obj', ctx=Load()),
                                                        Name(id='attr', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='attr', ctx=Store()),
                                                        iter=Name(id='items', ctx=Load()),
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
                    ],
                ),
                Return(
                    value=Name(id='g', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='discardattr',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='obj', annotation=None, type_comment=None),
                    arg(arg='key', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Perform a ``delattr(obj, key)`` but without crashing if ``key`` is not present. ', kind=None),
                ),
                Try(
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='delattr', ctx=Load()),
                                args=[
                                    Name(id='obj', ctx=Load()),
                                    Name(id='key', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='AttributeError', ctx=Load()),
                            name=None,
                            body=[Pass()],
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
            name='remove_accents',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='input_str', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Suboptimal-but-better-than-nothing way to replace accented\n    latin letters by an ASCII equivalent. Will obviously change the\n    meaning of input_str and work only for some cases', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='input_str', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Name(id='input_str', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='input_str', ctx=Store())],
                    value=Call(
                        func=Name(id='ustr', ctx=Load()),
                        args=[Name(id='input_str', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='nkfd_form', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='unicodedata', ctx=Load()),
                            attr='normalize',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='NFKD', kind=None),
                            Name(id='input_str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Constant(value='', kind='u'),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[
                            ListComp(
                                elt=Name(id='c', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='c', ctx=Store()),
                                        iter=Name(id='nkfd_form', ctx=Load()),
                                        ifs=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='unicodedata', ctx=Load()),
                                                        attr='combining',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='c', ctx=Load())],
                                                    keywords=[],
                                                ),
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
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='unquote',
            bases=[Name(id='str', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value="A subclass of str that implements repr() without enclosing quotation marks\n       or escaping, keeping the original string untouched. The name come from Lisp's unquote.\n       One of the uses for this is to preserve or insert bare variable names within dicts during eval()\n       of a dict's repr(). Use with care.\n\n       Some examples (notice that there are never quotes surrounding\n       the ``active_id`` name:\n\n       >>> unquote('active_id')\n       active_id\n       >>> d = {'test': unquote('active_id')}\n       >>> d\n       {'test': active_id}\n       >>> print d\n       {'test': active_id}\n    ", kind=None),
                ),
                FunctionDef(
                    name='__repr__',
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
                            value=Name(id='self', ctx=Load()),
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
            name='UnquoteEvalContext',
            bases=[Name(id='defaultdict', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Defaultdict-based evaluation context that returns\n       an ``unquote`` string for any missing name used during\n       the evaluation.\n       Mostly useful for evaluating OpenERP domains/contexts that\n       may refer to names that are unknown at the time of eval,\n       so that when the context/domain is converted back to a string,\n       the original names are preserved.\n\n       **Warning**: using an ``UnquoteEvalContext`` as context for ``eval()`` or\n       ``safe_eval()`` will shadow the builtins, which may cause other\n       failures, depending on what is evaluated.\n\n       Example (notice that ``section_id`` is preserved in the final\n       result) :\n\n       >>> context_str = "{\'default_user_id\': uid, \'default_section_id\': section_id}"\n       >>> eval(context_str, UnquoteEvalContext(uid=1))\n       {\'default_user_id\': 1, \'default_section_id\': section_id}\n\n       ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='UnquoteEvalContext', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=None, kind=None),
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
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
                    name='__missing__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
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
                                func=Name(id='unquote', ctx=Load()),
                                args=[Name(id='key', ctx=Load())],
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
            name='mute_logger',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value="Temporary suppress the logging.\n    Can be used as context manager or decorator.\n\n        @mute_logger('odoo.plic.ploc')\n        def do_stuff():\n            blahblah()\n\n        with mute_logger('odoo.foo.bar'):\n            do_suff()\n\n    ", kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='loggers', annotation=None, type_comment=None),
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
                                    attr='loggers',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='loggers', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='filter',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Constant(value=0, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__enter__',
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
                        For(
                            target=Name(id='logger', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='loggers',
                                ctx=Load(),
                            ),
                            body=[
                                Assert(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='logger', ctx=Load()),
                                            Name(id='str', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    msg=BinOp(
                                        left=Constant(value='A logger name must be a string, got %s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='type', ctx=Load()),
                                            args=[Name(id='logger', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='logging', ctx=Load()),
                                                    attr='getLogger',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='logger', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='addFilter',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='self', ctx=Load())],
                                        keywords=[],
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
                FunctionDef(
                    name='__exit__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='exc_type', annotation=None, type_comment=None),
                            arg(arg='exc_val', annotation=None, type_comment=None),
                            arg(arg='exc_tb', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        For(
                            target=Name(id='logger', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='loggers',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='logging', ctx=Load()),
                                                    attr='getLogger',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='logger', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='removeFilter',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='self', ctx=Load())],
                                        keywords=[],
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
                FunctionDef(
                    name='__call__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='func', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='deco',
                            args=arguments(
                                posonlyargs=[],
                                args=[],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Name(id='self', ctx=Load()),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='func', ctx=Load()),
                                                args=[
                                                    Starred(
                                                        value=Name(id='args', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='kwargs', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[
                                Call(
                                    func=Name(id='wraps', ctx=Load()),
                                    args=[Name(id='func', ctx=Load())],
                                    keywords=[],
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='deco', ctx=Load()),
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
            targets=[Name(id='_ph', ctx=Store())],
            value=Call(
                func=Name(id='object', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='CountingStream',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Stream wrapper counting the number of element it has yielded. Similar\n    role to ``enumerate``, but for use when the iteration process of the stream\n    isn't fully under caller control (the stream can be iterated from multiple\n    points including within a library)\n\n    ``start`` allows overriding the starting index (the index before the first\n    item is returned).\n\n    On each iteration (call to :meth:`~.next`), increases its :attr:`~.index`\n    by one.\n\n    .. attribute:: index\n\n        ``int``, index of the last yielded element in the stream. If the stream\n        has ended, will give an index 1-past the stream\n    ", kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stream', annotation=None, type_comment=None),
                            arg(arg='start', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='stream',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='iter', ctx=Load()),
                                args=[Name(id='stream', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='index',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='start', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='stopped',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__iter__',
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
                            value=Name(id='self', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='next',
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
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='stopped',
                                ctx=Load(),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='StopIteration', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='index',
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Constant(value=1, kind=None),
                        ),
                        Assign(
                            targets=[Name(id='val', ctx=Store())],
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='stream',
                                        ctx=Load(),
                                    ),
                                    Name(id='_ph', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='val', ctx=Load()),
                                ops=[Is()],
                                comparators=[Name(id='_ph', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stopped',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='StopIteration', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='val', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='__next__', ctx=Store())],
                    value=Name(id='next', ctx=Load()),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='stripped_sys_argv',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=arg(arg='strip_args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Return sys.argv with some arguments stripped, suitable for reexecution or subprocesses', kind=None),
                ),
                Assign(
                    targets=[Name(id='strip_args', ctx=Store())],
                    value=Call(
                        func=Name(id='sorted', ctx=Load()),
                        args=[
                            BinOp(
                                left=Call(
                                    func=Name(id='set', ctx=Load()),
                                    args=[Name(id='strip_args', ctx=Load())],
                                    keywords=[],
                                ),
                                op=BitOr(),
                                right=Call(
                                    func=Name(id='set', ctx=Load()),
                                    args=[
                                        List(
                                            elts=[
                                                Constant(value='-s', kind=None),
                                                Constant(value='--save', kind=None),
                                                Constant(value='-u', kind=None),
                                                Constant(value='--update', kind=None),
                                                Constant(value='-i', kind=None),
                                                Constant(value='--init', kind=None),
                                                Constant(value='--i18n-overwrite', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assert(
                    test=Call(
                        func=Name(id='all', ctx=Load()),
                        args=[
                            GeneratorExp(
                                elt=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='config', ctx=Load()),
                                            attr='parser',
                                            ctx=Load(),
                                        ),
                                        attr='has_option',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='s', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='s', ctx=Store()),
                                        iter=Name(id='strip_args', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    msg=None,
                ),
                Assign(
                    targets=[Name(id='takes_value', ctx=Store())],
                    value=Call(
                        func=Name(id='dict', ctx=Load()),
                        args=[
                            GeneratorExp(
                                elt=Tuple(
                                    elts=[
                                        Name(id='s', ctx=Load()),
                                        Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='config', ctx=Load()),
                                                            attr='parser',
                                                            ctx=Load(),
                                                        ),
                                                        attr='get_option',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='s', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='takes_value',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='s', ctx=Store()),
                                        iter=Name(id='strip_args', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
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
                                Name(id='longs', ctx=Store()),
                                Name(id='shorts', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Name(id='list', ctx=Load()),
                        args=[
                            GeneratorExp(
                                elt=Call(
                                    func=Name(id='tuple', ctx=Load()),
                                    args=[Name(id='y', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='_', ctx=Store()),
                                                Name(id='y', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Name(id='itergroupby', ctx=Load()),
                                            args=[
                                                Name(id='strip_args', ctx=Load()),
                                                Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='x', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Call(
                                                        func=Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='startswith',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='--', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
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
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='longs_eq', ctx=Store())],
                    value=Call(
                        func=Name(id='tuple', ctx=Load()),
                        args=[
                            GeneratorExp(
                                elt=BinOp(
                                    left=Name(id='l', ctx=Load()),
                                    op=Add(),
                                    right=Constant(value='=', kind=None),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='l', ctx=Store()),
                                        iter=Name(id='longs', ctx=Load()),
                                        ifs=[
                                            Subscript(
                                                value=Name(id='takes_value', ctx=Load()),
                                                slice=Name(id='l', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='args', ctx=Store())],
                    value=Subscript(
                        value=Attribute(
                            value=Name(id='sys', ctx=Load()),
                            attr='argv',
                            ctx=Load(),
                        ),
                        slice=Slice(lower=None, upper=None, step=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='strip',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='args', annotation=None, type_comment=None),
                            arg(arg='i', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='args', ctx=Load()),
                                                slice=Name(id='i', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='shorts', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='args', ctx=Load()),
                                                slice=Name(id='i', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='longs_eq', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='args', ctx=Load()),
                                            slice=Name(id='i', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='longs', ctx=Load())],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='i', ctx=Load()),
                                                ops=[GtE()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='args', ctx=Load()),
                                                    slice=BinOp(
                                                        left=Name(id='i', ctx=Load()),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='strip_args', ctx=Load())],
                                            ),
                                            Subscript(
                                                value=Name(id='takes_value', ctx=Load()),
                                                slice=Subscript(
                                                    value=Name(id='args', ctx=Load()),
                                                    slice=BinOp(
                                                        left=Name(id='i', ctx=Load()),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=ListComp(
                        elt=Name(id='x', ctx=Load()),
                        generators=[
                            comprehension(
                                target=Tuple(
                                    elts=[
                                        Name(id='i', ctx=Store()),
                                        Name(id='x', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                                iter=Call(
                                    func=Name(id='enumerate', ctx=Load()),
                                    args=[Name(id='args', ctx=Load())],
                                    keywords=[],
                                ),
                                ifs=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='strip', ctx=Load()),
                                            args=[
                                                Name(id='args', ctx=Load()),
                                                Name(id='i', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                is_async=0,
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='ConstantMapping',
            bases=[Name(id='Mapping', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    An immutable mapping returning the provided value for every single key.\n\n    Useful for default value to methods\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='__slots__', ctx=Store())],
                    value=List(
                        elts=[Constant(value='_value', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='val', annotation=None, type_comment=None),
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
                                    attr='_value',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='val', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__len__',
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
                            value=Constant(value='\n        defaultdict updates its length for each individually requested key, is\n        that really useful?\n        ', kind=None),
                        ),
                        Return(
                            value=Constant(value=0, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__iter__',
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
                            value=Constant(value='\n        same as len, defaultdict updates its iterable keyset with each key\n        requested, is there a point for this?\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='iter', ctx=Load()),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__getitem__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='item', annotation=None, type_comment=None),
                        ],
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
                                attr='_value',
                                ctx=Load(),
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
            name='dumpstacks',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='sig', annotation=None, type_comment=None),
                    arg(arg='frame', annotation=None, type_comment=None),
                    arg(arg='thread_idents', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Signal handler: dump a stack trace for each existing thread or given\n    thread(s) specified through the ``thread_idents`` sequence.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='code', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                FunctionDef(
                    name='extract_stack',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='stack', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='filename', ctx=Store()),
                                    Name(id='lineno', ctx=Store()),
                                    Name(id='name', ctx=Store()),
                                    Name(id='line', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='traceback', ctx=Load()),
                                    attr='extract_stack',
                                    ctx=Load(),
                                ),
                                args=[Name(id='stack', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=BinOp(
                                            left=Constant(value='File: "%s", line %d, in %s', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    Name(id='filename', ctx=Load()),
                                                    Name(id='lineno', ctx=Load()),
                                                    Name(id='name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ),
                                If(
                                    test=Name(id='line', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Yield(
                                                value=BinOp(
                                                    left=Constant(value='  %s', kind=None),
                                                    op=Mod(),
                                                    right=Tuple(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='strip',
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
                                        ),
                                    ],
                                    orelse=[],
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
                Assign(
                    targets=[Name(id='threads_info', ctx=Store())],
                    value=DictComp(
                        key=Attribute(
                            value=Name(id='th', ctx=Load()),
                            attr='ident',
                            ctx=Load(),
                        ),
                        value=Dict(
                            keys=[
                                Constant(value='repr', kind=None),
                                Constant(value='uid', kind=None),
                                Constant(value='dbname', kind=None),
                                Constant(value='url', kind=None),
                            ],
                            values=[
                                Call(
                                    func=Name(id='repr', ctx=Load()),
                                    args=[Name(id='th', ctx=Load())],
                                    keywords=[],
                                ),
                                Call(
                                    func=Name(id='getattr', ctx=Load()),
                                    args=[
                                        Name(id='th', ctx=Load()),
                                        Constant(value='uid', kind=None),
                                        Constant(value='n/a', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                Call(
                                    func=Name(id='getattr', ctx=Load()),
                                    args=[
                                        Name(id='th', ctx=Load()),
                                        Constant(value='dbname', kind=None),
                                        Constant(value='n/a', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                Call(
                                    func=Name(id='getattr', ctx=Load()),
                                    args=[
                                        Name(id='th', ctx=Load()),
                                        Constant(value='url', kind=None),
                                        Constant(value='n/a', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ],
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='th', ctx=Store()),
                                iter=Call(
                                    func=Attribute(
                                        value=Name(id='threading', ctx=Load()),
                                        attr='enumerate',
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
                    type_comment=None,
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='threadId', ctx=Store()),
                            Name(id='stack', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='_current_frames',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr='items',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='thread_idents', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Name(id='threadId', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='thread_idents', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='thread_info', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='threads_info', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='threadId', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='\n# Thread: %s (db:%s) (uid:%s) (url:%s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='thread_info', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='repr', kind=None),
                                                                Name(id='threadId', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='thread_info', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='dbname', kind=None),
                                                                Constant(value='n/a', kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='thread_info', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='uid', kind=None),
                                                                Constant(value='n/a', kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='thread_info', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='url', kind=None),
                                                                Constant(value='n/a', kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='line', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='extract_stack', ctx=Load()),
                                        args=[Name(id='stack', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='line', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                If(
                    test=Attribute(
                        value=Name(id='odoo', ctx=Load()),
                        attr='evented',
                        ctx=Load(),
                    ),
                    body=[
                        Import(
                            names=[alias(name='gc', asname=None)],
                        ),
                        ImportFrom(
                            module='greenlet',
                            names=[alias(name='greenlet', asname=None)],
                            level=0,
                        ),
                        For(
                            target=Name(id='ob', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='gc', ctx=Load()),
                                    attr='get_objects',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='isinstance', ctx=Load()),
                                                    args=[
                                                        Name(id='ob', ctx=Load()),
                                                        Name(id='greenlet', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='ob', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='\n# Greenlet: %r', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[Name(id='ob', ctx=Load())],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='line', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='extract_stack', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='ob', ctx=Load()),
                                                attr='gr_frame',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='line', ctx=Load())],
                                                keywords=[],
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
                            Call(
                                func=Attribute(
                                    value=Constant(value='\n', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='code', ctx=Load())],
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
            name='freehash',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='arg', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Try(
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='hash', ctx=Load()),
                                args=[Name(id='arg', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name=None,
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='arg', ctx=Load()),
                                            Name(id='Mapping', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='hash', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='frozendict', ctx=Load()),
                                                        args=[Name(id='arg', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='arg', ctx=Load()),
                                                    Name(id='Iterable', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Name(id='hash', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='frozenset', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Call(
                                                                            func=Name(id='freehash', ctx=Load()),
                                                                            args=[Name(id='item', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='item', ctx=Store()),
                                                                                iter=Name(id='arg', ctx=Load()),
                                                                                ifs=[],
                                                                                is_async=0,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Return(
                                                    value=Call(
                                                        func=Name(id='id', ctx=Load()),
                                                        args=[Name(id='arg', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
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
            name='clean_context',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='context', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" This function take a dictionary and remove each entry with its key starting with 'default_' ", kind=None),
                ),
                Return(
                    value=DictComp(
                        key=Name(id='k', ctx=Load()),
                        value=Name(id='v', ctx=Load()),
                        generators=[
                            comprehension(
                                target=Tuple(
                                    elts=[
                                        Name(id='k', ctx=Store()),
                                        Name(id='v', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                                iter=Call(
                                    func=Attribute(
                                        value=Name(id='context', ctx=Load()),
                                        attr='items',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ifs=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='k', ctx=Load()),
                                                attr='startswith',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='default_', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                is_async=0,
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='frozendict',
            bases=[Name(id='dict', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' An implementation of an immutable dictionary. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='__slots__', ctx=Store())],
                    value=Tuple(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__delitem__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[Constant(value="'__delitem__' not supported on frozendict", kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__setitem__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='val', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[Constant(value="'__setitem__' not supported on frozendict", kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='clear',
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
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[Constant(value="'clear' not supported on frozendict", kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='pop',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[Constant(value="'pop' not supported on frozendict", kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='popitem',
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
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[Constant(value="'popitem' not supported on frozendict", kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='setdefault',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[Constant(value="'setdefault' not supported on frozendict", kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='update',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[Constant(value="'update' not supported on frozendict", kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__hash__',
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
                            value=Call(
                                func=Name(id='hash', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='frozenset', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Tuple(
                                                    elts=[
                                                        Name(id='key', ctx=Load()),
                                                        Call(
                                                            func=Name(id='freehash', ctx=Load()),
                                                            args=[Name(id='val', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='key', ctx=Store()),
                                                                Name(id='val', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='items',
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
        ClassDef(
            name='Collector',
            bases=[Name(id='dict', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' A mapping from keys to tuples.  This implements a relation, and can be\n        seen as a space optimization for ``defaultdict(tuple)``.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='__slots__', ctx=Store())],
                    value=Tuple(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__getitem__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
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
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='key', ctx=Load()),
                                    Tuple(elts=[], ctx=Load()),
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
                    name='__setitem__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='val', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='val', ctx=Store())],
                            value=Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[Name(id='val', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='val', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='__setitem__',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='key', ctx=Load()),
                                            Name(id='val', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='key', ctx=Load()),
                                            Constant(value=None, kind=None),
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
                FunctionDef(
                    name='add',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='val', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Subscript(
                                value=Name(id='self', ctx=Load()),
                                slice=Name(id='key', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='val', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[Name(id='vals', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='self', ctx=Load()),
                                            slice=Name(id='key', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Name(id='vals', ctx=Load()),
                                        op=Add(),
                                        right=Tuple(
                                            elts=[Name(id='val', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
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
        ClassDef(
            name='StackMap',
            bases=[Name(id='MutableMapping', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' A stack of mappings behaving as a single mapping, and used to implement\n        nested scopes. The lookups search the stack from top to bottom, and\n        returns the first value found. Mutable operations modify the topmost\n        mapping only.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='__slots__', ctx=Store())],
                    value=List(
                        elts=[Constant(value='_maps', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='m', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_maps',
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='m', ctx=Load()),
                                    ops=[Is()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=List(elts=[], ctx=Load()),
                                orelse=List(
                                    elts=[Name(id='m', ctx=Load())],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__getitem__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='mapping', ctx=Store()),
                            iter=Call(
                                func=Name(id='reversed', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_maps',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Return(
                                            value=Subscript(
                                                value=Name(id='mapping', ctx=Load()),
                                                slice=Name(id='key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='KeyError', ctx=Load()),
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
                        Raise(
                            exc=Call(
                                func=Name(id='KeyError', ctx=Load()),
                                args=[Name(id='key', ctx=Load())],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__setitem__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='val', annotation=None, type_comment=None),
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
                                Subscript(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_maps',
                                            ctx=Load(),
                                        ),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='key', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='val', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__delitem__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Delete(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_maps',
                                            ctx=Load(),
                                        ),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='key', ctx=Load()),
                                    ctx=Del(),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__iter__',
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
                            value=Call(
                                func=Name(id='iter', ctx=Load()),
                                args=[
                                    SetComp(
                                        elt=Name(id='key', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='mapping', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_maps',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                            comprehension(
                                                target=Name(id='key', ctx=Store()),
                                                iter=Name(id='mapping', ctx=Load()),
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
                    name='__len__',
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
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Constant(value=1, kind=None),
                                        generators=[
                                            comprehension(
                                                target=Name(id='key', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
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
                            value=BinOp(
                                left=Constant(value='<StackMap %s>', kind='u'),
                                op=Mod(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_maps',
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='pushmap',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='m', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_maps',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    IfExp(
                                        test=Compare(
                                            left=Name(id='m', ctx=Load()),
                                            ops=[Is()],
                                            comparators=[Constant(value=None, kind=None)],
                                        ),
                                        body=Dict(keys=[], values=[]),
                                        orelse=Name(id='m', ctx=Load()),
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
                    name='popmap',
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
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_maps',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
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
            name='OrderedSet',
            bases=[Name(id='MutableSet', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' A set collection that remembers the elements first insertion order. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='__slots__', ctx=Store())],
                    value=List(
                        elts=[Constant(value='_map', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='elems', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Tuple(elts=[], ctx=Load())],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_map',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='fromkeys',
                                    ctx=Load(),
                                ),
                                args=[Name(id='elems', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__contains__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='elem', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Compare(
                                left=Name(id='elem', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_map',
                                        ctx=Load(),
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
                    name='__iter__',
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
                            value=Call(
                                func=Name(id='iter', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_map',
                                        ctx=Load(),
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
                    name='__len__',
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
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_map',
                                        ctx=Load(),
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
                    name='add',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='elem', annotation=None, type_comment=None),
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
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_map',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='elem', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='discard',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='elem', annotation=None, type_comment=None),
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_map',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='elem', ctx=Load()),
                                    Constant(value=None, kind=None),
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
                    name='update',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='elems', annotation=None, type_comment=None),
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_map',
                                        ctx=Load(),
                                    ),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='zip', ctx=Load()),
                                        args=[
                                            Name(id='elems', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='itertools', ctx=Load()),
                                                    attr='repeat',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=None, kind=None)],
                                                keywords=[],
                                            ),
                                        ],
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
                    name='difference_update',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='elems', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='elem', ctx=Store()),
                            iter=Name(id='elems', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='discard',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='elem', ctx=Load())],
                                        keywords=[],
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
                FunctionDef(
                    name='__repr__',
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
                            value=JoinedStr(
                                values=[
                                    FormattedValue(
                                        value=Attribute(
                                            value=Call(
                                                func=Name(id='type', ctx=Load()),
                                                args=[Name(id='self', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='__name__',
                                            ctx=Load(),
                                        ),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value='(', kind=None),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='list', ctx=Load()),
                                            args=[Name(id='self', ctx=Load())],
                                            keywords=[],
                                        ),
                                        conversion=114,
                                        format_spec=None,
                                    ),
                                    Constant(value=')', kind=None),
                                ],
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
            name='LastOrderedSet',
            bases=[Name(id='OrderedSet', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' A set collection that remembers the elements last insertion order. ', kind=None),
                ),
                FunctionDef(
                    name='add',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='elem', annotation=None, type_comment=None),
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
                                    value=Name(id='OrderedSet', ctx=Load()),
                                    attr='discard',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='elem', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='OrderedSet', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='elem', ctx=Load()),
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
        ClassDef(
            name='Callbacks',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' A simple queue of callback functions.  Upon run, every function is\n    called (in addition order), and the queue is emptied.\n\n        callbacks = Callbacks()\n\n        # add foo\n        def foo():\n            print("foo")\n\n        callbacks.add(foo)\n\n        # add bar\n        callbacks.add\n        def bar():\n            print("bar")\n\n        # add foo again\n        callbacks.add(foo)\n\n        # call foo(), bar(), foo(), then clear the callback queue\n        callbacks.run()\n\n    The queue also provides a ``data`` dictionary, that may be freely used to\n    store anything, but is mostly aimed at aggregating data for callbacks.  The\n    dictionary is automatically cleared by ``run()`` once all callback functions\n    have been called.\n\n        # register foo to process aggregated data\n        @callbacks.add\n        def foo():\n            print(sum(callbacks.data[\'foo\']))\n\n        callbacks.data.setdefault(\'foo\', []).append(1)\n        ...\n        callbacks.data.setdefault(\'foo\', []).append(2)\n        ...\n        callbacks.data.setdefault(\'foo\', []).append(3)\n\n        # call foo(), which prints 6\n        callbacks.run()\n\n    Given the global nature of ``data``, the keys should identify in a unique\n    way the data being stored.  It is recommended to use strings with a\n    structure like ``"{module}.{feature}"``.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='__slots__', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='_funcs', kind=None),
                            Constant(value='data', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_funcs',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='collections', ctx=Load()),
                                    attr='deque',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='data',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='add',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='func', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Add the given function. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_funcs',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='func', ctx=Load())],
                                keywords=[],
                            ),
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
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Call all the functions (in addition order), then clear associated data.\n        ', kind=None),
                        ),
                        While(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_funcs',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='func', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_funcs',
                                                ctx=Load(),
                                            ),
                                            attr='popleft',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='func', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='clear',
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
                    name='clear',
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
                            value=Constant(value=' Remove all callbacks and data from self. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_funcs',
                                        ctx=Load(),
                                    ),
                                    attr='clear',
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
                                        value=Name(id='self', ctx=Load()),
                                        attr='data',
                                        ctx=Load(),
                                    ),
                                    attr='clear',
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
            name='IterableGenerator',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' An iterable object based on a generator function, which is called each\n        time the object is iterated over.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='__slots__', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='func', kind=None),
                            Constant(value='args', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='func', annotation=None, type_comment=None),
                        ],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
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
                                    attr='func',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='func', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='args',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='args', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__iter__',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='func',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='args',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
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
            name='groupby',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='iterable', annotation=None, type_comment=None),
                    arg(arg='key', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a collection of pairs ``(key, elements)`` from ``iterable``. The\n        ``key`` is a function computing a key value for each element. This\n        function is similar to ``itertools.groupby``, but aggregates all\n        elements under the same key, not only consecutive elements.\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='key', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='key', ctx=Store())],
                            value=Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[arg(arg='arg', annotation=None, type_comment=None)],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=Name(id='arg', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='groups', ctx=Store())],
                    value=Call(
                        func=Name(id='defaultdict', ctx=Load()),
                        args=[Name(id='list', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='elem', ctx=Store()),
                    iter=Name(id='iterable', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='groups', ctx=Load()),
                                        slice=Call(
                                            func=Name(id='key', ctx=Load()),
                                            args=[Name(id='elem', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='elem', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='groups', ctx=Load()),
                            attr='items',
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
            name='unique',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='it', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' "Uniquifier" for the provided iterable: will output each element of\n    the iterable once.\n\n    The iterable\'s elements must be hashahble.\n\n    :param Iterable it:\n    :rtype: Iterator\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='seen', ctx=Store())],
                    value=Call(
                        func=Name(id='set', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='e', ctx=Store()),
                    iter=Name(id='it', ctx=Load()),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='e', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[Name(id='seen', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='seen', ctx=Load()),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='e', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Yield(
                                        value=Name(id='e', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
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
        ClassDef(
            name='Reverse',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Wraps a value and reverses its ordering, useful in key functions when\n    mixing ascending and descending sort on non-numeric data as the\n    ``reverse`` parameter can not do piecemeal reordering.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='__slots__', ctx=Store())],
                    value=List(
                        elts=[Constant(value='val', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='val', annotation=None, type_comment=None),
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
                                    attr='val',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='val', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__eq__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='val',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='other', ctx=Load()),
                                        attr='val',
                                        ctx=Load(),
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
                    name='__ne__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='val',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='other', ctx=Load()),
                                        attr='val',
                                        ctx=Load(),
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
                    name='__ge__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='val',
                                    ctx=Load(),
                                ),
                                ops=[LtE()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='other', ctx=Load()),
                                        attr='val',
                                        ctx=Load(),
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
                    name='__gt__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='val',
                                    ctx=Load(),
                                ),
                                ops=[Lt()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='other', ctx=Load()),
                                        attr='val',
                                        ctx=Load(),
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
                    name='__le__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='val',
                                    ctx=Load(),
                                ),
                                ops=[GtE()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='other', ctx=Load()),
                                        attr='val',
                                        ctx=Load(),
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
                    name='__lt__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='val',
                                    ctx=Load(),
                                ),
                                ops=[Gt()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='other', ctx=Load()),
                                        attr='val',
                                        ctx=Load(),
                                    ),
                                ],
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
            name='ignore',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=arg(arg='exc', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Try(
                    body=[
                        Expr(
                            value=Yield(value=None),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='exc', ctx=Load()),
                            name=None,
                            body=[Pass()],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            decorator_list=[Name(id='contextmanager', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='html_escape', ctx=Store())],
            value=Attribute(
                value=Name(id='markupsafe', ctx=Load()),
                attr='escape',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='get_lang',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='lang_code', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Retrieve the first lang object installed, by checking the parameter lang_code,\n    the context and then the company. If no lang is installed from those variables,\n    fallback on the first lang installed in the system.\n    :param str lang_code: the locale (i.e. en_US)\n    :return res.lang: the first lang found that is installed on the system.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='langs', ctx=Store())],
                    value=ListComp(
                        elt=Name(id='code', ctx=Load()),
                        generators=[
                            comprehension(
                                target=Tuple(
                                    elts=[
                                        Name(id='code', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                                iter=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Name(id='env', ctx=Load()),
                                            slice=Constant(value='res.lang', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='get_installed',
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
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lang', ctx=Store())],
                    value=Subscript(
                        value=Name(id='langs', ctx=Load()),
                        slice=Constant(value=0, kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='lang_code', ctx=Load()),
                            Compare(
                                left=Name(id='lang_code', ctx=Load()),
                                ops=[In()],
                                comparators=[Name(id='langs', ctx=Load())],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='lang', ctx=Store())],
                            value=Name(id='lang_code', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='env', ctx=Load()),
                                            attr='context',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='lang', kind=None)],
                                    keywords=[],
                                ),
                                ops=[In()],
                                comparators=[Name(id='langs', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='lang', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='env', ctx=Load()),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='lang', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='env', ctx=Load()),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='lang',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='langs', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='lang', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='env', ctx=Load()),
                                                            attr='user',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='lang',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='res.lang', kind=None),
                                ctx=Load(),
                            ),
                            attr='_lang_get',
                            ctx=Load(),
                        ),
                        args=[Name(id='lang', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='babel_locale_parse',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='lang_code', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Try(
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='babel', ctx=Load()),
                                        attr='Locale',
                                        ctx=Load(),
                                    ),
                                    attr='parse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='lang_code', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=None,
                            name=None,
                            body=[
                                Try(
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='babel', ctx=Load()),
                                                        attr='Locale',
                                                        ctx=Load(),
                                                    ),
                                                    attr='default',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=None,
                                            name=None,
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='babel', ctx=Load()),
                                                                attr='Locale',
                                                                ctx=Load(),
                                                            ),
                                                            attr='parse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='en_US', kind=None)],
                                                        keywords=[],
                                                    ),
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
            name='formatLang',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='value', annotation=None, type_comment=None),
                    arg(arg='digits', annotation=None, type_comment=None),
                    arg(arg='grouping', annotation=None, type_comment=None),
                    arg(arg='monetary', annotation=None, type_comment=None),
                    arg(arg='dp', annotation=None, type_comment=None),
                    arg(arg='currency_obj', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=True, kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value="\n        Assuming 'Account' decimal.precision=3:\n            formatLang(value) -> digits=2 (default)\n            formatLang(value, digits=4) -> digits=4\n            formatLang(value, dp='Account') -> digits=3\n            formatLang(value, digits=5, dp='Account') -> digits=5\n    ", kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='digits', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Name(id='digits', ctx=Store()),
                                Name(id='DEFAULT_DIGITS', ctx=Store()),
                            ],
                            value=Constant(value=2, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='dp', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='decimal_precision_obj', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='decimal.precision', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='digits', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='decimal_precision_obj', ctx=Load()),
                                            attr='precision_get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='dp', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='currency_obj', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='digits', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='currency_obj', ctx=Load()),
                                                attr='decimal_places',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='value', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='value', ctx=Load()),
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value='', kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='lang_obj', ctx=Store())],
                    value=Call(
                        func=Name(id='get_lang', ctx=Load()),
                        args=[Name(id='env', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='lang_obj', ctx=Load()),
                            attr='format',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=BinOp(
                                    left=Constant(value='%.', kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[Name(id='digits', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value='f', kind=None),
                            ),
                            Name(id='value', ctx=Load()),
                        ],
                        keywords=[
                            keyword(
                                arg='grouping',
                                value=Name(id='grouping', ctx=Load()),
                            ),
                            keyword(
                                arg='monetary',
                                value=Name(id='monetary', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='currency_obj', ctx=Load()),
                            Attribute(
                                value=Name(id='currency_obj', ctx=Load()),
                                attr='symbol',
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='currency_obj', ctx=Load()),
                                    attr='position',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='after', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='res', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='currency_obj', ctx=Load()),
                                                    attr='symbol',
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
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='currency_obj', ctx=Load()),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='currency_obj', ctx=Load()),
                                                    attr='position',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='before', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='res', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%s %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='currency_obj', ctx=Load()),
                                                            attr='symbol',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='res', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='res', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='format_date',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='value', annotation=None, type_comment=None),
                    arg(arg='lang_code', annotation=None, type_comment=None),
                    arg(arg='date_format', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='\n        Formats the date in a given format.\n\n        :param env: an environment.\n        :param date, datetime or string value: the date to format.\n        :param string lang_code: the lang code, if not specified it is extracted from the\n            environment context.\n        :param string date_format: the format or the date (LDML format), if not specified the\n            default format of the lang.\n        :return: date formatted in the specified format.\n        :rtype: string\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='value', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Constant(value='', kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='value', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='value', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Lt()],
                                comparators=[Name(id='DATE_LENGTH', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='value', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Name(id='DATE_LENGTH', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='fields',
                                                    ctx=Load(),
                                                ),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='fields',
                                                    ctx=Load(),
                                                ),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='context_timestamp',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Constant(value='res.lang', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='value', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='fields',
                                                    ctx=Load(),
                                                ),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='lang', ctx=Store())],
                    value=Call(
                        func=Name(id='get_lang', ctx=Load()),
                        args=[
                            Name(id='env', ctx=Load()),
                            Name(id='lang_code', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='locale', ctx=Store())],
                    value=Call(
                        func=Name(id='babel_locale_parse', ctx=Load()),
                        args=[
                            Attribute(
                                value=Name(id='lang', ctx=Load()),
                                attr='code',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='date_format', ctx=Load()),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='date_format', ctx=Store())],
                            value=Call(
                                func=Name(id='posix_to_ldml', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='lang', ctx=Load()),
                                        attr='date_format',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='locale',
                                        value=Name(id='locale', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='babel', ctx=Load()),
                                attr='dates',
                                ctx=Load(),
                            ),
                            attr='format_date',
                            ctx=Load(),
                        ),
                        args=[Name(id='value', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='format',
                                value=Name(id='date_format', ctx=Load()),
                            ),
                            keyword(
                                arg='locale',
                                value=Name(id='locale', ctx=Load()),
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
            name='parse_date',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='value', annotation=None, type_comment=None),
                    arg(arg='lang_code', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='\n        Parse the date from a given format. If it is not a valid format for the\n        localization, return the original string.\n\n        :param env: an environment.\n        :param string value: the date to parse.\n        :param string lang_code: the lang code, if not specified it is extracted from the\n            environment context.\n        :return: date object from the localized string\n        :rtype: datetime.date\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='lang', ctx=Store())],
                    value=Call(
                        func=Name(id='get_lang', ctx=Load()),
                        args=[
                            Name(id='env', ctx=Load()),
                            Name(id='lang_code', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='locale', ctx=Store())],
                    value=Call(
                        func=Name(id='babel_locale_parse', ctx=Load()),
                        args=[
                            Attribute(
                                value=Name(id='lang', ctx=Load()),
                                attr='code',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='babel', ctx=Load()),
                                        attr='dates',
                                        ctx=Load(),
                                    ),
                                    attr='parse_date',
                                    ctx=Load(),
                                ),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='locale',
                                        value=Name(id='locale', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=None,
                            name=None,
                            body=[
                                Return(
                                    value=Name(id='value', ctx=Load()),
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
            name='format_datetime',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='value', annotation=None, type_comment=None),
                    arg(arg='tz', annotation=None, type_comment=None),
                    arg(arg='dt_format', annotation=None, type_comment=None),
                    arg(arg='lang_code', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value='medium', kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Formats the datetime in a given format.\n\n        :param {str, datetime} value: naive datetime to format either in string or in datetime\n        :param {str} tz: name of the timezone  in which the given datetime should be localized\n        :param {str} dt_format: one of “full”, “long”, “medium”, or “short”, or a custom date/time pattern compatible with `babel` lib\n        :param {str} lang_code: ISO code of the language to use to render the given datetime\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='value', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Constant(value='', kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='value', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='timestamp', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='fields',
                                            ctx=Load(),
                                        ),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='from_string',
                                    ctx=Load(),
                                ),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='timestamp', ctx=Store())],
                            value=Name(id='value', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                ),
                Assign(
                    targets=[Name(id='tz_name', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Name(id='tz', ctx=Load()),
                            Attribute(
                                value=Attribute(
                                    value=Name(id='env', ctx=Load()),
                                    attr='user',
                                    ctx=Load(),
                                ),
                                attr='tz',
                                ctx=Load(),
                            ),
                            Constant(value='UTC', kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='utc_datetime', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='pytz', ctx=Load()),
                                attr='utc',
                                ctx=Load(),
                            ),
                            attr='localize',
                            ctx=Load(),
                        ),
                        args=[Name(id='timestamp', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='is_dst',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='context_tz', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pytz', ctx=Load()),
                                    attr='timezone',
                                    ctx=Load(),
                                ),
                                args=[Name(id='tz_name', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='localized_datetime', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='utc_datetime', ctx=Load()),
                                    attr='astimezone',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context_tz', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name=None,
                            body=[
                                Assign(
                                    targets=[Name(id='localized_datetime', ctx=Store())],
                                    value=Name(id='utc_datetime', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
                Assign(
                    targets=[Name(id='lang', ctx=Store())],
                    value=Call(
                        func=Name(id='get_lang', ctx=Load()),
                        args=[
                            Name(id='env', ctx=Load()),
                            Name(id='lang_code', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='locale', ctx=Store())],
                    value=Call(
                        func=Name(id='babel_locale_parse', ctx=Load()),
                        args=[
                            BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='lang', ctx=Load()),
                                        attr='code',
                                        ctx=Load(),
                                    ),
                                    Name(id='lang_code', ctx=Load()),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='dt_format', ctx=Load()),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='date_format', ctx=Store())],
                            value=Call(
                                func=Name(id='posix_to_ldml', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='lang', ctx=Load()),
                                        attr='date_format',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='locale',
                                        value=Name(id='locale', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='time_format', ctx=Store())],
                            value=Call(
                                func=Name(id='posix_to_ldml', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='lang', ctx=Load()),
                                        attr='time_format',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='locale',
                                        value=Name(id='locale', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dt_format', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%s %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='date_format', ctx=Load()),
                                        Name(id='time_format', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='babel', ctx=Load()),
                                attr='dates',
                                ctx=Load(),
                            ),
                            attr='format_datetime',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='localized_datetime', ctx=Load()),
                            Name(id='dt_format', ctx=Load()),
                        ],
                        keywords=[
                            keyword(
                                arg='locale',
                                value=Name(id='locale', ctx=Load()),
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
            name='format_time',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='value', annotation=None, type_comment=None),
                    arg(arg='tz', annotation=None, type_comment=None),
                    arg(arg='time_format', annotation=None, type_comment=None),
                    arg(arg='lang_code', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value='medium', kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=" Format the given time (hour, minute and second) with the current user preference (language, format, ...)\n\n        :param value: the time to format\n        :type value: `datetime.time` instance. Could be timezoned to display tzinfo according to format (e.i.: 'full' format)\n        :param tz: name of the timezone  in which the given datetime should be localized\n        :param time_format: one of “full”, “long”, “medium”, or “short”, or a custom time pattern\n        :param lang_code: ISO\n\n        :rtype str\n    ", kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='value', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Constant(value='', kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='value', ctx=Load()),
                            Attribute(
                                value=Name(id='datetime', ctx=Load()),
                                attr='time',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='localized_datetime', ctx=Store())],
                            value=Name(id='value', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='value', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='fields',
                                                    ctx=Load(),
                                                ),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='tz_name', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='tz', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='env', ctx=Load()),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='tz',
                                        ctx=Load(),
                                    ),
                                    Constant(value='UTC', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='utc_datetime', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='pytz', ctx=Load()),
                                        attr='utc',
                                        ctx=Load(),
                                    ),
                                    attr='localize',
                                    ctx=Load(),
                                ),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='is_dst',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='context_tz', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='pytz', ctx=Load()),
                                            attr='timezone',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='tz_name', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='localized_datetime', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='utc_datetime', ctx=Load()),
                                            attr='astimezone',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='context_tz', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='localized_datetime', ctx=Store())],
                                            value=Name(id='utc_datetime', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                ),
                Assign(
                    targets=[Name(id='lang', ctx=Store())],
                    value=Call(
                        func=Name(id='get_lang', ctx=Load()),
                        args=[
                            Name(id='env', ctx=Load()),
                            Name(id='lang_code', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='locale', ctx=Store())],
                    value=Call(
                        func=Name(id='babel_locale_parse', ctx=Load()),
                        args=[
                            Attribute(
                                value=Name(id='lang', ctx=Load()),
                                attr='code',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='time_format', ctx=Load()),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='time_format', ctx=Store())],
                            value=Call(
                                func=Name(id='posix_to_ldml', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='lang', ctx=Load()),
                                        attr='time_format',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='locale',
                                        value=Name(id='locale', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='babel', ctx=Load()),
                                attr='dates',
                                ctx=Load(),
                            ),
                            attr='format_time',
                            ctx=Load(),
                        ),
                        args=[Name(id='localized_datetime', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='format',
                                value=Name(id='time_format', ctx=Load()),
                            ),
                            keyword(
                                arg='locale',
                                value=Name(id='locale', ctx=Load()),
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
            name='_format_time_ago',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='time_delta', annotation=None, type_comment=None),
                    arg(arg='lang_code', annotation=None, type_comment=None),
                    arg(arg='add_direction', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value=True, kind=None),
                ],
            ),
            body=[
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='lang_code', ctx=Load()),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='langs', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='code', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='code', ctx=Store()),
                                                Name(id='_', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='env', ctx=Load()),
                                                    slice=Constant(value='res.lang', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='get_installed',
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lang_code', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='env', ctx=Load()),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='lang', kind=None)],
                                        keywords=[],
                                    ),
                                    ops=[In()],
                                    comparators=[Name(id='langs', ctx=Load())],
                                ),
                                body=Subscript(
                                    value=Attribute(
                                        value=Name(id='env', ctx=Load()),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='lang', kind=None),
                                    ctx=Load(),
                                ),
                                orelse=BoolOp(
                                    op=Or(),
                                    values=[
                                        Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='env', ctx=Load()),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='lang',
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='langs', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='locale', ctx=Store())],
                    value=Call(
                        func=Name(id='babel_locale_parse', ctx=Load()),
                        args=[Name(id='lang_code', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='babel', ctx=Load()),
                                attr='dates',
                                ctx=Load(),
                            ),
                            attr='format_timedelta',
                            ctx=Load(),
                        ),
                        args=[
                            UnaryOp(
                                op=USub(),
                                operand=Name(id='time_delta', ctx=Load()),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='add_direction',
                                value=Name(id='add_direction', ctx=Load()),
                            ),
                            keyword(
                                arg='locale',
                                value=Name(id='locale', ctx=Load()),
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
            name='format_decimalized_number',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='number', annotation=None, type_comment=None),
                    arg(arg='decimal', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=1, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='Format a number to display to nearest metrics unit next to it.\n\n    Do not display digits if all visible digits are null.\n    Do not display units higher then "Tera" because most of people don\'t know what\n    a "Yotta" is.\n\n    >>> format_decimalized_number(123_456.789)\n    123.5k\n    >>> format_decimalized_number(123_000.789)\n    123k\n    >>> format_decimalized_number(-123_456.789)\n    -123.5k\n    >>> format_decimalized_number(0.789)\n    0.8\n    ', kind=None),
                ),
                For(
                    target=Name(id='unit', ctx=Store()),
                    iter=List(
                        elts=[
                            Constant(value='', kind=None),
                            Constant(value='k', kind=None),
                            Constant(value='M', kind=None),
                            Constant(value='G', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='abs', ctx=Load()),
                                    args=[Name(id='number', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Lt()],
                                comparators=[Constant(value=1000.0, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=BinOp(
                                        left=Constant(value='%g%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='round', ctx=Load()),
                                                    args=[
                                                        Name(id='number', ctx=Load()),
                                                        Name(id='decimal', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Name(id='unit', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        AugAssign(
                            target=Name(id='number', ctx=Store()),
                            op=Div(),
                            value=Constant(value=1000.0, kind=None),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=BinOp(
                        left=Constant(value='%g%s', kind=None),
                        op=Mod(),
                        right=Tuple(
                            elts=[
                                Call(
                                    func=Name(id='round', ctx=Load()),
                                    args=[
                                        Name(id='number', ctx=Load()),
                                        Name(id='decimal', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                Constant(value='T', kind=None),
                            ],
                            ctx=Load(),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='format_decimalized_amount',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='amount', annotation=None, type_comment=None),
                    arg(arg='currency', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='Format a amount to display the currency and also display the metric unit of the amount.\n\n    >>> format_decimalized_amount(123_456.789, res.currency("$"))\n    $123.5k\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='formated_amount', ctx=Store())],
                    value=Call(
                        func=Name(id='format_decimalized_number', ctx=Load()),
                        args=[Name(id='amount', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='currency', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Name(id='formated_amount', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='currency', ctx=Load()),
                            attr='position',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='before', kind=None)],
                    ),
                    body=[
                        Return(
                            value=BinOp(
                                left=Constant(value='%s%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='currency', ctx=Load()),
                                                    attr='symbol',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='', kind=None),
                                            ],
                                        ),
                                        Name(id='formated_amount', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=BinOp(
                        left=Constant(value='%s %s', kind=None),
                        op=Mod(),
                        right=Tuple(
                            elts=[
                                Name(id='formated_amount', ctx=Load()),
                                BoolOp(
                                    op=Or(),
                                    values=[
                                        Attribute(
                                            value=Name(id='currency', ctx=Load()),
                                            attr='symbol',
                                            ctx=Load(),
                                        ),
                                        Constant(value='', kind=None),
                                    ],
                                ),
                            ],
                            ctx=Load(),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='format_amount',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='amount', annotation=None, type_comment=None),
                    arg(arg='currency', annotation=None, type_comment=None),
                    arg(arg='lang_code', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='fmt', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Constant(value='%.{0}f', kind=None),
                            attr='format',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='currency', ctx=Load()),
                                attr='decimal_places',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lang', ctx=Store())],
                    value=Call(
                        func=Name(id='get_lang', ctx=Load()),
                        args=[
                            Name(id='env', ctx=Load()),
                            Name(id='lang_code', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='formatted_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lang', ctx=Load()),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='fmt', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='currency', ctx=Load()),
                                                    attr='round',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='amount', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='grouping',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='monetary',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=' ', kind=None),
                                    Constant(value='\xa0', kind='u'),
                                ],
                                keywords=[],
                            ),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='-', kind=None),
                            Constant(value='-\ufeff', kind='u'),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Name(id='pre', ctx=Store()),
                        Name(id='post', ctx=Store()),
                    ],
                    value=Constant(value='', kind='u'),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='currency', ctx=Load()),
                            attr='position',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='before', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='pre', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='{symbol}\xa0', kind='u'),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='symbol',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='currency', ctx=Load()),
                                                    attr='symbol',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='post', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='\xa0{symbol}', kind='u'),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='symbol',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='currency', ctx=Load()),
                                                    attr='symbol',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Constant(value='{pre}{0}{post}', kind='u'),
                            attr='format',
                            ctx=Load(),
                        ),
                        args=[Name(id='formatted_amount', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='pre',
                                value=Name(id='pre', ctx=Load()),
                            ),
                            keyword(
                                arg='post',
                                value=Name(id='post', ctx=Load()),
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
            name='format_duration',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='value', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Format a float: used to display integral or fractional values as\n        human-readable time spans (e.g. 1.5 as "01:30").\n    ', kind=None),
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='hours', ctx=Store()),
                                Name(id='minutes', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Name(id='divmod', ctx=Load()),
                        args=[
                            BinOp(
                                left=Call(
                                    func=Name(id='abs', ctx=Load()),
                                    args=[Name(id='value', ctx=Load())],
                                    keywords=[],
                                ),
                                op=Mult(),
                                right=Constant(value=60, kind=None),
                            ),
                            Constant(value=60, kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='minutes', ctx=Store())],
                    value=Call(
                        func=Name(id='round', ctx=Load()),
                        args=[Name(id='minutes', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='minutes', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value=60, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='minutes', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='hours', ctx=Store()),
                            op=Add(),
                            value=Constant(value=1, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Name(id='value', ctx=Load()),
                        ops=[Lt()],
                        comparators=[Constant(value=0, kind=None)],
                    ),
                    body=[
                        Return(
                            value=BinOp(
                                left=Constant(value='-%02d:%02d', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='hours', ctx=Load()),
                                        Name(id='minutes', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=BinOp(
                        left=Constant(value='%02d:%02d', kind=None),
                        op=Mod(),
                        right=Tuple(
                            elts=[
                                Name(id='hours', ctx=Load()),
                                Name(id='minutes', ctx=Load()),
                            ],
                            ctx=Load(),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_consteq',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='str1', annotation=None, type_comment=None),
                    arg(arg='str2', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Constant-time string comparison. Suitable to compare bytestrings of fixed,\n        known length only, because length difference is optimized. ', kind=None),
                ),
                Return(
                    value=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='str1', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='str2', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            Compare(
                                left=Call(
                                    func=Name(id='sum', ctx=Load()),
                                    args=[
                                        GeneratorExp(
                                            elt=BinOp(
                                                left=Call(
                                                    func=Name(id='ord', ctx=Load()),
                                                    args=[Name(id='x', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=BitXor(),
                                                right=Call(
                                                    func=Name(id='ord', ctx=Load()),
                                                    args=[Name(id='y', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Tuple(
                                                        elts=[
                                                            Name(id='x', ctx=Store()),
                                                            Name(id='y', ctx=Store()),
                                                        ],
                                                        ctx=Store(),
                                                    ),
                                                    iter=Call(
                                                        func=Name(id='zip', ctx=Load()),
                                                        args=[
                                                            Name(id='str1', ctx=Load()),
                                                            Name(id='str2', ctx=Load()),
                                                        ],
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
                                ops=[Eq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='consteq', ctx=Store())],
            value=Call(
                func=Name(id='getattr', ctx=Load()),
                args=[
                    Attribute(
                        value=Name(id='passlib', ctx=Load()),
                        attr='utils',
                        ctx=Load(),
                    ),
                    Constant(value='consteq', kind=None),
                    Name(id='_consteq', ctx=Load()),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='Unpickler',
            bases=[
                Attribute(
                    value=Name(id='pickle_', ctx=Load()),
                    attr='Unpickler',
                    ctx=Load(),
                ),
                Name(id='object', ctx=Load()),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='find_global', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='find_class', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='_pickle_load',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='stream', annotation=None, type_comment=None),
                    arg(arg='encoding', annotation=None, type_comment=None),
                    arg(arg='errors', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value='ASCII', kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                If(
                    test=Compare(
                        left=Subscript(
                            value=Attribute(
                                value=Name(id='sys', ctx=Load()),
                                attr='version_info',
                                ctx=Load(),
                            ),
                            slice=Constant(value=0, kind=None),
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value=3, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='unpickler', ctx=Store())],
                            value=Call(
                                func=Name(id='Unpickler', ctx=Load()),
                                args=[Name(id='stream', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='encoding',
                                        value=Name(id='encoding', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='unpickler', ctx=Store())],
                            value=Call(
                                func=Name(id='Unpickler', ctx=Load()),
                                args=[Name(id='stream', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                ),
                Try(
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='unpickler', ctx=Load()),
                                    attr='load',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
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
                                            Constant(value='Failed unpickling data, returning default: %r', kind=None),
                                            Name(id='errors', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='exc_info',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Return(
                                    value=Name(id='errors', ctx=Load()),
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
        Assign(
            targets=[Name(id='pickle', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='types', ctx=Load()),
                    attr='ModuleType',
                    ctx=Load(),
                ),
                args=[
                    BinOp(
                        left=Name(id='__name__', ctx=Load()),
                        op=Add(),
                        right=Constant(value='.pickle', kind=None),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='pickle', ctx=Load()),
                    attr='load',
                    ctx=Store(),
                ),
            ],
            value=Name(id='_pickle_load', ctx=Load()),
            type_comment=None,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='pickle', ctx=Load()),
                    attr='loads',
                    ctx=Store(),
                ),
            ],
            value=Lambda(
                args=arguments(
                    posonlyargs=[],
                    args=[
                        arg(arg='text', annotation=None, type_comment=None),
                        arg(arg='encoding', annotation=None, type_comment=None),
                    ],
                    vararg=None,
                    kwonlyargs=[],
                    kw_defaults=[],
                    kwarg=None,
                    defaults=[Constant(value='ASCII', kind=None)],
                ),
                body=Call(
                    func=Name(id='_pickle_load', ctx=Load()),
                    args=[
                        Call(
                            func=Attribute(
                                value=Name(id='io', ctx=Load()),
                                attr='BytesIO',
                                ctx=Load(),
                            ),
                            args=[Name(id='text', ctx=Load())],
                            keywords=[],
                        ),
                    ],
                    keywords=[
                        keyword(
                            arg='encoding',
                            value=Name(id='encoding', ctx=Load()),
                        ),
                    ],
                ),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='pickle', ctx=Load()),
                    attr='dump',
                    ctx=Store(),
                ),
            ],
            value=Attribute(
                value=Name(id='pickle_', ctx=Load()),
                attr='dump',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='pickle', ctx=Load()),
                    attr='dumps',
                    ctx=Store(),
                ),
            ],
            value=Attribute(
                value=Name(id='pickle_', ctx=Load()),
                attr='dumps',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='DotDict',
            bases=[Name(id='dict', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value="Helper for dot.notation access to dictionary attributes\n\n        E.g.\n          foo = DotDict({'bar': False})\n          return foo.bar\n    ", kind=None),
                ),
                FunctionDef(
                    name='__getattr__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attrib', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='val', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='attrib', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=IfExp(
                                test=Compare(
                                    left=Call(
                                        func=Name(id='type', ctx=Load()),
                                        args=[Name(id='val', ctx=Load())],
                                        keywords=[],
                                    ),
                                    ops=[Is()],
                                    comparators=[Name(id='dict', ctx=Load())],
                                ),
                                body=Call(
                                    func=Name(id='DotDict', ctx=Load()),
                                    args=[Name(id='val', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Name(id='val', ctx=Load()),
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
            name='get_diff',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='data_from', annotation=None, type_comment=None),
                    arg(arg='data_to', annotation=None, type_comment=None),
                    arg(arg='custom_style', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Return, in an HTML table, the diff between two texts.\n\n    :param tuple data_from: tuple(text, name), name will be used as table header\n    :param tuple data_to: tuple(text, name), name will be used as table header\n    :param tuple custom_style: string, style css including <style> tag.\n    :return: a string containing the diff in an HTML table format.\n    ', kind=None),
                ),
                FunctionDef(
                    name='handle_style',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='html_diff', annotation=None, type_comment=None),
                            arg(arg='custom_style', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' The HtmlDiff lib will add some useful classes on the DOM to\n        identify elements. Simply append to those classes some BS4 ones.\n        For the table to fit the modal width, some custom style is needed.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='to_append', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='diff_header', kind=None),
                                    Constant(value='diff_next', kind=None),
                                    Constant(value='diff_add', kind=None),
                                    Constant(value='diff_chg', kind=None),
                                    Constant(value='diff_sub', kind=None),
                                ],
                                values=[
                                    Constant(value='bg-600 text-center align-top px-2', kind=None),
                                    Constant(value='d-none', kind=None),
                                    Constant(value='bg-success', kind=None),
                                    Constant(value='bg-warning', kind=None),
                                    Constant(value='bg-danger', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='old', ctx=Store()),
                                    Name(id='new', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='to_append', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='html_diff', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='html_diff', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='old', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='%s %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='old', ctx=Load()),
                                                        Name(id='new', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html_diff', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html_diff', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='nowrap', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='html_diff', ctx=Store()),
                            op=Add(),
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='custom_style', ctx=Load()),
                                    Constant(value='\n            <style>\n                table.diff { width: 100%; }\n                table.diff th.diff_header { width: 50%; }\n                table.diff td.diff_header { white-space: nowrap; }\n                table.diff td { word-break: break-all; }\n            </style>\n        ', kind=None),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='html_diff', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='diff', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Name(id='HtmlDiff', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='tabsize',
                                        value=Constant(value=2, kind=None),
                                    ),
                                ],
                            ),
                            attr='make_table',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='data_from', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='splitlines',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='data_to', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='splitlines',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            Subscript(
                                value=Name(id='data_from', ctx=Load()),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            Subscript(
                                value=Name(id='data_to', ctx=Load()),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='context',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='numlines',
                                value=Constant(value=3, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='handle_style', ctx=Load()),
                        args=[
                            Name(id='diff', ctx=Load()),
                            Name(id='custom_style', ctx=Load()),
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
            name='traverse_containers',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='val', annotation=None, type_comment=None),
                    arg(arg='type_', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Yields atoms filtered by specified type_ (or type tuple), traverses\n    through standard containers (non-string mappings or sequences) *unless*\n    they're selected by the type filter\n    ", kind=None),
                ),
                ImportFrom(
                    module='odoo.models',
                    names=[alias(name='BaseModel', asname=None)],
                    level=0,
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='val', ctx=Load()),
                            Name(id='type_', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Expr(
                            value=Yield(
                                value=Name(id='val', ctx=Load()),
                            ),
                        ),
                    ],
                    orelse=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='val', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Name(id='str', ctx=Load()),
                                            Name(id='bytes', ctx=Load()),
                                            Name(id='BaseModel', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[Return(value=None)],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='val', ctx=Load()),
                                            Name(id='Mapping', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='k', ctx=Store()),
                                                    Name(id='v', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='val', ctx=Load()),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=YieldFrom(
                                                        value=Call(
                                                            func=Name(id='traverse_containers', ctx=Load()),
                                                            args=[
                                                                Name(id='k', ctx=Load()),
                                                                Name(id='type_', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ),
                                                Expr(
                                                    value=YieldFrom(
                                                        value=Call(
                                                            func=Name(id='traverse_containers', ctx=Load()),
                                                            args=[
                                                                Name(id='v', ctx=Load()),
                                                                Name(id='type_', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='val', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='collections', ctx=Load()),
                                                            attr='abc',
                                                            ctx=Load(),
                                                        ),
                                                        attr='Sequence',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                For(
                                                    target=Name(id='v', ctx=Store()),
                                                    iter=Name(id='val', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=YieldFrom(
                                                                value=Call(
                                                                    func=Name(id='traverse_containers', ctx=Load()),
                                                                    args=[
                                                                        Name(id='v', ctx=Load()),
                                                                        Name(id='type_', ctx=Load()),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='hmac',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='scope', annotation=None, type_comment=None),
                    arg(arg='message', annotation=None, type_comment=None),
                    arg(arg='hash_function', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Attribute(
                        value=Name(id='hashlib', ctx=Load()),
                        attr='sha256',
                        ctx=Load(),
                    ),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Compute HMAC with `database.secret` config parameter as key.\n\n    :param env: sudo environment to use for retrieving config parameter\n    :param message: message to authenticate\n    :param scope: scope of the authentication, to have different signature for the same\n        message in different usage\n    :param hash_function: hash function to use for HMAC (default: SHA-256)\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='scope', ctx=Load()),
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValueError', ctx=Load()),
                                args=[Constant(value='Non-empty scope required', kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='secret', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='ir.config_parameter', kind=None),
                                ctx=Load(),
                            ),
                            attr='get_param',
                            ctx=Load(),
                        ),
                        args=[Constant(value='database.secret', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='message', ctx=Store())],
                    value=Call(
                        func=Name(id='repr', ctx=Load()),
                        args=[
                            Tuple(
                                elts=[
                                    Name(id='scope', ctx=Load()),
                                    Name(id='message', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='hmac_lib', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='secret', ctx=Load()),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='message', ctx=Load()),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Name(id='hash_function', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            attr='hexdigest',
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
    type_ignores=[],
)
