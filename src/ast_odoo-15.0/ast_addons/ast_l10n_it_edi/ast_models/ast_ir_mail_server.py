Module(
    body=[
        Import(
            names=[alias(name='zipfile', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='email', asname=None)],
        ),
        Import(
            names=[alias(name='email.policy', asname=None)],
        ),
        Import(
            names=[alias(name='dateutil', asname=None)],
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='xmlrpc',
            names=[alias(name='client', asname='xmlrpclib')],
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
            names=[
                alias(name='ValidationError', asname=None),
                alias(name='UserError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.l10n_it_edi.tools.remove_signature',
            names=[alias(name='remove_signature', asname=None)],
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
        ClassDef(
            name='FetchmailServer',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='fetchmail.server', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='fetchmail.server', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_is_pec', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='PEC server', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value="If PEC Server, only mail from '...@pec.fatturapa.it' will be processed.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_last_uid', ctx=Store())],
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
                                value=Constant(value='Last message UID IT', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_edi_invoice',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='att_name', annotation=None, type_comment=None),
                            arg(arg='send_state', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Search sent l10n_it_edi fatturaPA invoices ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='conditions', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='move_id', kind=None),
                                            Constant(value='!=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='edi_format_id.code', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='fattura_pa', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='attachment_id.name', kind=None),
                                            Constant(value='=', kind=None),
                                            Name(id='att_name', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='send_state', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='conditions', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='move_id.l10n_it_send_state', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='send_state', ctx=Load()),
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
                        Return(
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='account.edi.document', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='conditions', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='limit',
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                ),
                                attr='move_id',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_pec',
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
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='l10n_it_is_pec',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='server_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='imap', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='PEC mail server must be of type IMAP.', kind=None)],
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
                                Constant(value='l10n_it_is_pec', kind=None),
                                Constant(value='server_type', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='fetch_mail',
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
                            value=Constant(value=' WARNING: meant for cron usage only - will commit() after each email! ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='MailThread', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='mail.thread', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='server', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='s', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='s', ctx=Load()),
                                            attr='l10n_it_is_pec',
                                            ctx=Load(),
                                        ),
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
                                            Constant(value='start checking for new emails on %s PEC server %s', kind=None),
                                            Attribute(
                                                value=Name(id='server', ctx=Load()),
                                                attr='server_type',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='server', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='count', ctx=Store()),
                                                Name(id='failed', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='imap_server', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='imap_server', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='server', ctx=Load()),
                                                    attr='connect',
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
                                                    value=Name(id='imap_server', ctx=Load()),
                                                    attr='select',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='email_filter', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value='(UID %s:*)', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='server', ctx=Load()),
                                                            attr='l10n_it_last_uid',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='bypass_incoming_address_filter', ctx=Store())],
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
                                                    Constant(value='l10n_it_edi.bypass_incoming_address_filter', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='bypass_incoming_address_filter', ctx=Load()),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='email_filter', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='(FROM "@pec.fatturapa.it")', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='data', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='imap_server', ctx=Load()),
                                                        attr='uid',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='search', kind=None),
                                                        Constant(value=None, kind=None),
                                                        Starred(
                                                            value=Name(id='email_filter', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='new_max_uid', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='server', ctx=Load()),
                                                attr='l10n_it_last_uid',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='uid', ctx=Store()),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Name(id='int', ctx=Load()),
                                                            args=[Name(id='uid', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        ops=[LtE()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='server', ctx=Load()),
                                                                attr='l10n_it_last_uid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[Continue()],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='result', ctx=Store()),
                                                                Name(id='data', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='imap_server', ctx=Load()),
                                                            attr='uid',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='fetch', kind=None),
                                                            Name(id='uid', ctx=Load()),
                                                            Constant(value='(RFC822)', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Subscript(
                                                            value=Name(id='data', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    body=[Continue()],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='message', ctx=Store())],
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='data', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Constant(value='Seen', kind=None),
                                                        ops=[NotIn()],
                                                        comparators=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='data', ctx=Load()),
                                                                        slice=Constant(value=1, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='decode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='utf-8', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='imap_server', ctx=Load()),
                                                                    attr='uid',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='STORE', kind=None),
                                                                    Name(id='uid', ctx=Load()),
                                                                    Constant(value='+FLAGS', kind=None),
                                                                    Constant(value='\\Seen', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='imap_server', ctx=Load()),
                                                                    attr='uid',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='STORE', kind=None),
                                                                    Name(id='uid', ctx=Load()),
                                                                    Constant(value='-FLAGS', kind=None),
                                                                    Constant(value='\\Seen', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                If(
                                                    test=Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='message', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='xmlrpclib', ctx=Load()),
                                                                attr='Binary',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='message', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='bytes', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='message', ctx=Load()),
                                                                        attr='data',
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
                                                            Name(id='message', ctx=Load()),
                                                            Name(id='str', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='message', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='message', ctx=Load()),
                                                                    attr='encode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='utf-8', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='msg_txt', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='email', ctx=Load()),
                                                            attr='message_from_bytes',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='message', ctx=Load())],
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
                                                Try(
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_attachment_invoice',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='msg_txt', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='new_max_uid', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='max', ctx=Load()),
                                                                args=[
                                                                    Name(id='new_max_uid', ctx=Load()),
                                                                    Call(
                                                                        func=Name(id='int', ctx=Load()),
                                                                        args=[Name(id='uid', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
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
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='_logger', ctx=Load()),
                                                                            attr='info',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='Failed to process mail from %s server %s.', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='server', ctx=Load()),
                                                                                attr='server_type',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='server', ctx=Load()),
                                                                                attr='name',
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
                                                                AugAssign(
                                                                    target=Name(id='failed', ctx=Store()),
                                                                    op=Add(),
                                                                    value=Constant(value=1, kind=None),
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
                                                AugAssign(
                                                    target=Name(id='count', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='server', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='l10n_it_last_uid', kind=None)],
                                                        values=[Name(id='new_max_uid', ctx=Load())],
                                                    ),
                                                ],
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
                                                    Constant(value='Fetched %d email(s) on %s server %s; %d succeeded, %d failed.', kind=None),
                                                    Name(id='count', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='server', ctx=Load()),
                                                        attr='server_type',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='server', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Name(id='count', ctx=Load()),
                                                        op=Sub(),
                                                        right=Name(id='failed', ctx=Load()),
                                                    ),
                                                    Name(id='failed', ctx=Load()),
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
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='General failure when trying to fetch mail from %s server %s.', kind=None),
                                                            Attribute(
                                                                value=Name(id='server', ctx=Load()),
                                                                attr='server_type',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='server', ctx=Load()),
                                                                attr='name',
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
                                    finalbody=[
                                        If(
                                            test=Name(id='imap_server', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='imap_server', ctx=Load()),
                                                            attr='close',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='imap_server', ctx=Load()),
                                                            attr='logout',
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
                                                    value=Name(id='server', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        attr='Datetime',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='now',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='FetchmailServer', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='s', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=UnaryOp(
                                                            op=Not(),
                                                            operand=Attribute(
                                                                value=Name(id='s', ctx=Load()),
                                                                attr='l10n_it_is_pec',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='fetch_mail',
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
                    name='_attachment_invoice',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='msg_txt', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='parsed_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.thread', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_message_parse_extract_payload',
                                    ctx=Load(),
                                ),
                                args=[Name(id='msg_txt', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='body', ctx=Store()),
                                        Name(id='attachments', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='parsed_values', ctx=Load()),
                                        slice=Constant(value='body', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='parsed_values', ctx=Load()),
                                        slice=Constant(value='attachments', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='from_address', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='msg_txt', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='from', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attachment', ctx=Store()),
                            iter=Name(id='attachments', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='split_attachment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='attachment', ctx=Load()),
                                                attr='fname',
                                                ctx=Load(),
                                            ),
                                            attr='rpartition',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='.', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='split_attachment', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[Constant(value=3, kind=None)],
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
                                                    Constant(value='E-invoice filename not compliant: %s', kind=None),
                                                    Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='fname',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='attachment_name', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='split_attachment', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attachment_ext', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='split_attachment', ctx=Load()),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='split_underscore', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='attachment_name', ctx=Load()),
                                            attr='rsplit',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='_', kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='split_underscore', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[Constant(value=2, kind=None)],
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
                                                    Constant(value='E-invoice filename not compliant: %s', kind=None),
                                                    Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='fname',
                                                        ctx=Load(),
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
                                    test=Compare(
                                        left=Name(id='attachment_ext', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='zip', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='split_underscore', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value='RC', kind=None),
                                                            Constant(value='NS', kind=None),
                                                            Constant(value='MC', kind=None),
                                                            Constant(value='MT', kind=None),
                                                            Constant(value='EC', kind=None),
                                                            Constant(value='SE', kind=None),
                                                            Constant(value='NE', kind=None),
                                                            Constant(value='DT', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_message_receipt_invoice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='split_underscore', ctx=Load()),
                                                                slice=Constant(value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='attachment', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='att_filename', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='fname',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='match', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='re', ctx=Load()),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='([A-Z]{2}[A-Za-z0-9]{2,28}_[A-Za-z0-9]{0,5}.(xml.p7m|xml))', kind=None),
                                                            Name(id='att_filename', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='match', ctx=Load()),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Subscript(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='match', ctx=Load()),
                                                                            attr='groups',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='xml.p7m', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='att_content_data', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='remove_signature', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='attachment', ctx=Load()),
                                                                                attr='content',
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
                                                                        operand=Name(id='att_content_data', ctx=Load()),
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
                                                                                    Constant(value="E-invoice couldn't be read: %s", kind=None),
                                                                                    Name(id='att_filename', ctx=Load()),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        Continue(),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='att_filename', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='att_filename', ctx=Load()),
                                                                            attr='replace',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='.xml.p7m', kind=None),
                                                                            Constant(value='.xml', kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='att_content_data', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='attachment', ctx=Load()),
                                                                                attr='content',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='encode',
                                                                            ctx=Load(),
                                                                        ),
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
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_create_invoice_from_mail',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='att_content_data', ctx=Load()),
                                                            Name(id='att_filename', ctx=Load()),
                                                            Name(id='from_address', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='split_underscore', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='AT', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_message_AT_invoice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='attachment', ctx=Load())],
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
                                                            Constant(value='New E-invoice in zip file: %s', kind=None),
                                                            Attribute(
                                                                value=Name(id='attachment', ctx=Load()),
                                                                attr='fname',
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
                                                            attr='_create_invoice_from_mail_with_zip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='attachment', ctx=Load()),
                                                            Name(id='from_address', ctx=Load()),
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_invoice_from_mail',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='att_content_data', annotation=None, type_comment=None),
                            arg(arg='att_name', annotation=None, type_comment=None),
                            arg(arg='from_address', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Creates an invoice from the content of an email present in ir.attachments\n\n        :param att_content_data:   The 'utf-8' encoded bytes string representing the content of the attachment.\n        :param att_name:           The attachment's file name.\n        :param from_address:       The sender address of the email.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='invoices', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.move', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='existing', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.attachment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='att_name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='account.move', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='existing', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='E-invoice already exist: %s', kind=None),
                                            Name(id='att_name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='invoices', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.attachment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='raw', kind=None),
                                            Constant(value='res_model', kind=None),
                                            Constant(value='type', kind=None),
                                        ],
                                        values=[
                                            Name(id='att_name', ctx=Load()),
                                            Name(id='att_content_data', ctx=Load()),
                                            Constant(value='account.move', kind=None),
                                            Constant(value='binary', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='tree', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='att_content_data', ctx=Load())],
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='The xml file is badly formatted: %s', kind=None),
                                                    Name(id='att_name', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Name(id='invoices', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='invoices', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='l10n_it_edi.edi_fatturaPA', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_create_invoice_from_xml_tree',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='att_name', ctx=Load()),
                                    Name(id='tree', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='invoices', ctx=Load()),
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
                                            Constant(value='E-invoice not found in file: %s', kind=None),
                                            Name(id='att_name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='invoices', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='invoices', ctx=Load()),
                                    attr='l10n_it_send_state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='new', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='invoices', ctx=Load()),
                                    attr='invoice_source_email',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='from_address', ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='invoice', ctx=Store()),
                            iter=Name(id='invoices', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='no_new_invoice',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='default_res_id',
                                                        value=Attribute(
                                                            value=Name(id='invoice', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Original E-invoice XML file', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='attachment_ids',
                                                value=List(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='attachment', ctx=Load()),
                                                            attr='id',
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
                            orelse=[],
                            type_comment=None,
                        ),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='New E-invoices (%s), ids: %s', kind=None),
                                    Name(id='att_name', ctx=Load()),
                                    ListComp(
                                        elt=Attribute(
                                            value=Name(id='x', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Name(id='invoices', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='invoices', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_invoice_from_mail_with_zip',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attachment_zip', annotation=None, type_comment=None),
                            arg(arg='from_address', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='zipfile', ctx=Load()),
                                            attr='ZipFile',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='io', ctx=Load()),
                                                    attr='BytesIO',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='attachment_zip', ctx=Load()),
                                                        attr='content',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='z', ctx=Store()),
                                ),
                            ],
                            body=[
                                For(
                                    target=Name(id='att_name', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='z', ctx=Load()),
                                            attr='namelist',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='existing', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.attachment', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Name(id='att_name', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='res_model', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value='account.move', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='existing', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='E-invoice in zip file (%s) already exist: %s', kind=None),
                                                            Attribute(
                                                                value=Name(id='attachment_zip', ctx=Load()),
                                                                attr='fname',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='att_name', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='att_content', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='z', ctx=Load()),
                                                            attr='open',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='att_name', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='read',
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
                                                    attr='_create_invoice_from_mail',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='att_content', ctx=Load()),
                                                    Name(id='att_name', ctx=Load()),
                                                    Name(id='from_address', ctx=Load()),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_message_AT_invoice',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attachment_zip', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='zipfile', ctx=Load()),
                                            attr='ZipFile',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='io', ctx=Load()),
                                                    attr='BytesIO',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='attachment_zip', ctx=Load()),
                                                        attr='content',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='z', ctx=Store()),
                                ),
                            ],
                            body=[
                                For(
                                    target=Name(id='attachment_name', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='z', ctx=Load()),
                                            attr='namelist',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='split_name_attachment', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='attachment_name', ctx=Load()),
                                                    attr='rpartition',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='split_name_attachment', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Lt()],
                                                comparators=[Constant(value=3, kind=None)],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='split_underscore', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='split_name_attachment', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='rsplit',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='_', kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='split_underscore', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Lt()],
                                                comparators=[Constant(value=2, kind=None)],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='split_underscore', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='AT', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='attachment', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='z', ctx=Load()),
                                                                    attr='open',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='attachment_name', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='read',
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
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='New AT receipt for: %s', kind=None),
                                                            Subscript(
                                                                value=Name(id='split_underscore', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Try(
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='tree', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='etree', ctx=Load()),
                                                                    attr='fromstring',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='attachment', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
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
                                                                            attr='info',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='Error in decoding new receipt file: %s', kind=None),
                                                                            Name(id='attachment_name', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Return(value=None),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    finalbody=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='elements', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='tree', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='//NomeFile', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='elements', ctx=Load()),
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='elements', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='text',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='filename', ctx=Store())],
                                                            value=Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='elements', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='text',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[Return(value=None)],
                                                ),
                                                Assign(
                                                    targets=[Name(id='related_invoice', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_search_edi_invoice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='filename', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='related_invoice', ctx=Load()),
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
                                                                    Constant(value='Error: invoice not found for receipt file: %s', kind=None),
                                                                    Name(id='filename', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Return(value=None),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='related_invoice', ctx=Load()),
                                                            attr='l10n_it_send_state',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='failed_delivery', kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='info', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_return_multi_line_xml',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='tree', ctx=Load()),
                                                            List(
                                                                elts=[
                                                                    Constant(value='//IdentificativoSdI', kind=None),
                                                                    Constant(value='//DataOraRicezione', kind=None),
                                                                    Constant(value='//MessageId', kind=None),
                                                                    Constant(value='//PecMessageId', kind=None),
                                                                    Constant(value='//Note', kind=None),
                                                                ],
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
                                                            value=Name(id='related_invoice', ctx=Load()),
                                                            attr='message_post',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='body',
                                                                value=BinOp(
                                                                    left=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='ES certify that it has received the invoice and that the file                         could not be delivered to the addressee. <br/>%s', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    op=Mod(),
                                                                    right=Name(id='info', ctx=Load()),
                                                                ),
                                                            ),
                                                        ],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_message_receipt_invoice',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='receipt_type', annotation=None, type_comment=None),
                            arg(arg='attachment', annotation=None, type_comment=None),
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
                                Assign(
                                    targets=[Name(id='tree', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='content',
                                                        ctx=Load(),
                                                    ),
                                                    attr='encode',
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
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Error in decoding new receipt file: %s', kind=None),
                                                    Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='fname',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Dict(keys=[], values=[]),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='elements', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tree', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='//NomeFile', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='elements', ctx=Load()),
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='elements', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='text',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='filename', ctx=Store())],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Name(id='elements', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='text',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='receipt_type', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='RC', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='related_invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_search_edi_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='filename', ctx=Load()),
                                            Constant(value='sent', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='related_invoice', ctx=Load()),
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
                                                    Constant(value='Error: invoice not found for receipt file: %s', kind=None),
                                                    Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='fname',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(value=None),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='related_invoice', ctx=Load()),
                                            attr='l10n_it_send_state',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='delivered', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='info', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_return_multi_line_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='tree', ctx=Load()),
                                            List(
                                                elts=[
                                                    Constant(value='//IdentificativoSdI', kind=None),
                                                    Constant(value='//DataOraRicezione', kind=None),
                                                    Constant(value='//DataOraConsegna', kind=None),
                                                    Constant(value='//Note', kind=None),
                                                ],
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
                                            value=Name(id='related_invoice', ctx=Load()),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=BinOp(
                                                    left=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='E-Invoice is delivery to the destinatory:<br/>%s', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    op=Mod(),
                                                    right=Name(id='info', ctx=Load()),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='receipt_type', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='NS', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='related_invoice', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_search_edi_invoice',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='filename', ctx=Load()),
                                                    Constant(value='sent', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='related_invoice', ctx=Load()),
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
                                                            Constant(value='Error: invoice not found for receipt file: %s', kind=None),
                                                            Attribute(
                                                                value=Name(id='attachment', ctx=Load()),
                                                                attr='fname',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Return(value=None),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='related_invoice', ctx=Load()),
                                                    attr='l10n_it_send_state',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='invalid', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='error', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_return_error_xml',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='tree', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='related_invoice', ctx=Load()),
                                                    attr='message_post',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='body',
                                                        value=BinOp(
                                                            left=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Errors in the E-Invoice :<br/>%s', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            op=Mod(),
                                                            right=Name(id='error', ctx=Load()),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='related_invoice', ctx=Load()),
                                                    attr='activity_schedule',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mail.mail_activity_data_todo', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='summary',
                                                        value=Constant(value='Rejection notice', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=IfExp(
                                                            test=Attribute(
                                                                value=Name(id='related_invoice', ctx=Load()),
                                                                attr='invoice_user_id',
                                                                ctx=Load(),
                                                            ),
                                                            body=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='related_invoice', ctx=Load()),
                                                                    attr='invoice_user_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            orelse=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='user',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='receipt_type', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='MC', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='related_invoice', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_search_edi_invoice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='filename', ctx=Load()),
                                                            Constant(value='sent', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='related_invoice', ctx=Load()),
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
                                                                    Constant(value='Error: invoice not found for receipt file: %s', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='attachment', ctx=Load()),
                                                                        attr='fname',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Return(value=None),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='info', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_return_multi_line_xml',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='tree', ctx=Load()),
                                                            List(
                                                                elts=[
                                                                    Constant(value='//IdentificativoSdI', kind=None),
                                                                    Constant(value='//DataOraRicezione', kind=None),
                                                                    Constant(value='//Descrizione', kind=None),
                                                                    Constant(value='//MessageId', kind=None),
                                                                    Constant(value='//Note', kind=None),
                                                                ],
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
                                                            value=Name(id='related_invoice', ctx=Load()),
                                                            attr='message_post',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='body',
                                                                value=BinOp(
                                                                    left=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='The E-invoice is not delivered to the addressee. The Exchange System is                unable to deliver the file to the Public Administration. The Exchange System will                contact the PA to report the problem and request that they provide a solution.                 During the following 15 days, the Exchange System will try to forward the FatturaPA                file to the Administration in question again. More information:<br/>%s', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    op=Mod(),
                                                                    right=Name(id='info', ctx=Load()),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='receipt_type', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='NE', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='related_invoice', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_search_edi_invoice',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='filename', ctx=Load()),
                                                                    Constant(value='delivered', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='related_invoice', ctx=Load()),
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
                                                                            Constant(value='Error: invoice not found for receipt file: %s', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='attachment', ctx=Load()),
                                                                                attr='fname',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Return(value=None),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='elements', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='tree', ctx=Load()),
                                                                    attr='xpath',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='//Esito', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='elements', ctx=Load()),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='elements', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='text',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='elements', ctx=Load()),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='text',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='EC01', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='related_invoice', ctx=Load()),
                                                                                    attr='l10n_it_send_state',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Constant(value='delivered_accepted', kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='elements', ctx=Load()),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='text',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='EC02', kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[
                                                                                        Attribute(
                                                                                            value=Name(id='related_invoice', ctx=Load()),
                                                                                            attr='l10n_it_send_state',
                                                                                            ctx=Store(),
                                                                                        ),
                                                                                    ],
                                                                                    value=Constant(value='delivered_refused', kind=None),
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
                                                        Assign(
                                                            targets=[Name(id='info', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_return_multi_line_xml',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='tree', ctx=Load()),
                                                                    List(
                                                                        elts=[
                                                                            Constant(value='//Esito', kind=None),
                                                                            Constant(value='//Descrizione', kind=None),
                                                                            Constant(value='//IdentificativoSdI', kind=None),
                                                                            Constant(value='//DataOraRicezione', kind=None),
                                                                            Constant(value='//DataOraConsegna', kind=None),
                                                                            Constant(value='//Note', kind=None),
                                                                        ],
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
                                                                    value=Name(id='related_invoice', ctx=Load()),
                                                                    attr='message_post',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='body',
                                                                        value=BinOp(
                                                                            left=Call(
                                                                                func=Name(id='_', ctx=Load()),
                                                                                args=[Constant(value='Outcome notice: %s<br/>%s', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            op=Mod(),
                                                                            right=Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='related_invoice', ctx=Load()),
                                                                                        attr='l10n_it_send_state',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Name(id='info', ctx=Load()),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='related_invoice', ctx=Load()),
                                                                    attr='l10n_it_send_state',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='delivered_refused', kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='related_invoice', ctx=Load()),
                                                                            attr='activity_schedule',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='mail.mail_activity_todo', kind=None)],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='user_id',
                                                                                value=IfExp(
                                                                                    test=Attribute(
                                                                                        value=Name(id='related_invoice', ctx=Load()),
                                                                                        attr='invoice_user_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    body=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='related_invoice', ctx=Load()),
                                                                                            attr='invoice_user_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    orelse=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='env',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='user',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='summary',
                                                                                value=Constant(value='Outcome notice: Refused', kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='receipt_type', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='DT', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='related_invoice', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_search_edi_invoice',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='filename', ctx=Load()),
                                                                            Constant(value='delivered', kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=UnaryOp(
                                                                        op=Not(),
                                                                        operand=Name(id='related_invoice', ctx=Load()),
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
                                                                                    Constant(value='Error: invoice not found for receipt file: %s', kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='attachment', ctx=Load()),
                                                                                        attr='fname',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        Return(value=None),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='related_invoice', ctx=Load()),
                                                                            attr='l10n_it_send_state',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value='delivered_expired', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='info', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_return_multi_line_xml',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='tree', ctx=Load()),
                                                                            List(
                                                                                elts=[
                                                                                    Constant(value='//Descrizione', kind=None),
                                                                                    Constant(value='//IdentificativoSdI', kind=None),
                                                                                    Constant(value='//Note', kind=None),
                                                                                ],
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
                                                                            value=Name(id='related_invoice', ctx=Load()),
                                                                            attr='message_post',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='body',
                                                                                value=BinOp(
                                                                                    left=Call(
                                                                                        func=Name(id='_', ctx=Load()),
                                                                                        args=[Constant(value='Expiration of the maximum term for communication of acceptance/refusal:                 %s<br/>%s', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    op=Mod(),
                                                                                    right=Tuple(
                                                                                        elts=[
                                                                                            Name(id='filename', ctx=Load()),
                                                                                            Name(id='info', ctx=Load()),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_return_multi_line_xml',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                            arg(arg='element_tags', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='output_str', ctx=Store())],
                            value=Constant(value='<ul>', kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='element_tag', ctx=Store()),
                            iter=Name(id='element_tags', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='elements', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='element_tag', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='elements', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='element', ctx=Store()),
                                    iter=Name(id='elements', ctx=Load()),
                                    body=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='element', ctx=Load()),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='text', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Constant(value=' ', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='element', ctx=Load()),
                                                                        attr='text',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='split',
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
                                                AugAssign(
                                                    target=Name(id='output_str', ctx=Store()),
                                                    op=Add(),
                                                    value=BinOp(
                                                        left=Constant(value='<li>%s: %s</li>', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='element', ctx=Load()),
                                                                    attr='tag',
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='text', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Name(id='output_str', ctx=Load()),
                                op=Add(),
                                right=Constant(value='</ul>', kind=None),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_return_error_xml',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='output_str', ctx=Store())],
                            value=Constant(value='<ul>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='elements', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tree', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='//Errore', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='elements', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='element', ctx=Store()),
                            iter=Name(id='elements', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='descrizione', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value=' ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='element', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='text',
                                                        ctx=Load(),
                                                    ),
                                                    attr='split',
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
                                    test=Name(id='descrizione', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Name(id='output_str', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=Constant(value='<li>Errore %s: %s</li>', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Subscript(
                                                                value=Name(id='element', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='text',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='descrizione', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
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
                        Return(
                            value=BinOp(
                                left=Name(id='output_str', ctx=Load()),
                                op=Add(),
                                right=Constant(value='</ul>', kind=None),
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
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.mail_server', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.mail_server', kind=None),
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
                            targets=[Name(id='company', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.company', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='l10n_it_mail_pec_server_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='company', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_get_test_email_addresses',
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
                            targets=[Name(id='email_from', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='smtp_user',
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
                                                args=[Constant(value='Please configure Username for this Server PEC', kind=None)],
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
                            targets=[Name(id='email_to', ctx=Store())],
                            value=Attribute(
                                value=Name(id='company', ctx=Load()),
                                attr='l10n_it_address_recipient_fatturapa',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='email_to', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Please configure Government PEC-mail\tin company settings', kind=None)],
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
                                    Name(id='email_to', ctx=Load()),
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='wo_bounce_return_path', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='headers', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='headers', ctx=Load()),
                                            slice=Constant(value='Return-Path', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='email_from', ctx=Load()),
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
                                            Name(id='IrMailServer', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='build_email',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='email_from', ctx=Load()),
                                    Name(id='email_to', ctx=Load()),
                                    Name(id='subject', ctx=Load()),
                                    Name(id='body', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='email_cc',
                                        value=Name(id='email_cc', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='email_bcc',
                                        value=Name(id='email_bcc', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='reply_to',
                                        value=Name(id='reply_to', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='attachments',
                                        value=Name(id='attachments', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='message_id',
                                        value=Name(id='message_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='references',
                                        value=Name(id='references', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='object_id',
                                        value=Name(id='object_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='subtype',
                                        value=Name(id='subtype', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='headers',
                                        value=Name(id='headers', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='body_alternative',
                                        value=Name(id='body_alternative', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='subtype_alternative',
                                        value=Name(id='subtype_alternative', ctx=Load()),
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
