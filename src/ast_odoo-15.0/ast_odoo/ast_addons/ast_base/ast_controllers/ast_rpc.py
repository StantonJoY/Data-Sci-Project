Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='xmlrpc.client', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='date', asname=None),
                alias(name='datetime', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='xmlrpc.client',
            names=[
                alias(name='dumps', asname=None),
                alias(name='loads', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='markupsafe',
            names=[alias(name='Markup', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.wrappers',
            names=[alias(name='Response', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[
                alias(name='Controller', asname=None),
                alias(name='dispatch_rpc', asname=None),
                alias(name='request', asname=None),
                alias(name='route', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.service',
            names=[alias(name='wsgi_server', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.fields',
            names=[
                alias(name='Date', asname=None),
                alias(name='Datetime', asname=None),
                alias(name='Command', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='lazy', asname=None),
                alias(name='ustr', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='frozendict', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='XML_INVALID', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value=b'[\x00-\x08\x0b\x0c\x0f-\x1f]', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='OdooMarshaller',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='xmlrpc', ctx=Load()),
                        attr='client',
                        ctx=Load(),
                    ),
                    attr='Marshaller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='dispatch', ctx=Store())],
                    value=Call(
                        func=Name(id='dict', ctx=Load()),
                        args=[
                            Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='xmlrpc', ctx=Load()),
                                        attr='client',
                                        ctx=Load(),
                                    ),
                                    attr='Marshaller',
                                    ctx=Load(),
                                ),
                                attr='dispatch',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='dump_frozen_dict',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='write', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dump_struct',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='value', ctx=Load()),
                                    Name(id='write', ctx=Load()),
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
                        Subscript(
                            value=Name(id='dispatch', ctx=Load()),
                            slice=Name(id='frozendict', ctx=Load()),
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='dump_frozen_dict', ctx=Load()),
                    type_comment=None,
                ),
                FunctionDef(
                    name='dump_bytes',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='write', annotation=None, type_comment=None),
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
                                func=Attribute(
                                    value=Name(id='XML_INVALID', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='dump_unicode',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='', kind=None),
                                            Name(id='write', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='dump_unicode',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='ustr', ctx=Load()),
                                                args=[Name(id='value', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Name(id='write', ctx=Load()),
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
                Assign(
                    targets=[
                        Subscript(
                            value=Name(id='dispatch', ctx=Load()),
                            slice=Name(id='bytes', ctx=Load()),
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='dump_bytes', ctx=Load()),
                    type_comment=None,
                ),
                FunctionDef(
                    name='dump_datetime',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='write', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Datetime', ctx=Load()),
                                    attr='to_string',
                                    ctx=Load(),
                                ),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dump_unicode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='value', ctx=Load()),
                                    Name(id='write', ctx=Load()),
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
                        Subscript(
                            value=Name(id='dispatch', ctx=Load()),
                            slice=Name(id='datetime', ctx=Load()),
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='dump_datetime', ctx=Load()),
                    type_comment=None,
                ),
                FunctionDef(
                    name='dump_date',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='write', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Date', ctx=Load()),
                                    attr='to_string',
                                    ctx=Load(),
                                ),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dump_unicode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='value', ctx=Load()),
                                    Name(id='write', ctx=Load()),
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
                        Subscript(
                            value=Name(id='dispatch', ctx=Load()),
                            slice=Name(id='date', ctx=Load()),
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='dump_date', ctx=Load()),
                    type_comment=None,
                ),
                FunctionDef(
                    name='dump_lazy',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='write', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='v', ctx=Store())],
                            value=Attribute(
                                value=Name(id='value', ctx=Load()),
                                attr='_value',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dispatch',
                                        ctx=Load(),
                                    ),
                                    slice=Call(
                                        func=Name(id='type', ctx=Load()),
                                        args=[Name(id='v', ctx=Load())],
                                        keywords=[],
                                    ),
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='v', ctx=Load()),
                                    Name(id='write', ctx=Load()),
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
                        Subscript(
                            value=Name(id='dispatch', ctx=Load()),
                            slice=Name(id='lazy', ctx=Load()),
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='dump_lazy', ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Subscript(
                            value=Name(id='dispatch', ctx=Load()),
                            slice=Name(id='Command', ctx=Load()),
                            ctx=Store(),
                        ),
                    ],
                    value=Subscript(
                        value=Name(id='dispatch', ctx=Load()),
                        slice=Name(id='int', ctx=Load()),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Subscript(
                            value=Name(id='dispatch', ctx=Load()),
                            slice=Name(id='Markup', ctx=Load()),
                            ctx=Store(),
                        ),
                    ],
                    value=Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[
                                arg(arg='self', annotation=None, type_comment=None),
                                arg(arg='value', annotation=None, type_comment=None),
                                arg(arg='write', annotation=None, type_comment=None),
                            ],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=Call(
                            func=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dispatch',
                                    ctx=Load(),
                                ),
                                slice=Name(id='str', ctx=Load()),
                                ctx=Load(),
                            ),
                            args=[
                                Name(id='self', ctx=Load()),
                                Call(
                                    func=Name(id='str', ctx=Load()),
                                    args=[Name(id='value', ctx=Load())],
                                    keywords=[],
                                ),
                                Name(id='write', ctx=Load()),
                            ],
                            keywords=[],
                        ),
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[
                Attribute(
                    value=Attribute(
                        value=Name(id='xmlrpc', ctx=Load()),
                        attr='client',
                        ctx=Load(),
                    ),
                    attr='Marshaller',
                    ctx=Store(),
                ),
            ],
            value=Name(id='OdooMarshaller', ctx=Load()),
            type_comment=None,
        ),
        ClassDef(
            name='RPC',
            bases=[Name(id='Controller', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Handle RPC connections.', kind=None),
                ),
                FunctionDef(
                    name='_xmlrpc',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='service', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Common method to handle an XML-RPC request.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='httprequest',
                                        ctx=Load(),
                                    ),
                                    attr='get_data',
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
                                        Name(id='params', ctx=Store()),
                                        Name(id='method', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='loads', ctx=Load()),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='dispatch_rpc', ctx=Load()),
                                args=[
                                    Name(id='service', ctx=Load()),
                                    Name(id='method', ctx=Load()),
                                    Name(id='params', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='dumps', ctx=Load()),
                                args=[
                                    Tuple(
                                        elts=[Name(id='result', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='methodresponse',
                                        value=Constant(value=1, kind=None),
                                    ),
                                    keyword(
                                        arg='allow_none',
                                        value=Constant(value=False, kind=None),
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
                    name='xmlrpc_1',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='service', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='XML-RPC service that returns faultCode as strings.\n\n        This entrypoint is historical and non-compliant, but kept for\n        backwards-compatibility.\n        ', kind=None),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_xmlrpc',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='service', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='error',
                                    body=[
                                        Assign(
                                            targets=[Name(id='response', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='wsgi_server', ctx=Load()),
                                                    attr='xmlrpc_handle_exception_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='error', ctx=Load())],
                                                keywords=[],
                                            ),
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
                                func=Name(id='Response', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='response',
                                        value=Name(id='response', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='mimetype',
                                        value=Constant(value='text/xml', kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[Constant(value='/xmlrpc/<service>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                                keyword(
                                    arg='save_session',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='xmlrpc_2',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='service', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='XML-RPC service that returns faultCode as int.', kind=None),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_xmlrpc',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='service', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='error',
                                    body=[
                                        Assign(
                                            targets=[Name(id='response', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='wsgi_server', ctx=Load()),
                                                    attr='xmlrpc_handle_exception_int',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='error', ctx=Load())],
                                                keywords=[],
                                            ),
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
                                func=Name(id='Response', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='response',
                                        value=Name(id='response', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='mimetype',
                                        value=Constant(value='text/xml', kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[Constant(value='/xmlrpc/2/<service>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                                keyword(
                                    arg='save_session',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='jsonrpc',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='service', annotation=None, type_comment=None),
                            arg(arg='method', annotation=None, type_comment=None),
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
                            value=Constant(value=' Method used by client APIs to contact OpenERP. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='dispatch_rpc', ctx=Load()),
                                args=[
                                    Name(id='service', ctx=Load()),
                                    Name(id='method', ctx=Load()),
                                    Name(id='args', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[Constant(value='/jsonrpc', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='save_session',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
