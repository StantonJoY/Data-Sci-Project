Module(
    body=[
        Expr(
            value=Constant(value='\n\nWSGI stack, common code.\n\n', kind=None),
        ),
        Import(
            names=[alias(name='logging', asname=None)],
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
        ImportFrom(
            module='xmlrpc',
            names=[alias(name='client', asname='xmlrpclib')],
            level=0,
        ),
        Import(
            names=[alias(name='werkzeug.exceptions', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.wrappers', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.serving', asname=None)],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='config', asname=None)],
            level=0,
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
            targets=[Name(id='RPC_FAULT_CODE_CLIENT_ERROR', ctx=Store())],
            value=Constant(value=1, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='RPC_FAULT_CODE_APPLICATION_ERROR', ctx=Store())],
            value=Constant(value=1, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='RPC_FAULT_CODE_WARNING', ctx=Store())],
            value=Constant(value=2, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='RPC_FAULT_CODE_ACCESS_DENIED', ctx=Store())],
            value=Constant(value=3, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='RPC_FAULT_CODE_ACCESS_ERROR', ctx=Store())],
            value=Constant(value=4, kind=None),
            type_comment=None,
        ),
        FunctionDef(
            name='xmlrpc_handle_exception_int',
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
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='e', ctx=Load()),
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
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='fault', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='xmlrpclib', ctx=Load()),
                                    attr='Fault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='RPC_FAULT_CODE_WARNING', ctx=Load()),
                                    Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[Name(id='e', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='e', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='AccessError',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fault', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='xmlrpclib', ctx=Load()),
                                            attr='Fault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='RPC_FAULT_CODE_ACCESS_ERROR', ctx=Load()),
                                            Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='e', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='e', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='exceptions',
                                                    ctx=Load(),
                                                ),
                                                attr='AccessDenied',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='fault', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='xmlrpclib', ctx=Load()),
                                                    attr='Fault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='RPC_FAULT_CODE_ACCESS_DENIED', ctx=Load()),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='e', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='odoo', ctx=Load()),
                                                            attr='exceptions',
                                                            ctx=Load(),
                                                        ),
                                                        attr='UserError',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='fault', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='xmlrpclib', ctx=Load()),
                                                            attr='Fault',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='RPC_FAULT_CODE_WARNING', ctx=Load()),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='e', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='info', ctx=Store())],
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
                                                Assign(
                                                    targets=[Name(id='formatted_info', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Constant(value='', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='traceback', ctx=Load()),
                                                                    attr='format_exception',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Starred(
                                                                        value=Name(id='info', ctx=Load()),
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
                                                Assign(
                                                    targets=[Name(id='fault', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='xmlrpclib', ctx=Load()),
                                                            attr='Fault',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='RPC_FAULT_CODE_APPLICATION_ERROR', ctx=Load()),
                                                            Name(id='formatted_info', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='xmlrpclib', ctx=Load()),
                            attr='dumps',
                            ctx=Load(),
                        ),
                        args=[Name(id='fault', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='allow_none',
                                value=Constant(value=None, kind=None),
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
            name='xmlrpc_handle_exception_string',
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
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='e', ctx=Load()),
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
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='fault', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='xmlrpclib', ctx=Load()),
                                    attr='Fault',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='warning -- Warning\n\n', kind=None),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[Name(id='e', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='e', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='MissingError',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fault', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='xmlrpclib', ctx=Load()),
                                            attr='Fault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='warning -- MissingError\n\n', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Name(id='e', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='e', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='exceptions',
                                                    ctx=Load(),
                                                ),
                                                attr='AccessError',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='fault', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='xmlrpclib', ctx=Load()),
                                                    attr='Fault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='warning -- AccessError\n\n', kind=None),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[Name(id='e', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='e', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='odoo', ctx=Load()),
                                                            attr='exceptions',
                                                            ctx=Load(),
                                                        ),
                                                        attr='AccessDenied',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='fault', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='xmlrpclib', ctx=Load()),
                                                            attr='Fault',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='AccessDenied', kind=None),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='e', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='e', ctx=Load()),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='odoo', ctx=Load()),
                                                                    attr='exceptions',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='UserError',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='fault', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='xmlrpclib', ctx=Load()),
                                                                    attr='Fault',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Constant(value='warning -- UserError\n\n', kind=None),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='str', ctx=Load()),
                                                                            args=[Name(id='e', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    Constant(value='', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='info', ctx=Store())],
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
                                                        Assign(
                                                            targets=[Name(id='formatted_info', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Constant(value='', kind=None),
                                                                    attr='join',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='traceback', ctx=Load()),
                                                                            attr='format_exception',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Starred(
                                                                                value=Name(id='info', ctx=Load()),
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
                                                        Assign(
                                                            targets=[Name(id='fault', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='xmlrpclib', ctx=Load()),
                                                                    attr='Fault',
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
                                                                    Name(id='formatted_info', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
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
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='xmlrpclib', ctx=Load()),
                            attr='dumps',
                            ctx=Load(),
                        ),
                        args=[Name(id='fault', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='allow_none',
                                value=Constant(value=None, kind=None),
                            ),
                            keyword(
                                arg='encoding',
                                value=Constant(value=None, kind=None),
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
            name='application_unproxied',
            args=arguments(
                posonlyargs=[],
                args=[
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
                    value=Constant(value=' WSGI entry point.', kind=None),
                ),
                If(
                    test=Call(
                        func=Name(id='hasattr', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='current_thread',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            Constant(value='uid', kind=None),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Delete(
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
                                    ctx=Del(),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='hasattr', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='current_thread',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            Constant(value='dbname', kind=None),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Delete(
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
                                    ctx=Del(),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='hasattr', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='current_thread',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            Constant(value='url', kind=None),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Delete(
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
                                    attr='url',
                                    ctx=Del(),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='http',
                                ctx=Load(),
                            ),
                            attr='root',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='environ', ctx=Load()),
                            Name(id='start_response', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='result', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Call(
                            func=Attribute(
                                value=Attribute(
                                    value=Name(id='werkzeug', ctx=Load()),
                                    attr='exceptions',
                                    ctx=Load(),
                                ),
                                attr='NotFound',
                                ctx=Load(),
                            ),
                            args=[Constant(value='No handler found.\n', kind=None)],
                            keywords=[],
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
        Try(
            body=[
                ImportFrom(
                    module='werkzeug.middleware.proxy_fix',
                    names=[alias(name='ProxyFix', asname='ProxyFix_')],
                    level=0,
                ),
                Assign(
                    targets=[Name(id='ProxyFix', ctx=Store())],
                    value=Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='app', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=Call(
                            func=Name(id='ProxyFix_', ctx=Load()),
                            args=[Name(id='app', ctx=Load())],
                            keywords=[
                                keyword(
                                    arg='x_for',
                                    value=Constant(value=1, kind=None),
                                ),
                                keyword(
                                    arg='x_proto',
                                    value=Constant(value=1, kind=None),
                                ),
                                keyword(
                                    arg='x_host',
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                        ),
                    ),
                    type_comment=None,
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        ImportFrom(
                            module='werkzeug.contrib.fixers',
                            names=[alias(name='ProxyFix', asname=None)],
                            level=0,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        FunctionDef(
            name='application',
            args=arguments(
                posonlyargs=[],
                args=[
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
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='proxy_mode', kind=None),
                                ctx=Load(),
                            ),
                            Compare(
                                left=Constant(value='HTTP_X_FORWARDED_HOST', kind=None),
                                ops=[In()],
                                comparators=[Name(id='environ', ctx=Load())],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Call(
                                    func=Name(id='ProxyFix', ctx=Load()),
                                    args=[Name(id='application_unproxied', ctx=Load())],
                                    keywords=[],
                                ),
                                args=[
                                    Name(id='environ', ctx=Load()),
                                    Name(id='start_response', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[
                        Return(
                            value=Call(
                                func=Name(id='application_unproxied', ctx=Load()),
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
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
