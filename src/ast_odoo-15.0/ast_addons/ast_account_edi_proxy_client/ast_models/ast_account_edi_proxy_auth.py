Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='hashlib', asname=None)],
        ),
        Import(
            names=[alias(name='hmac', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.urls', asname=None)],
        ),
        ClassDef(
            name='OdooEdiProxyAuth',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='requests', ctx=Load()),
                        attr='auth',
                        ctx=Load(),
                    ),
                    attr='AuthBase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' For routes that needs to be authenticated and verified for access.\n        Allows:\n        1) to preserve the integrity of the message between the endpoints.\n        2) to check user access rights and account validity\n        3) to avoid that multiple database use the same credentials, via a refresh_token that expire after 24h.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='id_client',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='user', ctx=Load()),
                                            Attribute(
                                                value=Name(id='user', ctx=Load()),
                                                attr='id_client',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='refresh_token',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='user', ctx=Load()),
                                            Attribute(
                                                value=Name(id='user', ctx=Load()),
                                                attr='refresh_token',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Constant(value=False, kind=None),
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
                    name='__call__',
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
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id_client',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='refresh_token',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Name(id='request', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='msg_timestamp', ctx=Store())],
                            value=Call(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='parsed_url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='werkzeug', ctx=Load()),
                                        attr='urls',
                                        ctx=Load(),
                                    ),
                                    attr='url_parse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='path_url',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Attribute(
                                value=Name(id='request', ctx=Load()),
                                attr='body',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='body', ctx=Load()),
                                    Name(id='bytes', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='body', ctx=Load()),
                                            attr='decode',
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
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='loads',
                                    ctx=Load(),
                                ),
                                args=[Name(id='body', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='message', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%s|%s|%s|%s|%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='msg_timestamp', ctx=Load()),
                                        Attribute(
                                            value=Name(id='parsed_url', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id_client',
                                            ctx=Load(),
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='dumps',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='werkzeug', ctx=Load()),
                                                            attr='urls',
                                                            ctx=Load(),
                                                        ),
                                                        attr='url_decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='parsed_url', ctx=Load()),
                                                            attr='query',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='sort_keys',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='dumps',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='body', ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='sort_keys',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='h', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='hmac', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='base64', ctx=Load()),
                                            attr='b64decode',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='refresh_token',
                                                ctx=Load(),
                                            ),
                                        ],
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
                                ],
                                keywords=[
                                    keyword(
                                        arg='digestmod',
                                        value=Attribute(
                                            value=Name(id='hashlib', ctx=Load()),
                                            attr='sha256',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='headers',
                                        ctx=Load(),
                                    ),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='odoo-edi-client-id', kind=None),
                                            Constant(value='odoo-edi-signature', kind=None),
                                            Constant(value='odoo-edi-timestamp', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id_client',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='h', ctx=Load()),
                                                    attr='hexdigest',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Name(id='msg_timestamp', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='request', ctx=Load()),
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
