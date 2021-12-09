Module(
    body=[
        Import(
            names=[alias(name='ast', asname=None)],
        ),
        Import(
            names=[alias(name='collections', asname=None)],
        ),
        Import(
            names=[alias(name='contextlib', asname=None)],
        ),
        Import(
            names=[alias(name='copy', asname=None)],
        ),
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='functools', asname=None)],
        ),
        Import(
            names=[alias(name='hashlib', asname=None)],
        ),
        Import(
            names=[alias(name='hmac', asname=None)],
        ),
        Import(
            names=[alias(name='inspect', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='mimetypes', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='pprint', asname=None)],
        ),
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
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
            names=[alias(name='warnings', asname=None)],
        ),
        ImportFrom(
            module='os.path',
            names=[alias(name='join', asname='opj')],
            level=0,
        ),
        ImportFrom(
            module='zlib',
            names=[alias(name='adler32', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='babel.core', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='date', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='passlib.utils', asname=None)],
        ),
        Import(
            names=[alias(name='psycopg2', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.datastructures', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.exceptions', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.local', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.routing', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.wrappers', asname=None)],
        ),
        ImportFrom(
            module='werkzeug',
            names=[alias(name='urls', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.wsgi',
            names=[alias(name='wrap_file', asname=None)],
            level=0,
        ),
        Try(
            body=[
                ImportFrom(
                    module='werkzeug.middleware.shared_data',
                    names=[alias(name='SharedDataMiddleware', asname=None)],
                    level=0,
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        ImportFrom(
                            module='werkzeug.wsgi',
                            names=[alias(name='SharedDataMiddleware', asname=None)],
                            level=0,
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
                    names=[alias(name='psutil', asname=None)],
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='psutil', ctx=Store())],
                            value=Constant(value=None, kind=None),
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
            module='service.server',
            names=[alias(name='memory_info', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='service',
            names=[
                alias(name='security', asname=None),
                alias(name='model', asname='service_model'),
            ],
            level=1,
        ),
        ImportFrom(
            module='tools.func',
            names=[alias(name='lazy_property', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='tools',
            names=[alias(name='profiler', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='tools',
            names=[
                alias(name='ustr', asname=None),
                alias(name='consteq', asname=None),
                alias(name='frozendict', asname=None),
                alias(name='pycompat', asname=None),
                alias(name='unique', asname=None),
                alias(name='date_utils', asname=None),
            ],
            level=1,
        ),
        ImportFrom(
            module='tools.mimetypes',
            names=[alias(name='guess_mimetype', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='tools.misc',
            names=[alias(name='str2bool', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='tools._vendor',
            names=[alias(name='sessions', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='modules.module',
            names=[alias(name='read_manifest', asname=None)],
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
            targets=[Name(id='rpc_request', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[
                    BinOp(
                        left=Name(id='__name__', ctx=Load()),
                        op=Add(),
                        right=Constant(value='.rpc.request', kind=None),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='rpc_response', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[
                    BinOp(
                        left=Name(id='__name__', ctx=Load()),
                        op=Add(),
                        right=Constant(value='.rpc.response', kind=None),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='STATIC_CACHE', ctx=Store())],
            value=BinOp(
                left=BinOp(
                    left=Constant(value=3600, kind=None),
                    op=Mult(),
                    right=Constant(value=24, kind=None),
                ),
                op=Mult(),
                right=Constant(value=7, kind=None),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='STATIC_CACHE_LONG', ctx=Store())],
            value=BinOp(
                left=BinOp(
                    left=Constant(value=3600, kind=None),
                    op=Mult(),
                    right=Constant(value=24, kind=None),
                ),
                op=Mult(),
                right=Constant(value=365, kind=None),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Subscript(
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='babel', ctx=Load()),
                            attr='core',
                            ctx=Load(),
                        ),
                        attr='LOCALE_ALIASES',
                        ctx=Load(),
                    ),
                    slice=Constant(value='nb', kind=None),
                    ctx=Store(),
                ),
            ],
            value=Constant(value='nb_NO', kind=None),
            type_comment=None,
        ),
        Expr(
            value=Constant(value=" Debug mode is stored in session and should always be a string.\n    It can be activated with an URL query string `debug=<mode>` where\n    mode is either:\n    - 'tests' to load tests assets\n    - 'assets' to load assets non minified\n    - any other truthy value to enable simple debug mode (to show some\n      technical feature, to show complete traceback in frontend error..)\n    - any falsy value to disable debug mode\n\n    You can use any truthy/falsy value from `str2bool` (eg: 'on', 'f'..)\n    Multiple debug modes can be activated simultaneously, separated with\n    a comma (eg: 'tests, assets').\n", kind=None),
        ),
        Assign(
            targets=[Name(id='ALLOWED_DEBUG_MODES', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='', kind=None),
                    Constant(value='1', kind=None),
                    Constant(value='assets', kind=None),
                    Constant(value='tests', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_request_stack', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Attribute(
                        value=Name(id='werkzeug', ctx=Load()),
                        attr='local',
                        ctx=Load(),
                    ),
                    attr='LocalStack',
                    ctx=Load(),
                ),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='request', ctx=Store())],
            value=Call(
                func=Name(id='_request_stack', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        Expr(
            value=Constant(value='\n    A global proxy that always redirect to the current request object.\n', kind=None),
        ),
        FunctionDef(
            name='replace_request_password',
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
                If(
                    test=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='args', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[Gt()],
                        comparators=[Constant(value=2, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='args', ctx=Load()),
                                    slice=Constant(value=2, kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='*', kind=None),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Name(id='tuple', ctx=Load()),
                        args=[Name(id='args', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='NO_POSTMORTEM', ctx=Store())],
            value=Tuple(
                elts=[
                    Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='exceptions',
                            ctx=Load(),
                        ),
                        attr='AccessDenied',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='exceptions',
                            ctx=Load(),
                        ),
                        attr='UserError',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='exceptions',
                            ctx=Load(),
                        ),
                        attr='RedirectWarning',
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='dispatch_rpc',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='service_name', annotation=None, type_comment=None),
                    arg(arg='method', annotation=None, type_comment=None),
                    arg(arg='params', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Handle a RPC call.\n\n    This is pure Python code, the actual marshalling (from/to XML-RPC) is done\n    in a upper layer.\n    ', kind=None),
                ),
                Try(
                    body=[
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
                        Assign(
                            targets=[Name(id='rpc_response_flag', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rpc_response', ctx=Load()),
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
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='rpc_request_flag', ctx=Load()),
                                    Name(id='rpc_response_flag', ctx=Load()),
                                ],
                            ),
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
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='psutil', ctx=Load()),
                                    body=[
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
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='rpc_request', ctx=Load()),
                                            Name(id='rpc_response_flag', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='netsvc',
                                                        ctx=Load(),
                                                    ),
                                                    attr='log',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='rpc_request', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='logging', ctx=Load()),
                                                        attr='DEBUG',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='%s.%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='service_name', ctx=Load()),
                                                                Name(id='method', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Call(
                                                        func=Name(id='replace_request_password', ctx=Load()),
                                                        args=[Name(id='params', ctx=Load())],
                                                        keywords=[],
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
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='current_thread',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='uid',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='current_thread',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='dbname',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='service_name', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='common', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='dispatch', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='service',
                                                ctx=Load(),
                                            ),
                                            attr='common',
                                            ctx=Load(),
                                        ),
                                        attr='dispatch',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='service_name', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='db', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='dispatch', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='service',
                                                        ctx=Load(),
                                                    ),
                                                    attr='db',
                                                    ctx=Load(),
                                                ),
                                                attr='dispatch',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='service_name', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='object', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='dispatch', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='odoo', ctx=Load()),
                                                                attr='service',
                                                                ctx=Load(),
                                                            ),
                                                            attr='model',
                                                            ctx=Load(),
                                                        ),
                                                        attr='dispatch',
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
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='dispatch', ctx=Load()),
                                args=[
                                    Name(id='method', ctx=Load()),
                                    Name(id='params', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='rpc_request_flag', ctx=Load()),
                                    Name(id='rpc_response_flag', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='end_time', ctx=Store())],
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
                                    targets=[Name(id='end_memory', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='psutil', ctx=Load()),
                                    body=[
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
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='logline', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s.%s time:%.3fs mem: %sk -> %sk (diff: %sk)', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='service_name', ctx=Load()),
                                                Name(id='method', ctx=Load()),
                                                BinOp(
                                                    left=Name(id='end_time', ctx=Load()),
                                                    op=Sub(),
                                                    right=Name(id='start_time', ctx=Load()),
                                                ),
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
                                                BinOp(
                                                    left=BinOp(
                                                        left=Name(id='end_memory', ctx=Load()),
                                                        op=Sub(),
                                                        right=Name(id='start_memory', ctx=Load()),
                                                    ),
                                                    op=Div(),
                                                    right=Constant(value=1024, kind=None),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='rpc_response_flag', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='netsvc',
                                                        ctx=Load(),
                                                    ),
                                                    attr='log',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='rpc_response', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='logging', ctx=Load()),
                                                        attr='DEBUG',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='logline', ctx=Load()),
                                                    Name(id='result', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='netsvc',
                                                        ctx=Load(),
                                                    ),
                                                    attr='log',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='rpc_request', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='logging', ctx=Load()),
                                                        attr='DEBUG',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='logline', ctx=Load()),
                                                    Call(
                                                        func=Name(id='replace_request_password', ctx=Load()),
                                                        args=[Name(id='params', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='depth',
                                                        value=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='NO_POSTMORTEM', ctx=Load()),
                            name=None,
                            body=[Raise(exc=None, cause=None)],
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
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='tools',
                                                        ctx=Load(),
                                                    ),
                                                    attr='exception_to_unicode',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='e', ctx=Load())],
                                                keywords=[],
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
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='tools',
                                                    ctx=Load(),
                                                ),
                                                attr='debugger',
                                                ctx=Load(),
                                            ),
                                            attr='post_mortem',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='tools',
                                                    ctx=Load(),
                                                ),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='sys', ctx=Load()),
                                                    attr='exc_info',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
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
        ClassDef(
            name='WebRequest',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Parent class for all Odoo Web request types, mostly deals with\n    initialization and setup of the request object (the dispatching itself has\n    to be handled by the subclasses)\n\n    :param httprequest: a wrapped werkzeug Request object\n    :type httprequest: :class:`werkzeug.wrappers.BaseRequest`\n\n    .. attribute:: httprequest\n\n        the original :class:`werkzeug.wrappers.Request` object provided to the\n        request\n\n    .. attribute:: params\n\n        :class:`~collections.Mapping` of request parameters, not generally\n        useful as they're provided directly to the handler method as keyword\n        arguments\n    ", kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='httprequest', annotation=None, type_comment=None),
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
                                    attr='httprequest',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='httprequest', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='httpresponse',
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
                                    attr='disable_db',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='endpoint',
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
                                    attr='endpoint_arguments',
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
                                    attr='auth_method',
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
                                    attr='_cr',
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
                                    attr='_uid',
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
                                    attr='_context',
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
                                    attr='_env',
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
                                    attr='_failed',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='db',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='threading', ctx=Load()),
                                                    attr='current_thread',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='dbname',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='session',
                                    ctx=Load(),
                                ),
                                attr='uid',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='threading', ctx=Load()),
                                                    attr='current_thread',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='uid',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='uid',
                                        ctx=Load(),
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
                    name='cr',
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
                            value=Constant(value=' :class:`~odoo.sql_db.Cursor` initialized for the current method call.\n\n        Accessing the cursor when the current request uses the ``none``\n        authentication will raise an exception.\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='db',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='RuntimeError', ctx=Load()),
                                        args=[Constant(value='request not bound to a database', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_cr',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_cr',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='registry',
                                                ctx=Load(),
                                            ),
                                            attr='cursor',
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
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_cr',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='uid',
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
                                attr='_uid',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='uid',
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
                                    attr='_uid',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='val', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_env',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='uid', ctx=Load()),
                            attr='setter',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='context',
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
                            value=Constant(value=' :class:`~collections.Mapping` of context values for the current request ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_context',
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_context',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='frozendict', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='session',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
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
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_context',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='context',
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
                                    attr='_context',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='frozendict', ctx=Load()),
                                args=[Name(id='val', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_env',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='context', ctx=Load()),
                            attr='setter',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='env',
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
                            value=Constant(value=' The :class:`~odoo.api.Environment` bound to current request. ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_env',
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_env',
                                            ctx=Store(),
                                        ),
                                    ],
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
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='uid',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='context',
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
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_env',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='session',
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
                            value=Constant(value=' :class:`OpenERPSession` holding the HTTP session data for the\n        current http session\n        ', kind=None),
                        ),
                        Return(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='httprequest',
                                    ctx=Load(),
                                ),
                                attr='session',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='lazy_property', ctx=Load())],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_request_stack', ctx=Load()),
                                    attr='push',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='self', ctx=Load()),
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
                            arg(arg='exc_value', annotation=None, type_comment=None),
                            arg(arg='traceback', annotation=None, type_comment=None),
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
                                    value=Name(id='_request_stack', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_cr',
                                ctx=Load(),
                            ),
                            body=[
                                Try(
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='exc_type', ctx=Load()),
                                                        ops=[Is()],
                                                        comparators=[Constant(value=None, kind=None)],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_failed',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_cr',
                                                                ctx=Load(),
                                                            ),
                                                            attr='commit',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                If(
                                                    test=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='registry',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='registry',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='signal_changes',
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
                                            orelse=[
                                                If(
                                                    test=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='registry',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='registry',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='reset_changes',
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
                                        ),
                                    ],
                                    handlers=[],
                                    orelse=[],
                                    finalbody=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cr',
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
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='disable_db',
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
                                    attr='uid',
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
                    name='set_handler',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='endpoint', annotation=None, type_comment=None),
                            arg(arg='arguments', annotation=None, type_comment=None),
                            arg(arg='auth', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='arguments', ctx=Store())],
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
                                                value=Name(id='arguments', ctx=Load()),
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
                                                    args=[Constant(value='_ignored_', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='endpoint_arguments',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='arguments', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='endpoint',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='endpoint', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='auth_method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='auth', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_handle_exception',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='exception', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Called within an except block to allow converting exceptions\n           to abitrary responses. Anything returned (except None) will\n           be used as response.', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_failed',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='exception', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='isinstance', ctx=Load()),
                                            args=[
                                                Name(id='exception', ctx=Load()),
                                                Name(id='NO_POSTMORTEM', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='isinstance', ctx=Load()),
                                            args=[
                                                Name(id='exception', ctx=Load()),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='werkzeug', ctx=Load()),
                                                        attr='exceptions',
                                                        ctx=Load(),
                                                    ),
                                                    attr='HTTPException',
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='tools',
                                                    ctx=Load(),
                                                ),
                                                attr='debugger',
                                                ctx=Load(),
                                            ),
                                            attr='post_mortem',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='tools',
                                                    ctx=Load(),
                                                ),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='sys', ctx=Load()),
                                                    attr='exc_info',
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
                            targets=[Name(id='new_cause', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='with_traceback',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='exception', ctx=Load()),
                                        attr='__traceback__',
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
                                    value=Name(id='new_cause', ctx=Load()),
                                    attr='__cause__',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='exception', ctx=Load()),
                                        attr='__cause__',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='exception', ctx=Load()),
                                        attr='__context__',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Raise(
                            exc=Call(
                                func=Attribute(
                                    value=Name(id='exception', ctx=Load()),
                                    attr='with_traceback',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=None, kind=None)],
                                keywords=[],
                            ),
                            cause=Name(id='new_cause', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='redirect',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='location', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
                            arg(arg='local', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=303, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='location', ctx=Load()),
                                    Attribute(
                                        value=Name(id='urls', ctx=Load()),
                                        attr='URL',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='location', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='location', ctx=Load()),
                                            attr='to_url',
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
                        If(
                            test=Name(id='local', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='location', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='urls', ctx=Load()),
                                                            attr='url_parse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='location', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='scheme',
                                                        value=Constant(value='', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='netloc',
                                                        value=Constant(value='', kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='to_url',
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='request', ctx=Load()),
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='registry',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.http', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_redirect',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='location', ctx=Load()),
                                            Name(id='code', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='werkzeug', ctx=Load()),
                                        attr='utils',
                                        ctx=Load(),
                                    ),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='location', ctx=Load()),
                                    Name(id='code', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='Response',
                                        value=Name(id='Response', ctx=Load()),
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
                    name='redirect_query',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='location', annotation=None, type_comment=None),
                            arg(arg='query', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
                            arg(arg='local', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=303, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=Name(id='query', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='location', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Constant(value='?', kind=None),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='urls', ctx=Load()),
                                                attr='url_encode',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='query', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[Name(id='location', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='code',
                                        value=Name(id='code', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='local',
                                        value=Name(id='local', ctx=Load()),
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
                    name='_is_cors_preflight',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='endpoint', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_call_function',
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
                        Assign(
                            targets=[Name(id='request', ctx=Store())],
                            value=Name(id='self', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='endpoint',
                                            ctx=Load(),
                                        ),
                                        attr='routing',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='type', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_request_type',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='msg', ctx=Store())],
                                    value=Constant(value="%s, %s: Function declared as capable of handling request of type '%s' but called with a request of type '%s'", kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='params', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='endpoint',
                                                    ctx=Load(),
                                                ),
                                                attr='original',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='endpoint',
                                                        ctx=Load(),
                                                    ),
                                                    attr='routing',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='type', kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_request_type',
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
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='msg', ctx=Load()),
                                            Starred(
                                                value=Name(id='params', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='BadRequest',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='msg', ctx=Load()),
                                                op=Mod(),
                                                right=Name(id='params', ctx=Load()),
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
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='endpoint_arguments',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='endpoint_arguments',
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
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='endpoint',
                                    ctx=Load(),
                                ),
                                attr='first_arg_is_req',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='args', ctx=Store())],
                                    value=BinOp(
                                        left=Tuple(
                                            elts=[Name(id='request', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Name(id='args', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='first_time', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='checked_call',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='___dbname', annotation=None, type_comment=None)],
                                vararg=arg(arg='a', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kw', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Nonlocal(names=['first_time']),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='first_time', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='rollback',
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
                                                        attr='env',
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
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='first_time', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='endpoint',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Name(id='a', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='kw', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='result', ctx=Load()),
                                                    Name(id='Response', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='result', ctx=Load()),
                                                attr='is_qweb',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='flatten',
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
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_cr',
                                            ctx=Load(),
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='flush',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='result', ctx=Load()),
                                ),
                            ],
                            decorator_list=[
                                Attribute(
                                    value=Name(id='service_model', ctx=Load()),
                                    attr='check',
                                    ctx=Load(),
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='db',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='checked_call', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='db',
                                                ctx=Load(),
                                            ),
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
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='endpoint',
                                    ctx=Load(),
                                ),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='registry_cr',
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
                                    value=Name(id='warnings', ctx=Load()),
                                    attr='warn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='please use request.registry and request.cr directly', kind=None),
                                    Name(id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Yield(
                                value=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='cr',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='contextlib', ctx=Load()),
                            attr='contextmanager',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='registry',
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
                            value=Constant(value='\n        The registry to the database linked to this request. Can be ``None``\n        if the current request uses the ``none`` authentication.\n\n        .. deprecated:: 8.0\n\n            use :attr:`.env`\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='registry',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='db',
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
                            value=Constant(value='\n        The database linked to this request. Can be ``None``\n        if the current request uses the ``none`` authentication.\n        ', kind=None),
                        ),
                        Return(
                            value=IfExp(
                                test=UnaryOp(
                                    op=Not(),
                                    operand=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='disable_db',
                                        ctx=Load(),
                                    ),
                                ),
                                body=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    attr='db',
                                    ctx=Load(),
                                ),
                                orelse=Constant(value=None, kind=None),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='csrf_token',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='time_limit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Generates and returns a CSRF token for the current session\n\n        :param time_limit: the CSRF token validity period (in seconds), or\n                           ``None`` for the token to be valid as long as the\n                           current user session is (the default)\n        :type time_limit: int | None\n        :returns: ASCII token string\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='token', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='session',
                                    ctx=Load(),
                                ),
                                attr='sid',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='max_ts', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
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
                                        op=Add(),
                                        right=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='time_limit', ctx=Load()),
                                                Constant(value=31536000, kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%s%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='token', ctx=Load()),
                                        Name(id='max_ts', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='secret', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='database.secret', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Name(id='secret', ctx=Load()),
                            msg=Constant(value='CSRF protection requires a configured database secret', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='hm', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='hmac', ctx=Load()),
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
                                                args=[Constant(value='ascii', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='msg', ctx=Load()),
                                                    attr='encode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='utf-8', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='hashlib', ctx=Load()),
                                                attr='sha1',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='hexdigest',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='%so%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='hm', ctx=Load()),
                                        Name(id='max_ts', ctx=Load()),
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
                    name='validate_csrf',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='csrf', annotation=None, type_comment=None),
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
                                operand=Name(id='csrf', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='hm', ctx=Store()),
                                                Name(id='_', ctx=Store()),
                                                Name(id='max_ts', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='csrf', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='rpartition',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='o', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='UnicodeEncodeError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=Name(id='max_ts', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[Name(id='max_ts', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Lt()],
                                                comparators=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
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
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Return(
                                                    value=Constant(value=False, kind=None),
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
                            targets=[Name(id='token', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='session',
                                    ctx=Load(),
                                ),
                                attr='sid',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%s%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='token', ctx=Load()),
                                        Name(id='max_ts', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='secret', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='database.secret', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Name(id='secret', ctx=Load()),
                            msg=Constant(value='CSRF protection requires a configured database secret', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='hm_expected', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='hmac', ctx=Load()),
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
                                                args=[Constant(value='ascii', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='msg', ctx=Load()),
                                                    attr='encode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='utf-8', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='hashlib', ctx=Load()),
                                                attr='sha1',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='hexdigest',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='consteq', ctx=Load()),
                                args=[
                                    Name(id='hm', ctx=Load()),
                                    Name(id='hm_expected', ctx=Load()),
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
            name='route',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='route', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kw', annotation=None, type_comment=None),
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value="Decorator marking the decorated method as being a handler for\n    requests. The method must be part of a subclass of ``Controller``.\n\n    :param route: string or array. The route part that will determine which\n                  http requests will match the decorated method. Can be a\n                  single string or an array of strings. See werkzeug's routing\n                  documentation for the format of route expression (\n                  http://werkzeug.pocoo.org/docs/routing/ ).\n    :param type: The type of request, can be ``'http'`` or ``'json'``.\n    :param auth: The type of authentication method, can on of the following:\n\n                 * ``user``: The user must be authenticated and the current request\n                   will perform using the rights of the user.\n                 * ``public``: The user may or may not be authenticated. If she isn't,\n                   the current request will perform using the shared Public user.\n                 * ``none``: The method is always active, even if there is no\n                   database. Mainly used by the framework and authentication\n                   modules. There request code will not have any facilities to access\n                   the database nor have any configuration indicating the current\n                   database nor the current user.\n    :param methods: A sequence of http methods this route applies to. If not\n                    specified, all methods are allowed.\n    :param cors: The Access-Control-Allow-Origin cors directive value.\n    :param bool csrf: Whether CSRF protection should be enabled for the route.\n\n                      Defaults to ``True``. See :ref:`CSRF Protection\n                      <csrf>` for more.\n\n    .. _csrf:\n\n    .. admonition:: CSRF Protection\n        :class: alert-warning\n\n        .. versionadded:: 9.0\n\n        Odoo implements token-based `CSRF protection\n        <https://en.wikipedia.org/wiki/CSRF>`_.\n\n        CSRF protection is enabled by default and applies to *UNSAFE*\n        HTTP methods as defined by :rfc:`7231` (all methods other than\n        ``GET``, ``HEAD``, ``TRACE`` and ``OPTIONS``).\n\n        CSRF protection is implemented by checking requests using\n        unsafe methods for a value called ``csrf_token`` as part of\n        the request's form data. That value is removed from the form\n        as part of the validation and does not have to be taken in\n        account by your own form processing.\n\n        When adding a new controller for an unsafe method (mostly POST\n        for e.g. forms):\n\n        * if the form is generated in Python, a csrf token is\n          available via :meth:`request.csrf_token()\n          <odoo.http.WebRequest.csrf_token`, the\n          :data:`~odoo.http.request` object is available by default\n          in QWeb (python) templates, it may have to be added\n          explicitly if you are not using QWeb.\n\n        * if the form is generated in Javascript, the CSRF token is\n          added by default to the QWeb (js) rendering context as\n          ``csrf_token`` and is otherwise available as ``csrf_token``\n          on the ``web.core`` module:\n\n          .. code-block:: javascript\n\n              require('web.core').csrf_token\n\n        * if the endpoint can be called by external parties (not from\n          Odoo) as e.g. it is a REST API or a `webhook\n          <https://en.wikipedia.org/wiki/Webhook>`_, CSRF protection\n          must be disabled on the endpoint. If possible, you may want\n          to implement other methods of request validation (to ensure\n          it is not called by an unrelated third-party).\n\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='routing', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='kw', ctx=Load()),
                            attr='copy',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assert(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            Compare(
                                left=Constant(value='type', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='routing', ctx=Load())],
                            ),
                            Compare(
                                left=Subscript(
                                    value=Name(id='routing', ctx=Load()),
                                    slice=Constant(value='type', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='http', kind=None),
                                            Constant(value='json', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    msg=None,
                ),
                FunctionDef(
                    name='decorator',
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
                        If(
                            test=Name(id='route', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='route', ctx=Load()),
                                            Name(id='list', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='routes', ctx=Store())],
                                            value=Name(id='route', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='routes', ctx=Store())],
                                            value=List(
                                                elts=[Name(id='route', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='routing', ctx=Load()),
                                            slice=Constant(value='routes', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='routes', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='wrong', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='routing', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='method', kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='wrong', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='kw', ctx=Load()),
                                                    attr='setdefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='methods', kind=None),
                                                    Name(id='wrong', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value="<function %s.%s> defined with invalid routing parameter 'method', assuming 'methods'", kind=None),
                                                    Attribute(
                                                        value=Name(id='f', ctx=Load()),
                                                        attr='__module__',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='f', ctx=Load()),
                                                        attr='__name__',
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
                        ),
                        FunctionDef(
                            name='response_wrap',
                            args=arguments(
                                posonlyargs=[],
                                args=[],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kw', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='params', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='inspect', ctx=Load()),
                                                        attr='signature',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='f', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='parameters',
                                                ctx=Load(),
                                            ),
                                            attr='values',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='is_kwargs', ctx=Store())],
                                    value=Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='p', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='p', ctx=Load()),
                                                attr='kind',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='inspect', ctx=Load()),
                                                        attr='Parameter',
                                                        ctx=Load(),
                                                    ),
                                                    attr='VAR_KEYWORD',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='any', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Call(
                                                        func=Name(id='is_kwargs', ctx=Load()),
                                                        args=[Name(id='p', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='p', ctx=Store()),
                                                            iter=Name(id='params', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='is_keyword_compatible', ctx=Store())],
                                            value=Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='p', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='kind',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='inspect', ctx=Load()),
                                                                        attr='Parameter',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='POSITIONAL_OR_KEYWORD',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='inspect', ctx=Load()),
                                                                        attr='Parameter',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='KEYWORD_ONLY',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='fargs', ctx=Store())],
                                            value=SetComp(
                                                elt=Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='p', ctx=Store()),
                                                        iter=Name(id='params', ctx=Load()),
                                                        ifs=[
                                                            Call(
                                                                func=Name(id='is_keyword_compatible', ctx=Load()),
                                                                args=[Name(id='p', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='ignored', ctx=Store())],
                                            value=ListComp(
                                                elt=BinOp(
                                                    left=Constant(value='<%s=%s>', kind=None),
                                                    op=Mod(),
                                                    right=Tuple(
                                                        elts=[
                                                            Name(id='k', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='kw', ctx=Load()),
                                                                    attr='pop',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='k', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='k', ctx=Store()),
                                                        iter=Call(
                                                            func=Name(id='list', ctx=Load()),
                                                            args=[Name(id='kw', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        ifs=[
                                                            Compare(
                                                                left=Name(id='k', ctx=Load()),
                                                                ops=[NotIn()],
                                                                comparators=[Name(id='fargs', ctx=Load())],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='ignored', ctx=Load()),
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
                                                                left=Constant(value='<function %s.%s> called ignoring args %s', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Name(id='f', ctx=Load()),
                                                                            attr='__module__',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='f', ctx=Load()),
                                                                            attr='__name__',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Constant(value=', ', kind=None),
                                                                                attr='join',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='ignored', ctx=Load())],
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
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
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
                                                value=Name(id='kw', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='response', ctx=Load()),
                                                    Name(id='Response', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='f', ctx=Load()),
                                                    attr='routing_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='json', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='response', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='response', ctx=Load()),
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
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='Response', ctx=Load()),
                                                args=[Name(id='response', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='response', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='werkzeug', ctx=Load()),
                                                    attr='exceptions',
                                                    ctx=Load(),
                                                ),
                                                attr='HTTPException',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='response', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='get_response',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='httprequest',
                                                            ctx=Load(),
                                                        ),
                                                        attr='environ',
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
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='response', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='werkzeug', ctx=Load()),
                                                    attr='wrappers',
                                                    ctx=Load(),
                                                ),
                                                attr='BaseResponse',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='response', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Response', ctx=Load()),
                                                    attr='force_type',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='response', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='set_default',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Name(id='response', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='<function %s.%s> returns an invalid response type for an http request', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='f', ctx=Load()),
                                                            attr='__module__',
                                                            ctx=Load(),
                                                        ),
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
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='response', ctx=Load()),
                                ),
                            ],
                            decorator_list=[
                                Call(
                                    func=Attribute(
                                        value=Name(id='functools', ctx=Load()),
                                        attr='wraps',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='f', ctx=Load())],
                                    keywords=[],
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='response_wrap', ctx=Load()),
                                    attr='routing',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='routing', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='response_wrap', ctx=Load()),
                                    attr='original_func',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='f', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='response_wrap', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Name(id='decorator', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='JsonRequest',
            bases=[Name(id='WebRequest', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Request handler for `JSON-RPC 2\n    <http://www.jsonrpc.org/specification>`_ over HTTP\n\n    * ``method`` is ignored\n    * ``params`` must be a JSON object (not an array) and is passed as keyword\n      arguments to the handler method\n    * the handler method\'s result is returned as JSON-RPC ``result`` and\n      wrapped in the `JSON-RPC Response\n      <http://www.jsonrpc.org/specification#response_object>`_\n\n    Successful request::\n\n      --> {"jsonrpc": "2.0",\n           "method": "call",\n           "params": {"context": {},\n                      "arg1": "val1" },\n           "id": null}\n\n      <-- {"jsonrpc": "2.0",\n           "result": { "res1": "val1" },\n           "id": null}\n\n    Request producing a error::\n\n      --> {"jsonrpc": "2.0",\n           "method": "call",\n           "params": {"context": {},\n                      "arg1": "val1" },\n           "id": null}\n\n      <-- {"jsonrpc": "2.0",\n           "error": {"code": 1,\n                     "message": "End user error message.",\n                     "data": {"code": "codestring",\n                              "debug": "traceback" } },\n           "id": null}\n\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_request_type', ctx=Store())],
                    value=Constant(value='json', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
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
                                            Name(id='JsonRequest', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
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
                                    attr='params',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='httprequest',
                                    ctx=Load(),
                                ),
                                attr='args',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='request', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='request_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='args', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='request', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='httprequest',
                                                ctx=Load(),
                                            ),
                                            attr='get_data',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='charset',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jsonrequest',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='loads',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='request', ctx=Load())],
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
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='Invalid JSON data: %r', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[Name(id='request', ctx=Load())],
                                                    ctx=Load(),
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
                                                args=[
                                                    Constant(value='%s: %s', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='httprequest',
                                                            ctx=Load(),
                                                        ),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='msg', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='werkzeug', ctx=Load()),
                                                        attr='exceptions',
                                                        ctx=Load(),
                                                    ),
                                                    attr='BadRequest',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='msg', ctx=Load())],
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='params',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='jsonrequest',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='params', kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='context',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='params',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='context', kind=None),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='session',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_json_response',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='result', annotation=None, type_comment=None),
                            arg(arg='error', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='jsonrpc', kind=None),
                                    Constant(value='id', kind=None),
                                ],
                                values=[
                                    Constant(value='2.0', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='jsonrequest',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='error', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='response', ctx=Load()),
                                            slice=Constant(value='error', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='error', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='result', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='response', ctx=Load()),
                                            slice=Constant(value='result', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='result', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='mime', ctx=Store())],
                            value=Constant(value='application/json', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='dumps',
                                    ctx=Load(),
                                ),
                                args=[Name(id='response', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Attribute(
                                            value=Name(id='date_utils', ctx=Load()),
                                            attr='json_default',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='Response', ctx=Load()),
                                args=[Name(id='body', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='status',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Name(id='error', ctx=Load()),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='error', ctx=Load()),
                                                                attr='pop',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='http_status', kind=None),
                                                                Constant(value=200, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                                Constant(value=200, kind=None),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='headers',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='Content-Type', kind=None),
                                                        Name(id='mime', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        Constant(value='Content-Length', kind=None),
                                                        Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='body', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
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
                    name='_handle_exception',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='exception', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Called within an except block to allow converting exceptions\n           to arbitrary responses. Anything returned (except None) will\n           be used as response.', kind=None),
                        ),
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='JsonRequest', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_handle_exception',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='exception', ctx=Load())],
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
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='isinstance', ctx=Load()),
                                                    args=[
                                                        Name(id='exception', ctx=Load()),
                                                        Name(id='SessionExpiredException', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='exception', ctx=Load()),
                                                                attr='args',
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='exception', ctx=Load()),
                                                                        attr='args',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='bus.Bus not available in test mode', kind=None)],
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
                                                                args=[Name(id='exception', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Call(
                                                                func=Name(id='isinstance', ctx=Load()),
                                                                args=[
                                                                    Name(id='exception', ctx=Load()),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='odoo', ctx=Load()),
                                                                                    attr='exceptions',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='UserError',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='werkzeug', ctx=Load()),
                                                                                    attr='exceptions',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='NotFound',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                                                            attr='warning',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='exception', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='_logger', ctx=Load()),
                                                                            attr='exception',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='Exception during JSON request handling.', kind=None)],
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
                                        Assign(
                                            targets=[Name(id='error', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='code', kind=None),
                                                    Constant(value='message', kind=None),
                                                    Constant(value='data', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=200, kind=None),
                                                    Constant(value='Odoo Server Error', kind=None),
                                                    Call(
                                                        func=Name(id='serialize_exception', ctx=Load()),
                                                        args=[Name(id='exception', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='exception', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='werkzeug', ctx=Load()),
                                                            attr='exceptions',
                                                            ctx=Load(),
                                                        ),
                                                        attr='NotFound',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='error', ctx=Load()),
                                                            slice=Constant(value='http_status', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=404, kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='error', ctx=Load()),
                                                            slice=Constant(value='code', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=404, kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='error', ctx=Load()),
                                                            slice=Constant(value='message', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='404: Not Found', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='exception', ctx=Load()),
                                                    Name(id='AuthenticationError', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='error', ctx=Load()),
                                                            slice=Constant(value='code', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=100, kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='error', ctx=Load()),
                                                            slice=Constant(value='message', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='Odoo Session Invalid', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='exception', ctx=Load()),
                                                    Name(id='SessionExpiredException', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='error', ctx=Load()),
                                                            slice=Constant(value='code', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=100, kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='error', ctx=Load()),
                                                            slice=Constant(value='message', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='Odoo Session Expired', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_json_response',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='error',
                                                        value=Name(id='error', ctx=Load()),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='dispatch',
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
                        Assign(
                            targets=[Name(id='rpc_response_flag', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rpc_response', ctx=Load()),
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
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='rpc_request_flag', ctx=Load()),
                                    Name(id='rpc_response_flag', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='endpoint', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='endpoint',
                                                ctx=Load(),
                                            ),
                                            attr='method',
                                            ctx=Load(),
                                        ),
                                        attr='__name__',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='model', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='params',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='model', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='method', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='params',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='method', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='args', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='params',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='args', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
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
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='psutil', ctx=Load()),
                                    body=[
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
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='rpc_request', ctx=Load()),
                                            Name(id='rpc_response_flag', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='rpc_request', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='%s: %s %s, %s', kind=None),
                                                    Name(id='endpoint', ctx=Load()),
                                                    Name(id='model', ctx=Load()),
                                                    Name(id='method', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='pprint', ctx=Load()),
                                                            attr='pformat',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='args', ctx=Load())],
                                                        keywords=[],
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
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_call_function',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='params',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='rpc_request_flag', ctx=Load()),
                                    Name(id='rpc_response_flag', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='end_time', ctx=Store())],
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
                                    targets=[Name(id='end_memory', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='psutil', ctx=Load()),
                                    body=[
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
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='logline', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s: %s %s: time:%.3fs mem: %sk -> %sk (diff: %sk)', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='endpoint', ctx=Load()),
                                                Name(id='model', ctx=Load()),
                                                Name(id='method', ctx=Load()),
                                                BinOp(
                                                    left=Name(id='end_time', ctx=Load()),
                                                    op=Sub(),
                                                    right=Name(id='start_time', ctx=Load()),
                                                ),
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
                                                BinOp(
                                                    left=BinOp(
                                                        left=Name(id='end_memory', ctx=Load()),
                                                        op=Sub(),
                                                        right=Name(id='start_memory', ctx=Load()),
                                                    ),
                                                    op=Div(),
                                                    right=Constant(value=1024, kind=None),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='rpc_response_flag', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='rpc_response', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='%s, %s', kind=None),
                                                    Name(id='logline', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='pprint', ctx=Load()),
                                                            attr='pformat',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='result', ctx=Load())],
                                                        keywords=[],
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
                                                    value=Name(id='rpc_request', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='logline', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_json_response',
                                    ctx=Load(),
                                ),
                                args=[Name(id='result', ctx=Load())],
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
            name='serialize_exception',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='e', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=Dict(
                        keys=[
                            Constant(value='name', kind=None),
                            Constant(value='debug', kind=None),
                            Constant(value='message', kind=None),
                            Constant(value='arguments', kind=None),
                            Constant(value='context', kind=None),
                        ],
                        values=[
                            IfExp(
                                test=Attribute(
                                    value=Call(
                                        func=Name(id='type', ctx=Load()),
                                        args=[Name(id='e', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='__module__',
                                    ctx=Load(),
                                ),
                                body=BinOp(
                                    left=BinOp(
                                        left=Attribute(
                                            value=Call(
                                                func=Name(id='type', ctx=Load()),
                                                args=[Name(id='e', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='__module__',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Constant(value='.', kind=None),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Call(
                                            func=Name(id='type', ctx=Load()),
                                            args=[Name(id='e', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='__name__',
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Attribute(
                                    value=Call(
                                        func=Name(id='type', ctx=Load()),
                                        args=[Name(id='e', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='__name__',
                                    ctx=Load(),
                                ),
                            ),
                            Call(
                                func=Attribute(
                                    value=Name(id='traceback', ctx=Load()),
                                    attr='format_exc',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            Call(
                                func=Name(id='ustr', ctx=Load()),
                                args=[Name(id='e', ctx=Load())],
                                keywords=[],
                            ),
                            Attribute(
                                value=Name(id='e', ctx=Load()),
                                attr='args',
                                ctx=Load(),
                            ),
                            Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='e', ctx=Load()),
                                    Constant(value='context', kind=None),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
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
            name='HttpRequest',
            bases=[Name(id='WebRequest', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Handler for the ``http`` request type.\n\n    matched routing parameters, query string parameters, form_ parameters\n    and files are passed to the handler method as keyword arguments.\n\n    In case of name conflict, routing parameters have priority.\n\n    The handler method's result can be:\n\n    * a falsy value, in which case the HTTP response will be an\n      `HTTP 204`_ (No Content)\n    * a werkzeug Response object, which is returned as-is\n    * a ``str`` or ``unicode``, will be wrapped in a Response object and\n      interpreted as HTML\n\n    .. _form: http://www.w3.org/TR/html401/interact/forms.html#h-17.13.4.2\n    .. _HTTP 204: http://tools.ietf.org/html/rfc7231#section-6.3.5\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='_request_type', ctx=Store())],
                    value=Constant(value='http', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
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
                                            Name(id='HttpRequest', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='collections', ctx=Load()),
                                    attr='OrderedDict',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='args',
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
                                    value=Name(id='params', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='form',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='params', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='files',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='params', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='session_id', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='params',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='params', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_handle_exception',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='exception', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Called within an except block to allow converting exceptions\n           to abitrary responses. Anything returned (except None) will\n           be used as response.', kind=None),
                        ),
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='HttpRequest', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_handle_exception',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='exception', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='SessionExpiredException', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='redirect', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='req', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='httprequest',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='req', ctx=Load()),
                                                    attr='method',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='POST', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='session',
                                                                ctx=Load(),
                                                            ),
                                                            attr='save_request_data',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='redirect', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Constant(value='/web/proxy/post{r.full_path}', kind=None),
                                                            attr='format',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='r',
                                                                value=Name(id='req', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='params',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='noredirect', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='redirect', ctx=Store())],
                                                            value=Attribute(
                                                                value=Name(id='req', ctx=Load()),
                                                                attr='url',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                        If(
                                            test=Name(id='redirect', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='query', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='werkzeug', ctx=Load()),
                                                                attr='urls',
                                                                ctx=Load(),
                                                            ),
                                                            attr='url_encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='redirect', kind=None)],
                                                                values=[Name(id='redirect', ctx=Load())],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='redirect',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='/web/login?%s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='query', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Attribute(
                                        value=Attribute(
                                            value=Name(id='werkzeug', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='HTTPException',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Return(
                                            value=Name(id='e', ctx=Load()),
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
                    name='_is_cors_preflight',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='endpoint', annotation=None, type_comment=None),
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
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='httprequest',
                                                ctx=Load(),
                                            ),
                                            attr='method',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='OPTIONS', kind=None)],
                                    ),
                                    Name(id='endpoint', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='endpoint', ctx=Load()),
                                                attr='routing',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='cors', kind=None)],
                                        keywords=[],
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
                    name='dispatch',
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
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_cors_preflight',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='endpoint',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='headers', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='Access-Control-Max-Age', kind=None),
                                            Constant(value='Access-Control-Allow-Headers', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value=60, kind=None),
                                                    op=Mult(),
                                                    right=Constant(value=60, kind=None),
                                                ),
                                                op=Mult(),
                                                right=Constant(value=24, kind=None),
                                            ),
                                            Constant(value='Origin, X-Requested-With, Content-Type, Accept, Authorization', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='Response', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='status',
                                                value=Constant(value=200, kind=None),
                                            ),
                                            keyword(
                                                arg='headers',
                                                value=Name(id='headers', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='httprequest',
                                                ctx=Load(),
                                            ),
                                            attr='method',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='GET', kind=None),
                                                    Constant(value='HEAD', kind=None),
                                                    Constant(value='OPTIONS', kind=None),
                                                    Constant(value='TRACE', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='endpoint',
                                                    ctx=Load(),
                                                ),
                                                attr='routing',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='csrf', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='token', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='params',
                                                ctx=Load(),
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='csrf_token', kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='validate_csrf',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='token', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='token', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
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
                                                            Constant(value="CSRF validation failed on path '%s'", kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='httprequest',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='path',
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
                                                            Constant(value='No CSRF validation token provided for path \'%s\'\n\nOdoo URLs are CSRF-protected by default (when accessed with unsafe\nHTTP methods). See\nhttps://www.odoo.com/documentation/15.0/developer/reference/addons/http.html#csrf for\nmore details.\n\n* if this endpoint is accessed through Odoo via py-QWeb form, embed a CSRF\n  token in the form, Tokens are available via `request.csrf_token()`\n  can be provided through a hidden input and must be POST-ed named\n  `csrf_token` e.g. in your form add:\n\n      <input type="hidden" name="csrf_token" t-att-value="request.csrf_token()"/>\n\n* if the form is generated or posted in javascript, the token value is\n  available as `csrf_token` on `web.core` and as the `csrf_token`\n  value in the default js-qweb execution context\n\n* if the form is accessed by an external third party (e.g. REST API\n  endpoint, payment gateway callback) you will need to disable CSRF\n  protection (and implement your own protection if necessary) by\n  passing the `csrf=False` parameter to the `route` decorator.\n                    ', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='httprequest',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='werkzeug', ctx=Load()),
                                                        attr='exceptions',
                                                        ctx=Load(),
                                                    ),
                                                    attr='BadRequest',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Session expired (invalid CSRF token)', kind=None)],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_call_function',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='params',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='r', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='r', ctx=Store())],
                                    value=Call(
                                        func=Name(id='Response', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='status',
                                                value=Constant(value=204, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                    name='make_response',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='headers', annotation=None, type_comment=None),
                            arg(arg='cookies', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Helper for non-HTML responses, or HTML responses with custom\n        response headers or cookies.\n\n        While handlers can just return the HTML markup of a page they want to\n        send as a string if non-HTML data is returned they need to create a\n        complete response object, or the returned data will not be correctly\n        interpreted by the clients.\n\n        :param basestring data: response body\n        :param headers: HTTP headers to set on the response\n        :type headers: ``[(name, value)]``\n        :param collections.Mapping cookies: cookies to set on the client\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Name(id='Response', ctx=Load()),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='headers',
                                        value=Name(id='headers', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='cookies', ctx=Load()),
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
                                            value=Name(id='cookies', ctx=Load()),
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
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='set_cookie',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='k', ctx=Load()),
                                                    Name(id='v', ctx=Load()),
                                                ],
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
                        Return(
                            value=Name(id='response', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='render',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='qcontext', annotation=None, type_comment=None),
                            arg(arg='lazy', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Lazy render of a QWeb template.\n\n        The actual rendering of the given template will occur at then end of\n        the dispatching. Meanwhile, the template and/or qcontext can be\n        altered or even replaced by a static response.\n\n        :param basestring template: template to render\n        :param dict qcontext: Rendering context to use\n        :param bool lazy: whether the template rendering should be deferred\n                          until the last possible moment\n        :param kw: forwarded to werkzeug's Response object\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Name(id='Response', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='template',
                                        value=Name(id='template', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='qcontext',
                                        value=Name(id='qcontext', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='kw', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='lazy', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='render',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='not_found',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='description', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Shortcut for a `HTTP 404\n        <http://tools.ietf.org/html/rfc7231#section-6.5.4>`_ (Not Found)\n        response\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='werkzeug', ctx=Load()),
                                        attr='exceptions',
                                        ctx=Load(),
                                    ),
                                    attr='NotFound',
                                    ctx=Load(),
                                ),
                                args=[Name(id='description', ctx=Load())],
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
            targets=[Name(id='addons_manifest', ctx=Store())],
            value=Dict(keys=[], values=[]),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='controllers_per_module', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='collections', ctx=Load()),
                    attr='defaultdict',
                    ctx=Load(),
                ),
                args=[Name(id='list', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='ControllerType',
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
                                            Name(id='ControllerType', ctx=Load()),
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
                                    value=Name(id='attrs', ctx=Load()),
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
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='inspect', ctx=Load()),
                                                    attr='isfunction',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='v', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='hasattr', ctx=Load()),
                                                args=[
                                                    Name(id='v', ctx=Load()),
                                                    Constant(value='original_func', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='routing_type', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='v', ctx=Load()),
                                                        attr='routing',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='type', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='parent', ctx=Store())],
                                            value=ListComp(
                                                elt=Name(id='claz', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='claz', ctx=Store()),
                                                        iter=Name(id='bases', ctx=Load()),
                                                        ifs=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                        args=[
                                                                            Name(id='claz', ctx=Load()),
                                                                            Name(id='ControllerType', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='hasattr', ctx=Load()),
                                                                        args=[
                                                                            Name(id='claz', ctx=Load()),
                                                                            Name(id='k', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='parent_routing_type', ctx=Store())],
                                            value=IfExp(
                                                test=Name(id='parent', ctx=Load()),
                                                body=Attribute(
                                                    value=Attribute(
                                                        value=Call(
                                                            func=Name(id='getattr', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='parent', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='k', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='original_func',
                                                        ctx=Load(),
                                                    ),
                                                    attr='routing_type',
                                                    ctx=Load(),
                                                ),
                                                orelse=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Name(id='routing_type', ctx=Load()),
                                                        Constant(value='http', kind=None),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='routing_type', ctx=Load()),
                                                        ops=[IsNot()],
                                                        comparators=[Constant(value=None, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='routing_type', ctx=Load()),
                                                        ops=[IsNot()],
                                                        comparators=[Name(id='parent_routing_type', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='routing_type', ctx=Store())],
                                                    value=Name(id='parent_routing_type', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='Subclass re-defines <function %s.%s.%s> with different type than original. Will use original type: %r', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='__module__',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='__name__',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Name(id='k', ctx=Load()),
                                                                        Name(id='parent_routing_type', ctx=Load()),
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
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='v', ctx=Load()),
                                                        attr='original_func',
                                                        ctx=Load(),
                                                    ),
                                                    attr='routing_type',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='routing_type', ctx=Load()),
                                                    Name(id='parent_routing_type', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='sign', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='inspect', ctx=Load()),
                                                    attr='signature',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='v', ctx=Load()),
                                                        attr='original_func',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='first_arg', ctx=Store())],
                                            value=IfExp(
                                                test=Compare(
                                                    left=Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='sign', ctx=Load()),
                                                                attr='parameters',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    ops=[GtE()],
                                                    comparators=[Constant(value=2, kind=None)],
                                                ),
                                                body=Subscript(
                                                    value=Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='sign', ctx=Load()),
                                                                attr='parameters',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                orelse=Constant(value=None, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='first_arg', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value='req', kind=None),
                                                            Constant(value='request', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='v', ctx=Load()),
                                                            attr='_first_arg_is_req',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
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
                        Assign(
                            targets=[Name(id='name_class', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    BinOp(
                                        left=Constant(value='%s.%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='__module__',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='__name__',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    Name(id='cls', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='class_path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='name_class', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='.', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Compare(
                                    left=Subscript(
                                        value=Name(id='class_path', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=2, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    ops=[Eq()],
                                    comparators=[
                                        List(
                                            elts=[
                                                Constant(value='odoo', kind=None),
                                                Constant(value='addons', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='module', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='module', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='class_path', ctx=Load()),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Compare(
                                            left=Constant(value='Controller', kind=None),
                                            ops=[In()],
                                            comparators=[
                                                Call(
                                                    func=Name(id='globals', ctx=Load()),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Compare(
                                            left=Name(id='Controller', ctx=Load()),
                                            ops=[In()],
                                            comparators=[Name(id='bases', ctx=Load())],
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
                                    value=Subscript(
                                        value=Name(id='controllers_per_module', ctx=Load()),
                                        slice=Name(id='module', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='name_class', ctx=Load())],
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
            targets=[Name(id='Controller', ctx=Store())],
            value=Call(
                func=Name(id='ControllerType', ctx=Load()),
                args=[
                    Constant(value='Controller', kind=None),
                    Tuple(
                        elts=[Name(id='object', ctx=Load())],
                        ctx=Load(),
                    ),
                    Dict(keys=[], values=[]),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='EndPoint',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='method', annotation=None, type_comment=None),
                            arg(arg='routing', annotation=None, type_comment=None),
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
                                    attr='method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='method', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='original',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='method', ctx=Load()),
                                    Constant(value='original_func', kind=None),
                                    Name(id='method', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='routing',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='routing', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='arguments',
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
                    name='first_arg_is_req',
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
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='method',
                                        ctx=Load(),
                                    ),
                                    Constant(value='_first_arg_is_req', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__call__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='method',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
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
        FunctionDef(
            name='_generate_routing_rules',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='modules', annotation=None, type_comment=None),
                    arg(arg='nodb_only', annotation=None, type_comment=None),
                    arg(arg='converters', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                FunctionDef(
                    name='get_subclasses',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='klass', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='valid',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='c', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='c', ctx=Load()),
                                                        attr='__module__',
                                                        ctx=Load(),
                                                    ),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='odoo.addons.', kind=None)],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='c', ctx=Load()),
                                                                attr='__module__',
                                                                ctx=Load(),
                                                            ),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='modules', ctx=Load())],
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
                            targets=[Name(id='subclasses', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='klass', ctx=Load()),
                                    attr='__subclasses__',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='subclass', ctx=Store()),
                            iter=Name(id='subclasses', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='valid', ctx=Load()),
                                        args=[Name(id='subclass', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='get_subclasses', ctx=Load()),
                                                        args=[Name(id='subclass', ctx=Load())],
                                                        keywords=[],
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='result', ctx=Load()),
                                    ),
                                    Call(
                                        func=Name(id='valid', ctx=Load()),
                                        args=[Name(id='klass', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=List(
                                        elts=[Name(id='klass', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                For(
                    target=Name(id='module', ctx=Store()),
                    iter=Name(id='modules', ctx=Load()),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='module', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[Name(id='controllers_per_module', ctx=Load())],
                            ),
                            body=[Continue()],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='_', ctx=Store()),
                                    Name(id='cls', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Subscript(
                                value=Name(id='controllers_per_module', ctx=Load()),
                                slice=Name(id='module', ctx=Load()),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='subclasses', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='unique', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Name(id='c', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='c', ctx=Store()),
                                                                iter=Call(
                                                                    func=Name(id='get_subclasses', ctx=Load()),
                                                                    args=[Name(id='cls', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Name(id='c', ctx=Load()),
                                                                        ops=[IsNot()],
                                                                        comparators=[Name(id='cls', ctx=Load())],
                                                                    ),
                                                                ],
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
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='subclasses', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='name', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%s (extended by %s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='__name__',
                                                            ctx=Load(),
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Constant(value=', ', kind=None),
                                                                attr='join',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                GeneratorExp(
                                                                    elt=Attribute(
                                                                        value=Name(id='sub', ctx=Load()),
                                                                        attr='__name__',
                                                                        ctx=Load(),
                                                                    ),
                                                                    generators=[
                                                                        comprehension(
                                                                            target=Name(id='sub', ctx=Store()),
                                                                            iter=Name(id='subclasses', ctx=Load()),
                                                                            ifs=[],
                                                                            is_async=0,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='cls', ctx=Store())],
                                            value=Call(
                                                func=Name(id='type', ctx=Load()),
                                                args=[
                                                    Name(id='name', ctx=Load()),
                                                    Call(
                                                        func=Name(id='tuple', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='reversed', ctx=Load()),
                                                                args=[Name(id='subclasses', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='o', ctx=Store())],
                                    value=Call(
                                        func=Name(id='cls', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='members', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='inspect', ctx=Load()),
                                            attr='getmembers',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='o', ctx=Load()),
                                            Attribute(
                                                value=Name(id='inspect', ctx=Load()),
                                                attr='ismethod',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='_', ctx=Store()),
                                            Name(id='mv', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Name(id='members', ctx=Load()),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='hasattr', ctx=Load()),
                                                args=[
                                                    Name(id='mv', ctx=Load()),
                                                    Constant(value='routing', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='routing', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='type',
                                                                value=Constant(value='http', kind=None),
                                                            ),
                                                            keyword(
                                                                arg='auth',
                                                                value=Constant(value='user', kind=None),
                                                            ),
                                                            keyword(
                                                                arg='methods',
                                                                value=Constant(value=None, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='routes',
                                                                value=Constant(value=None, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='methods_done', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='claz', ctx=Store()),
                                                    iter=Call(
                                                        func=Name(id='reversed', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='mv', ctx=Load()),
                                                                            attr='__self__',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='__class__',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='mro',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='fn', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='getattr', ctx=Load()),
                                                                args=[
                                                                    Name(id='claz', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='mv', ctx=Load()),
                                                                        attr='__name__',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=None, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='fn', ctx=Load()),
                                                                    Call(
                                                                        func=Name(id='hasattr', ctx=Load()),
                                                                        args=[
                                                                            Name(id='fn', ctx=Load()),
                                                                            Constant(value='routing', kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Compare(
                                                                        left=Name(id='fn', ctx=Load()),
                                                                        ops=[NotIn()],
                                                                        comparators=[Name(id='methods_done', ctx=Load())],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='methods_done', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='fn', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='routing', ctx=Load()),
                                                                            attr='update',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='fn', ctx=Load()),
                                                                                attr='routing',
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
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='nodb_only', ctx=Load()),
                                                            ),
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='routing', ctx=Load()),
                                                                    slice=Constant(value='auth', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='none', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assert(
                                                            test=Subscript(
                                                                value=Name(id='routing', ctx=Load()),
                                                                slice=Constant(value='routes', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            msg=BinOp(
                                                                left=Constant(value='Method %r has not route defined', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='mv', ctx=Load()),
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='endpoint', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='EndPoint', ctx=Load()),
                                                                args=[
                                                                    Name(id='mv', ctx=Load()),
                                                                    Name(id='routing', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        For(
                                                            target=Name(id='url', ctx=Store()),
                                                            iter=Subscript(
                                                                value=Name(id='routing', ctx=Load()),
                                                                slice=Constant(value='routes', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Yield(
                                                                        value=Tuple(
                                                                            elts=[
                                                                                Name(id='url', ctx=Load()),
                                                                                Name(id='endpoint', ctx=Load()),
                                                                                Name(id='routing', ctx=Load()),
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
        ClassDef(
            name='AuthenticationError',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[Pass()],
            decorator_list=[],
        ),
        ClassDef(
            name='SessionExpiredException',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[Pass()],
            decorator_list=[],
        ),
        ClassDef(
            name='OpenERPSession',
            bases=[
                Attribute(
                    value=Name(id='sessions', ctx=Load()),
                    attr='Session',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='inited',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='modified',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rotate',
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
                                            Name(id='OpenERPSession', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='inited',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_default_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='modified',
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
                    name='__getattr__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attr', annotation=None, type_comment=None),
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
                                    Name(id='attr', ctx=Load()),
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
                    name='__setattr__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='k', annotation=None, type_comment=None),
                            arg(arg='v', annotation=None, type_comment=None),
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
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Constant(value='inited', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='object', ctx=Load()),
                                                    attr='__getattribute__',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Name(id='k', ctx=Load()),
                                                ],
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
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='__setitem__',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='k', ctx=Load()),
                                                            Name(id='v', ctx=Load()),
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='object', ctx=Load()),
                                    attr='__setattr__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='k', ctx=Load()),
                                    Name(id='v', ctx=Load()),
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
                    name='authenticate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='db', annotation=None, type_comment=None),
                            arg(arg='login', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Authenticate the current user with the given db, login and\n        password. If successful, store the authentication parameters in the\n        current session and request, unless multi-factor-authentication\n        is activated. In that case, that last part will be done by\n        :ref:`finalize`.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='wsgienv', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='httprequest',
                                    ctx=Load(),
                                ),
                                attr='environ',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='env', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='interactive',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='base_location',
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='httprequest',
                                                        ctx=Load(),
                                                    ),
                                                    attr='url_root',
                                                    ctx=Load(),
                                                ),
                                                attr='rstrip',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='/', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='HTTP_HOST',
                                        value=Subscript(
                                            value=Name(id='wsgienv', ctx=Load()),
                                            slice=Constant(value='HTTP_HOST', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='REMOTE_ADDR',
                                        value=Subscript(
                                            value=Name(id='wsgienv', ctx=Load()),
                                            slice=Constant(value='REMOTE_ADDR', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='registry',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='db', ctx=Load())],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='authenticate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='db', ctx=Load()),
                                    Name(id='login', ctx=Load()),
                                    Name(id='password', ctx=Load()),
                                    Name(id='env', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='pre_uid',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='uid', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rotate',
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
                                    attr='db',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='db', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='login',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='login', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='disable_db',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='user',
                                                    value=Name(id='uid', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='uid', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='_mfa_url',
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='finalize',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='uid', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='finalize',
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
                            value=Constant(value=' Finalizes a partial session, should be called on MFA validation to\n        convert a partial / pre-session into a full-fledged "logged-in" one\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rotate',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='uid',
                                    ctx=Store(),
                                ),
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='uid',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='pre_uid', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='user',
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='uid',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='uid',
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
                                    attr='session_token',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user', ctx=Load()),
                                    attr='_compute_session_token',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sid',
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
                                    attr='get_context',
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
                    name='check_security',
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
                            value=Constant(value='\n        Check the current authentication parameters to know if those are still\n        valid. This method should be called at each request. If the\n        authentication fails, a :exc:`SessionExpiredException` is raised.\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='db',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='uid',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='SessionExpiredException', ctx=Load()),
                                        args=[Constant(value='Session expired', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
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
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='context',
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
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='security', ctx=Load()),
                                        attr='check_session',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='self', ctx=Load()),
                                        Name(id='env', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='SessionExpiredException', ctx=Load()),
                                        args=[Constant(value='Session expired', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
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
                    name='logout',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='keep_db', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        For(
                            target=Name(id='k', ctx=Store()),
                            iter=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Name(id='keep_db', ctx=Load()),
                                                        Compare(
                                                            left=Name(id='k', ctx=Load()),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='db', kind=None)],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            Compare(
                                                left=Name(id='k', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='debug', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Delete(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='self', ctx=Load()),
                                                    slice=Name(id='k', ctx=Load()),
                                                    ctx=Del(),
                                                ),
                                            ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_default_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rotate',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_values',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='db', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='uid', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='login', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='session_token', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='context', kind=None),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='debug', kind=None),
                                    Constant(value='', kind=None),
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
                    name='get_context',
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
                            value=Constant(value="\n        Re-initializes the current user's session context (based on his\n        preferences) by calling res.users.get_context() with the old context.\n\n        :returns: the new context\n        ", kind=None),
                        ),
                        Assert(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='uid',
                                ctx=Load(),
                            ),
                            msg=Constant(value='The user needs to be logged-in to initialize his context', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='context',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
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
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='uid', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='uid',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fix_lang',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='context',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_fix_lang',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='context', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" OpenERP provides languages which may not make sense and/or may not\n        be understood by the web client's libraries.\n\n        Fix those here.\n\n        :param dict context: context to fix\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='lang', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='lang', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='lang', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='ar_AR', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='lang', ctx=Store())],
                                    value=Constant(value='ar', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='lang', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='babel', ctx=Load()),
                                            attr='core',
                                            ctx=Load(),
                                        ),
                                        attr='LOCALE_ALIASES',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='lang', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='babel', ctx=Load()),
                                                attr='core',
                                                ctx=Load(),
                                            ),
                                            attr='LOCALE_ALIASES',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='lang', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='context', ctx=Load()),
                                    slice=Constant(value='lang', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='lang', ctx=Load()),
                                    Constant(value='en_US', kind=None),
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
                    name='save_action',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='action', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        This method store an action object in the session and returns an integer\n        identifying that action. The method get_action() can be used to get\n        back the action.\n\n        :param the_action: The action to save in the session.\n        :type the_action: anything\n        :return: A key identifying the saved action.\n        :rtype: integer\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='saved_actions', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='saved_actions', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='next', kind=None),
                                            Constant(value='actions', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Subscript(
                                            value=Name(id='saved_actions', ctx=Load()),
                                            slice=Constant(value='actions', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[GtE()],
                                comparators=[Constant(value=10, kind=None)],
                            ),
                            body=[
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='saved_actions', ctx=Load()),
                                                slice=Constant(value='actions', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='saved_actions', ctx=Load()),
                                                        slice=Constant(value='actions', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='key', ctx=Store())],
                            value=Subscript(
                                value=Name(id='saved_actions', ctx=Load()),
                                slice=Constant(value='next', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='saved_actions', ctx=Load()),
                                        slice=Constant(value='actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='key', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='action', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='saved_actions', ctx=Load()),
                                    slice=Constant(value='next', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Name(id='key', ctx=Load()),
                                op=Add(),
                                right=Constant(value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='modified',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='key', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_action',
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
                        Expr(
                            value=Constant(value='\n        Gets back a previously saved action. This method can return None if the action\n        was saved since too much time (this case should be handled in a smart way).\n\n        :param key: The key given by save_action()\n        :type key: integer\n        :return: The saved action or None.\n        :rtype: anything\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='saved_actions', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='saved_actions', kind=None),
                                    Dict(keys=[], values=[]),
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
                                            value=Name(id='saved_actions', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='actions', kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='key', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='save_request_data',
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
                            names=[alias(name='uuid', asname=None)],
                        ),
                        Assign(
                            targets=[Name(id='req', ctx=Store())],
                            value=Attribute(
                                value=Name(id='request', ctx=Load()),
                                attr='httprequest',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='files', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='werkzeug', ctx=Load()),
                                        attr='datastructures',
                                        ctx=Load(),
                                    ),
                                    attr='MultiDict',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='f', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='req', ctx=Load()),
                                        attr='files',
                                        ctx=Load(),
                                    ),
                                    attr='values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='storename', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='werkzeug_%s_%s.file', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sid',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='uuid', ctx=Load()),
                                                            attr='uuid4',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='hex',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
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
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='root', ctx=Load()),
                                                    attr='session_store',
                                                    ctx=Load(),
                                                ),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            Name(id='storename', ctx=Load()),
                                        ],
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
                                                    Name(id='path', ctx=Load()),
                                                    Constant(value='w', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='fp', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='f', ctx=Load()),
                                                    attr='save',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='fp', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='files', ctx=Load()),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='f', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='storename', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='f', ctx=Load()),
                                                        attr='filename',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='f', ctx=Load()),
                                                        attr='content_type',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='self', ctx=Load()),
                                    slice=Constant(value='serialized_request_data', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='form', kind=None),
                                    Constant(value='files', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='req', ctx=Load()),
                                        attr='form',
                                        ctx=Load(),
                                    ),
                                    Name(id='files', ctx=Load()),
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
                    name='load_request_data',
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
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='serialized_request_data', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='files', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='werkzeug', ctx=Load()),
                                        attr='datastructures',
                                        ctx=Load(),
                                    ),
                                    attr='MultiDict',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                If(
                                    test=Name(id='data', ctx=Load()),
                                    body=[
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='name', ctx=Store()),
                                                    Tuple(
                                                        elts=[
                                                            Name(id='storename', ctx=Store()),
                                                            Name(id='filename', ctx=Store()),
                                                            Name(id='content_type', ctx=Store()),
                                                        ],
                                                        ctx=Store(),
                                                    ),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='files', kind=None),
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='root', ctx=Load()),
                                                                    attr='session_store',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='storename', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='files', ctx=Load()),
                                                            attr='add',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='name', ctx=Load()),
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='path', ctx=Load()),
                                                                    Name(id='filename', ctx=Load()),
                                                                    Name(id='content_type', ctx=Load()),
                                                                ],
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
                                        Expr(
                                            value=Yield(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='werkzeug', ctx=Load()),
                                                            attr='datastructures',
                                                            ctx=Load(),
                                                        ),
                                                        attr='CombinedMultiDict',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Subscript(
                                                                    value=Name(id='data', ctx=Load()),
                                                                    slice=Constant(value='form', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='files', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Yield(
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='f', ctx=Store()),
                                            Name(id='_', ctx=Store()),
                                            Name(id='_', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='files', ctx=Load()),
                                            attr='values',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
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
                                                        args=[Name(id='f', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='IOError', ctx=Load()),
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
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='contextlib', ctx=Load()),
                            attr='contextmanager',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='session_gc',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='session_store', annotation=None, type_comment=None)],
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
                                value=Name(id='random', ctx=Load()),
                                attr='random',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        ops=[Lt()],
                        comparators=[Constant(value=0.001, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='last_week', ctx=Store())],
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
                                right=BinOp(
                                    left=BinOp(
                                        left=BinOp(
                                            left=Constant(value=60, kind=None),
                                            op=Mult(),
                                            right=Constant(value=60, kind=None),
                                        ),
                                        op=Mult(),
                                        right=Constant(value=24, kind=None),
                                    ),
                                    op=Mult(),
                                    right=Constant(value=7, kind=None),
                                ),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='fname', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='listdir',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='session_store', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                            Attribute(
                                                value=Name(id='session_store', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            Name(id='fname', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='path',
                                                            ctx=Load(),
                                                        ),
                                                        attr='getmtime',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='path', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Lt()],
                                                comparators=[Name(id='last_week', ctx=Load())],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='unlink',
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
        Assign(
            targets=[Name(id='ODOO_DISABLE_SESSION_GC', ctx=Store())],
            value=Call(
                func=Name(id='str2bool', ctx=Load()),
                args=[
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
                            Constant(value='ODOO_DISABLE_SESSION_GC', kind=None),
                            Constant(value='0', kind=None),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        If(
            test=Name(id='ODOO_DISABLE_SESSION_GC', ctx=Load()),
            body=[
                Assign(
                    targets=[Name(id='session_gc', ctx=Store())],
                    value=Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='s', annotation=None, type_comment=None)],
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
            orelse=[],
        ),
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='mimetypes', ctx=Load()),
                    attr='add_type',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='application/font-woff', kind=None),
                    Constant(value='.woff', kind=None),
                ],
                keywords=[],
            ),
        ),
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='mimetypes', ctx=Load()),
                    attr='add_type',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='application/vnd.ms-fontobject', kind=None),
                    Constant(value='.eot', kind=None),
                ],
                keywords=[],
            ),
        ),
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='mimetypes', ctx=Load()),
                    attr='add_type',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='application/x-font-ttf', kind=None),
                    Constant(value='.ttf', kind=None),
                ],
                keywords=[],
            ),
        ),
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='mimetypes', ctx=Load()),
                    attr='add_type',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='image/svg+xml', kind=None),
                    Constant(value='.svg', kind=None),
                ],
                keywords=[],
            ),
        ),
        ClassDef(
            name='Response',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='werkzeug', ctx=Load()),
                        attr='wrappers',
                        ctx=Load(),
                    ),
                    attr='Response',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Response object passed through controller route chain.\n\n    In addition to the :class:`werkzeug.wrappers.Response` parameters, this\n    class's constructor can take the following additional parameters\n    for QWeb Lazy Rendering.\n\n    :param basestring template: template to render\n    :param dict qcontext: Rendering context to use\n    :param int uid: User id to use for the ir.ui.view render call,\n                    ``None`` to use the request's user (the default)\n\n    these attributes are available as parameters on the Response object and\n    can be altered at any time before rendering\n\n    Also exposes all the attributes and methods of\n    :class:`werkzeug.wrappers.Response`.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='default_mimetype', ctx=Store())],
                    value=Constant(value='text/html', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='template', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kw', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='template', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='qcontext', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kw', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='qcontext', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kw', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='uid', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Response', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kw', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='set_default',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='template', ctx=Load()),
                                    Name(id='qcontext', ctx=Load()),
                                    Name(id='uid', ctx=Load()),
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
                    name='set_default',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='qcontext', annotation=None, type_comment=None),
                            arg(arg='uid', annotation=None, type_comment=None),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='template', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='qcontext',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='qcontext', ctx=Load()),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='qcontext',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='response_template', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='template',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='uid',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='uid', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='endpoint',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Constant(value='cors', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='endpoint',
                                                    ctx=Load(),
                                                ),
                                                attr='routing',
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
                                                attr='headers',
                                                ctx=Load(),
                                            ),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Access-Control-Allow-Origin', kind=None),
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='endpoint',
                                                        ctx=Load(),
                                                    ),
                                                    attr='routing',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='cors', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='methods', ctx=Store())],
                                    value=Constant(value='GET, POST', kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='endpoint',
                                                    ctx=Load(),
                                                ),
                                                attr='routing',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='json', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='methods', ctx=Store())],
                                            value=Constant(value='POST', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='endpoint',
                                                            ctx=Load(),
                                                        ),
                                                        attr='routing',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='methods', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='methods', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Constant(value=', ', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='request', ctx=Load()),
                                                                        attr='endpoint',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='routing',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='methods', kind=None),
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
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='headers',
                                                ctx=Load(),
                                            ),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Access-Control-Allow-Methods', kind=None),
                                            Name(id='methods', ctx=Load()),
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
                    name='is_qweb',
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
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='template',
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='render',
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
                            value=Constant(value=" Renders the Response's template, returns the result\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='env', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='user',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='uid',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='uid',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='SUPERUSER_ID',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='qcontext',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='request', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='request', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_render_template',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='template',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='qcontext',
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
                    name='flatten',
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
                            value=Constant(value=" Forces the rendering of the response's template, sets the result\n        as response body and unsets :attr:`.template`\n        ", kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='template',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='response',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='render',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='template',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='DisableCacheMiddleware',
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
                            arg(arg='environ', annotation=None, type_comment=None),
                            arg(arg='start_response', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='start_wrapped',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='status', annotation=None, type_comment=None),
                                    arg(arg='headers', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='req', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='wrappers',
                                                ctx=Load(),
                                            ),
                                            attr='Request',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='environ', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='root', ctx=Load()),
                                            attr='setup_session',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='req', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='req', ctx=Load()),
                                                attr='session',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='req', ctx=Load()),
                                                    attr='session',
                                                    ctx=Load(),
                                                ),
                                                attr='debug',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Compare(
                                                    left=Constant(value='wkhtmltopdf', kind=None),
                                                    ops=[In()],
                                                    comparators=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='req', ctx=Load()),
                                                                    attr='headers',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='User-Agent', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Constant(value='assets', kind=None),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='req', ctx=Load()),
                                                                    attr='session',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='debug',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Constant(value='.js', kind=None),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='req', ctx=Load()),
                                                                        attr='base_url',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Compare(
                                                                left=Constant(value='.css', kind=None),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='req', ctx=Load()),
                                                                        attr='base_url',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='new_headers', ctx=Store())],
                                                    value=List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='Cache-Control', kind=None),
                                                                    Constant(value='no-store', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='new_headers', ctx=Store())],
                                                    value=List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='Cache-Control', kind=None),
                                                                    Constant(value='no-cache', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='k', ctx=Store()),
                                                    Name(id='v', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Name(id='headers', ctx=Load()),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='k', ctx=Load()),
                                                                attr='lower',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='cache-control', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='new_headers', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Name(id='k', ctx=Load()),
                                                                            Name(id='v', ctx=Load()),
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
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='start_response', ctx=Load()),
                                                args=[
                                                    Name(id='status', ctx=Load()),
                                                    Name(id='new_headers', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='start_response', ctx=Load()),
                                                args=[
                                                    Name(id='status', ctx=Load()),
                                                    Name(id='headers', ctx=Load()),
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='app',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='environ', ctx=Load()),
                                    Name(id='start_wrapped', ctx=Load()),
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
            name='Root',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Root WSGI application for the OpenERP Web Client.\n    ', kind=None),
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
                                    attr='_loaded',
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
                    name='session_store',
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
                            targets=[Name(id='path', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='tools',
                                        ctx=Load(),
                                    ),
                                    attr='config',
                                    ctx=Load(),
                                ),
                                attr='session_dir',
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
                                    Constant(value='HTTP sessions stored in: %s', kind=None),
                                    Name(id='path', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='ODOO_DISABLE_SESSION_GC', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Default session GC disabled, manual GC required.', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sessions', ctx=Load()),
                                    attr='FilesystemSessionStore',
                                    ctx=Load(),
                                ),
                                args=[Name(id='path', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='session_class',
                                        value=Name(id='OpenERPSession', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='renew_missing',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='lazy_property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='nodb_routing_map',
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
                                args=[Constant(value='Generating nondb routing', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='routing_map', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='werkzeug', ctx=Load()),
                                        attr='routing',
                                        ctx=Load(),
                                    ),
                                    attr='Map',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='strict_slashes',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='converters',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='url', ctx=Store()),
                                    Name(id='endpoint', ctx=Store()),
                                    Name(id='routing', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='http',
                                        ctx=Load(),
                                    ),
                                    attr='_generate_routing_rules',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=List(
                                            elts=[Constant(value='', kind=None)],
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='conf',
                                                ctx=Load(),
                                            ),
                                            attr='server_wide_modules',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='rule', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='routing',
                                                ctx=Load(),
                                            ),
                                            attr='Rule',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='url', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='endpoint',
                                                value=Name(id='endpoint', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='methods',
                                                value=Subscript(
                                                    value=Name(id='routing', ctx=Load()),
                                                    slice=Constant(value='methods', kind=None),
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
                                            value=Name(id='rule', ctx=Load()),
                                            attr='merge_slashes',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='routing_map', ctx=Load()),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='rule', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='routing_map', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='lazy_property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__call__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='environ', annotation=None, type_comment=None),
                            arg(arg='start_response', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Handle a WSGI request\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_loaded',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_loaded',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='load_addons',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dispatch',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='environ', ctx=Load()),
                                    Name(id='start_response', ctx=Load()),
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
                    name='load_addons',
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
                            value=Constant(value=' Load all addons from addons path containing static files and\n        controllers and configure them.  ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='statics', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='manifests', ctx=Store())],
                            value=Name(id='addons_manifest', ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='addons_path', ctx=Store()),
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
                                For(
                                    target=Name(id='module', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='listdir',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='addons_path', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='module', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='manifests', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='mod_path', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='opj', ctx=Load()),
                                                        args=[
                                                            Name(id='addons_path', ctx=Load()),
                                                            Name(id='module', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='manifest', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='read_manifest', ctx=Load()),
                                                        args=[
                                                            Name(id='addons_path', ctx=Load()),
                                                            Name(id='module', ctx=Load()),
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
                                                                operand=Name(id='manifest', ctx=Load()),
                                                            ),
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    UnaryOp(
                                                                        op=Not(),
                                                                        operand=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='manifest', ctx=Load()),
                                                                                attr='get',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Constant(value='installable', kind=None),
                                                                                Constant(value=True, kind=None),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    Compare(
                                                                        left=Constant(value='assets', kind=None),
                                                                        ops=[NotIn()],
                                                                        comparators=[Name(id='manifest', ctx=Load())],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[Continue()],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='manifest', ctx=Load()),
                                                            slice=Constant(value='addons_path', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='addons_path', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='manifests', ctx=Load()),
                                                            slice=Name(id='module', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='manifest', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='path_static', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='opj', ctx=Load()),
                                                        args=[
                                                            Name(id='addons_path', ctx=Load()),
                                                            Name(id='module', ctx=Load()),
                                                            Constant(value='static', kind=None),
                                                        ],
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
                                                        args=[Name(id='path_static', ctx=Load())],
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
                                                                    Constant(value='Loading %s', kind=None),
                                                                    Name(id='module', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='statics', ctx=Load()),
                                                                    slice=BinOp(
                                                                        left=Constant(value='/%s/static', kind=None),
                                                                        op=Mod(),
                                                                        right=Name(id='module', ctx=Load()),
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='path_static', ctx=Load()),
                                                            type_comment=None,
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='statics', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='HTTP Configuring static files', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='app', ctx=Store())],
                            value=Call(
                                func=Name(id='SharedDataMiddleware', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dispatch',
                                        ctx=Load(),
                                    ),
                                    Name(id='statics', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='cache_timeout',
                                        value=Name(id='STATIC_CACHE', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dispatch',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='DisableCacheMiddleware', ctx=Load()),
                                args=[Name(id='app', ctx=Load())],
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
                    name='setup_session',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='httprequest', annotation=None, type_comment=None),
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
                                func=Name(id='session_gc', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='session_store',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='sid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='httprequest', ctx=Load()),
                                        attr='args',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='session_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='explicit_session', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='sid', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sid', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='httprequest', ctx=Load()),
                                                attr='headers',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='X-Openerp-Session-Id', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='sid', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sid', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='httprequest', ctx=Load()),
                                                attr='cookies',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='session_id', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='explicit_session', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='sid', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='httprequest', ctx=Load()),
                                            attr='session',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='session_store',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='httprequest', ctx=Load()),
                                            attr='session',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='session_store',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='sid', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='explicit_session', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='setup_db',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='httprequest', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='db', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='httprequest', ctx=Load()),
                                    attr='session',
                                    ctx=Load(),
                                ),
                                attr='db',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='db', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='db', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            Call(
                                                func=Name(id='db_filter', ctx=Load()),
                                                args=[
                                                    List(
                                                        elts=[Name(id='db', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='httprequest',
                                                        value=Name(id='httprequest', ctx=Load()),
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
                                                    Constant(value="Logged into database '%s', but dbfilter rejects it; logging session out.", kind=None),
                                                    Name(id='db', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='httprequest', ctx=Load()),
                                                        attr='session',
                                                        ctx=Load(),
                                                    ),
                                                    attr='logout',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='db', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='db', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='httprequest', ctx=Load()),
                                                attr='session',
                                                ctx=Load(),
                                            ),
                                            attr='db',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='db_monodb', ctx=Load()),
                                        args=[Name(id='httprequest', ctx=Load())],
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
                    name='setup_lang',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='httprequest', annotation=None, type_comment=None),
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
                                left=Constant(value='lang', kind=None),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='httprequest', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='alang', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='httprequest', ctx=Load()),
                                                    attr='accept_languages',
                                                    ctx=Load(),
                                                ),
                                                attr='best',
                                                ctx=Load(),
                                            ),
                                            Constant(value='en-US', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='code', ctx=Store()),
                                                        Name(id='territory', ctx=Store()),
                                                        Name(id='_', ctx=Store()),
                                                        Name(id='_', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='babel', ctx=Load()),
                                                        attr='core',
                                                        ctx=Load(),
                                                    ),
                                                    attr='parse_locale',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='alang', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='sep',
                                                        value=Constant(value='-', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='territory', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='lang', ctx=Store())],
                                                    value=BinOp(
                                                        left=Constant(value='%s_%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='code', ctx=Load()),
                                                                Name(id='territory', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='lang', ctx=Store())],
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='babel', ctx=Load()),
                                                                attr='core',
                                                                ctx=Load(),
                                                            ),
                                                            attr='LOCALE_ALIASES',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='code', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Tuple(
                                                elts=[
                                                    Name(id='ValueError', ctx=Load()),
                                                    Name(id='KeyError', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[Name(id='lang', ctx=Store())],
                                                    value=Constant(value='en_US', kind=None),
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
                                        Subscript(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='httprequest', ctx=Load()),
                                                    attr='session',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='lang', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='lang', ctx=Load()),
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
                    name='get_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='httprequest', annotation=None, type_comment=None),
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
                                    value=Name(id='httprequest', ctx=Load()),
                                    attr='mimetype',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='application/json', kind=None),
                                            Constant(value='application/json-rpc', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='JsonRequest', ctx=Load()),
                                        args=[Name(id='httprequest', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Call(
                                        func=Name(id='HttpRequest', ctx=Load()),
                                        args=[Name(id='httprequest', ctx=Load())],
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
                    name='get_response',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='httprequest', annotation=None, type_comment=None),
                            arg(arg='result', annotation=None, type_comment=None),
                            arg(arg='explicit_session', annotation=None, type_comment=None),
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
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='result', ctx=Load()),
                                            Name(id='Response', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='result', ctx=Load()),
                                        attr='is_qweb',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='flatten',
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
                                            name='e',
                                            body=[
                                                If(
                                                    test=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='db',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='result', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='registry',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='ir.http', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='_handle_exception',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='e', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[Raise(exc=None, cause=None)],
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
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='result', ctx=Load()),
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
                            body=[
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Call(
                                        func=Name(id='Response', ctx=Load()),
                                        args=[Name(id='result', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='mimetype',
                                                value=Constant(value='text/html', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Name(id='result', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='save_session', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='endpoint',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='endpoint',
                                                    ctx=Load(),
                                                ),
                                                attr='routing',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='save_session', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='save_session', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='response', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='httprequest', ctx=Load()),
                                    attr='session',
                                    ctx=Load(),
                                ),
                                attr='should_save',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Attribute(
                                            value=Name(id='httprequest', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='rotate',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='session_store',
                                                        ctx=Load(),
                                                    ),
                                                    attr='delete',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='httprequest', ctx=Load()),
                                                        attr='session',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='httprequest', ctx=Load()),
                                                        attr='session',
                                                        ctx=Load(),
                                                    ),
                                                    attr='sid',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='session_store',
                                                        ctx=Load(),
                                                    ),
                                                    attr='generate_key',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Attribute(
                                                    value=Name(id='httprequest', ctx=Load()),
                                                    attr='session',
                                                    ctx=Load(),
                                                ),
                                                attr='uid',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='httprequest', ctx=Load()),
                                                                attr='session',
                                                                ctx=Load(),
                                                            ),
                                                            attr='session_token',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='security', ctx=Load()),
                                                            attr='compute_session_token',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='httprequest', ctx=Load()),
                                                                attr='session',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='env',
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
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='httprequest', ctx=Load()),
                                                        attr='session',
                                                        ctx=Load(),
                                                    ),
                                                    attr='modified',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='session_store',
                                                ctx=Load(),
                                            ),
                                            attr='save',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='httprequest', ctx=Load()),
                                                attr='session',
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='explicit_session', ctx=Load()),
                                    ),
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='response', ctx=Load()),
                                            Constant(value='set_cookie', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='set_cookie',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='session_id', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='httprequest', ctx=Load()),
                                                    attr='session',
                                                    ctx=Load(),
                                                ),
                                                attr='sid',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='max_age',
                                                value=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=Constant(value=90, kind=None),
                                                            op=Mult(),
                                                            right=Constant(value=24, kind=None),
                                                        ),
                                                        op=Mult(),
                                                        right=Constant(value=60, kind=None),
                                                    ),
                                                    op=Mult(),
                                                    right=Constant(value=60, kind=None),
                                                ),
                                            ),
                                            keyword(
                                                arg='httponly',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
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
                            arg(arg='environ', annotation=None, type_comment=None),
                            arg(arg='start_response', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Performs the actual WSGI dispatching for the application.\n        ', kind=None),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='httprequest', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='wrappers',
                                                ctx=Load(),
                                            ),
                                            attr='Request',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='environ', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='httprequest', ctx=Load()),
                                            attr='parameter_storage_class',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='werkzeug', ctx=Load()),
                                            attr='datastructures',
                                            ctx=Load(),
                                        ),
                                        attr='ImmutableOrderedMultiDict',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='current_thread', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='current_thread',
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
                                            value=Name(id='current_thread', ctx=Load()),
                                            attr='url',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='httprequest', ctx=Load()),
                                        attr='url',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='current_thread', ctx=Load()),
                                            attr='query_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='current_thread', ctx=Load()),
                                            attr='query_time',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='current_thread', ctx=Load()),
                                            attr='perf_t0',
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
                                    targets=[Name(id='explicit_session', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='setup_session',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='httprequest', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='setup_db',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='httprequest', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='setup_lang',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='httprequest', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='request', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_request',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='httprequest', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                FunctionDef(
                                    name='_dispatch_nodb',
                                    args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                    body=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='func', ctx=Store()),
                                                                Name(id='arguments', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='nodb_routing_map',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='bind_to_environ',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='httprequest',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='environ',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='match',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='werkzeug', ctx=Load()),
                                                            attr='exceptions',
                                                            ctx=Load(),
                                                        ),
                                                        attr='HTTPException',
                                                        ctx=Load(),
                                                    ),
                                                    name='e',
                                                    body=[
                                                        Return(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='_handle_exception',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='e', ctx=Load())],
                                                                keywords=[],
                                                            ),
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
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='set_handler',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='func', ctx=Load()),
                                                    Name(id='arguments', ctx=Load()),
                                                    Constant(value='none', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='result', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='dispatch',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='Exception', ctx=Load()),
                                                    name='e',
                                                    body=[
                                                        Return(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='_handle_exception',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='e', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                        Return(
                                            value=Name(id='result', ctx=Load()),
                                        ),
                                    ],
                                    decorator_list=[],
                                    returns=None,
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='request_manager', ctx=Store())],
                                    value=Name(id='request', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='profile_session',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='request_manager', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_profiler_context_manager',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='request', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Name(id='request_manager', ctx=Load()),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='db', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='session',
                                                    ctx=Load(),
                                                ),
                                                attr='db',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='db', ctx=Load()),
                                            body=[
                                                Try(
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='odoo', ctx=Load()),
                                                                            attr='registry',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='db', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='check_signaling',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        With(
                                                            items=[
                                                                withitem(
                                                                    context_expr=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='odoo', ctx=Load()),
                                                                                attr='tools',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='mute_logger',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='odoo.sql_db', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    optional_vars=None,
                                                                ),
                                                            ],
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='ir_http', ctx=Store())],
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='registry',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='ir.http', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Tuple(
                                                                elts=[
                                                                    Name(id='AttributeError', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='psycopg2', ctx=Load()),
                                                                        attr='OperationalError',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='psycopg2', ctx=Load()),
                                                                        attr='ProgrammingError',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            name=None,
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='request', ctx=Load()),
                                                                                attr='session',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='logout',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                If(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='request', ctx=Load()),
                                                                                attr='httprequest',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='path',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='/web', kind=None)],
                                                                    ),
                                                                    body=[Raise(exc=None, cause=None)],
                                                                    orelse=[
                                                                        Assign(
                                                                            targets=[Name(id='result', ctx=Store())],
                                                                            value=Call(
                                                                                func=Name(id='_dispatch_nodb', ctx=Load()),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='result', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='ir_http', ctx=Load()),
                                                                    attr='_dispatch',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    finalbody=[],
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='result', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_dispatch_nodb', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='response', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_response',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='httprequest', ctx=Load()),
                                                    Name(id='result', ctx=Load()),
                                                    Name(id='explicit_session', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='response', ctx=Load()),
                                        args=[
                                            Name(id='environ', ctx=Load()),
                                            Name(id='start_response', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Attribute(
                                            value=Name(id='werkzeug', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='HTTPException',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='e', ctx=Load()),
                                                args=[
                                                    Name(id='environ', ctx=Load()),
                                                    Name(id='start_response', ctx=Load()),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_profiler_context_manager',
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
                        Expr(
                            value=Constant(value=' Return a context manager that combines a profiler and ``request``. ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='profile_session',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='session',
                                                ctx=Load(),
                                            ),
                                            attr='profile_expiration',
                                            ctx=Load(),
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='datetime', ctx=Load()),
                                                            attr='now',
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
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='session',
                                                        ctx=Load(),
                                                    ),
                                                    attr='profile_session',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Profiling expiration reached, disabling profiling', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Constant(value='set_profiling', kind=None),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='httprequest',
                                                            ctx=Load(),
                                                        ),
                                                        attr='path',
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
                                                        args=[Constant(value='Profiling disabled on set_profiling route', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='httprequest',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='startswith',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='/longpolling', kind=None)],
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
                                                                args=[Constant(value='Profiling disabled for longpolling', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Attribute(
                                                                value=Name(id='odoo', ctx=Load()),
                                                                attr='evented',
                                                                ctx=Load(),
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='_logger', ctx=Load()),
                                                                            attr='debug',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='Profiling disabled for evented server', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Try(
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='prof', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='profiler', ctx=Load()),
                                                                                    attr='Profiler',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='db',
                                                                                        value=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='request', ctx=Load()),
                                                                                                attr='session',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='db',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    keyword(
                                                                                        arg='description',
                                                                                        value=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='request', ctx=Load()),
                                                                                                attr='httprequest',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='full_path',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    keyword(
                                                                                        arg='profile_session',
                                                                                        value=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='request', ctx=Load()),
                                                                                                attr='session',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='profile_session',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    keyword(
                                                                                        arg='collectors',
                                                                                        value=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='request', ctx=Load()),
                                                                                                attr='session',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='profile_collectors',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    keyword(
                                                                                        arg='params',
                                                                                        value=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='request', ctx=Load()),
                                                                                                attr='session',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='profile_params',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Return(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='profiler', ctx=Load()),
                                                                                    attr='Nested',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Name(id='prof', ctx=Load()),
                                                                                    Name(id='request', ctx=Load()),
                                                                                ],
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
                                                                                        args=[Constant(value='Failure during Profiler creation', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                                Assign(
                                                                                    targets=[
                                                                                        Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='request', ctx=Load()),
                                                                                                attr='session',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='profile_session',
                                                                                            ctx=Store(),
                                                                                        ),
                                                                                    ],
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
                        Return(
                            value=Name(id='request', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_db_router',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='db', annotation=None, type_comment=None),
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
                                operand=Name(id='db', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='nodb_routing_map',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.http', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='routing_map',
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
        FunctionDef(
            name='db_list',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='force', annotation=None, type_comment=None),
                    arg(arg='httprequest', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Assign(
                    targets=[Name(id='dbs', ctx=Store())],
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
                        args=[Name(id='force', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='db_filter', ctx=Load()),
                        args=[Name(id='dbs', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='httprequest',
                                value=Name(id='httprequest', ctx=Load()),
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
            name='db_filter',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='dbs', annotation=None, type_comment=None),
                    arg(arg='httprequest', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='httprequest', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Name(id='httprequest', ctx=Load()),
                            Attribute(
                                value=Name(id='request', ctx=Load()),
                                attr='httprequest',
                                ctx=Load(),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='h', ctx=Store())],
                    value=Subscript(
                        value=Call(
                            func=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='httprequest', ctx=Load()),
                                            attr='environ',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='HTTP_HOST', kind=None),
                                        Constant(value='', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                attr='split',
                                ctx=Load(),
                            ),
                            args=[Constant(value=':', kind=None)],
                            keywords=[],
                        ),
                        slice=Constant(value=0, kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='d', ctx=Store()),
                                Name(id='_', ctx=Store()),
                                Name(id='r', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Attribute(
                            value=Name(id='h', ctx=Load()),
                            attr='partition',
                            ctx=Load(),
                        ),
                        args=[Constant(value='.', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Name(id='d', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='www', kind=None)],
                            ),
                            Name(id='r', ctx=Load()),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='d', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='r', ctx=Load()),
                                        attr='partition',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='.', kind=None)],
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
                        slice=Constant(value='dbfilter', kind=None),
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='d', ctx=Store()),
                                        Name(id='h', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='escape',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='d', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='escape',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='h', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
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
                                                slice=Constant(value='dbfilter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='%h', kind=None),
                                            Name(id='h', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%d', kind=None),
                                    Name(id='d', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dbs', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='i', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='i', ctx=Store()),
                                        iter=Name(id='dbs', ctx=Load()),
                                        ifs=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='match',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='r', ctx=Load()),
                                                    Name(id='i', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
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
                                slice=Constant(value='db_name', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='exposed_dbs', ctx=Store())],
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='db', ctx=Load()),
                                                        attr='strip',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='db', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
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
                                                                    slice=Constant(value='db_name', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=',', kind=None)],
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
                                    targets=[Name(id='dbs', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='exposed_dbs', ctx=Load()),
                                                    attr='intersection',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='dbs', ctx=Load())],
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
                ),
                Return(
                    value=Name(id='dbs', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='db_monodb',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='httprequest', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='\n        Magic function to find the current database.\n\n        Implementation details:\n\n        * Magic\n        * More magic\n\n        Returns ``None`` if the magic is not magic enough.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='httprequest', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Name(id='httprequest', ctx=Load()),
                            Attribute(
                                value=Name(id='request', ctx=Load()),
                                attr='httprequest',
                                ctx=Load(),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='dbs', ctx=Store())],
                    value=Call(
                        func=Name(id='db_list', ctx=Load()),
                        args=[
                            Constant(value=True, kind=None),
                            Name(id='httprequest', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='db_session', ctx=Store())],
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='httprequest', ctx=Load()),
                            attr='session',
                            ctx=Load(),
                        ),
                        attr='db',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='db_session', ctx=Load()),
                        ops=[In()],
                        comparators=[Name(id='dbs', ctx=Load())],
                    ),
                    body=[
                        Return(
                            value=Name(id='db_session', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='dbs', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value=1, kind=None)],
                    ),
                    body=[
                        Return(
                            value=Subscript(
                                value=Name(id='dbs', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Constant(value=None, kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='send_file',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='filepath_or_fp', annotation=None, type_comment=None),
                    arg(arg='mimetype', annotation=None, type_comment=None),
                    arg(arg='as_attachment', annotation=None, type_comment=None),
                    arg(arg='filename', annotation=None, type_comment=None),
                    arg(arg='mtime', annotation=None, type_comment=None),
                    arg(arg='add_etags', annotation=None, type_comment=None),
                    arg(arg='cache_timeout', annotation=None, type_comment=None),
                    arg(arg='conditional', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=False, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=True, kind=None),
                    Name(id='STATIC_CACHE', ctx=Load()),
                    Constant(value=True, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value="This is a modified version of Flask's send_file()\n\n    Sends the contents of a file to the client. This will use the\n    most efficient method available and configured.  By default it will\n    try to use the WSGI server's file_wrapper support.\n\n    By default it will try to guess the mimetype for you, but you can\n    also explicitly provide one.  For extra security you probably want\n    to send certain files as attachment (HTML for instance).  The mimetype\n    guessing requires a `filename` or an `attachment_filename` to be\n    provided.\n\n    Please never pass filenames to this function from user sources without\n    checking them first.\n\n    :param filepath_or_fp: the filename of the file to send.\n                           Alternatively a file object might be provided\n                           in which case `X-Sendfile` might not work and\n                           fall back to the traditional method.  Make sure\n                           that the file pointer is positioned at the start\n                           of data to send before calling :func:`send_file`.\n    :param mimetype: the mimetype of the file if provided, otherwise\n                     auto detection happens.\n    :param as_attachment: set to `True` if you want to send this file with\n                          a ``Content-Disposition: attachment`` header.\n    :param filename: the filename for the attachment if it differs from the file's filename or\n                     if using file object without 'name' attribute (eg: E-tags with StringIO).\n    :param mtime: last modification time to use for contitional response.\n    :param add_etags: set to `False` to disable attaching of etags.\n    :param conditional: set to `False` to disable conditional responses.\n\n    :param cache_timeout: the timeout in seconds for the headers.\n    ", kind=None),
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='filepath_or_fp', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='filename', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='filename', ctx=Store())],
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
                                        args=[Name(id='filepath_or_fp', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='file', ctx=Store())],
                            value=Call(
                                func=Name(id='open', ctx=Load()),
                                args=[
                                    Name(id='filepath_or_fp', ctx=Load()),
                                    Constant(value='rb', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='mtime', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='mtime', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='getmtime',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='filepath_or_fp', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='file', ctx=Store())],
                            value=Name(id='filepath_or_fp', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='filename', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='filename', ctx=Store())],
                                    value=Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='file', ctx=Load()),
                                            Constant(value='name', kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='file', ctx=Load()),
                            attr='seek',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value=0, kind=None),
                            Constant(value=2, kind=None),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='size', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='file', ctx=Load()),
                            attr='tell',
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
                            value=Name(id='file', ctx=Load()),
                            attr='seek',
                            ctx=Load(),
                        ),
                        args=[Constant(value=0, kind=None)],
                        keywords=[],
                    ),
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Name(id='mimetype', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            Name(id='filename', ctx=Load()),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='mimetypes', ctx=Load()),
                                        attr='guess_type',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='filename', ctx=Load())],
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
                If(
                    test=Compare(
                        left=Name(id='mimetype', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Constant(value='application/octet-stream', kind=None),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='headers', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='werkzeug', ctx=Load()),
                                attr='datastructures',
                                ctx=Load(),
                            ),
                            attr='Headers',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='as_attachment', ctx=Load()),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='filename', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='TypeError', ctx=Load()),
                                        args=[Constant(value='filename unavailable, required for sending as attachment', kind=None)],
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
                                    value=Name(id='headers', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Content-Disposition', kind=None),
                                    Constant(value='attachment', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='filename',
                                        value=Name(id='filename', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='headers', ctx=Load()),
                                    slice=Constant(value='Content-Length', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='size', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='data', ctx=Store())],
                    value=Call(
                        func=Name(id='wrap_file', ctx=Load()),
                        args=[
                            Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='httprequest',
                                    ctx=Load(),
                                ),
                                attr='environ',
                                ctx=Load(),
                            ),
                            Name(id='file', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rv', ctx=Store())],
                    value=Call(
                        func=Name(id='Response', ctx=Load()),
                        args=[Name(id='data', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='mimetype',
                                value=Name(id='mimetype', ctx=Load()),
                            ),
                            keyword(
                                arg='headers',
                                value=Name(id='headers', ctx=Load()),
                            ),
                            keyword(
                                arg='direct_passthrough',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='mtime', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='server_format', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='tools',
                                                ctx=Load(),
                                            ),
                                            attr='misc',
                                            ctx=Load(),
                                        ),
                                        attr='DEFAULT_SERVER_DATETIME_FORMAT',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='mtime', ctx=Store())],
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
                                            Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='mtime', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='.', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='server_format', ctx=Load()),
                                        ],
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
                                            targets=[Name(id='mtime', ctx=Store())],
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
                If(
                    test=Compare(
                        left=Name(id='mtime', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='rv', ctx=Load()),
                                    attr='last_modified',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='mtime', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Attribute(
                                value=Name(id='rv', ctx=Load()),
                                attr='cache_control',
                                ctx=Load(),
                            ),
                            attr='public',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                If(
                    test=Name(id='cache_timeout', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='rv', ctx=Load()),
                                        attr='cache_control',
                                        ctx=Load(),
                                    ),
                                    attr='max_age',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='cache_timeout', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='rv', ctx=Load()),
                                    attr='expires',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
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
                                        op=Add(),
                                        right=Name(id='cache_timeout', ctx=Load()),
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
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='add_etags', ctx=Load()),
                            Name(id='filename', ctx=Load()),
                            Name(id='mtime', ctx=Load()),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rv', ctx=Load()),
                                    attr='set_etag',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='odoo-%s-%s-%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='mtime', ctx=Load()),
                                                Name(id='size', ctx=Load()),
                                                BinOp(
                                                    left=Call(
                                                        func=Name(id='adler32', ctx=Load()),
                                                        args=[
                                                            IfExp(
                                                                test=Call(
                                                                    func=Name(id='isinstance', ctx=Load()),
                                                                    args=[
                                                                        Name(id='filename', ctx=Load()),
                                                                        Name(id='str', ctx=Load()),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                body=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='filename', ctx=Load()),
                                                                        attr='encode',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='utf-8', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                orelse=Name(id='filename', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    op=BitAnd(),
                                                    right=Constant(value=4294967295, kind=None),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='conditional', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='rv', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rv', ctx=Load()),
                                            attr='make_conditional',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='httprequest',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='rv', ctx=Load()),
                                            attr='status_code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=304, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='rv', ctx=Load()),
                                                        attr='headers',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='x-sendfile', kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
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
                Return(
                    value=Name(id='rv', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='content_disposition',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='filename', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='filename', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='tools',
                                ctx=Load(),
                            ),
                            attr='ustr',
                            ctx=Load(),
                        ),
                        args=[Name(id='filename', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='escaped', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='urls', ctx=Load()),
                            attr='url_quote',
                            ctx=Load(),
                        ),
                        args=[Name(id='filename', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='safe',
                                value=Constant(value='', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=BinOp(
                        left=Constant(value="attachment; filename*=UTF-8''%s", kind=None),
                        op=Mod(),
                        right=Name(id='escaped', ctx=Load()),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='set_safe_image_headers',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='headers', annotation=None, type_comment=None),
                    arg(arg='content', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Return new headers based on `headers` but with `Content-Length` and\n    `Content-Type` set appropriately depending on the given `content` only if it\n    is safe to do, as well as `X-Content-Type-Options: nosniff` so that if the\n    file is of an unsafe type, it is not interpreted as that type if the\n    `Content-type` header was already set to a different mimetype', kind=None),
                ),
                Assign(
                    targets=[Name(id='content_type', ctx=Store())],
                    value=Call(
                        func=Name(id='guess_mimetype', ctx=Load()),
                        args=[Name(id='content', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='safe_types', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='image/jpeg', kind=None),
                            Constant(value='image/png', kind=None),
                            Constant(value='image/gif', kind=None),
                            Constant(value='image/x-icon', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='content_type', ctx=Load()),
                        ops=[In()],
                        comparators=[Name(id='safe_types', ctx=Load())],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='headers', ctx=Store())],
                            value=Call(
                                func=Name(id='set_header_field', ctx=Load()),
                                args=[
                                    Name(id='headers', ctx=Load()),
                                    Constant(value='Content-Type', kind=None),
                                    Name(id='content_type', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='headers', ctx=Store())],
                    value=Call(
                        func=Name(id='set_header_field', ctx=Load()),
                        args=[
                            Name(id='headers', ctx=Load()),
                            Constant(value='X-Content-Type-Options', kind=None),
                            Constant(value='nosniff', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='set_header_field', ctx=Load()),
                        args=[
                            Name(id='headers', ctx=Load()),
                            Constant(value='Content-Length', kind=None),
                            Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='content', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Name(id='headers', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='set_header_field',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='headers', annotation=None, type_comment=None),
                    arg(arg='name', annotation=None, type_comment=None),
                    arg(arg='value', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return new headers based on `headers` but with `value` set for the\n    header field `name`.\n\n    :param headers: the existing headers\n    :type headers: list of tuples (name, value)\n\n    :param name: the header field name\n    :type name: string\n\n    :param value: the value to set for the `name` header\n    :type value: string\n\n    :return: the updated headers\n    :rtype: list of tuples (name, value)\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='dictheaders', ctx=Store())],
                    value=Call(
                        func=Name(id='dict', ctx=Load()),
                        args=[Name(id='headers', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Subscript(
                            value=Name(id='dictheaders', ctx=Load()),
                            slice=Name(id='name', ctx=Load()),
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='value', ctx=Load()),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='list', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='dictheaders', ctx=Load()),
                                    attr='items',
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
        Assign(
            targets=[Name(id='root', ctx=Store())],
            value=Call(
                func=Name(id='Root', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
