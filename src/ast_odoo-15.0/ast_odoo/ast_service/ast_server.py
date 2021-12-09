Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='errno', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='os.path', asname=None)],
        ),
        Import(
            names=[alias(name='platform', asname=None)],
        ),
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='select', asname=None)],
        ),
        Import(
            names=[alias(name='signal', asname=None)],
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
            names=[alias(name='unittest', asname=None)],
        ),
        ImportFrom(
            module='itertools',
            names=[alias(name='chain', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='psutil', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.serving', asname=None)],
        ),
        ImportFrom(
            module='werkzeug.debug',
            names=[alias(name='DebuggedApplication', asname=None)],
            level=0,
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
                    names=[alias(name='fcntl', asname=None)],
                ),
                Import(
                    names=[alias(name='resource', asname=None)],
                ),
                Try(
                    body=[
                        Import(
                            names=[alias(name='inotify', asname=None)],
                        ),
                        ImportFrom(
                            module='inotify.adapters',
                            names=[alias(name='InotifyTrees', asname=None)],
                            level=0,
                        ),
                        ImportFrom(
                            module='inotify.constants',
                            names=[
                                alias(name='IN_MODIFY', asname=None),
                                alias(name='IN_CREATE', asname=None),
                                alias(name='IN_MOVED_TO', asname=None),
                            ],
                            level=0,
                        ),
                        Assign(
                            targets=[Name(id='INOTIFY_LISTEN_EVENTS', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='IN_MODIFY', ctx=Load()),
                                    op=BitOr(),
                                    right=Name(id='IN_CREATE', ctx=Load()),
                                ),
                                op=BitOr(),
                                right=Name(id='IN_MOVED_TO', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='ImportError', ctx=Load()),
                            name=None,
                            body=[
                                Assign(
                                    targets=[Name(id='inotify', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            orelse=[
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='signal', ctx=Load()),
                            attr='SIGHUP',
                            ctx=Store(),
                        ),
                    ],
                    value=UnaryOp(
                        op=USub(),
                        operand=Constant(value=1, kind=None),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='inotify', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
            ],
        ),
        If(
            test=UnaryOp(
                op=Not(),
                operand=Name(id='inotify', ctx=Load()),
            ),
            body=[
                Try(
                    body=[
                        Import(
                            names=[alias(name='watchdog', asname=None)],
                        ),
                        ImportFrom(
                            module='watchdog.observers',
                            names=[alias(name='Observer', asname=None)],
                            level=0,
                        ),
                        ImportFrom(
                            module='watchdog.events',
                            names=[
                                alias(name='FileCreatedEvent', asname=None),
                                alias(name='FileModifiedEvent', asname=None),
                                alias(name='FileMovedEvent', asname=None),
                            ],
                            level=0,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='ImportError', ctx=Load()),
                            name=None,
                            body=[
                                Assign(
                                    targets=[Name(id='watchdog', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            orelse=[],
        ),
        Try(
            body=[
                ImportFrom(
                    module='setproctitle',
                    names=[alias(name='setproctitle', asname=None)],
                    level=0,
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='setproctitle', ctx=Store())],
                            value=Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[arg(arg='x', annotation=None, type_comment=None)],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=Constant(value=None, kind=None),
                            ),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo.modules',
            names=[alias(name='get_modules', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.registry',
            names=[alias(name='Registry', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.release',
            names=[alias(name='nt_service_name', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='config', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='stripped_sys_argv', asname=None),
                alias(name='dumpstacks', asname=None),
                alias(name='log_ormcache_stats', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='tests',
            names=[
                alias(name='loader', asname=None),
                alias(name='runner', asname=None),
            ],
            level=2,
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
            targets=[Name(id='SLEEP_INTERVAL', ctx=Store())],
            value=Constant(value=60, kind=None),
            type_comment=None,
        ),
        FunctionDef(
            name='memory_info',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='process', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    :return: the relevant memory usage according to the OS in bytes.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='pmem', ctx=Store())],
                    value=Call(
                        func=BoolOp(
                            op=Or(),
                            values=[
                                Call(
                                    func=Name(id='getattr', ctx=Load()),
                                    args=[
                                        Name(id='process', ctx=Load()),
                                        Constant(value='memory_info', kind=None),
                                        Constant(value=None, kind=None),
                                    ],
                                    keywords=[],
                                ),
                                Attribute(
                                    value=Name(id='process', ctx=Load()),
                                    attr='get_memory_info',
                                    ctx=Load(),
                                ),
                            ],
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Call(
                            func=Attribute(
                                value=Name(id='platform', ctx=Load()),
                                attr='system',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='Darwin', kind=None)],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Name(id='pmem', ctx=Load()),
                                attr='rss',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Attribute(
                        value=Name(id='pmem', ctx=Load()),
                        attr='vms',
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='set_limit_memory_hard',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='posix', kind=None)],
                            ),
                            Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='limit_memory_hard', kind=None),
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='rlimit', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Call(
                                        func=Attribute(
                                            value=Name(id='platform', ctx=Load()),
                                            attr='system',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    ops=[Eq()],
                                    comparators=[Constant(value='Darwin', kind=None)],
                                ),
                                body=Attribute(
                                    value=Name(id='resource', ctx=Load()),
                                    attr='RLIMIT_RSS',
                                    ctx=Load(),
                                ),
                                orelse=Attribute(
                                    value=Name(id='resource', ctx=Load()),
                                    attr='RLIMIT_AS',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='soft', ctx=Store()),
                                        Name(id='hard', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='resource', ctx=Load()),
                                    attr='getrlimit',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rlimit', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='resource', ctx=Load()),
                                    attr='setrlimit',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='rlimit', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='limit_memory_hard', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='hard', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
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
            name='empty_pipe',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='fd', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Try(
                    body=[
                        While(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='fd', ctx=Load()),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[Pass()],
                            orelse=[],
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='OSError', ctx=Load()),
                            name='e',
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='e', ctx=Load()),
                                            attr='errno',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='errno', ctx=Load()),
                                                        attr='EAGAIN',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[Raise(exc=None, cause=None)],
                                    orelse=[],
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
        ClassDef(
            name='LoggingBaseWSGIServerMixIn',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='handle_error',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='request', annotation=None, type_comment=None),
                            arg(arg='client_address', annotation=None, type_comment=None),
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
                                Tuple(
                                    elts=[
                                        Name(id='t', ctx=Store()),
                                        Name(id='e', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='exc_info',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='t', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='socket', ctx=Load()),
                                                attr='error',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='e', ctx=Load()),
                                            attr='errno',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='errno', ctx=Load()),
                                                attr='EPIPE',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='exception',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Exception happened during processing of request from %s', kind=None),
                                    Name(id='client_address', ctx=Load()),
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
            name='BaseWSGIServerNoBind',
            bases=[
                Name(id='LoggingBaseWSGIServerMixIn', ctx=Load()),
                Attribute(
                    value=Attribute(
                        value=Name(id='werkzeug', ctx=Load()),
                        attr='serving',
                        ctx=Load(),
                    ),
                    attr='BaseWSGIServer',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' werkzeug Base WSGI Server patched to skip socket binding. PreforkServer\n    use this class, sets the socket and calls the process_request() manually\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='app', annotation=None, type_comment=None),
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
                                        value=Attribute(
                                            value=Name(id='werkzeug', ctx=Load()),
                                            attr='serving',
                                            ctx=Load(),
                                        ),
                                        attr='BaseWSGIServer',
                                        ctx=Load(),
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Constant(value='127.0.0.1', kind=None),
                                    Constant(value=0, kind=None),
                                    Name(id='app', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='socket',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='socket',
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
                    name='server_activate',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='RequestHandler',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='werkzeug', ctx=Load()),
                        attr='serving',
                        ctx=Load(),
                    ),
                    attr='WSGIRequestHandler',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='setup',
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
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='test_enable', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='test_file', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='timeout',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=5, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='RequestHandler', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setup',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='me', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='currentThread',
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
                                    value=Name(id='me', ctx=Load()),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Constant(value='odoo.service.http.request.%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='me', ctx=Load()),
                                            attr='ident',
                                            ctx=Load(),
                                        ),
                                    ],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ThreadedWSGIServerReloadable',
            bases=[
                Name(id='LoggingBaseWSGIServerMixIn', ctx=Load()),
                Attribute(
                    value=Attribute(
                        value=Name(id='werkzeug', ctx=Load()),
                        attr='serving',
                        ctx=Load(),
                    ),
                    attr='ThreadedWSGIServer',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' werkzeug Threaded WSGI Server patched to allow reusing a listen socket\n    given by the environment, this is used by autoreload to keep the listen\n    socket open when a reload happens.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='host', annotation=None, type_comment=None),
                            arg(arg='port', annotation=None, type_comment=None),
                            arg(arg='app', annotation=None, type_comment=None),
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
                                    attr='max_http_threads',
                                    ctx=Store(),
                                ),
                            ],
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
                                args=[Constant(value='ODOO_MAX_HTTP_THREADS', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='max_http_threads',
                                ctx=Load(),
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='max_http_threads',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='max_http_threads',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='max_http_threads',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=BinOp(
                                                        left=Subscript(
                                                            value=Name(id='config', ctx=Load()),
                                                            slice=Constant(value='db_maxconn', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        op=FloorDiv(),
                                                        right=Constant(value=2, kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='http_threads_sem',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='Semaphore',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='max_http_threads',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ThreadedWSGIServerReloadable', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='host', ctx=Load()),
                                    Name(id='port', ctx=Load()),
                                    Name(id='app', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='handler',
                                        value=Name(id='RequestHandler', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='daemon_threads',
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
                    name='server_bind',
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
                            targets=[Name(id='SD_LISTEN_FDS_START', ctx=Store())],
                            value=Constant(value=3, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='environ',
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='LISTEN_FDS', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='1', kind=None)],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='environ',
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='LISTEN_PID', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[
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
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='reload_socket',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='socket',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='socket', ctx=Load()),
                                            attr='fromfd',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='SD_LISTEN_FDS_START', ctx=Load()),
                                            Attribute(
                                                value=Name(id='socket', ctx=Load()),
                                                attr='AF_INET',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='socket', ctx=Load()),
                                                attr='SOCK_STREAM',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
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
                                        args=[Constant(value='HTTP service (werkzeug) running through socket activation', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='reload_socket',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='ThreadedWSGIServerReloadable', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='server_bind',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='HTTP service (werkzeug) running on %s:%s', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='server_name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='server_port',
                                                ctx=Load(),
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
                FunctionDef(
                    name='server_activate',
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='reload_socket',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='ThreadedWSGIServerReloadable', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='server_activate',
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
                    name='process_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='request', annotation=None, type_comment=None),
                            arg(arg='client_address', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Start a new thread to process the request.\n        Override the default method of class socketserver.ThreadingMixIn\n        to be able to get the thread object which is instantiated\n        and set its start time as an attribute\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='t', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='Thread',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='target',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='process_request_thread',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='args',
                                        value=Tuple(
                                            elts=[
                                                Name(id='request', ctx=Load()),
                                                Name(id='client_address', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='t', ctx=Load()),
                                    attr='daemon',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='daemon_threads',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='t', ctx=Load()),
                                    attr='type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='http', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='t', ctx=Load()),
                                    attr='start_time',
                                    ctx=Store(),
                                ),
                            ],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='t', ctx=Load()),
                                    attr='start',
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
                    name='_handle_request_noblock',
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
                            value=Constant(value='\n        In the python module `socketserver` `process_request` loop,\n        the __shutdown_request flag is not checked between select and accept.\n        Thus when we set it to `True` thanks to the call `httpd.shutdown`,\n        a last request is accepted before exiting the loop.\n        We override this function to add an additional check before the accept().\n        ', kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_BaseServer__shutdown_request',
                                ctx=Load(),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='max_http_threads',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='http_threads_sem',
                                                    ctx=Load(),
                                                ),
                                                attr='acquire',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='timeout',
                                                    value=Constant(value=0.1, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ThreadedWSGIServerReloadable', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_handle_request_noblock',
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
                    name='shutdown_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='request', annotation=None, type_comment=None),
                        ],
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
                                attr='max_http_threads',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='http_threads_sem',
                                                ctx=Load(),
                                            ),
                                            attr='release',
                                            ctx=Load(),
                                        ),
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='shutdown_request',
                                    ctx=Load(),
                                ),
                                args=[Name(id='request', ctx=Load())],
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
            name='FSWatcherBase',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='handle_file',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='path', ctx=Load()),
                                            attr='endswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='.py', kind=None)],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='path',
                                                            ctx=Load(),
                                                        ),
                                                        attr='basename',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='path', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='startswith',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='.~', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='source', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
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
                                                op=Add(),
                                                right=Constant(value=b'\n', kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='compile', ctx=Load()),
                                                args=[
                                                    Name(id='source', ctx=Load()),
                                                    Name(id='path', ctx=Load()),
                                                    Constant(value='exec', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='IOError', ctx=Load()),
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
                                                            Constant(value='autoreload: python code change detected, IOError for %s', kind=None),
                                                            Name(id='path', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='SyntaxError', ctx=Load()),
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
                                                            Constant(value='autoreload: python code change detected, SyntaxError in %s', kind=None),
                                                            Name(id='path', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='getattr', ctx=Load()),
                                                    args=[
                                                        Name(id='odoo', ctx=Load()),
                                                        Constant(value='phoenix', kind=None),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='autoreload: python code updated, autoreload activated', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='restart', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Return(
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='FSWatcherWatchdog',
            bases=[Name(id='FSWatcherBase', ctx=Load())],
            keywords=[],
            body=[
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
                                    attr='observer',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='Observer', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='path', ctx=Store()),
                            iter=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='addons',
                                    ctx=Load(),
                                ),
                                attr='__path__',
                                ctx=Load(),
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
                                            Constant(value='Watching addons folder %s', kind=None),
                                            Name(id='path', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='observer',
                                                ctx=Load(),
                                            ),
                                            attr='schedule',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Name(id='path', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='recursive',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
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
                    name='dispatch',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='event', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Name(id='FileCreatedEvent', ctx=Load()),
                                            Name(id='FileModifiedEvent', ctx=Load()),
                                            Name(id='FileMovedEvent', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='is_directory',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Name(id='event', ctx=Load()),
                                                    Constant(value='dest_path', kind=None),
                                                    Attribute(
                                                        value=Name(id='event', ctx=Load()),
                                                        attr='src_path',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='handle_file',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='path', ctx=Load())],
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
                    name='start',
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
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='observer',
                                        ctx=Load(),
                                    ),
                                    attr='start',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='AutoReload watcher running with watchdog', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='stop',
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
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='observer',
                                        ctx=Load(),
                                    ),
                                    attr='stop',
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
                                        attr='observer',
                                        ctx=Load(),
                                    ),
                                    attr='join',
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
            name='FSWatcherInotify',
            bases=[Name(id='FSWatcherBase', ctx=Load())],
            keywords=[],
            body=[
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
                                    attr='started',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='inotify', ctx=Load()),
                                            attr='adapters',
                                            ctx=Load(),
                                        ),
                                        attr='_LOGGER',
                                        ctx=Load(),
                                    ),
                                    attr='setLevel',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='ERROR',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='paths_to_watch', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='path', ctx=Store()),
                            iter=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='addons',
                                    ctx=Load(),
                                ),
                                attr='__path__',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='paths_to_watch', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='path', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Watching addons folder %s', kind=None),
                                            Name(id='path', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='watcher',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='InotifyTrees', ctx=Load()),
                                args=[Name(id='paths_to_watch', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='mask',
                                        value=Name(id='INOTIFY_LISTEN_EVENTS', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='block_duration_s',
                                        value=Constant(value=0.5, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='AutoReload watcher running with inotify', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dir_creation_events', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value='IN_MOVED_TO', kind=None),
                                            Constant(value='IN_CREATE', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='started',
                                ctx=Load(),
                            ),
                            body=[
                                For(
                                    target=Name(id='event', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='watcher',
                                                ctx=Load(),
                                            ),
                                            attr='event_gen',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='timeout_s',
                                                value=Constant(value=0, kind=None),
                                            ),
                                            keyword(
                                                arg='yield_nones',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='_', ctx=Store()),
                                                        Name(id='type_names', ctx=Store()),
                                                        Name(id='path', ctx=Store()),
                                                        Name(id='filename', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='event', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Constant(value='IN_ISDIR', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='type_names', ctx=Load())],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Constant(value='IN_DELETE', kind=None),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='type_names', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='full_path', ctx=Store())],
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
                                                                    Name(id='path', ctx=Load()),
                                                                    Name(id='filename', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='handle_file',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='full_path', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            body=[Return(value=None)],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(id='dir_creation_events', ctx=Load()),
                                                            attr='intersection',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='type_names', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='full_path', ctx=Store())],
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
                                                                    Name(id='path', ctx=Load()),
                                                                    Name(id='filename', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
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
                                                                args=[Name(id='full_path', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                For(
                                                                    target=Name(id='file', ctx=Store()),
                                                                    iter=Name(id='files', ctx=Load()),
                                                                    body=[
                                                                        If(
                                                                            test=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='handle_file',
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
                                                                                            Name(id='root', ctx=Load()),
                                                                                            Name(id='file', ctx=Load()),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            body=[Return(value=None)],
                                                                            orelse=[],
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
                                            ],
                                        ),
                                    ],
                                    orelse=[],
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
                    name='start',
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
                                    attr='started',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='thread',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='Thread',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='target',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='run',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='odoo.service.autoreload.watcher', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='thread',
                                        ctx=Load(),
                                    ),
                                    attr='setDaemon',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=True, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='thread',
                                        ctx=Load(),
                                    ),
                                    attr='start',
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
                    name='stop',
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
                                    attr='started',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='thread',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Delete(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='watcher',
                                    ctx=Del(),
                                ),
                            ],
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
            name='CommonServer',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='app', annotation=None, type_comment=None),
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
                                    attr='app',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='app', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_on_stop_funcs',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='interface',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='http_interface', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='0.0.0.0', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='port',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='http_port', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='pid',
                                    ctx=Store(),
                                ),
                            ],
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='close_socket',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sock', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Closes a socket instance cleanly\n        :param sock: the network socket to close\n        :type sock: socket.socket\n        ', kind=None),
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sock', ctx=Load()),
                                            attr='shutdown',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='socket', ctx=Load()),
                                                attr='SHUT_RDWR',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='socket', ctx=Load()),
                                        attr='error',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='errno',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='errno', ctx=Load()),
                                                        attr='EBADF',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[Return(value=None)],
                                            orelse=[],
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='errno',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='errno', ctx=Load()),
                                                                attr='ENOTCONN',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='platform', ctx=Load()),
                                                                attr='system',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='Darwin', kind=None),
                                                                    Constant(value='Windows', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[Raise(exc=None, cause=None)],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sock', ctx=Load()),
                                    attr='close',
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
                    name='on_stop',
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
                            value=Constant(value=' Register a cleanup function to be executed when the server stops ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_on_stop_funcs',
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
                    name='stop',
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
                            target=Name(id='func', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_on_stop_funcs',
                                ctx=Load(),
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='on_close call %s', kind=None),
                                                    Name(id='func', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='func', ctx=Load()),
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
                                                            Constant(value='Exception in %s', kind=None),
                                                            Attribute(
                                                                value=Name(id='func', ctx=Load()),
                                                                attr='__name__',
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ThreadedServer',
            bases=[Name(id='CommonServer', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='app', annotation=None, type_comment=None),
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
                                            Name(id='ThreadedServer', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[Name(id='app', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='main_thread_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='threading', ctx=Load()),
                                        attr='currentThread',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='ident',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='quit_signals_received',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='httpd',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='limits_reached_threads',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='limit_reached_time',
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
                    name='signal_handler',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sig', annotation=None, type_comment=None),
                            arg(arg='frame', annotation=None, type_comment=None),
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
                                left=Name(id='sig', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='signal', ctx=Load()),
                                                attr='SIGINT',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='signal', ctx=Load()),
                                                attr='SIGTERM',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='quit_signals_received',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='quit_signals_received',
                                            ctx=Load(),
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
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
                                                args=[Constant(value='Forced shutdown.\n', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='_exit',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0, kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='KeyboardInterrupt', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id='hasattr', ctx=Load()),
                                                args=[
                                                    Name(id='signal', ctx=Load()),
                                                    Constant(value='SIGXCPU', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Name(id='sig', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='signal', ctx=Load()),
                                                        attr='SIGXCPU',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
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
                                                args=[Constant(value='CPU time limit exceeded! Shutting down immediately\n', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='sys', ctx=Load()),
                                                        attr='stderr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='flush',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='_exit',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0, kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='sig', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='signal', ctx=Load()),
                                                        attr='SIGHUP',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='odoo', ctx=Load()),
                                                            attr='phoenix',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='quit_signals_received',
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Constant(value=1, kind=None),
                                                ),
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='KeyboardInterrupt', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
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
                    name='process_limit',
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
                            targets=[Name(id='memory', ctx=Store())],
                            value=Call(
                                func=Name(id='memory_info', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='psutil', ctx=Load()),
                                            attr='Process',
                                            ctx=Load(),
                                        ),
                                        args=[
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
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='limit_memory_soft', kind=None),
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Name(id='memory', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[
                                            Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='limit_memory_soft', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Server memory limit (%s) reached.', kind=None),
                                            Name(id='memory', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='limits_reached_threads',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='threading', ctx=Load()),
                                                    attr='currentThread',
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
                        For(
                            target=Name(id='thread', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='enumerate',
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
                                                operand=Attribute(
                                                    value=Name(id='thread', ctx=Load()),
                                                    attr='daemon',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='getattr', ctx=Load()),
                                                    args=[
                                                        Name(id='thread', ctx=Load()),
                                                        Constant(value='type', kind=None),
                                                        Constant(value=None, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='cron', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Name(id='thread', ctx=Load()),
                                                    Constant(value='start_time', kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='thread_execution_time', ctx=Store())],
                                                    value=BinOp(
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
                                                        right=Attribute(
                                                            value=Name(id='thread', ctx=Load()),
                                                            attr='start_time',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='thread_limit_time_real', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='config', ctx=Load()),
                                                        slice=Constant(value='limit_time_real', kind=None),
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
                                                                    func=Name(id='getattr', ctx=Load()),
                                                                    args=[
                                                                        Name(id='thread', ctx=Load()),
                                                                        Constant(value='type', kind=None),
                                                                        Constant(value=None, kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='cron', kind=None)],
                                                            ),
                                                            Subscript(
                                                                value=Name(id='config', ctx=Load()),
                                                                slice=Constant(value='limit_time_real_cron', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='config', ctx=Load()),
                                                                    slice=Constant(value='limit_time_real_cron', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='thread_limit_time_real', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='config', ctx=Load()),
                                                                slice=Constant(value='limit_time_real_cron', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='thread_limit_time_real', ctx=Load()),
                                                            Compare(
                                                                left=Name(id='thread_execution_time', ctx=Load()),
                                                                ops=[Gt()],
                                                                comparators=[Name(id='thread_limit_time_real', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='warning',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='Thread %s virtual real time limit (%d/%ds) reached.', kind=None),
                                                                    Name(id='thread', ctx=Load()),
                                                                    Name(id='thread_execution_time', ctx=Load()),
                                                                    Name(id='thread_limit_time_real', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='limits_reached_threads',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='add',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='thread', ctx=Load())],
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
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='thread', ctx=Store()),
                            iter=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='limits_reached_threads',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='thread', ctx=Load()),
                                                attr='is_alive',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='limits_reached_threads',
                                                        ctx=Load(),
                                                    ),
                                                    attr='remove',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='thread', ctx=Load())],
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='limits_reached_threads',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='limit_reached_time',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='limit_reached_time',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='time', ctx=Load()),
                                                    attr='time',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='limit_reached_time',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=None, kind=None),
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
                    name='cron_thread',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='number', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        ImportFrom(
                            module='odoo.addons.base.models.ir_cron',
                            names=[alias(name='ir_cron', asname=None)],
                            level=0,
                        ),
                        Assign(
                            targets=[Name(id='conn', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='sql_db',
                                        ctx=Load(),
                                    ),
                                    attr='db_connect',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='postgres', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='conn', ctx=Load()),
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
                                    targets=[Name(id='pg_conn', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='cr', ctx=Load()),
                                        attr='_cnx',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='LISTEN cron_trigger', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='commit',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                While(
                                    test=Constant(value=True, kind=None),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='select', ctx=Load()),
                                                    attr='select',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[Name(id='pg_conn', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                    List(elts=[], ctx=Load()),
                                                    BinOp(
                                                        left=Name(id='SLEEP_INTERVAL', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='number', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='time', ctx=Load()),
                                                    attr='sleep',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='number', ctx=Load()),
                                                        op=Div(),
                                                        right=Constant(value=100, kind=None),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='pg_conn', ctx=Load()),
                                                    attr='poll',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='registries', ctx=Store())],
                                            value=Attribute(
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
                                                attr='registries',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='cron%d polling for jobs', kind=None),
                                                    Name(id='number', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='db_name', ctx=Store()),
                                                    Name(id='registry', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='registries', ctx=Load()),
                                                        attr='d',
                                                        ctx=Load(),
                                                    ),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Attribute(
                                                        value=Name(id='registry', ctx=Load()),
                                                        attr='ready',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='thread', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='threading', ctx=Load()),
                                                                    attr='currentThread',
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
                                                                    value=Name(id='thread', ctx=Load()),
                                                                    attr='start_time',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
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
                                                        Try(
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='ir_cron', ctx=Load()),
                                                                            attr='_process_jobs',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='db_name', ctx=Load())],
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
                                                                                    Constant(value='cron%d encountered an Exception:', kind=None),
                                                                                    Name(id='number', ctx=Load()),
                                                                                ],
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
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='thread', ctx=Load()),
                                                                    attr='start_time',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=None, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
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
                    name='cron_spawn',
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
                            value=Constant(value=' Start the above runner function in a daemon thread.\n\n        The thread is a typical daemon thread: it will never quit and must be\n        terminated when the main process exits - with no consequence (the processing\n        threads it spawns are not marked daemon).\n\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
                                        attr='datetime',
                                        ctx=Load(),
                                    ),
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2012-01-01', kind=None),
                                    Constant(value='%Y-%m-%d', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
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
                                        slice=Constant(value='max_cron_threads', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                FunctionDef(
                                    name='target',
                                    args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cron_thread',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='i', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    decorator_list=[],
                                    returns=None,
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='t', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='Thread',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='target',
                                                value=Name(id='target', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='name',
                                                value=BinOp(
                                                    left=Constant(value='odoo.service.cron.cron%d', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='i', ctx=Load()),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='t', ctx=Load()),
                                            attr='setDaemon',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=True, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='t', ctx=Load()),
                                            attr='type',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='cron', kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='t', ctx=Load()),
                                            attr='start',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                                            BinOp(
                                                left=Constant(value='cron%d started!', kind=None),
                                                op=Mod(),
                                                right=Name(id='i', ctx=Load()),
                                            ),
                                        ],
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
                    name='http_thread',
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
                        FunctionDef(
                            name='app',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='e', annotation=None, type_comment=None),
                                    arg(arg='s', annotation=None, type_comment=None),
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
                                            attr='app',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='e', ctx=Load()),
                                            Name(id='s', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='httpd',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='ThreadedWSGIServerReloadable', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='interface',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='port',
                                        ctx=Load(),
                                    ),
                                    Name(id='app', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='httpd',
                                        ctx=Load(),
                                    ),
                                    attr='serve_forever',
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
                    name='http_spawn',
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
                            targets=[Name(id='t', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='Thread',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='target',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='http_thread',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='odoo.service.httpd', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='t', ctx=Load()),
                                    attr='setDaemon',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=True, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='t', ctx=Load()),
                                    attr='start',
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
                    name='start',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stop', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Setting signal handlers', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='set_limit_memory_hard', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
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
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='signal_handler',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
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
                                                attr='SIGTERM',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='signal_handler',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
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
                                                attr='SIGCHLD',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='signal_handler',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
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
                                                attr='SIGHUP',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='signal_handler',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
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
                                                attr='SIGXCPU',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='signal_handler',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
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
                                                attr='SIGQUIT',
                                                ctx=Load(),
                                            ),
                                            Name(id='dumpstacks', ctx=Load()),
                                        ],
                                        keywords=[],
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
                                                attr='SIGUSR1',
                                                ctx=Load(),
                                            ),
                                            Name(id='log_ormcache_stats', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='nt', kind=None)],
                                    ),
                                    body=[
                                        Import(
                                            names=[alias(name='win32api', asname=None)],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='win32api', ctx=Load()),
                                                    attr='SetConsoleCtrlHandler',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='sig', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='signal_handler',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(id='sig', ctx=Load()),
                                                                Constant(value=None, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='test_mode', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='test_enable', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='test_file', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='test_mode', ctx=Load()),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='http_enable', kind=None),
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='stop', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='http_spawn',
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
                    name='stop',
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
                            value=Constant(value=' Shutdown the WSGI server. Wait for non daemon threads.\n        ', kind=None),
                        ),
                        If(
                            test=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='odoo', ctx=Load()),
                                    Constant(value='phoenix', kind=None),
                                    Constant(value=None, kind=None),
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
                                        args=[Constant(value='Initiating server reload', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Initiating shutdown', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Hit CTRL-C again or send a second signal to force the shutdown.', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='stop_time', ctx=Store())],
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='httpd',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='httpd',
                                                ctx=Load(),
                                            ),
                                            attr='shutdown',
                                            ctx=Load(),
                                        ),
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='stop',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='me', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='currentThread',
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
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='current thread: %r', kind=None),
                                    Name(id='me', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='thread', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='enumerate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='debug',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='process %r (%r)', kind=None),
                                            Name(id='thread', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='thread', ctx=Load()),
                                                    attr='isDaemon',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='thread', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Name(id='me', ctx=Load())],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='thread', ctx=Load()),
                                                        attr='isDaemon',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='thread', ctx=Load()),
                                                    attr='ident',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='main_thread_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Name(id='thread', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='limits_reached_threads',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        While(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='thread', ctx=Load()),
                                                            attr='is_alive',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Compare(
                                                        left=BinOp(
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
                                                            right=Name(id='stop_time', ctx=Load()),
                                                        ),
                                                        ops=[Lt()],
                                                        comparators=[Constant(value=1, kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='debug',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='join and sleep', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='thread', ctx=Load()),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=0.05, kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='time', ctx=Load()),
                                                            attr='sleep',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=0.05, kind=None)],
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='shutdown',
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
                    name='run',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='preload', annotation=None, type_comment=None),
                            arg(arg='stop', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Start the http server and the cron thread then wait for a signal.\n\n        The first SIGINT or SIGTERM signal will initiate a graceful shutdown while\n        a second one if any will force an immediate exit.\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='stop',
                                        value=Name(id='stop', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='rc', ctx=Store())],
                            value=Call(
                                func=Name(id='preload_registries', ctx=Load()),
                                args=[Name(id='preload', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='stop', ctx=Load()),
                            body=[
                                If(
                                    test=Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='test_enable', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='logger', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='tests',
                                                        ctx=Load(),
                                                    ),
                                                    attr='runner',
                                                    ctx=Load(),
                                                ),
                                                attr='_logger',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='Registry', ctx=Load()),
                                                            attr='registries',
                                                            ctx=Load(),
                                                        ),
                                                        attr='_lock',
                                                        ctx=Load(),
                                                    ),
                                                    optional_vars=None,
                                                ),
                                            ],
                                            body=[
                                                For(
                                                    target=Tuple(
                                                        elts=[
                                                            Name(id='db', ctx=Store()),
                                                            Name(id='registry', ctx=Store()),
                                                        ],
                                                        ctx=Store(),
                                                    ),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='Registry', ctx=Load()),
                                                                    attr='registries',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='d',
                                                                ctx=Load(),
                                                            ),
                                                            attr='items',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='report', ctx=Store())],
                                                            value=Attribute(
                                                                value=Name(id='registry', ctx=Load()),
                                                                attr='_assertion_report',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='log', ctx=Store())],
                                                            value=IfExp(
                                                                test=UnaryOp(
                                                                    op=Not(),
                                                                    operand=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='report', ctx=Load()),
                                                                            attr='wasSuccessful',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                body=Attribute(
                                                                    value=Name(id='logger', ctx=Load()),
                                                                    attr='error',
                                                                    ctx=Load(),
                                                                ),
                                                                orelse=IfExp(
                                                                    test=UnaryOp(
                                                                        op=Not(),
                                                                        operand=Attribute(
                                                                            value=Name(id='report', ctx=Load()),
                                                                            attr='testsRun',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    body=Attribute(
                                                                        value=Name(id='logger', ctx=Load()),
                                                                        attr='warning',
                                                                        ctx=Load(),
                                                                    ),
                                                                    orelse=Attribute(
                                                                        value=Name(id='logger', ctx=Load()),
                                                                        attr='info',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='log', ctx=Load()),
                                                                args=[
                                                                    Constant(value='%s when loading database %r', kind=None),
                                                                    Name(id='report', ctx=Load()),
                                                                    Name(id='db', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stop',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='rc', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='cron_spawn',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                While(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='quit_signals_received',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='process_limit',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='limit_reached_time',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='has_other_valid_requests', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='any', ctx=Load()),
                                                        args=[
                                                            GeneratorExp(
                                                                elt=BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        UnaryOp(
                                                                            op=Not(),
                                                                            operand=Attribute(
                                                                                value=Name(id='t', ctx=Load()),
                                                                                attr='daemon',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                        Compare(
                                                                            left=Name(id='t', ctx=Load()),
                                                                            ops=[NotIn()],
                                                                            comparators=[
                                                                                Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='limits_reached_threads',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='t', ctx=Store()),
                                                                        iter=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='threading', ctx=Load()),
                                                                                attr='enumerate',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        ifs=[
                                                                            Compare(
                                                                                left=Call(
                                                                                    func=Name(id='getattr', ctx=Load()),
                                                                                    args=[
                                                                                        Name(id='t', ctx=Load()),
                                                                                        Constant(value='type', kind=None),
                                                                                        Constant(value=None, kind=None),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='http', kind=None)],
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
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='has_other_valid_requests', ctx=Load()),
                                                            ),
                                                            Compare(
                                                                left=BinOp(
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
                                                                    right=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='limit_reached_time',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Name(id='SLEEP_INTERVAL', ctx=Load())],
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
                                                                args=[Constant(value='Dumping stacktrace of limit exceeding threads before reloading', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='dumpstacks', ctx=Load()),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='thread_idents',
                                                                        value=ListComp(
                                                                            elt=Attribute(
                                                                                value=Name(id='thread', ctx=Load()),
                                                                                attr='ident',
                                                                                ctx=Load(),
                                                                            ),
                                                                            generators=[
                                                                                comprehension(
                                                                                    target=Name(id='thread', ctx=Store()),
                                                                                    iter=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='limits_reached_threads',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ifs=[],
                                                                                    is_async=0,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='reload',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='time', ctx=Load()),
                                                                    attr='sleep',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=1, kind=None)],
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
                                                            value=Name(id='time', ctx=Load()),
                                                            attr='sleep',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='SLEEP_INTERVAL', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='KeyboardInterrupt', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='stop',
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
                    name='reload',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='kill',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pid',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='signal', ctx=Load()),
                                        attr='SIGHUP',
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
        ClassDef(
            name='GeventServer',
            bases=[Name(id='CommonServer', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='app', annotation=None, type_comment=None),
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
                                            Name(id='GeventServer', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[Name(id='app', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='port',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='longpolling_port', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='httpd',
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
                    name='process_limits',
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
                            targets=[Name(id='restart', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ppid',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='getppid',
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
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='LongPolling Parent changed', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='pid',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='restart', ctx=Store())],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='memory', ctx=Store())],
                            value=Call(
                                func=Name(id='memory_info', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='psutil', ctx=Load()),
                                            attr='Process',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='pid',
                                                ctx=Load(),
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
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='limit_memory_soft', kind=None),
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Name(id='memory', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[
                                            Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='limit_memory_soft', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='LongPolling virtual memory limit reached: %s', kind=None),
                                            Name(id='memory', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='restart', ctx=Store())],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='restart', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='kill',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='pid',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='signal', ctx=Load()),
                                                attr='SIGTERM',
                                                ctx=Load(),
                                            ),
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
                    name='watchdog',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='beat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=4, kind=None)],
                    ),
                    body=[
                        Import(
                            names=[alias(name='gevent', asname=None)],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ppid',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='getppid',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Constant(value=True, kind=None),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='process_limits',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='gevent', ctx=Load()),
                                            attr='sleep',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='beat', ctx=Load())],
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
                    name='start',
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
                        Import(
                            names=[alias(name='gevent', asname=None)],
                        ),
                        Try(
                            body=[
                                ImportFrom(
                                    module='gevent.pywsgi',
                                    names=[
                                        alias(name='WSGIServer', asname=None),
                                        alias(name='WSGIHandler', asname=None),
                                    ],
                                    level=0,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ImportError', ctx=Load()),
                                    name=None,
                                    body=[
                                        ImportFrom(
                                            module='gevent.wsgi',
                                            names=[
                                                alias(name='WSGIServer', asname=None),
                                                alias(name='WSGIHandler', asname=None),
                                            ],
                                            level=0,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        ClassDef(
                            name='ProxyHandler',
                            bases=[Name(id='WSGIHandler', ctx=Load())],
                            keywords=[],
                            body=[
                                Expr(
                                    value=Constant(value=" When logging requests, try to get the client address from\n            the environment so we get proxyfix's modifications (if any).\n\n            Derived from werzeug.serving.WSGIRequestHandler.log\n            / werzeug.serving.WSGIRequestHandler.address_string\n            ", kind=None),
                                ),
                                FunctionDef(
                                    name='format_request',
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
                                            targets=[Name(id='old_address', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='client_address',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Constant(value='environ', kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='client_address',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='environ',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='REMOTE_ADDR', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='client_address',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='client_address',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='<local>', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                        Try(
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='super', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='format_request',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[],
                                            orelse=[],
                                            finalbody=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='client_address',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='old_address', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    decorator_list=[],
                                    returns=None,
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='set_limit_memory_hard', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
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
                                                attr='SIGQUIT',
                                                ctx=Load(),
                                            ),
                                            Name(id='dumpstacks', ctx=Load()),
                                        ],
                                        keywords=[],
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
                                                attr='SIGUSR1',
                                                ctx=Load(),
                                            ),
                                            Name(id='log_ormcache_stats', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='gevent', ctx=Load()),
                                            attr='spawn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='watchdog',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='httpd',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='WSGIServer', ctx=Load()),
                                args=[
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='interface',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='port',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='app',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='log',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='logging', ctx=Load()),
                                                attr='getLogger',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='longpolling', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='error_log',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='logging', ctx=Load()),
                                                attr='getLogger',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='longpolling', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='handler_class',
                                        value=Name(id='ProxyHandler', ctx=Load()),
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
                                    Constant(value='Evented Service (longpolling) running on %s:%s', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='interface',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='port',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='httpd',
                                                ctx=Load(),
                                            ),
                                            attr='serve_forever',
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Evented Service (longpolling): uncaught error during main loop', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Raise(exc=None, cause=None),
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
                    name='stop',
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
                        Import(
                            names=[alias(name='gevent', asname=None)],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='httpd',
                                        ctx=Load(),
                                    ),
                                    attr='stop',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='stop',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='gevent', ctx=Load()),
                                    attr='shutdown',
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
                    name='run',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='preload', annotation=None, type_comment=None),
                            arg(arg='stop', annotation=None, type_comment=None),
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
                                    attr='start',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='stop',
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
            name='PreforkServer',
            bases=[Name(id='CommonServer', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Multiprocessing inspired by (g)unicorn.\n    PreforkServer (aka Multicorn) currently uses accept(2) as dispatching\n    method between workers but we plan to replace it by a more intelligent\n    dispatcher to will parse the first HTTP request line.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='app', annotation=None, type_comment=None),
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[Name(id='app', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='population',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='workers', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='timeout',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='limit_time_real', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='limit_request',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='limit_request', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='cron_timeout',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='limit_time_real_cron', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=None, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='cron_timeout',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[
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
                                            attr='cron_timeout',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='timeout',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='beat',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=4, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='socket',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='workers_http',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='workers_cron',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='workers',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='generation',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='queue',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='long_polling_pid',
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
                    name='pipe_new',
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
                            targets=[Name(id='pipe', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='pipe',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='fd', ctx=Store()),
                            iter=Name(id='pipe', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='flags', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='fcntl', ctx=Load()),
                                                attr='fcntl',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='fd', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='fcntl', ctx=Load()),
                                                    attr='F_GETFL',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='O_NONBLOCK',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fcntl', ctx=Load()),
                                            attr='fcntl',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='fd', ctx=Load()),
                                            Attribute(
                                                value=Name(id='fcntl', ctx=Load()),
                                                attr='F_SETFL',
                                                ctx=Load(),
                                            ),
                                            Name(id='flags', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='flags', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='fcntl', ctx=Load()),
                                                attr='fcntl',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='fd', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='fcntl', ctx=Load()),
                                                    attr='F_GETFD',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Name(id='fcntl', ctx=Load()),
                                            attr='FD_CLOEXEC',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fcntl', ctx=Load()),
                                            attr='fcntl',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='fd', ctx=Load()),
                                            Attribute(
                                                value=Name(id='fcntl', ctx=Load()),
                                                attr='F_SETFD',
                                                ctx=Load(),
                                            ),
                                            Name(id='flags', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='pipe', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='pipe_ping',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pipe', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='pipe', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=b'.', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='IOError', ctx=Load()),
                                    name='e',
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='errno',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='errno', ctx=Load()),
                                                                attr='EAGAIN',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='errno', ctx=Load()),
                                                                attr='EINTR',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[Raise(exc=None, cause=None)],
                                            orelse=[],
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
                    name='signal_handler',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sig', annotation=None, type_comment=None),
                            arg(arg='frame', annotation=None, type_comment=None),
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
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='queue',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[Constant(value=5, kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='sig', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='signal', ctx=Load()),
                                                attr='SIGCHLD',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='queue',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='sig', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='pipe_ping',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='pipe',
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
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Dropping signal: %s', kind=None),
                                            Name(id='sig', ctx=Load()),
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
                    name='worker_spawn',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='klass', annotation=None, type_comment=None),
                            arg(arg='workers_registry', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        AugAssign(
                            target=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='generation',
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Constant(value=1, kind=None),
                        ),
                        Assign(
                            targets=[Name(id='worker', ctx=Store())],
                            value=Call(
                                func=Name(id='klass', ctx=Load()),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='fork',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='pid', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='worker', ctx=Load()),
                                            attr='pid',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='pid', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='workers',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='pid', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='worker', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='workers_registry', ctx=Load()),
                                            slice=Name(id='pid', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='worker', ctx=Load()),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='worker', ctx=Load()),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='worker', ctx=Load()),
                                            attr='run',
                                            ctx=Load(),
                                        ),
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
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='long_polling_spawn',
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
                            targets=[Name(id='nargs', ctx=Store())],
                            value=Call(
                                func=Name(id='stripped_sys_argv', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cmd', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Attribute(
                                            value=Name(id='sys', ctx=Load()),
                                            attr='executable',
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='sys', ctx=Load()),
                                                attr='argv',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        Constant(value='gevent', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Subscript(
                                    value=Name(id='nargs', ctx=Load()),
                                    slice=Slice(
                                        lower=Constant(value=1, kind=None),
                                        upper=None,
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='popen', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='Popen',
                                    ctx=Load(),
                                ),
                                args=[Name(id='cmd', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='long_polling_pid',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='popen', ctx=Load()),
                                attr='pid',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='worker_pop',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pid', annotation=None, type_comment=None),
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
                                left=Name(id='pid', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='long_polling_pid',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='long_polling_pid',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='pid', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='workers',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='debug',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Worker (%s) unregistered', kind=None),
                                            Name(id='pid', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='workers_http',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='pid', ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='workers_cron',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='pid', ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='u', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='workers',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='pid', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='u', ctx=Load()),
                                                    attr='close',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='OSError', ctx=Load()),
                                            name=None,
                                            body=[Return(value=None)],
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
                    name='worker_kill',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pid', annotation=None, type_comment=None),
                            arg(arg='sig', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='kill',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='pid', ctx=Load()),
                                            Name(id='sig', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='OSError', ctx=Load()),
                                    name='e',
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='errno',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='errno', ctx=Load()),
                                                        attr='ESRCH',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='worker_pop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='pid', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
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
                    name='process_signals',
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
                        While(
                            test=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='queue',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sig', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='queue',
                                                ctx=Load(),
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='sig', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='signal', ctx=Load()),
                                                        attr='SIGINT',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='signal', ctx=Load()),
                                                        attr='SIGTERM',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Name(id='KeyboardInterrupt', ctx=Load()),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='sig', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='signal', ctx=Load()),
                                                        attr='SIGHUP',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='odoo', ctx=Load()),
                                                            attr='phoenix',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                                Raise(
                                                    exc=Name(id='KeyboardInterrupt', ctx=Load()),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='sig', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='signal', ctx=Load()),
                                                                attr='SIGQUIT',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='dumpstacks', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='sig', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='signal', ctx=Load()),
                                                                        attr='SIGUSR1',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Name(id='log_ormcache_stats', ctx=Load()),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='sig', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Name(id='signal', ctx=Load()),
                                                                                attr='SIGTTIN',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        AugAssign(
                                                                            target=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='population',
                                                                                ctx=Store(),
                                                                            ),
                                                                            op=Add(),
                                                                            value=Constant(value=1, kind=None),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Name(id='sig', ctx=Load()),
                                                                                ops=[Eq()],
                                                                                comparators=[
                                                                                    Attribute(
                                                                                        value=Name(id='signal', ctx=Load()),
                                                                                        attr='SIGTTOU',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                AugAssign(
                                                                                    target=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='population',
                                                                                        ctx=Store(),
                                                                                    ),
                                                                                    op=Sub(),
                                                                                    value=Constant(value=1, kind=None),
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
                                        ),
                                    ],
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
                    name='process_zombie',
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
                        While(
                            test=Constant(value=1, kind=None),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='wpid', ctx=Store()),
                                                        Name(id='status', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='waitpid',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='WNOHANG',
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
                                                operand=Name(id='wpid', ctx=Load()),
                                            ),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=BinOp(
                                                    left=Name(id='status', ctx=Load()),
                                                    op=RShift(),
                                                    right=Constant(value=8, kind=None),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=3, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='msg', ctx=Store())],
                                                    value=Constant(value='Critial worker error (%s)', kind=None),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='critical',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='msg', ctx=Load()),
                                                            Name(id='wpid', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='Exception', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='msg', ctx=Load()),
                                                                op=Mod(),
                                                                right=Name(id='wpid', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='worker_pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='wpid', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='OSError', ctx=Load()),
                                            name='e',
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='errno',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='errno', ctx=Load()),
                                                                attr='ECHILD',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[Break()],
                                                    orelse=[],
                                                ),
                                                Raise(exc=None, cause=None),
                                            ],
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
                    name='process_timeout',
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
                            targets=[Name(id='now', ctx=Store())],
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
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='pid', ctx=Store()),
                                    Name(id='worker', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='workers',
                                        ctx=Load(),
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
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='worker', ctx=Load()),
                                                    attr='watchdog_timeout',
                                                    ctx=Load(),
                                                ),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Compare(
                                                left=BinOp(
                                                    left=Name(id='now', ctx=Load()),
                                                    op=Sub(),
                                                    right=Attribute(
                                                        value=Name(id='worker', ctx=Load()),
                                                        attr='watchdog_time',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                ops=[GtE()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='worker', ctx=Load()),
                                                        attr='watchdog_timeout',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='%s (%s) timeout after %ss', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='worker', ctx=Load()),
                                                            attr='__class__',
                                                            ctx=Load(),
                                                        ),
                                                        attr='__name__',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='pid', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='worker', ctx=Load()),
                                                        attr='watchdog_timeout',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='worker_kill',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='pid', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='signal', ctx=Load()),
                                                        attr='SIGKILL',
                                                        ctx=Load(),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='process_spawn',
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
                            test=Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='http_enable', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                While(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='workers_http',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='population',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='worker_spawn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='WorkerHTTP', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='workers_http',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='long_polling_pid',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='long_polling_spawn',
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
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='workers_cron',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Lt()],
                                comparators=[
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='max_cron_threads', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='worker_spawn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='WorkerCron', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='workers_cron',
                                                ctx=Load(),
                                            ),
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
                    name='sleep',
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
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='fds', ctx=Store())],
                                    value=DictComp(
                                        key=Subscript(
                                            value=Attribute(
                                                value=Name(id='w', ctx=Load()),
                                                attr='watchdog_pipe',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        value=Name(id='w', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='w', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='workers',
                                                            ctx=Load(),
                                                        ),
                                                        attr='values',
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
                                    targets=[Name(id='fd_in', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Name(id='list', ctx=Load()),
                                            args=[Name(id='fds', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=List(
                                            elts=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='pipe',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ready', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='select', ctx=Load()),
                                            attr='select',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='fd_in', ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='beat',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='fd', ctx=Store()),
                                    iter=Subscript(
                                        value=Name(id='ready', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='fd', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='fds', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Subscript(
                                                                value=Name(id='fds', ctx=Load()),
                                                                slice=Name(id='fd', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='watchdog_time',
                                                            ctx=Store(),
                                                        ),
                                                    ],
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
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='empty_pipe', ctx=Load()),
                                                args=[Name(id='fd', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='select', ctx=Load()),
                                        attr='error',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='args',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='errno', ctx=Load()),
                                                                attr='EINTR',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[Raise(exc=None, cause=None)],
                                            orelse=[],
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
                    name='start',
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
                                    attr='pipe',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='pipe_new',
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
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='signal_handler',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
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
                                        attr='SIGTERM',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='signal_handler',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
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
                                        attr='SIGHUP',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='signal_handler',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
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
                                        attr='SIGCHLD',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='signal_handler',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
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
                                        attr='SIGTTIN',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='signal_handler',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
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
                                        attr='SIGTTOU',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='signal_handler',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
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
                                        attr='SIGQUIT',
                                        ctx=Load(),
                                    ),
                                    Name(id='dumpstacks', ctx=Load()),
                                ],
                                keywords=[],
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
                                        attr='SIGUSR1',
                                        ctx=Load(),
                                    ),
                                    Name(id='log_ormcache_stats', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='http_enable', kind=None),
                                ctx=Load(),
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
                                            Constant(value='HTTP service (werkzeug) running on %s:%s', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='interface',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='port',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='socket',
                                            ctx=Store(),
                                        ),
                                    ],
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
                                                attr='SOCK_STREAM',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='socket',
                                                ctx=Load(),
                                            ),
                                            attr='setsockopt',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='socket', ctx=Load()),
                                                attr='SOL_SOCKET',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='socket', ctx=Load()),
                                                attr='SO_REUSEADDR',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='socket',
                                                ctx=Load(),
                                            ),
                                            attr='setblocking',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='socket',
                                                ctx=Load(),
                                            ),
                                            attr='bind',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='interface',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='port',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='socket',
                                                ctx=Load(),
                                            ),
                                            attr='listen',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value=8, kind=None),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='population',
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='stop',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='graceful', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='long_polling_pid',
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='worker_kill',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='long_polling_pid',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='signal', ctx=Load()),
                                                attr='SIGKILL',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='long_polling_pid',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='graceful', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Stopping gracefully', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='stop',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='limit', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='time', ctx=Load()),
                                                attr='time',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='timeout',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='pid', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='workers',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='worker_kill',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='pid', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='signal', ctx=Load()),
                                                        attr='SIGINT',
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
                                While(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='workers',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='time', ctx=Load()),
                                                        attr='time',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Lt()],
                                                comparators=[Name(id='limit', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='process_signals',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='KeyboardInterrupt', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='info',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='Forced shutdown.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Break(),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='process_zombie',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='time', ctx=Load()),
                                                    attr='sleep',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0.1, kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Stopping forcefully', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        For(
                            target=Name(id='pid', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='workers',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='worker_kill',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='pid', ctx=Load()),
                                            Attribute(
                                                value=Name(id='signal', ctx=Load()),
                                                attr='SIGTERM',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='socket',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='socket',
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
                    name='run',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='preload', annotation=None, type_comment=None),
                            arg(arg='stop', annotation=None, type_comment=None),
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
                                    attr='start',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='rc', ctx=Store())],
                            value=Call(
                                func=Name(id='preload_registries', ctx=Load()),
                                args=[Name(id='preload', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='stop', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stop',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='rc', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='sql_db',
                                        ctx=Load(),
                                    ),
                                    attr='close_all',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                args=[Constant(value='Multiprocess starting', kind=None)],
                                keywords=[],
                            ),
                        ),
                        While(
                            test=Constant(value=1, kind=None),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='process_signals',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='process_zombie',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='process_timeout',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='process_spawn',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sleep',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='KeyboardInterrupt', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='debug',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='Multiprocess clean stop', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='stop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Break(),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='stop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=False, kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Return(
                                                    value=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
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
            name='Worker',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Workers ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='multi', annotation=None, type_comment=None),
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
                                    attr='multi',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='multi', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='watchdog_time',
                                    ctx=Store(),
                                ),
                            ],
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='watchdog_pipe',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='multi', ctx=Load()),
                                    attr='pipe_new',
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
                                    attr='eintr_pipe',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='multi', ctx=Load()),
                                    attr='pipe_new',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='wakeup_fd_r',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='wakeup_fd_w',
                                            ctx=Store(),
                                        ),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='eintr_pipe',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='watchdog_timeout',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='multi', ctx=Load()),
                                attr='timeout',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ppid',
                                    ctx=Store(),
                                ),
                            ],
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='pid',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='alive',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='request_max',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='multi', ctx=Load()),
                                attr='limit_request',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='request_count',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='setproctitle',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='title', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='setproctitle', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='odoo: %s %s %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='__class__',
                                                        ctx=Load(),
                                                    ),
                                                    attr='__name__',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pid',
                                                    ctx=Load(),
                                                ),
                                                Name(id='title', ctx=Load()),
                                            ],
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
                FunctionDef(
                    name='close',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='close',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='watchdog_pipe',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='close',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='watchdog_pipe',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='close',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eintr_pipe',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='close',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eintr_pipe',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
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
                    name='signal_handler',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sig', annotation=None, type_comment=None),
                            arg(arg='frame', annotation=None, type_comment=None),
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
                                    attr='alive',
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
                    name='signal_time_expired_handler',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='n', annotation=None, type_comment=None),
                            arg(arg='stack', annotation=None, type_comment=None),
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
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Worker (%d) CPU time limit (%s) reached.', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pid',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='limit_time_cpu', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='Exception', ctx=Load()),
                                args=[Constant(value='CPU time limit exceeded.', kind=None)],
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
                    name='sleep',
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
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='select', ctx=Load()),
                                            attr='select',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='multi',
                                                            ctx=Load(),
                                                        ),
                                                        attr='socket',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='wakeup_fd_r',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(elts=[], ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='multi',
                                                    ctx=Load(),
                                                ),
                                                attr='beat',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='empty_pipe', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='wakeup_fd_r',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='select', ctx=Load()),
                                        attr='error',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='args',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='errno', ctx=Load()),
                                                                attr='EINTR',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[Raise(exc=None, cause=None)],
                                            orelse=[],
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
                    name='check_limits',
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
                                    attr='ppid',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='getppid',
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
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Worker (%s) Parent changed', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='pid',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='alive',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='request_count',
                                    ctx=Load(),
                                ),
                                ops=[GtE()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='request_max',
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
                                            Constant(value='Worker (%d) max request (%s) reached.', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='pid',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='request_count',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='alive',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='memory', ctx=Store())],
                            value=Call(
                                func=Name(id='memory_info', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='psutil', ctx=Load()),
                                            attr='Process',
                                            ctx=Load(),
                                        ),
                                        args=[
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
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='limit_memory_soft', kind=None),
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Name(id='memory', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[
                                            Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='limit_memory_soft', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
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
                                            Constant(value='Worker (%d) virtual memory limit (%s) reached.', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='pid',
                                                ctx=Load(),
                                            ),
                                            Name(id='memory', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='alive',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='set_limit_memory_hard', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='resource', ctx=Load()),
                                    attr='getrusage',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='resource', ctx=Load()),
                                        attr='RUSAGE_SELF',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cpu_time', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='r', ctx=Load()),
                                    attr='ru_utime',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='r', ctx=Load()),
                                    attr='ru_stime',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='soft', ctx=Store()),
                                        Name(id='hard', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='resource', ctx=Load()),
                                    attr='getrlimit',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='resource', ctx=Load()),
                                        attr='RLIMIT_CPU',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='resource', ctx=Load()),
                                    attr='setrlimit',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='resource', ctx=Load()),
                                        attr='RLIMIT_CPU',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='cpu_time', ctx=Load()),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Name(id='config', ctx=Load()),
                                                            slice=Constant(value='limit_time_cpu', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='hard', ctx=Load()),
                                        ],
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
                    name='process_work',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
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
                    name='start',
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
                                    attr='pid',
                                    ctx=Store(),
                                ),
                            ],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='setproctitle',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Worker %s (%s) alive', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='__class__',
                                            ctx=Load(),
                                        ),
                                        attr='__name__',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pid',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='random', ctx=Load()),
                                    attr='seed',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='multi',
                                    ctx=Load(),
                                ),
                                attr='socket',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='flags', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='fcntl', ctx=Load()),
                                                attr='fcntl',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='multi',
                                                        ctx=Load(),
                                                    ),
                                                    attr='socket',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='fcntl', ctx=Load()),
                                                    attr='F_GETFD',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Name(id='fcntl', ctx=Load()),
                                            attr='FD_CLOEXEC',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fcntl', ctx=Load()),
                                            attr='fcntl',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='multi',
                                                    ctx=Load(),
                                                ),
                                                attr='socket',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='fcntl', ctx=Load()),
                                                attr='F_SETFD',
                                                ctx=Load(),
                                            ),
                                            Name(id='flags', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='multi',
                                                    ctx=Load(),
                                                ),
                                                attr='socket',
                                                ctx=Load(),
                                            ),
                                            attr='setblocking',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
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
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='signal_handler',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
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
                                        attr='SIGXCPU',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='signal_time_expired_handler',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
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
                                        attr='SIGTERM',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='signal', ctx=Load()),
                                        attr='SIG_DFL',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
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
                                        attr='SIGHUP',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='signal', ctx=Load()),
                                        attr='SIG_DFL',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
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
                                        attr='SIGCHLD',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='signal', ctx=Load()),
                                        attr='SIG_DFL',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
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
                                        attr='SIGTTIN',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='signal', ctx=Load()),
                                        attr='SIG_DFL',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
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
                                        attr='SIGTTOU',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='signal', ctx=Load()),
                                        attr='SIG_DFL',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='signal', ctx=Load()),
                                    attr='set_wakeup_fd',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='wakeup_fd_w',
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
                    name='stop',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
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
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='start',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='t', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='Thread',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=BinOp(
                                                    left=Constant(value='Worker %s (%s) workthread', kind=None),
                                                    op=Mod(),
                                                    right=Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='__class__',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='__name__',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='pid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                            keyword(
                                                arg='target',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_runloop',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='t', ctx=Load()),
                                            attr='daemon',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='t', ctx=Load()),
                                            attr='start',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='t', ctx=Load()),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Worker (%s) exiting. request_count: %s, registry count: %s.', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='pid',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='request_count',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Attribute(
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
                                                        attr='registries',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stop',
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
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Worker (%s) Exception occurred, exiting...', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='pid',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                    name='_runloop',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='signal', ctx=Load()),
                                    attr='pthread_sigmask',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='signal', ctx=Load()),
                                        attr='SIG_BLOCK',
                                        ctx=Load(),
                                    ),
                                    Set(
                                        elts=[
                                            Attribute(
                                                value=Name(id='signal', ctx=Load()),
                                                attr='SIGXCPU',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='signal', ctx=Load()),
                                                attr='SIGINT',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='signal', ctx=Load()),
                                                attr='SIGQUIT',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='signal', ctx=Load()),
                                                attr='SIGUSR1',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                While(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='alive',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='check_limits',
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
                                                        attr='multi',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pipe_ping',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='watchdog_pipe',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sleep',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='alive',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='process_work',
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
                            handlers=[
                                ExceptHandler(
                                    type=None,
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Worker %s (%s) Exception occurred, exiting...', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='__class__',
                                                            ctx=Load(),
                                                        ),
                                                        attr='__name__',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='pid',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='WorkerHTTP',
            bases=[Name(id='Worker', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' HTTP Request workers ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='multi', annotation=None, type_comment=None),
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
                                            Name(id='WorkerHTTP', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[Name(id='multi', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='sock_timeout', ctx=Store())],
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
                                args=[Constant(value='ODOO_HTTP_SOCKET_TIMEOUT', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sock_timeout',
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Name(id='sock_timeout', ctx=Load()),
                                body=Call(
                                    func=Name(id='float', ctx=Load()),
                                    args=[Name(id='sock_timeout', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Constant(value=2, kind=None),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='process_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='client', annotation=None, type_comment=None),
                            arg(arg='addr', annotation=None, type_comment=None),
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
                                    value=Name(id='client', ctx=Load()),
                                    attr='setblocking',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=1, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='client', ctx=Load()),
                                    attr='settimeout',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sock_timeout',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='client', ctx=Load()),
                                    attr='setsockopt',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='socket', ctx=Load()),
                                        attr='IPPROTO_TCP',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='socket', ctx=Load()),
                                        attr='TCP_NODELAY',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='flags', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='fcntl', ctx=Load()),
                                        attr='fcntl',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='client', ctx=Load()),
                                        Attribute(
                                            value=Name(id='fcntl', ctx=Load()),
                                            attr='F_GETFD',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=BitOr(),
                                right=Attribute(
                                    value=Name(id='fcntl', ctx=Load()),
                                    attr='FD_CLOEXEC',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='fcntl', ctx=Load()),
                                    attr='fcntl',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='client', ctx=Load()),
                                    Attribute(
                                        value=Name(id='fcntl', ctx=Load()),
                                        attr='F_SETFD',
                                        ctx=Load(),
                                    ),
                                    Name(id='flags', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='server',
                                        ctx=Load(),
                                    ),
                                    attr='socket',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='client', ctx=Load()),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='server',
                                                ctx=Load(),
                                            ),
                                            attr='process_request',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='client', ctx=Load()),
                                            Name(id='addr', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='IOError', ctx=Load()),
                                    name='e',
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='errno',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='errno', ctx=Load()),
                                                        attr='EPIPE',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[Raise(exc=None, cause=None)],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='request_count',
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Constant(value=1, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='process_work',
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
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='client', ctx=Store()),
                                                Name(id='addr', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='multi',
                                                    ctx=Load(),
                                                ),
                                                attr='socket',
                                                ctx=Load(),
                                            ),
                                            attr='accept',
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='process_request',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='client', ctx=Load()),
                                            Name(id='addr', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='socket', ctx=Load()),
                                        attr='error',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='errno',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='errno', ctx=Load()),
                                                                attr='EAGAIN',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='errno', ctx=Load()),
                                                                attr='ECONNABORTED',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[Raise(exc=None, cause=None)],
                                            orelse=[],
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
                    name='start',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Worker', ctx=Load()),
                                    attr='start',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='server',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='BaseWSGIServerNoBind', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='multi',
                                            ctx=Load(),
                                        ),
                                        attr='app',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
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
        ClassDef(
            name='WorkerCron',
            bases=[Name(id='Worker', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Cron workers ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='multi', annotation=None, type_comment=None),
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
                                            Name(id='WorkerCron', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[Name(id='multi', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='db_index',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='watchdog_timeout',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='multi', ctx=Load()),
                                attr='cron_timeout',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='sleep',
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
                                    attr='db_index',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='interval', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='SLEEP_INTERVAL', ctx=Load()),
                                        op=Add(),
                                        right=BinOp(
                                            left=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='pid',
                                                ctx=Load(),
                                            ),
                                            op=Mod(),
                                            right=Constant(value=10, kind=None),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='select', ctx=Load()),
                                                    attr='select',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='wakeup_fd_r',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='dbcursor',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_cnx',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                    List(elts=[], ctx=Load()),
                                                    Name(id='interval', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='time', ctx=Load()),
                                                    attr='sleep',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='pid',
                                                                ctx=Load(),
                                                            ),
                                                            op=Div(),
                                                            right=Constant(value=100, kind=None),
                                                        ),
                                                        op=Mod(),
                                                        right=Constant(value=0.1, kind=None),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='dbcursor',
                                                            ctx=Load(),
                                                        ),
                                                        attr='_cnx',
                                                        ctx=Load(),
                                                    ),
                                                    attr='poll',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='empty_pipe', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='wakeup_fd_r',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='select', ctx=Load()),
                                                attr='error',
                                                ctx=Load(),
                                            ),
                                            name='e',
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='e', ctx=Load()),
                                                                attr='args',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='errno', ctx=Load()),
                                                                attr='EINTR',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[Raise(exc=None, cause=None)],
                                                    orelse=[],
                                                ),
                                            ],
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
                    name='_db_list',
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
                            test=Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='db_name', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='db_names', ctx=Store())],
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
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='db_names', ctx=Store())],
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
                                            attr='list_dbs',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=True, kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='db_names', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='process_work',
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
                            targets=[Name(id='rpc_request', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='getLogger',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='odoo.netsvc.rpc.request', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rpc_request_flag', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rpc_request', ctx=Load()),
                                    attr='isEnabledFor',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='DEBUG',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='WorkerCron (%s) polling for jobs', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pid',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='db_names', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_db_list',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='db_names', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='db_index',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='db_index',
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='db_names', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='db_name', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='db_names', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='db_index',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='setproctitle',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='db_name', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Name(id='rpc_request_flag', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='start_time', ctx=Store())],
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
                                            targets=[Name(id='start_memory', ctx=Store())],
                                            value=Call(
                                                func=Name(id='memory_info', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='psutil', ctx=Load()),
                                                            attr='Process',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
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
                                ImportFrom(
                                    module='odoo.addons',
                                    names=[alias(name='base', asname=None)],
                                    level=0,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='base', ctx=Load()),
                                                        attr='models',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ir_cron',
                                                    ctx=Load(),
                                                ),
                                                attr='ir_cron',
                                                ctx=Load(),
                                            ),
                                            attr='_process_jobs',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='db_name', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='db_names', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='sql_db',
                                                        ctx=Load(),
                                                    ),
                                                    attr='close_db',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='db_name', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='rpc_request_flag', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='run_time', ctx=Store())],
                                            value=BinOp(
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
                                                right=Name(id='start_time', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='end_memory', ctx=Store())],
                                            value=Call(
                                                func=Name(id='memory_info', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='psutil', ctx=Load()),
                                                            attr='Process',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
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
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='vms_diff', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Name(id='end_memory', ctx=Load()),
                                                    op=Sub(),
                                                    right=Name(id='start_memory', ctx=Load()),
                                                ),
                                                op=Div(),
                                                right=Constant(value=1024, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='logline', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%s time:%.3fs mem: %sk -> %sk (diff: %sk)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='db_name', ctx=Load()),
                                                        Name(id='run_time', ctx=Load()),
                                                        BinOp(
                                                            left=Name(id='start_memory', ctx=Load()),
                                                            op=Div(),
                                                            right=Constant(value=1024, kind=None),
                                                        ),
                                                        BinOp(
                                                            left=Name(id='end_memory', ctx=Load()),
                                                            op=Div(),
                                                            right=Constant(value=1024, kind=None),
                                                        ),
                                                        Name(id='vms_diff', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='WorkerCron (%s) %s', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='pid',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='logline', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='request_count',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='request_count',
                                                    ctx=Load(),
                                                ),
                                                ops=[GtE()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='request_max',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='request_max',
                                                    ctx=Load(),
                                                ),
                                                ops=[Lt()],
                                                comparators=[
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='db_names', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='There are more dabatases to process than allowed by the `limit_request` configuration variable: %s more.', kind=None),
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='db_names', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='request_max',
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
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='db_index',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=0, kind=None),
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
                    name='start',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='nice',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=10, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Worker', ctx=Load()),
                                    attr='start',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='multi',
                                    ctx=Load(),
                                ),
                                attr='socket',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='multi',
                                                    ctx=Load(),
                                                ),
                                                attr='socket',
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
                        Assign(
                            targets=[Name(id='dbconn', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='sql_db',
                                        ctx=Load(),
                                    ),
                                    attr='db_connect',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='postgres', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dbcursor',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dbconn', ctx=Load()),
                                    attr='cursor',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dbcursor',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='LISTEN cron_trigger', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dbcursor',
                                        ctx=Load(),
                                    ),
                                    attr='commit',
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
                    name='stop',
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='stop',
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
                                        attr='dbcursor',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[Name(id='server', ctx=Store())],
            value=Constant(value=None, kind=None),
            type_comment=None,
        ),
        FunctionDef(
            name='load_server_wide_modules',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='server_wide_modules', ctx=Store())],
                    value=BinOp(
                        left=Set(
                            elts=[
                                Constant(value='base', kind=None),
                                Constant(value='web', kind=None),
                            ],
                        ),
                        op=BitOr(),
                        right=Call(
                            func=Name(id='set', ctx=Load()),
                            args=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='conf',
                                        ctx=Load(),
                                    ),
                                    attr='server_wide_modules',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='m', ctx=Store()),
                    iter=Name(id='server_wide_modules', ctx=Load()),
                    body=[
                        Try(
                            body=[
                                Expr(
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
                                            attr='load_openerp_module',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='m', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=Constant(value='', kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='m', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='web', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='msg', ctx=Store())],
                                                    value=Constant(value='\nThe `web` module is provided by the addons found in the `openerp-web` project.\nMaybe you forgot to add those addons in your addons_path configuration.', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Failed to load server-wide module `%s`.%s', kind=None),
                                                    Name(id='m', ctx=Load()),
                                                    Name(id='msg', ctx=Load()),
                                                ],
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
                    orelse=[],
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_reexec',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='updated_modules', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='reexecute openerp-server process with (nearly) the same arguments', kind=None),
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='tools',
                                    ctx=Load(),
                                ),
                                attr='osutil',
                                ctx=Load(),
                            ),
                            attr='is_running_as_nt_service',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='call',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='net stop {0} && net start {0}', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='nt_service_name', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='shell',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='exe', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='basename',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='sys', ctx=Load()),
                                attr='executable',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='args', ctx=Store())],
                    value=Call(
                        func=Name(id='stripped_sys_argv', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='updated_modules', ctx=Load()),
                    body=[
                        AugAssign(
                            target=Name(id='args', ctx=Store()),
                            op=Add(),
                            value=List(
                                elts=[
                                    Constant(value='-u', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=',', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='updated_modules', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='args', ctx=Load()),
                            ),
                            Compare(
                                left=Subscript(
                                    value=Name(id='args', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Name(id='exe', ctx=Load())],
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='args', ctx=Load()),
                                    attr='insert',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=0, kind=None),
                                    Name(id='exe', ctx=Load()),
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
                            value=Name(id='os', ctx=Load()),
                            attr='execve',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='sys', ctx=Load()),
                                attr='executable',
                                ctx=Load(),
                            ),
                            Name(id='args', ctx=Load()),
                            Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='environ',
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
            name='load_test_file_py',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='registry', annotation=None, type_comment=None),
                    arg(arg='test_file', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                ImportFrom(
                    module='odoo.tests.common',
                    names=[alias(name='OdooSuite', asname=None)],
                    level=0,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='currentThread',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr='testing',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                Try(
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='test_path', ctx=Store()),
                                        Name(id='_', ctx=Store()),
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
                                        args=[Name(id='test_file', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='mod', ctx=Store()),
                            iter=ListComp(
                                elt=Name(id='m', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='m', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='get_modules', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Compare(
                                                left=BinOp(
                                                    left=Constant(value='/%s/', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='m', ctx=Load()),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='test_file', ctx=Load())],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='mod_mod', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='loader', ctx=Load()),
                                            attr='get_test_modules',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='mod', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='mod_path', ctx=Store()),
                                                        Name(id='_', ctx=Store()),
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
                                                args=[
                                                    Call(
                                                        func=Name(id='getattr', ctx=Load()),
                                                        args=[
                                                            Name(id='mod_mod', ctx=Load()),
                                                            Constant(value='__file__', kind=None),
                                                            Constant(value='', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='test_path', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='config', ctx=Load()),
                                                            attr='_normalize',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='mod_path', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='tests', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='loader', ctx=Load()),
                                                            attr='unwrap_suite',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='unittest', ctx=Load()),
                                                                            attr='TestLoader',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='loadTestsFromModule',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='mod_mod', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='suite', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='OdooSuite', ctx=Load()),
                                                        args=[Name(id='tests', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='log',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='logging', ctx=Load()),
                                                                attr='INFO',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='running tests %s.', kind=None),
                                                            Attribute(
                                                                value=Name(id='mod_mod', ctx=Load()),
                                                                attr='__name__',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='suite', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='registry', ctx=Load()),
                                                                attr='_assertion_report',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='registry', ctx=Load()),
                                                                    attr='_assertion_report',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='wasSuccessful',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='error',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='%s: at least one error occurred in a test', kind=None),
                                                                    Name(id='test_file', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Return(value=None),
                                            ],
                                            orelse=[],
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
                    handlers=[],
                    orelse=[],
                    finalbody=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='currentThread',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='testing',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
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
            name='preload_registries',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='dbnames', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Preload a registries, possibly run a test file.', kind=None),
                ),
                Assign(
                    targets=[Name(id='dbnames', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Name(id='dbnames', ctx=Load()),
                            List(elts=[], ctx=Load()),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rc', ctx=Store())],
                    value=Constant(value=0, kind=None),
                    type_comment=None,
                ),
                For(
                    target=Name(id='dbname', ctx=Store()),
                    iter=Name(id='dbnames', ctx=Load()),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='update_module', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='init', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='update', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='registry', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Registry', ctx=Load()),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='dbname', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='update_module',
                                                value=Name(id='update_module', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='test_file', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='test_file', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='test_file', kind=None),
                                                ctx=Load(),
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
                                                        attr='isfile',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='test_file', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='test file %s cannot be found', kind=None),
                                                            Name(id='test_file', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Name(id='test_file', ctx=Load()),
                                                                attr='endswith',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='py', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='warning',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='test file %s is not a python file', kind=None),
                                                                    Name(id='test_file', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='info',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='loading test file %s', kind=None),
                                                                    Name(id='test_file', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='load_test_file_py', ctx=Load()),
                                                                args=[
                                                                    Name(id='registry', ctx=Load()),
                                                                    Name(id='test_file', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='test_enable', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='t0', ctx=Store())],
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
                                            targets=[Name(id='t0_sql', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='sql_db',
                                                    ctx=Load(),
                                                ),
                                                attr='sql_counter',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='module_names', ctx=Store())],
                                            value=IfExp(
                                                test=Name(id='update_module', ctx=Load()),
                                                body=Attribute(
                                                    value=Name(id='registry', ctx=Load()),
                                                    attr='updated_modules',
                                                    ctx=Load(),
                                                ),
                                                orelse=Call(
                                                    func=Name(id='sorted', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='registry', ctx=Load()),
                                                            attr='_init_modules',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
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
                                                args=[Constant(value='Starting post tests', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='tests_before', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='registry', ctx=Load()),
                                                    attr='_assertion_report',
                                                    ctx=Load(),
                                                ),
                                                attr='testsRun',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='result', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='loader', ctx=Load()),
                                                    attr='run_suite',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='loader', ctx=Load()),
                                                            attr='make_suite',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='module_names', ctx=Load()),
                                                            Constant(value='post_install', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='registry', ctx=Load()),
                                                        attr='_assertion_report',
                                                        ctx=Load(),
                                                    ),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='result', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='%d post-tests in %.2fs, %s queries', kind=None),
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='registry', ctx=Load()),
                                                                attr='_assertion_report',
                                                                ctx=Load(),
                                                            ),
                                                            attr='testsRun',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Name(id='tests_before', ctx=Load()),
                                                    ),
                                                    BinOp(
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
                                                        right=Name(id='t0', ctx=Load()),
                                                    ),
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='odoo', ctx=Load()),
                                                                attr='sql_db',
                                                                ctx=Load(),
                                                            ),
                                                            attr='sql_counter',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Name(id='t0_sql', ctx=Load()),
                                                    ),
                                                ],
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
                                                    value=Name(id='registry', ctx=Load()),
                                                    attr='_assertion_report',
                                                    ctx=Load(),
                                                ),
                                                attr='wasSuccessful',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='rc', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[],
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
                                                    attr='critical',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Failed to initialize database `%s`.', kind=None),
                                                    Name(id='dbname', ctx=Load()),
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
                                            value=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
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
                Return(
                    value=Name(id='rc', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='start',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='preload', annotation=None, type_comment=None),
                    arg(arg='stop', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Start the odoo http server and cron processor.\n    ', kind=None),
                ),
                Global(names=['server']),
                Expr(
                    value=Call(
                        func=Name(id='load_server_wide_modules', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                ),
                If(
                    test=Attribute(
                        value=Name(id='odoo', ctx=Load()),
                        attr='evented',
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='server', ctx=Store())],
                            value=Call(
                                func=Name(id='GeventServer', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='service',
                                                ctx=Load(),
                                            ),
                                            attr='wsgi_server',
                                            ctx=Load(),
                                        ),
                                        attr='application',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='workers', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='test_enable', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='config', ctx=Load()),
                                                slice=Constant(value='test_file', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Unit testing in workers mode could fail; use --workers 0.', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='server', ctx=Store())],
                                    value=Call(
                                        func=Name(id='PreforkServer', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='service',
                                                        ctx=Load(),
                                                    ),
                                                    attr='wsgi_server',
                                                    ctx=Load(),
                                                ),
                                                attr='application',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='sys', ctx=Load()),
                                                attr='version_info',
                                                ctx=Load(),
                                            ),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=2, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value=5, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='werkzeug', ctx=Load()),
                                                            attr='serving',
                                                            ctx=Load(),
                                                        ),
                                                        attr='WSGIRequestHandler',
                                                        ctx=Load(),
                                                    ),
                                                    attr='wbufsize',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='platform', ctx=Load()),
                                                        attr='system',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='Linux', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='sys', ctx=Load()),
                                                    attr='maxsize',
                                                    ctx=Load(),
                                                ),
                                                ops=[Gt()],
                                                comparators=[
                                                    BinOp(
                                                        left=Constant(value=2, kind=None),
                                                        op=Pow(),
                                                        right=Constant(value=32, kind=None),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Constant(value='MALLOC_ARENA_MAX', kind=None),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='environ',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Import(
                                                    names=[alias(name='ctypes', asname=None)],
                                                ),
                                                Assign(
                                                    targets=[Name(id='libc', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ctypes', ctx=Load()),
                                                            attr='CDLL',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='libc.so.6', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='M_ARENA_MAX', ctx=Store())],
                                                    value=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=8, kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assert(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(id='libc', ctx=Load()),
                                                            attr='mallopt',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='ctypes', ctx=Load()),
                                                                    attr='c_int',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='M_ARENA_MAX', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='ctypes', ctx=Load()),
                                                                    attr='c_int',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=2, kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    msg=None,
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
                                                                args=[Constant(value='Could not set ARENA_MAX through mallopt()', kind=None)],
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
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='server', ctx=Store())],
                                    value=Call(
                                        func=Name(id='ThreadedServer', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='service',
                                                        ctx=Load(),
                                                    ),
                                                    attr='wsgi_server',
                                                    ctx=Load(),
                                                ),
                                                attr='application',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                ),
                Assign(
                    targets=[Name(id='watcher', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Constant(value='reload', kind=None),
                                ops=[In()],
                                comparators=[
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='dev_mode', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='evented',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    body=[
                        If(
                            test=Name(id='inotify', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='watcher', ctx=Store())],
                                    value=Call(
                                        func=Name(id='FSWatcherInotify', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='watcher', ctx=Load()),
                                            attr='start',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='watchdog', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='watcher', ctx=Store())],
                                            value=Call(
                                                func=Name(id='FSWatcherWatchdog', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='watcher', ctx=Load()),
                                                    attr='start',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='posix', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='platform', ctx=Load()),
                                                                attr='system',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='Darwin', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='module', ctx=Store())],
                                                    value=Constant(value='inotify', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='module', ctx=Store())],
                                                    value=Constant(value='watchdog', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value="'%s' module not installed. Code autoreload feature is disabled", kind=None),
                                                    Name(id='module', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Constant(value='werkzeug', kind=None),
                        ops=[In()],
                        comparators=[
                            Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='dev_mode', kind=None),
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='server', ctx=Load()),
                                    attr='app',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='DebuggedApplication', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='server', ctx=Load()),
                                        attr='app',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='evalex',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='rc', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='server', ctx=Load()),
                            attr='run',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='preload', ctx=Load()),
                            Name(id='stop', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='watcher', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='watcher', ctx=Load()),
                                    attr='stop',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='getattr', ctx=Load()),
                        args=[
                            Name(id='odoo', ctx=Load()),
                            Constant(value='phoenix', kind=None),
                            Constant(value=False, kind=None),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='_reexec', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=IfExp(
                        test=Name(id='rc', ctx=Load()),
                        body=Name(id='rc', ctx=Load()),
                        orelse=Constant(value=0, kind=None),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='restart',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value=' Restart the server\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='os', ctx=Load()),
                            attr='name',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='nt', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='Thread',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='target',
                                                value=Name(id='_reexec', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    attr='start',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='kill',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='server', ctx=Load()),
                                        attr='pid',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='signal', ctx=Load()),
                                        attr='SIGHUP',
                                        ctx=Load(),
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
