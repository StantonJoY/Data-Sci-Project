Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='account_edi_proxy_auth',
            names=[alias(name='OdooEdiProxyAuth', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='cryptography.hazmat.backends',
            names=[alias(name='default_backend', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='cryptography.hazmat.primitives.asymmetric',
            names=[alias(name='rsa', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='cryptography.hazmat.primitives',
            names=[alias(name='serialization', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='cryptography.hazmat.primitives',
            names=[alias(name='hashes', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='cryptography.hazmat.primitives.asymmetric',
            names=[alias(name='padding', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='cryptography.fernet',
            names=[alias(name='Fernet', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        Import(
            names=[alias(name='uuid', asname=None)],
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
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
            targets=[Name(id='DEFAULT_SERVER_URL', ctx=Store())],
            value=Constant(value='https://l10n-it-edi.api.odoo.com', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TIMEOUT', ctx=Store())],
            value=Constant(value=30, kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='AccountEdiProxyError',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
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
                                    attr='code',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='code', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='message',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='message', ctx=Load()),
                            type_comment=None,
                        ),
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
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='message', ctx=Load()),
                                            Name(id='code', ctx=Load()),
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
            decorator_list=[],
        ),
        ClassDef(
            name='AccountEdiProxyClientUser',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Represents a user of the proxy for an electronic invoicing format.\n    An edi_proxy_user has a unique identification on a specific format (for example, the vat for Peppol) which\n    allows to identify him when receiving a document addressed to him. It is linked to a specific company on a specific\n    Odoo database.\n    It also owns a key with which each file should be decrypted with (the proxy encrypt all the files with the public key).\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='account_edi_proxy_client.user', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Account EDI proxy user', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='active', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='id_client', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='edi_format_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.edi.format', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='edi_format_code', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='edi_format_id.code', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='edi_identification', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The unique id that identifies this user for on the edi format, typically the vat', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='private_key', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='attachment',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_system', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="The key to encrypt all the user's data", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='refresh_token', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_system', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='unique_id_client', kind=None),
                                    Constant(value='unique(id_client)', kind=None),
                                    Constant(value='This id_client is already used on another user.', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                elts=[
                                    Constant(value='unique_edi_identification_per_format', kind=None),
                                    Constant(value='unique(edi_identification, edi_format_id)', kind=None),
                                    Constant(value='This edi identification is already assigned to a user', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_make_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Make a request to proxy and handle the generic elements of the reponse (errors, new refresh token).\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='payload', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='jsonrpc', kind=None),
                                    Constant(value='method', kind=None),
                                    Constant(value='params', kind=None),
                                    Constant(value='id', kind=None),
                                ],
                                values=[
                                    Constant(value='2.0', kind=None),
                                    Constant(value='call', kind=None),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='params', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
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
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
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
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account_edi_proxy_client.demo', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[Constant(value="Can't access the proxy in demo mode", kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='requests', ctx=Load()),
                                                    attr='post',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='url', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='json',
                                                        value=Name(id='payload', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='timeout',
                                                        value=Name(id='TIMEOUT', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='headers',
                                                        value=Dict(
                                                            keys=[Constant(value='content-type', kind=None)],
                                                            values=[Constant(value='application/json', kind=None)],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='auth',
                                                        value=Call(
                                                            func=Name(id='OdooEdiProxyAuth', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='user',
                                                                    value=Name(id='self', ctx=Load()),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            attr='json',
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
                                    type=Tuple(
                                        elts=[
                                            Name(id='ValueError', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='requests', ctx=Load()),
                                                    attr='exceptions',
                                                    ctx=Load(),
                                                ),
                                                attr='ConnectionError',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='requests', ctx=Load()),
                                                    attr='exceptions',
                                                    ctx=Load(),
                                                ),
                                                attr='MissingSchema',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='requests', ctx=Load()),
                                                    attr='exceptions',
                                                    ctx=Load(),
                                                ),
                                                attr='Timeout',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='requests', ctx=Load()),
                                                    attr='exceptions',
                                                    ctx=Load(),
                                                ),
                                                attr='HTTPError',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='AccountEdiProxyError', ctx=Load()),
                                                args=[
                                                    Constant(value='connection_error', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='The url that this service requested returned an error. The url it tried to contact was %s', kind=None),
                                                            Name(id='url', ctx=Load()),
                                                        ],
                                                        keywords=[],
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
                        If(
                            test=Compare(
                                left=Constant(value='error', kind=None),
                                ops=[In()],
                                comparators=[Name(id='response', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='message', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='The url that this service requested returned an error. The url it tried to contact was %s. %s', kind=None),
                                            Name(id='url', ctx=Load()),
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='response', ctx=Load()),
                                                    slice=Constant(value='error', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='message', kind=None),
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
                                            value=Subscript(
                                                value=Name(id='response', ctx=Load()),
                                                slice=Constant(value='error', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='code', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=404, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='message', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='The url that this service does not exist. The url it tried to contact was %s', kind=None),
                                                    Name(id='url', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccountEdiProxyError', ctx=Load()),
                                        args=[
                                            Constant(value='connection_error', kind=None),
                                            Name(id='message', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='proxy_error', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='response', ctx=Load()),
                                        slice=Constant(value='result', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='proxy_error', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='proxy_error', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='error_code', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='proxy_error', ctx=Load()),
                                        slice=Constant(value='code', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='error_code', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='refresh_token_expired', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_renew_token',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_make_request',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='url', ctx=Load()),
                                                    Name(id='params', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='error_code', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='no_such_user', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='active',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccountEdiProxyError', ctx=Load()),
                                        args=[
                                            Name(id='error_code', ctx=Load()),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='proxy_error', ctx=Load()),
                                                        slice=Constant(value='message', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
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
                            value=Subscript(
                                value=Name(id='response', ctx=Load()),
                                slice=Constant(value='result', kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_register_proxy_user',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                            arg(arg='edi_format', annotation=None, type_comment=None),
                            arg(arg='edi_identification', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Generate the public_key/private_key that will be used to encrypt the file, send a request to the proxy\n        to register the user with the public key and create the user with the private key.\n\n        :param company: the company of the user.\n        :param edi_identification: The unique ID that identifies this user on this edi network and to which the files will be addressed.\n                                   Typically the vat.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='private_key', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rsa', ctx=Load()),
                                    attr='generate_private_key',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='public_exponent',
                                        value=Constant(value=65537, kind=None),
                                    ),
                                    keyword(
                                        arg='key_size',
                                        value=Constant(value=2048, kind=None),
                                    ),
                                    keyword(
                                        arg='backend',
                                        value=Call(
                                            func=Name(id='default_backend', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='private_pem', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='private_key', ctx=Load()),
                                    attr='private_bytes',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='encoding',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='serialization', ctx=Load()),
                                                attr='Encoding',
                                                ctx=Load(),
                                            ),
                                            attr='PEM',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='format',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='serialization', ctx=Load()),
                                                attr='PrivateFormat',
                                                ctx=Load(),
                                            ),
                                            attr='PKCS8',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='encryption_algorithm',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='serialization', ctx=Load()),
                                                attr='NoEncryption',
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
                        Assign(
                            targets=[Name(id='public_key', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='private_key', ctx=Load()),
                                    attr='public_key',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='public_pem', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='public_key', ctx=Load()),
                                    attr='public_bytes',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='encoding',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='serialization', ctx=Load()),
                                                attr='Encoding',
                                                ctx=Load(),
                                            ),
                                            attr='PEM',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='format',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='serialization', ctx=Load()),
                                                attr='PublicFormat',
                                                ctx=Load(),
                                            ),
                                            attr='SubjectPublicKeyInfo',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
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
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account_edi_proxy_client.demo', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='id_client', kind=None),
                                            Constant(value='refresh_token', kind=None),
                                        ],
                                        values=[
                                            Constant(value='demo', kind=None),
                                            Constant(value='demo', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='server_url', ctx=Store())],
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
                                                    attr='get_param',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='account_edi_proxy_client.edi_server_url', kind=None),
                                                    Name(id='DEFAULT_SERVER_URL', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='response', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_make_request',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='server_url', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value='/iap/account_edi/1/create_user', kind=None),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='params',
                                                        value=Dict(
                                                            keys=[
                                                                Constant(value='dbuuid', kind=None),
                                                                Constant(value='company_id', kind=None),
                                                                Constant(value='edi_format_code', kind=None),
                                                                Constant(value='edi_identification', kind=None),
                                                                Constant(value='public_key', kind=None),
                                                            ],
                                                            values=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='company', ctx=Load()),
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='ir.config_parameter', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='get_param',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='database.uuid', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='company', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='edi_format', ctx=Load()),
                                                                    attr='code',
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='edi_identification', ctx=Load()),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='base64', ctx=Load()),
                                                                                attr='b64encode',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='public_pem', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='decode',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='AccountEdiProxyError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='e', ctx=Load()),
                                                                attr='message',
                                                                ctx=Load(),
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
                                If(
                                    test=Compare(
                                        left=Constant(value='error', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='response', ctx=Load())],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='response', ctx=Load()),
                                                        slice=Constant(value='error', kind=None),
                                                        ctx=Load(),
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='id_client', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='edi_format_id', kind=None),
                                            Constant(value='edi_identification', kind=None),
                                            Constant(value='private_key', kind=None),
                                            Constant(value='refresh_token', kind=None),
                                        ],
                                        values=[
                                            Subscript(
                                                value=Name(id='response', ctx=Load()),
                                                slice=Constant(value='id_client', kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='edi_format', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='edi_identification', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='b64encode',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='private_pem', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Subscript(
                                                value=Name(id='response', ctx=Load()),
                                                slice=Constant(value='refresh_token', kind=None),
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
                    name='_renew_token',
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
                            value=Constant(value=' Request the proxy for a new refresh token.\n\n        Request to the proxy should be made with a refresh token that expire after 24h to avoid\n        that multiple database use the same credentials. When receiving an error for an expired refresh_token,\n        This method makes a request to get a new refresh token.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='server_url', ctx=Store())],
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
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account_edi_proxy_client.edi_server_url', kind=None),
                                    Name(id='DEFAULT_SERVER_URL', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='server_url', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value='/iap/account_edi/1/renew_token', kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='error', kind=None),
                                ops=[In()],
                                comparators=[Name(id='response', ctx=Load())],
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
                                            Subscript(
                                                value=Name(id='response', ctx=Load()),
                                                slice=Constant(value='error', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[Constant(value='Proxy error, please contact Odoo (code: 3)', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='refresh_token',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='response', ctx=Load()),
                                slice=Constant(value='refresh_token', kind=None),
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
                    name='_decrypt_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='symmetric_key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Decrypt the data. Note that the data is encrypted with a symmetric key, which is encrypted with an asymmetric key.\n        We must therefore decrypt the symmetric key.\n\n        :param data:            The data to decrypt.\n        :param symmetric_key:   The symmetric_key encrypted with self.private_key.public_key()\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='private_key', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='serialization', ctx=Load()),
                                    attr='load_pem_private_key',
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
                                                attr='private_key',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='password',
                                        value=Constant(value=None, kind=None),
                                    ),
                                    keyword(
                                        arg='backend',
                                        value=Call(
                                            func=Name(id='default_backend', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='key', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='private_key', ctx=Load()),
                                    attr='decrypt',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='base64', ctx=Load()),
                                            attr='b64decode',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='symmetric_key', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='padding', ctx=Load()),
                                            attr='OAEP',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='mgf',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='padding', ctx=Load()),
                                                        attr='MGF1',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='algorithm',
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='hashes', ctx=Load()),
                                                                    attr='SHA256',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            keyword(
                                                arg='algorithm',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='hashes', ctx=Load()),
                                                        attr='SHA256',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='label',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='f', ctx=Store())],
                            value=Call(
                                func=Name(id='Fernet', ctx=Load()),
                                args=[Name(id='key', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='f', ctx=Load()),
                                    attr='decrypt',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='base64', ctx=Load()),
                                            attr='b64decode',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='data', ctx=Load())],
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
    ],
    type_ignores=[],
)
