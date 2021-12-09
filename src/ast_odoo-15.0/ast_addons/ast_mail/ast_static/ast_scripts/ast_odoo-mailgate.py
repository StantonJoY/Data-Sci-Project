Module(
    body=[
        Import(
            names=[alias(name='optparse', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='traceback', asname=None)],
        ),
        Import(
            names=[alias(name='xmlrpclib', asname=None)],
        ),
        FunctionDef(
            name='main',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='op', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='optparse', ctx=Load()),
                            attr='OptionParser',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='usage',
                                value=Constant(value='usage: %prog [options]', kind=None),
                            ),
                            keyword(
                                arg='version',
                                value=Constant(value='%prog v1.2', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='op', ctx=Load()),
                            attr='add_option',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='-d', kind=None),
                            Constant(value='--database', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='dest',
                                value=Constant(value='database', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Odoo database name (default: %default)', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='odoo', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='op', ctx=Load()),
                            attr='add_option',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='-u', kind=None),
                            Constant(value='--userid', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='dest',
                                value=Constant(value='userid', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Odoo user id to connect with (default: %default)', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=1, kind=None),
                            ),
                            keyword(
                                arg='type',
                                value=Name(id='int', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='op', ctx=Load()),
                            attr='add_option',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='-p', kind=None),
                            Constant(value='--password', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='dest',
                                value=Constant(value='password', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Odoo user password (default: %default)', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='admin', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='op', ctx=Load()),
                            attr='add_option',
                            ctx=Load(),
                        ),
                        args=[Constant(value='--host', kind=None)],
                        keywords=[
                            keyword(
                                arg='dest',
                                value=Constant(value='host', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Odoo host (default: %default)', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='localhost', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='op', ctx=Load()),
                            attr='add_option',
                            ctx=Load(),
                        ),
                        args=[Constant(value='--port', kind=None)],
                        keywords=[
                            keyword(
                                arg='dest',
                                value=Constant(value='port', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Odoo port (default: %default)', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=8069, kind=None),
                            ),
                            keyword(
                                arg='type',
                                value=Name(id='int', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='o', ctx=Store()),
                                Name(id='args', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Attribute(
                            value=Name(id='op', ctx=Load()),
                            attr='parse_args',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=Call(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='models', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='xmlrpclib', ctx=Load()),
                                    attr='ServerProxy',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='http://%s:%s/xmlrpc/2/object', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='o', ctx=Load()),
                                                    attr='host',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='o', ctx=Load()),
                                                    attr='port',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='allow_none',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='models', ctx=Load()),
                                    attr='execute_kw',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='o', ctx=Load()),
                                        attr='database',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='o', ctx=Load()),
                                        attr='userid',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='o', ctx=Load()),
                                        attr='password',
                                        ctx=Load(),
                                    ),
                                    Constant(value='mail.thread', kind=None),
                                    Constant(value='message_process', kind=None),
                                    List(
                                        elts=[
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='xmlrpclib', ctx=Load()),
                                                    attr='Binary',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='msg', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Attribute(
                                value=Name(id='xmlrpclib', ctx=Load()),
                                attr='Fault',
                                ctx=Load(),
                            ),
                            name='e',
                            body=[
                                Assign(
                                    targets=[Name(id='err', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='xmlrpclib.Fault: %s\n%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='faultCode',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='faultString',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
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
                                        args=[Name(id='err', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name='e',
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='traceback', ctx=Load()),
                                            attr='print_exc',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Name(id='sys', ctx=Load()),
                                                attr='stderr',
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
                                        args=[Constant(value=2, kind=None)],
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
        If(
            test=Compare(
                left=Name(id='__name__', ctx=Load()),
                ops=[Eq()],
                comparators=[Constant(value='__main__', kind=None)],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Name(id='main', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                ),
            ],
            orelse=[],
        ),
    ],
    type_ignores=[],
)
