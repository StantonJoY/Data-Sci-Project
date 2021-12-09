Module(
    body=[
        ImportFrom(
            module='email.message',
            names=[alias(name='EmailMessage', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='email.utils',
            names=[alias(name='make_msgid', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='email', asname=None)],
        ),
        Import(
            names=[alias(name='email.policy', asname=None)],
        ),
        Import(
            names=[alias(name='html2text', asname=None)],
        ),
        Import(
            names=[alias(name='idna', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='smtplib', asname=None)],
        ),
        Import(
            names=[alias(name='ssl', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        ImportFrom(
            module='socket',
            names=[
                alias(name='gaierror', asname=None),
                alias(name='timeout', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='OpenSSL',
            names=[alias(name='crypto', asname='SSLCrypto')],
            level=0,
        ),
        ImportFrom(
            module='OpenSSL.crypto',
            names=[
                alias(name='Error', asname='SSLCryptoError'),
                alias(name='FILETYPE_PEM', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='OpenSSL.SSL',
            names=[alias(name='Error', asname='SSLError')],
            level=0,
        ),
        ImportFrom(
            module='urllib3.contrib.pyopenssl',
            names=[alias(name='PyOpenSSLContext', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
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
            module='odoo.tools',
            names=[
                alias(name='ustr', asname=None),
                alias(name='pycompat', asname=None),
                alias(name='formataddr', asname=None),
                alias(name='email_normalize', asname=None),
                alias(name='encapsulate_email', asname=None),
                alias(name='email_domain_extract', asname=None),
                alias(name='email_domain_normalize', asname=None),
            ],
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
            targets=[Name(id='_test_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Constant(value='odoo.tests', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='SMTP_TIMEOUT', ctx=Store())],
            value=Constant(value=60, kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='MailDeliveryException',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Specific exception subclass for mail delivery errors', kind=None),
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='_print_debug',
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
                            value=Name(id='_logger', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Constant(value=' ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[Name(id='a', ctx=Load())],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='a', ctx=Store()),
                                                iter=Name(id='args', ctx=Load()),
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
        Assign(
            targets=[
                Attribute(
                    value=Attribute(
                        value=Name(id='smtplib', ctx=Load()),
                        attr='SMTP',
                        ctx=Load(),
                    ),
                    attr='_print_debug',
                    ctx=Store(),
                ),
            ],
            value=Name(id='_print_debug', ctx=Load()),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='RFC5322_IDENTIFICATION_HEADERS', ctx=Store())],
            value=Set(
                elts=[
                    Constant(value='message-id', kind=None),
                    Constant(value='in-reply-to', kind=None),
                    Constant(value='references', kind=None),
                    Constant(value='resent-msg-id', kind=None),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_noFoldPolicy', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='email', ctx=Load()),
                            attr='policy',
                            ctx=Load(),
                        ),
                        attr='SMTP',
                        ctx=Load(),
                    ),
                    attr='clone',
                    ctx=Load(),
                ),
                args=[],
                keywords=[
                    keyword(
                        arg='max_line_length',
                        value=Constant(value=None, kind=None),
                    ),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='IdentificationFieldsNoFoldPolicy',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='email', ctx=Load()),
                        attr='policy',
                        ctx=Load(),
                    ),
                    attr='EmailPolicy',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='_fold',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='name', ctx=Load()),
                                        attr='lower',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[In()],
                                comparators=[Name(id='RFC5322_IDENTIFICATION_HEADERS', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_noFoldPolicy', ctx=Load()),
                                            attr='_fold',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='name', ctx=Load()),
                                            Name(id='value', ctx=Load()),
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_fold',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='name', ctx=Load()),
                                    Name(id='value', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[
                Attribute(
                    value=Attribute(
                        value=Name(id='email', ctx=Load()),
                        attr='policy',
                        ctx=Load(),
                    ),
                    attr='SMTP',
                    ctx=Store(),
                ),
            ],
            value=Call(
                func=Name(id='IdentificationFieldsNoFoldPolicy', ctx=Load()),
                args=[],
                keywords=[
                    keyword(
                        arg='linesep',
                        value=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='email', ctx=Load()),
                                    attr='policy',
                                    ctx=Load(),
                                ),
                                attr='SMTP',
                                ctx=Load(),
                            ),
                            attr='linesep',
                            ctx=Load(),
                        ),
                    ),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='WriteToLogger',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='s', annotation=None, type_comment=None),
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
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[Name(id='s', ctx=Load())],
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
            targets=[
                Attribute(
                    value=Name(id='smtplib', ctx=Load()),
                    attr='stderr',
                    ctx=Store(),
                ),
            ],
            value=Call(
                func=Name(id='WriteToLogger', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='is_ascii',
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
                        func=Name(id='all', ctx=Load()),
                        args=[
                            GeneratorExp(
                                elt=Compare(
                                    left=Call(
                                        func=Name(id='ord', ctx=Load()),
                                        args=[Name(id='cp', ctx=Load())],
                                        keywords=[],
                                    ),
                                    ops=[Lt()],
                                    comparators=[Constant(value=128, kind=None)],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='cp', ctx=Store()),
                                        iter=Name(id='s', ctx=Load()),
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
        Assign(
            targets=[Name(id='address_pattern', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='([^ ,<@]+@[^> ,]+)', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='extract_rfc2822_addresses',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='text', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Returns a list of valid RFC2822 addresses\n       that can be found in ``source``, ignoring\n       malformed ones and non-ASCII ones.\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='text', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='candidates', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='address_pattern', ctx=Load()),
                            attr='findall',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Name(id='ustr', ctx=Load()),
                                args=[Name(id='text', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=ListComp(
                        elt=Call(
                            func=Name(id='formataddr', ctx=Load()),
                            args=[
                                Tuple(
                                    elts=[
                                        Constant(value='', kind=None),
                                        Name(id='c', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='charset',
                                    value=Constant(value='ascii', kind=None),
                                ),
                            ],
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='c', ctx=Store()),
                                iter=Name(id='candidates', ctx=Load()),
                                ifs=[],
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
            name='IrMailServer',
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
                    value=Constant(value='Represents an SMTP server, able to send outgoing emails, with SSL and TLS capabilities.', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.mail_server', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Mail Server', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='sequence', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='NO_VALID_RECIPIENT', ctx=Store())],
                    value=Constant(value='At least one valid recipient address should be specified for outgoing emails (To/Cc/Bcc)', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Description', kind=None),
                            ),
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
                    targets=[Name(id='from_filter', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='From Filter', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Define for which email address or domain this server can be used.\ne.g.: "notification@odoo.com" or "odoo.com"', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='smtp_host', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='SMTP Server', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Hostname or IP of SMTP server', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='smtp_port', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='SMTP Port', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=25, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='SMTP Port. Usually 465 for SSL, and 25 or 587 for other cases.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='smtp_authentication', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='login', kind=None),
                                            Constant(value='Username', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='certificate', kind=None),
                                            Constant(value='SSL Certificate', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Authenticate with', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='login', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='smtp_user', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Username', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Optional username for SMTP authentication', kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_system', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='smtp_pass', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Password', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Optional password for SMTP authentication', kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_system', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='smtp_encryption', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='none', kind=None),
                                            Constant(value='None', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='starttls', kind=None),
                                            Constant(value='TLS (STARTTLS)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='ssl', kind=None),
                                            Constant(value='SSL/TLS', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Connection Security', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='none', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Choose the connection encryption scheme:\n- None: SMTP sessions are done in cleartext.\n- TLS (STARTTLS): TLS encryption is requested at start of SMTP session (Recommended)\n- SSL/TLS: SMTP sessions are encrypted with SSL/TLS through a dedicated port (default: 465)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='smtp_ssl_certificate', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='SSL Certificate', kind=None)],
                        keywords=[
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_system', kind=None),
                            ),
                            keyword(
                                arg='attachment',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='SSL certificate used for authentication', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='smtp_ssl_private_key', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='SSL Private Key', kind=None)],
                        keywords=[
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_system', kind=None),
                            ),
                            keyword(
                                arg='attachment',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='SSL private key used for authentication', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='smtp_debug', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Debugging', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If enabled, the full output of SMTP sessions will be written to the server log at DEBUG level (this is very verbose and may include confidential info!)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Priority', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=10, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='When no specific mail server is requested for a mail, the highest priority one is used. Default priority is 10 (smaller number = higher priority)', kind=None),
                            ),
                        ],
                    ),
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
                FunctionDef(
                    name='_check_smtp_ssl_files',
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
                            value=Constant(value='We must provided both files or none.', kind=None),
                        ),
                        For(
                            target=Name(id='mail_server', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='mail_server', ctx=Load()),
                                                attr='smtp_ssl_certificate',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='mail_server', ctx=Load()),
                                                    attr='smtp_ssl_private_key',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='SSL private key is missing for %s.', kind=None),
                                                            Attribute(
                                                                value=Name(id='mail_server', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
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
                                                    Attribute(
                                                        value=Name(id='mail_server', ctx=Load()),
                                                        attr='smtp_ssl_private_key',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='mail_server', ctx=Load()),
                                                            attr='smtp_ssl_certificate',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='SSL certificate is missing for %s.', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='mail_server', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='smtp_ssl_certificate', kind=None),
                                Constant(value='smtp_ssl_private_key', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_test_email_addresses',
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='email_from', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                                attr='email',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='email_from', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Please configure an email on the current user to simulate sending an email message via this outgoing server', kind=None)],
                                                keywords=[],
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
                            value=Tuple(
                                elts=[
                                    Name(id='email_from', ctx=Load()),
                                    Constant(value='noreply@odoo.com', kind=None),
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
                    name='test_smtp_connection',
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
                            target=Name(id='server', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='smtp', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='smtp', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='connect',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='mail_server_id',
                                                        value=Attribute(
                                                            value=Name(id='server', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='email_from', ctx=Store()),
                                                        Name(id='email_to', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='server', ctx=Load()),
                                                    attr='_get_test_email_addresses',
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
                                                        Name(id='code', ctx=Store()),
                                                        Name(id='repl', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='smtp', ctx=Load()),
                                                    attr='mail',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='email_from', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='code', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=250, kind=None)],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='The server refused the sender address (%(email_from)s) with error %(repl)s', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                op=Mod(),
                                                                right=Call(
                                                                    func=Name(id='locals', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[],
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
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='code', ctx=Store()),
                                                        Name(id='repl', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='smtp', ctx=Load()),
                                                    attr='rcpt',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='email_to', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='code', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=250, kind=None),
                                                            Constant(value=251, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='The server refused the test recipient (%(email_to)s) with error %(repl)s', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                op=Mod(),
                                                                right=Call(
                                                                    func=Name(id='locals', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[],
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='smtp', ctx=Load()),
                                                    attr='putcmd',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='data', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='code', ctx=Store()),
                                                        Name(id='repl', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='smtp', ctx=Load()),
                                                    attr='getreply',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='code', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=354, kind=None)],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='The server refused the test connection with error %(repl)s', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                op=Mod(),
                                                                right=Call(
                                                                    func=Name(id='locals', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[],
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
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='UserError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Name(id='e', ctx=Load()),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Tuple(
                                                elts=[
                                                    Name(id='UnicodeError', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='idna', ctx=Load()),
                                                            attr='core',
                                                            ctx=Load(),
                                                        ),
                                                        attr='InvalidCodepoint',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='Invalid server name !\n %s', kind=None),
                                                                    Call(
                                                                        func=Name(id='ustr', ctx=Load()),
                                                                        args=[Name(id='e', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
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
                                        ExceptHandler(
                                            type=Tuple(
                                                elts=[
                                                    Name(id='gaierror', ctx=Load()),
                                                    Name(id='timeout', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='No response received. Check server address and port number.\n %s', kind=None),
                                                                    Call(
                                                                        func=Name(id='ustr', ctx=Load()),
                                                                        args=[Name(id='e', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
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
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='smtplib', ctx=Load()),
                                                attr='SMTPServerDisconnected',
                                                ctx=Load(),
                                            ),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='The server has closed the connection unexpectedly. Check configuration served on this port number.\n %s', kind=None),
                                                                    Call(
                                                                        func=Name(id='ustr', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='e', ctx=Load()),
                                                                                attr='strerror',
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
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='smtplib', ctx=Load()),
                                                attr='SMTPResponseException',
                                                ctx=Load(),
                                            ),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='Server replied with following exception:\n %s', kind=None),
                                                                    Call(
                                                                        func=Name(id='ustr', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='e', ctx=Load()),
                                                                                attr='smtp_error',
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
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='smtplib', ctx=Load()),
                                                attr='SMTPNotSupportedError',
                                                ctx=Load(),
                                            ),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='An option is not supported by the server:\n %s', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='e', ctx=Load()),
                                                                        attr='strerror',
                                                                        ctx=Load(),
                                                                    ),
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
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='smtplib', ctx=Load()),
                                                attr='SMTPException',
                                                ctx=Load(),
                                            ),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='An SMTP exception occurred. Check port number and connection security type.\n %s', kind=None),
                                                                    Call(
                                                                        func=Name(id='ustr', ctx=Load()),
                                                                        args=[Name(id='e', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
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
                                        ExceptHandler(
                                            type=Name(id='SSLError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='An SSL exception occurred. Check connection security type.\n %s', kind=None),
                                                                    Call(
                                                                        func=Name(id='ustr', ctx=Load()),
                                                                        args=[Name(id='e', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
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
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='Connection Test Failed! Here is what we got instead:\n %s', kind=None),
                                                                    Call(
                                                                        func=Name(id='ustr', ctx=Load()),
                                                                        args=[Name(id='e', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
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
                                    finalbody=[
                                        Try(
                                            body=[
                                                If(
                                                    test=Name(id='smtp', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='smtp', ctx=Load()),
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
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='Exception', ctx=Load()),
                                                    name=None,
                                                    body=[Pass()],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='message', ctx=Store())],
                            value=Call(
                                func=Name(id='_', ctx=Load()),
                                args=[Constant(value='Connection Test Successful!', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='tag', kind=None),
                                    Constant(value='params', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.client', kind=None),
                                    Constant(value='display_notification', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='message', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='sticky', kind=None),
                                        ],
                                        values=[
                                            Name(id='message', ctx=Load()),
                                            Constant(value='success', kind=None),
                                            Constant(value=False, kind=None),
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
                FunctionDef(
                    name='connect',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='host', annotation=None, type_comment=None),
                            arg(arg='port', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                            arg(arg='encryption', annotation=None, type_comment=None),
                            arg(arg='smtp_from', annotation=None, type_comment=None),
                            arg(arg='ssl_certificate', annotation=None, type_comment=None),
                            arg(arg='ssl_private_key', annotation=None, type_comment=None),
                            arg(arg='smtp_debug', annotation=None, type_comment=None),
                            arg(arg='mail_server_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Returns a new SMTP connection to the given SMTP server.\n           When running in test mode, this method does nothing and returns `None`.\n\n           :param host: host or IP of SMTP server to connect to, if mail_server_id not passed\n           :param int port: SMTP port to connect to\n           :param user: optional username to authenticate with\n           :param password: optional password to authenticate with\n           :param string encryption: optional, ``\'ssl\'`` | ``\'starttls\'``\n           :param smtp_from: FROM SMTP envelop, used to find the best mail server\n           :param ssl_certificate: filename of the SSL certificate used for authentication\n               Used when no mail server is given and overwrite  the odoo-bin argument "smtp_ssl_certificate"\n           :param ssl_private_key: filename of the SSL private key used for authentication\n               Used when no mail server is given and overwrite  the odoo-bin argument "smtp_ssl_private_key"\n           :param bool smtp_debug: toggle debugging of SMTP sessions (all i/o\n                              will be output in logs)\n           :param mail_server_id: ID of specific mail server to use (overrides other parameters)\n        ', kind=None),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_test_mode',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Name(id='mail_server', ctx=Store()),
                                Name(id='smtp_encryption', ctx=Store()),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='mail_server_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='mail_server', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='mail_server_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='host', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='mail_server', ctx=Store()),
                                                        Name(id='smtp_from', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='_find_mail_server',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='smtp_from', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='ssl_context', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='mail_server', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='smtp_server', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='mail_server', ctx=Load()),
                                        attr='smtp_host',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='smtp_port', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='mail_server', ctx=Load()),
                                        attr='smtp_port',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='mail_server', ctx=Load()),
                                            attr='smtp_authentication',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='login', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='smtp_user', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='mail_server', ctx=Load()),
                                                attr='smtp_user',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='smtp_password', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='mail_server', ctx=Load()),
                                                attr='smtp_pass',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='smtp_user', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='smtp_password', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='smtp_encryption', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='mail_server', ctx=Load()),
                                        attr='smtp_encryption',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='smtp_debug', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='smtp_debug', ctx=Load()),
                                            Attribute(
                                                value=Name(id='mail_server', ctx=Load()),
                                                attr='smtp_debug',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='from_filter', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='mail_server', ctx=Load()),
                                        attr='from_filter',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='mail_server', ctx=Load()),
                                                    attr='smtp_authentication',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='certificate', kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='mail_server', ctx=Load()),
                                                attr='smtp_ssl_certificate',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='mail_server', ctx=Load()),
                                                attr='smtp_ssl_private_key',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='ssl_context', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='PyOpenSSLContext', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='ssl', ctx=Load()),
                                                                attr='PROTOCOL_TLS',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='smtp_ssl_certificate', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='base64', ctx=Load()),
                                                            attr='b64decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='mail_server', ctx=Load()),
                                                                attr='smtp_ssl_certificate',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='certificate', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='SSLCrypto', ctx=Load()),
                                                            attr='load_certificate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='FILETYPE_PEM', ctx=Load()),
                                                            Name(id='smtp_ssl_certificate', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='smtp_ssl_private_key', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='base64', ctx=Load()),
                                                            attr='b64decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='mail_server', ctx=Load()),
                                                                attr='smtp_ssl_private_key',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='private_key', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='SSLCrypto', ctx=Load()),
                                                            attr='load_privatekey',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='FILETYPE_PEM', ctx=Load()),
                                                            Name(id='smtp_ssl_private_key', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='ssl_context', ctx=Load()),
                                                                attr='_ctx',
                                                                ctx=Load(),
                                                            ),
                                                            attr='use_certificate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='certificate', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='ssl_context', ctx=Load()),
                                                                attr='_ctx',
                                                                ctx=Load(),
                                                            ),
                                                            attr='use_privatekey',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='private_key', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='ssl_context', ctx=Load()),
                                                                attr='_ctx',
                                                                ctx=Load(),
                                                            ),
                                                            attr='check_privatekey',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='SSLCryptoError', ctx=Load()),
                                                    name='e',
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='UserError', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[
                                                                            Constant(value='The private key or the certificate is not a valid file. \n%s', kind=None),
                                                                            Call(
                                                                                func=Name(id='str', ctx=Load()),
                                                                                args=[Name(id='e', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
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
                                                ExceptHandler(
                                                    type=Name(id='SSLError', ctx=Load()),
                                                    name='e',
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='UserError', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[
                                                                            Constant(value='Could not load your certificate / private key. \n%s', kind=None),
                                                                            Call(
                                                                                func=Name(id='str', ctx=Load()),
                                                                                args=[Name(id='e', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
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
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='smtp_server', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='host', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='tools', ctx=Load()),
                                                        attr='config',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='smtp_server', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='smtp_port', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='port', ctx=Load()),
                                            ops=[Is()],
                                            comparators=[Constant(value=None, kind=None)],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='config',
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='smtp_port', kind=None),
                                                Constant(value=25, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        orelse=Name(id='port', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='smtp_user', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='user', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='tools', ctx=Load()),
                                                        attr='config',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='smtp_user', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='smtp_password', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='password', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='tools', ctx=Load()),
                                                        attr='config',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='smtp_password', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='from_filter', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='from_filter', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='smtp_encryption', ctx=Store())],
                                    value=Name(id='encryption', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='smtp_encryption', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='tools', ctx=Load()),
                                                        attr='config',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='smtp_ssl', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='smtp_encryption', ctx=Store())],
                                            value=Constant(value='starttls', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='smtp_ssl_certificate_filename', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='ssl_certificate', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='tools', ctx=Load()),
                                                        attr='config',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='smtp_ssl_certificate_filename', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='smtp_ssl_private_key_filename', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='ssl_private_key', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='tools', ctx=Load()),
                                                        attr='config',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='smtp_ssl_private_key_filename', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='smtp_ssl_certificate_filename', ctx=Load()),
                                            Name(id='smtp_ssl_private_key_filename', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='ssl_context', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='PyOpenSSLContext', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='ssl', ctx=Load()),
                                                                attr='PROTOCOL_TLS',
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
                                                            value=Name(id='ssl_context', ctx=Load()),
                                                            attr='load_cert_chain',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='smtp_ssl_certificate_filename', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='keyfile',
                                                                value=Name(id='smtp_ssl_private_key_filename', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='ssl_context', ctx=Load()),
                                                                attr='_ctx',
                                                                ctx=Load(),
                                                            ),
                                                            attr='check_privatekey',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='SSLCryptoError', ctx=Load()),
                                                    name='e',
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='UserError', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[
                                                                            Constant(value='The private key or the certificate is not a valid file. \n%s', kind=None),
                                                                            Call(
                                                                                func=Name(id='str', ctx=Load()),
                                                                                args=[Name(id='e', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
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
                                                ExceptHandler(
                                                    type=Name(id='SSLError', ctx=Load()),
                                                    name='e',
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='UserError', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[
                                                                            Constant(value='Could not load your certificate / private key. \n%s', kind=None),
                                                                            Call(
                                                                                func=Name(id='str', ctx=Load()),
                                                                                args=[Name(id='e', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
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
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='smtp_server', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Missing SMTP Server', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    op=Add(),
                                                    right=Constant(value='\n', kind=None),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Please define at least one SMTP server, or provide the SMTP parameters explicitly.', kind=None)],
                                                    keywords=[],
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
                        If(
                            test=Compare(
                                left=Name(id='smtp_encryption', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='ssl', kind=None)],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='SMTP_SSL', kind=None),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='smtplib', ctx=Load()),
                                                attr='__all__',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Your Odoo Server does not support SMTP-over-SSL. You could use STARTTLS instead. If SSL is needed, an upgrade to Python 2.6 on the server-side should do the trick.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='connection', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='smtplib', ctx=Load()),
                                            attr='SMTP_SSL',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='smtp_server', ctx=Load()),
                                            Name(id='smtp_port', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='timeout',
                                                value=Name(id='SMTP_TIMEOUT', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='connection', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='smtplib', ctx=Load()),
                                            attr='SMTP',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='smtp_server', ctx=Load()),
                                            Name(id='smtp_port', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='timeout',
                                                value=Name(id='SMTP_TIMEOUT', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='connection', ctx=Load()),
                                    attr='set_debuglevel',
                                    ctx=Load(),
                                ),
                                args=[Name(id='smtp_debug', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='smtp_encryption', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='starttls', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='connection', ctx=Load()),
                                            attr='starttls',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='context',
                                                value=Name(id='ssl_context', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='smtp_user', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='local', ctx=Store()),
                                                Name(id='at', ctx=Store()),
                                                Name(id='domain', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='smtp_user', ctx=Load()),
                                            attr='rpartition',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='@', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='at', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='smtp_user', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Name(id='local', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='at', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='idna', ctx=Load()),
                                                                attr='encode',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='domain', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='ascii', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='connection', ctx=Load()),
                                            attr='login',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='smtp_user', ctx=Load()),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='smtp_password', ctx=Load()),
                                                    Constant(value='', kind=None),
                                                ],
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
                                    value=Name(id='connection', ctx=Load()),
                                    attr='ehlo_or_helo_if_needed',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='connection', ctx=Load()),
                                    attr='from_filter',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='from_filter', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='connection', ctx=Load()),
                                    attr='smtp_from',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='smtp_from', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='connection', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='build_email',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='email_from', annotation=None, type_comment=None),
                            arg(arg='email_to', annotation=None, type_comment=None),
                            arg(arg='subject', annotation=None, type_comment=None),
                            arg(arg='body', annotation=None, type_comment=None),
                            arg(arg='email_cc', annotation=None, type_comment=None),
                            arg(arg='email_bcc', annotation=None, type_comment=None),
                            arg(arg='reply_to', annotation=None, type_comment=None),
                            arg(arg='attachments', annotation=None, type_comment=None),
                            arg(arg='message_id', annotation=None, type_comment=None),
                            arg(arg='references', annotation=None, type_comment=None),
                            arg(arg='object_id', annotation=None, type_comment=None),
                            arg(arg='subtype', annotation=None, type_comment=None),
                            arg(arg='headers', annotation=None, type_comment=None),
                            arg(arg='body_alternative', annotation=None, type_comment=None),
                            arg(arg='subtype_alternative', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value='plain', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value='plain', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Constructs an RFC2822 email.message.Message object based on the keyword arguments passed, and returns it.\n\n           :param string email_from: sender email address\n           :param list email_to: list of recipient addresses (to be joined with commas)\n           :param string subject: email subject (no pre-encoding/quoting necessary)\n           :param string body: email body, of the type ``subtype`` (by default, plaintext).\n                               If html subtype is used, the message will be automatically converted\n                               to plaintext and wrapped in multipart/alternative, unless an explicit\n                               ``body_alternative`` version is passed.\n           :param string body_alternative: optional alternative body, of the type specified in ``subtype_alternative``\n           :param string reply_to: optional value of Reply-To header\n           :param string object_id: optional tracking identifier, to be included in the message-id for\n                                    recognizing replies. Suggested format for object-id is "res_id-model",\n                                    e.g. "12345-crm.lead".\n           :param string subtype: optional mime subtype for the text body (usually \'plain\' or \'html\'),\n                                  must match the format of the ``body`` parameter. Default is \'plain\',\n                                  making the content part of the mail "text/plain".\n           :param string subtype_alternative: optional mime subtype of ``body_alternative`` (usually \'plain\'\n                                              or \'html\'). Default is \'plain\'.\n           :param list attachments: list of (filename, filecontents) pairs, where filecontents is a string\n                                    containing the bytes of the attachment\n           :param list email_cc: optional list of string values for CC header (to be joined with commas)\n           :param list email_bcc: optional list of string values for BCC header (to be joined with commas)\n           :param dict headers: optional map of headers to set on the outgoing mail (may override the\n                                other headers, including Subject, Reply-To, Message-Id, etc.)\n           :rtype: email.message.EmailMessage\n           :return: the new RFC2822 email message\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='email_from', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='email_from', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_default_from_address',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Name(id='email_from', ctx=Load()),
                            msg=Constant(value='You must either provide a sender address explicitly or configure using the combination of `mail.catchall.domain` and `mail.default.from` ICPs, in the server configuration file or with the --email-from startup parameter.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='headers', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='headers', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='email_cc', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='email_cc', ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='email_bcc', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='email_bcc', ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='body', ctx=Load()),
                                    Constant(value='', kind='u'),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=Call(
                                func=Name(id='EmailMessage', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='policy',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='email', ctx=Load()),
                                                attr='policy',
                                                ctx=Load(),
                                            ),
                                            attr='SMTP',
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
                                    value=Name(id='msg', ctx=Load()),
                                    attr='set_charset',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='utf-8', kind=None)],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='message_id', ctx=Load()),
                            ),
                            body=[
                                If(
                                    test=Name(id='object_id', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='message_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='generate_tracking_message_id',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='object_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='message_id', ctx=Store())],
                                            value=Call(
                                                func=Name(id='make_msgid', ctx=Load()),
                                                args=[],
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
                            targets=[
                                Subscript(
                                    value=Name(id='msg', ctx=Load()),
                                    slice=Constant(value='Message-Id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='message_id', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='references', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='msg', ctx=Load()),
                                            slice=Constant(value='references', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='references', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='msg', ctx=Load()),
                                    slice=Constant(value='Subject', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='subject', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='msg', ctx=Load()),
                                    slice=Constant(value='From', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='email_from', ctx=Load()),
                            type_comment=None,
                        ),
                        Delete(
                            targets=[
                                Subscript(
                                    value=Name(id='msg', ctx=Load()),
                                    slice=Constant(value='Reply-To', kind=None),
                                    ctx=Del(),
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='msg', ctx=Load()),
                                    slice=Constant(value='Reply-To', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='reply_to', ctx=Load()),
                                    Name(id='email_from', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='msg', ctx=Load()),
                                    slice=Constant(value='To', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='email_to', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='email_cc', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='msg', ctx=Load()),
                                            slice=Constant(value='Cc', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='email_cc', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='email_bcc', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='msg', ctx=Load()),
                                            slice=Constant(value='Bcc', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='email_bcc', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='msg', ctx=Load()),
                                    slice=Constant(value='Date', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
                                        attr='datetime',
                                        ctx=Load(),
                                    ),
                                    attr='utcnow',
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
                                    Name(id='key', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='headers', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='msg', ctx=Load()),
                                            slice=Call(
                                                func=Attribute(
                                                    value=Name(id='pycompat', ctx=Load()),
                                                    attr='to_text',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='ustr', ctx=Load()),
                                                        args=[Name(id='key', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='value', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='email_body', ctx=Store())],
                            value=Call(
                                func=Name(id='ustr', ctx=Load()),
                                args=[Name(id='body', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='subtype', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='html', kind=None)],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='body_alternative', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='msg', ctx=Load()),
                                            attr='add_alternative',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='html2text', ctx=Load()),
                                                    attr='html2text',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='email_body', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='subtype',
                                                value=Constant(value='plain', kind=None),
                                            ),
                                            keyword(
                                                arg='charset',
                                                value=Constant(value='utf-8', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='msg', ctx=Load()),
                                            attr='add_alternative',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='email_body', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='subtype',
                                                value=Name(id='subtype', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='charset',
                                                value=Constant(value='utf-8', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='body_alternative', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='msg', ctx=Load()),
                                                    attr='add_alternative',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='ustr', ctx=Load()),
                                                        args=[Name(id='body_alternative', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='subtype',
                                                        value=Name(id='subtype_alternative', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='charset',
                                                        value=Constant(value='utf-8', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='msg', ctx=Load()),
                                                    attr='add_alternative',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='email_body', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='subtype',
                                                        value=Name(id='subtype', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='charset',
                                                        value=Constant(value='utf-8', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='msg', ctx=Load()),
                                                    attr='set_content',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='email_body', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='subtype',
                                                        value=Name(id='subtype', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='charset',
                                                        value=Constant(value='utf-8', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='attachments', ctx=Load()),
                            body=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='fname', ctx=Store()),
                                            Name(id='fcontent', ctx=Store()),
                                            Name(id='mime', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Name(id='attachments', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='maintype', ctx=Store()),
                                                        Name(id='subtype', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=IfExp(
                                                test=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Name(id='mime', ctx=Load()),
                                                        Compare(
                                                            left=Constant(value='/', kind=None),
                                                            ops=[In()],
                                                            comparators=[Name(id='mime', ctx=Load())],
                                                        ),
                                                    ],
                                                ),
                                                body=Call(
                                                    func=Attribute(
                                                        value=Name(id='mime', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='/', kind=None)],
                                                    keywords=[],
                                                ),
                                                orelse=Tuple(
                                                    elts=[
                                                        Constant(value='application', kind=None),
                                                        Constant(value='octet-stream', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='msg', ctx=Load()),
                                                    attr='add_attachment',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='fcontent', ctx=Load()),
                                                    Name(id='maintype', ctx=Load()),
                                                    Name(id='subtype', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='filename',
                                                        value=Name(id='fname', ctx=Load()),
                                                    ),
                                                ],
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
                            value=Name(id='msg', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_default_bounce_address',
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
                            value=Constant(value='Compute the default bounce address.\n\n        The default bounce address is used to set the envelop address if no\n        envelop address is provided in the message.  It is formed by properly\n        joining the parameters "mail.bounce.alias" and\n        "mail.catchall.domain".\n\n        If "mail.bounce.alias" is not set it defaults to "postmaster-odoo".\n\n        If "mail.catchall.domain" is not set, return None.\n\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='get_param', ctx=Store())],
                            value=Attribute(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='postmaster', ctx=Store())],
                            value=Call(
                                func=Name(id='get_param', ctx=Load()),
                                args=[Constant(value='mail.bounce.alias', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value='postmaster-odoo', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Name(id='get_param', ctx=Load()),
                                args=[Constant(value='mail.catchall.domain', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='postmaster', ctx=Load()),
                                    Name(id='domain', ctx=Load()),
                                ],
                            ),
                            body=[
                                Return(
                                    value=BinOp(
                                        left=Constant(value='%s@%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='postmaster', ctx=Load()),
                                                Name(id='domain', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_default_from_address',
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
                            value=Constant(value='Compute the default from address.\n\n        Used for the "header from" address when no other has been received.\n\n        :return str/None:\n            Combines config parameters ``mail.default.from`` and\n            ``mail.catchall.domain`` to generate a default sender address.\n\n            If some of those parameters is not defined, it will default to the\n            ``--email-from`` CLI/config parameter.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='get_param', ctx=Store())],
                            value=Attribute(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Name(id='get_param', ctx=Load()),
                                args=[Constant(value='mail.catchall.domain', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='email_from', ctx=Store())],
                            value=Call(
                                func=Name(id='get_param', ctx=Load()),
                                args=[Constant(value='mail.default.from', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='email_from', ctx=Load()),
                                    Name(id='domain', ctx=Load()),
                                ],
                            ),
                            body=[
                                Return(
                                    value=BinOp(
                                        left=Constant(value='%s@%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='email_from', ctx=Load()),
                                                Name(id='domain', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='tools', ctx=Load()),
                                        attr='config',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='email_from', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_email_message',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                            arg(arg='smtp_session', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Prepare the SMTP information (from, to, message) before sending.\n\n        :param message: the email.message.Message to send, information like the\n            Return-Path, the From, etc... will be used to find the smtp_from and to smtp_to\n        :param smtp_session: the opened SMTP session to use to authenticate the sender\n        :return: smtp_from, smtp_to_list, message\n            smtp_from: email to used during the authentication to the mail server\n            smtp_to_list: list of email address which will receive the email\n            message: the email.message.Message to send\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='bounce_address', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=Name(id='message', ctx=Load()),
                                        slice=Constant(value='Return-Path', kind=None),
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_default_bounce_address',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Name(id='message', ctx=Load()),
                                        slice=Constant(value='From', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='smtp_from', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=Name(id='message', ctx=Load()),
                                        slice=Constant(value='From', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='bounce_address', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Name(id='smtp_from', ctx=Load()),
                            msg=Constant(value='The Return-Path or From header is required for any outbound email', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='email_to', ctx=Store())],
                            value=Subscript(
                                value=Name(id='message', ctx=Load()),
                                slice=Constant(value='To', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='email_cc', ctx=Store())],
                            value=Subscript(
                                value=Name(id='message', ctx=Load()),
                                slice=Constant(value='Cc', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='email_bcc', ctx=Store())],
                            value=Subscript(
                                value=Name(id='message', ctx=Load()),
                                slice=Constant(value='Bcc', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Delete(
                            targets=[
                                Subscript(
                                    value=Name(id='message', ctx=Load()),
                                    slice=Constant(value='Bcc', kind=None),
                                    ctx=Del(),
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='smtp_to_list', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='address', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='base', ctx=Store()),
                                        iter=List(
                                            elts=[
                                                Name(id='email_to', ctx=Load()),
                                                Name(id='email_cc', ctx=Load()),
                                                Name(id='email_bcc', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                    comprehension(
                                        target=Name(id='address', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='extract_rfc2822_addresses', ctx=Load()),
                                            args=[Name(id='base', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ifs=[Name(id='address', ctx=Load())],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Name(id='smtp_to_list', ctx=Load()),
                            msg=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='NO_VALID_RECIPIENT',
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='x_forge_to', ctx=Store())],
                            value=Subscript(
                                value=Name(id='message', ctx=Load()),
                                slice=Constant(value='X-Forge-To', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='x_forge_to', ctx=Load()),
                            body=[
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='message', ctx=Load()),
                                            slice=Constant(value='X-Forge-To', kind=None),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='message', ctx=Load()),
                                            slice=Constant(value='To', kind=None),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='message', ctx=Load()),
                                            slice=Constant(value='To', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='x_forge_to', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='from_filter', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='smtp_session', ctx=Load()),
                                    Constant(value='from_filter', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='smtp_from', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='smtp_session', ctx=Load()),
                                            Constant(value='smtp_from', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='smtp_from', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='notifications_email', ctx=Store())],
                            value=Call(
                                func=Name(id='email_normalize', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_default_from_address',
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='notifications_email', ctx=Load()),
                                    Compare(
                                        left=Name(id='smtp_from', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Name(id='notifications_email', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='message', ctx=Load()),
                                            slice=Constant(value='From', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='notifications_email', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='smtp_from', ctx=Store())],
                                    value=Call(
                                        func=Name(id='encapsulate_email', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='message', ctx=Load()),
                                                slice=Constant(value='From', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='notifications_email', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='message', ctx=Load()),
                                    slice=Constant(value='From', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Name(id='smtp_from', ctx=Load())],
                            ),
                            body=[
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='message', ctx=Load()),
                                            slice=Constant(value='From', kind=None),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='message', ctx=Load()),
                                            slice=Constant(value='From', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='smtp_from', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_match_from_filter',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bounce_address', ctx=Load()),
                                    Name(id='from_filter', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='smtp_from', ctx=Store())],
                                    value=Name(id='bounce_address', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='smtp_from_rfc2822', ctx=Store())],
                            value=Call(
                                func=Name(id='extract_rfc2822_addresses', ctx=Load()),
                                args=[Name(id='smtp_from', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Name(id='smtp_from_rfc2822', ctx=Load()),
                            msg=JoinedStr(
                                values=[
                                    Constant(value="Malformed 'Return-Path' or 'From' address: ", kind=None),
                                    FormattedValue(
                                        value=Name(id='smtp_from', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=' - It should contain one valid plain ASCII email', kind=None),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='smtp_from', ctx=Store())],
                            value=Subscript(
                                value=Name(id='smtp_from_rfc2822', ctx=Load()),
                                slice=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='smtp_from', ctx=Load()),
                                    Name(id='smtp_to_list', ctx=Load()),
                                    Name(id='message', ctx=Load()),
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
                    name='send_email',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                            arg(arg='mail_server_id', annotation=None, type_comment=None),
                            arg(arg='smtp_server', annotation=None, type_comment=None),
                            arg(arg='smtp_port', annotation=None, type_comment=None),
                            arg(arg='smtp_user', annotation=None, type_comment=None),
                            arg(arg='smtp_password', annotation=None, type_comment=None),
                            arg(arg='smtp_encryption', annotation=None, type_comment=None),
                            arg(arg='smtp_ssl_certificate', annotation=None, type_comment=None),
                            arg(arg='smtp_ssl_private_key', annotation=None, type_comment=None),
                            arg(arg='smtp_debug', annotation=None, type_comment=None),
                            arg(arg='smtp_session', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Sends an email directly (no queuing).\n\n        No retries are done, the caller should handle MailDeliveryException in order to ensure that\n        the mail is never lost.\n\n        If the mail_server_id is provided, sends using this mail server, ignoring other smtp_* arguments.\n        If mail_server_id is None and smtp_server is None, use the default mail server (highest priority).\n        If mail_server_id is None and smtp_server is not None, use the provided smtp_* arguments.\n        If both mail_server_id and smtp_server are None, look for an 'smtp_server' value in server config,\n        and fails if not found.\n\n        :param message: the email.message.Message to send. The envelope sender will be extracted from the\n                        ``Return-Path`` (if present), or will be set to the default bounce address.\n                        The envelope recipients will be extracted from the combined list of ``To``,\n                        ``CC`` and ``BCC`` headers.\n        :param smtp_session: optional pre-established SMTP session. When provided,\n                             overrides `mail_server_id` and all the `smtp_*` parameters.\n                             Passing the matching `mail_server_id` may yield better debugging/log\n                             messages. The caller is in charge of disconnecting the session.\n        :param mail_server_id: optional id of ir.mail_server to use for sending. overrides other smtp_* arguments.\n        :param smtp_server: optional hostname of SMTP server to use\n        :param smtp_encryption: optional TLS mode, one of 'none', 'starttls' or 'ssl' (see ir.mail_server fields for explanation)\n        :param smtp_port: optional SMTP port, if mail_server_id is not passed\n        :param smtp_user: optional SMTP user, if mail_server_id is not passed\n        :param smtp_password: optional SMTP password to use, if mail_server_id is not passed\n        :param smtp_ssl_certificate: filename of the SSL certificate used for authentication\n        :param smtp_ssl_private_key: filename of the SSL private key used for authentication\n        :param smtp_debug: optional SMTP debug flag, if mail_server_id is not passed\n        :return: the Message-ID of the message that was just sent, if successfully sent, otherwise raises\n                 MailDeliveryException and logs root cause.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='smtp', ctx=Store())],
                            value=Name(id='smtp_session', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='smtp', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='smtp', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='connect',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='smtp_server', ctx=Load()),
                                            Name(id='smtp_port', ctx=Load()),
                                            Name(id='smtp_user', ctx=Load()),
                                            Name(id='smtp_password', ctx=Load()),
                                            Name(id='smtp_encryption', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='smtp_from',
                                                value=Subscript(
                                                    value=Name(id='message', ctx=Load()),
                                                    slice=Constant(value='From', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='ssl_certificate',
                                                value=Name(id='smtp_ssl_certificate', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='ssl_private_key',
                                                value=Name(id='smtp_ssl_private_key', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='smtp_debug',
                                                value=Name(id='smtp_debug', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='mail_server_id',
                                                value=Name(id='mail_server_id', ctx=Load()),
                                            ),
                                        ],
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
                                        Name(id='smtp_from', ctx=Store()),
                                        Name(id='smtp_to_list', ctx=Store()),
                                        Name(id='message', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_email_message',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='message', ctx=Load()),
                                    Name(id='smtp', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_test_mode',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_test_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='skip sending email in test mode', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Subscript(
                                        value=Name(id='message', ctx=Load()),
                                        slice=Constant(value='Message-Id', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='message_id', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='message', ctx=Load()),
                                        slice=Constant(value='Message-Id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='sys', ctx=Load()),
                                            attr='version_info',
                                            ctx=Load(),
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value=7, kind=None),
                                                    Constant(value=4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='message_str', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='message', ctx=Load()),
                                                    attr='as_string',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='message_str', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='sub',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='\r+(?!\n)', kind=None),
                                                    Constant(value='', kind=None),
                                                    Name(id='message_str', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='mail_options', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=UnaryOp(
                                                            op=Not(),
                                                            operand=Call(
                                                                func=Name(id='is_ascii', ctx=Load()),
                                                                args=[Name(id='addr', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='addr', ctx=Store()),
                                                                iter=BinOp(
                                                                    left=Name(id='smtp_to_list', ctx=Load()),
                                                                    op=Add(),
                                                                    right=List(
                                                                        elts=[Name(id='smtp_from', ctx=Load())],
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='mail_options', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='SMTPUTF8', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='smtp', ctx=Load()),
                                                    attr='sendmail',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='smtp_from', ctx=Load()),
                                                    Name(id='smtp_to_list', ctx=Load()),
                                                    Name(id='message_str', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='mail_options',
                                                        value=Name(id='mail_options', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='smtp', ctx=Load()),
                                                    attr='send_message',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='message', ctx=Load()),
                                                    Name(id='smtp_from', ctx=Load()),
                                                    Name(id='smtp_to_list', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='smtp_session', ctx=Load()),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='smtp', ctx=Load()),
                                                    attr='quit',
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
                                    type=Attribute(
                                        value=Name(id='smtplib', ctx=Load()),
                                        attr='SMTPServerDisconnected',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[Raise(exc=None, cause=None)],
                                ),
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Assign(
                                            targets=[Name(id='params', ctx=Store())],
                                            value=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='ustr', ctx=Load()),
                                                        args=[Name(id='smtp_server', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='__class__',
                                                            ctx=Load(),
                                                        ),
                                                        attr='__name__',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='ustr', ctx=Load()),
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value="Mail delivery failed via SMTP server '%s'.\n%s: %s", kind=None),
                                                    Starred(
                                                        value=Name(id='params', ctx=Load()),
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
                                                args=[Name(id='msg', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='MailDeliveryException', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Mail Delivery Failed', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Name(id='msg', ctx=Load()),
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
                        Return(
                            value=Name(id='message_id', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_find_mail_server',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='email_from', annotation=None, type_comment=None),
                            arg(arg='mail_servers', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Find the appropriate mail server for the given email address.\n\n        Returns: Record<ir.mail_server>, email_from\n        - Mail server to use to send the email (None if we use the odoo-bin arguments)\n        - Email FROM to use to send the email (in some case, it might be impossible\n          to use the given email address directly if no mail server is configured for)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='email_from_normalized', ctx=Store())],
                            value=Call(
                                func=Name(id='email_normalize', ctx=Load()),
                                args=[Name(id='email_from', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='email_from_domain', ctx=Store())],
                            value=Call(
                                func=Name(id='email_domain_extract', ctx=Load()),
                                args=[Name(id='email_from_normalized', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='notifications_email', ctx=Store())],
                            value=Call(
                                func=Name(id='email_normalize', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_default_from_address',
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
                            targets=[Name(id='notifications_domain', ctx=Store())],
                            value=Call(
                                func=Name(id='email_domain_extract', ctx=Load()),
                                args=[Name(id='notifications_email', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='mail_servers', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='mail_servers', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='order',
                                                value=Constant(value='sequence', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='mail_server', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mail_servers', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='m', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Call(
                                                func=Name(id='email_normalize', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='m', ctx=Load()),
                                                        attr='from_filter',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            ops=[Eq()],
                                            comparators=[Name(id='email_from_normalized', ctx=Load())],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='mail_server', ctx=Load()),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Subscript(
                                                value=Name(id='mail_server', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='email_from', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='mail_server', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mail_servers', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='m', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Call(
                                                func=Name(id='email_domain_normalize', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='m', ctx=Load()),
                                                        attr='from_filter',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            ops=[Eq()],
                                            comparators=[Name(id='email_from_domain', ctx=Load())],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='mail_server', ctx=Load()),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Subscript(
                                                value=Name(id='mail_server', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='email_from', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='notifications_email', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='mail_server', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mail_servers', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='m', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Call(
                                                        func=Name(id='email_normalize', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='m', ctx=Load()),
                                                                attr='from_filter',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Name(id='notifications_email', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='mail_server', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Name(id='mail_server', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='notifications_email', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='mail_server', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mail_servers', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='m', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Call(
                                                        func=Name(id='email_domain_normalize', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='m', ctx=Load()),
                                                                attr='from_filter',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Name(id='notifications_domain', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='mail_server', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Name(id='mail_server', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='notifications_email', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='mail_server', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mail_servers', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='m', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='m', ctx=Load()),
                                                attr='from_filter',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='mail_server', ctx=Load()),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Subscript(
                                                value=Name(id='mail_server', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='email_from', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='mail_servers', ctx=Load()),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Subscript(
                                                value=Name(id='mail_servers', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='email_from', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='from_filter', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='tools', ctx=Load()),
                                        attr='config',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='from_filter', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_match_from_filter',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='email_from', ctx=Load()),
                                    Name(id='from_filter', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value=None, kind=None),
                                            Name(id='email_from', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='notifications_email', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_match_from_filter',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='notifications_email', ctx=Load()),
                                            Name(id='from_filter', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value=None, kind=None),
                                            Name(id='notifications_email', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value=None, kind=None),
                                    Name(id='email_from', ctx=Load()),
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
                    name='_match_from_filter',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='email_from', annotation=None, type_comment=None),
                            arg(arg='from_filter', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Return True is the given email address match the "from_filter" field.\n\n        The from filter can be Falsy (always match),\n        a domain name or an full email address.\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='from_filter', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='normalized_mail_from', ctx=Store())],
                            value=Call(
                                func=Name(id='email_normalize', ctx=Load()),
                                args=[Name(id='email_from', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='@', kind=None),
                                ops=[In()],
                                comparators=[Name(id='from_filter', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Compare(
                                        left=Call(
                                            func=Name(id='email_normalize', ctx=Load()),
                                            args=[Name(id='from_filter', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='normalized_mail_from', ctx=Load())],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Compare(
                                left=Call(
                                    func=Name(id='email_domain_extract', ctx=Load()),
                                    args=[Name(id='normalized_mail_from', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Call(
                                        func=Name(id='email_domain_normalize', ctx=Load()),
                                        args=[Name(id='from_filter', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_encryption',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='smtp_encryption',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='ssl', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='smtp_port',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=465, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Compare(
                                            left=Constant(value='SMTP_SSL', kind=None),
                                            ops=[In()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='smtplib', ctx=Load()),
                                                    attr='__all__',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Constant(value='warning', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='title', kind=None),
                                                    Constant(value='message', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Warning', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Your server does not seem to support SSL, you may want to try STARTTLS instead', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
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
                                            attr='smtp_port',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=25, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='smtp_encryption', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_test_mode',
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
                            value=Constant(value='Return True if we are running the tests, so we do not send real emails.\n\n        Can be overridden in tests after mocking the SMTP lib to test in depth the\n        outgoing mail server.\n        ', kind=None),
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
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
                                            Constant(value='testing', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='registry',
                                                ctx=Load(),
                                            ),
                                            attr='in_test_mode',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
