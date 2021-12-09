Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug', asname=None)],
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.link_tracker.tests.common',
            names=[alias(name='MockLinkTracker', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mail.tests.common',
            names=[
                alias(name='MailCase', asname=None),
                alias(name='MailCommon', asname=None),
                alias(name='mail_new_test_user', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.sql_db',
            names=[alias(name='Cursor', asname=None)],
            level=0,
        ),
        ClassDef(
            name='MassMailCase',
            bases=[
                Name(id='MailCase', ctx=Load()),
                Name(id='MockLinkTracker', ctx=Load()),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='assertMailingStatistics',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='mailing', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Helper to assert mailing statistics fields. As we have many of them\n        it helps lessening test asserts. ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='kwargs', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='expected', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='kwargs', ctx=Load()),
                                            slice=Constant(value='expected', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='mailing', ctx=Load()),
                                                attr='mailing_trace_ids',
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='kwargs', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='delivered', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='kwargs', ctx=Load()),
                                            slice=Constant(value='delivered', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='mailing', ctx=Load()),
                                                attr='mailing_trace_ids',
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
                        For(
                            target=Name(id='fname', ctx=Store()),
                            iter=List(
                                elts=[
                                    Constant(value='scheduled', kind=None),
                                    Constant(value='expected', kind=None),
                                    Constant(value='sent', kind=None),
                                    Constant(value='delivered', kind=None),
                                    Constant(value='opened', kind=None),
                                    Constant(value='replied', kind=None),
                                    Constant(value='clicked', kind=None),
                                    Constant(value='canceled', kind=None),
                                    Constant(value='failed', kind=None),
                                    Constant(value='bounced', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='mailing', ctx=Load()),
                                                slice=Name(id='fname', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='fname', ctx=Load()),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            BinOp(
                                                left=Constant(value='Mailing %s statistics failed: got %s instead of %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='fname', ctx=Load()),
                                                        Subscript(
                                                            value=Name(id='mailing', ctx=Load()),
                                                            slice=Name(id='fname', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='kwargs', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(id='fname', ctx=Load()),
                                                                Constant(value=0, kind=None),
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
                    name='assertMailTraces',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='recipients_info', annotation=None, type_comment=None),
                            arg(arg='mailing', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='check_mail', annotation=None, type_comment=None),
                            arg(arg='sent_unlink', annotation=None, type_comment=None),
                            arg(arg='author', annotation=None, type_comment=None),
                            arg(arg='mail_links_info', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Check content of traces. Traces are fetched based on a given mailing\n        and records. Their content is compared to recipients_info structure that\n        holds expected information. Links content may be checked, notably to\n        assert shortening or unsubscribe links. Mail.mail records may optionally\n        be checked.\n\n        :param recipients_info: list[{\n            # TRACE\n            'partner': res.partner record (may be empty),\n            'email': email used when sending email (may be empty, computed based on partner),\n            'trace_status': outgoing / sent / open / reply / bounce / error / cancel (sent by default),\n            'record: linked record,\n            # MAIL.MAIL\n            'content': optional content that should be present in mail.mail body_html;\n            'failure_type': optional failure reason;\n            }, { ... }]\n\n        :param mailing: a mailing.mailing record from which traces have been\n          generated;\n        :param records: records given to mailing that generated traces. It is\n          used notably to find traces using their IDs;\n        :param check_mail: if True, also check mail.mail records that should be\n          linked to traces;\n        :param sent_unlink: it True, sent mail.mail are deleted and we check gateway\n          output result instead of actual mail.mail records;\n        :param mail_links_info: if given, should follow order of ``recipients_info``\n          and give details about links. See ``assertLinkShortenedHtml`` helper for\n          more details about content to give;\n        :param author: author of sent mail.mail;\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='state_mapping', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='sent', kind=None),
                                    Constant(value='open', kind=None),
                                    Constant(value='reply', kind=None),
                                    Constant(value='error', kind=None),
                                    Constant(value='cancel', kind=None),
                                    Constant(value='bounce', kind=None),
                                ],
                                values=[
                                    Constant(value='sent', kind=None),
                                    Constant(value='sent', kind=None),
                                    Constant(value='sent', kind=None),
                                    Constant(value='exception', kind=None),
                                    Constant(value='cancel', kind=None),
                                    Constant(value='cancel', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='traces', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.trace', kind=None),
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
                                                    Constant(value='mass_mailing_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='mailing', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='records', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Attribute(
                                                        value=Name(id='s', ctx=Load()),
                                                        attr='model',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='records', ctx=Load()),
                                                            attr='_name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='s', ctx=Store()),
                                                        iter=Name(id='traces', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='s', ctx=Load()),
                                                    attr='res_id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='s', ctx=Store()),
                                                        iter=Name(id='traces', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='records', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='mail_links_info', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='mail_links_info', ctx=Store())],
                                    value=BinOp(
                                        left=List(
                                            elts=[Constant(value=None, kind=None)],
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='recipients_info', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='recipient_info', ctx=Store()),
                                    Name(id='link_info', ctx=Store()),
                                    Name(id='record', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='recipients_info', ctx=Load()),
                                    Name(id='mail_links_info', ctx=Load()),
                                    Name(id='records', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partner', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='recipient_info', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='partner', kind=None),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='email', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='recipient_info', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='email', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='status', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='recipient_info', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='trace_status', kind=None),
                                            Constant(value='sent', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='record', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='record', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='recipient_info', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='record', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='content', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='recipient_info', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='content', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='email', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Name(id='partner', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='email', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='email_normalized',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='recipient_trace', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='traces', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='t', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='t', ctx=Load()),
                                                                        attr='email',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Name(id='email', ctx=Load())],
                                                                ),
                                                                BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        UnaryOp(
                                                                            op=Not(),
                                                                            operand=Name(id='email', ctx=Load()),
                                                                        ),
                                                                        UnaryOp(
                                                                            op=Not(),
                                                                            operand=Attribute(
                                                                                value=Name(id='t', ctx=Load()),
                                                                                attr='email',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='t', ctx=Load()),
                                                                attr='trace_status',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Name(id='status', ctx=Load())],
                                                        ),
                                                        IfExp(
                                                            test=Name(id='record', ctx=Load()),
                                                            body=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='t', ctx=Load()),
                                                                    attr='res_id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            orelse=Constant(value=True, kind=None),
                                                        ),
                                                    ],
                                                ),
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='recipient_trace', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            BinOp(
                                                left=Constant(value='MailTrace: email %s (recipient %s, status: %s, record: %s): found %s records (1 expected)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='email', ctx=Load()),
                                                        Name(id='partner', ctx=Load()),
                                                        Name(id='status', ctx=Load()),
                                                        Name(id='record', ctx=Load()),
                                                        Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='recipient_trace', ctx=Load())],
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='recipient_trace', ctx=Load()),
                                                        attr='mail_mail_id_int',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Constant(value='failure_type', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='recipient_info', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Name(id='status', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='error', kind=None),
                                                            Constant(value='cancel', kind=None),
                                                            Constant(value='bounce', kind=None),
                                                        ],
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
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='recipient_trace', ctx=Load()),
                                                        attr='failure_type',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='recipient_info', ctx=Load()),
                                                        slice=Constant(value='failure_type', kind=None),
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
                                    test=Name(id='check_mail', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='author', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='author', ctx=Store())],
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
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='fields_values', ctx=Store())],
                                            value=Dict(
                                                keys=[Constant(value='mailing_id', kind=None)],
                                                values=[Name(id='mailing', ctx=Load())],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='partner', ctx=Load()),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='status', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='sent', kind=None)],
                                                            ),
                                                            Name(id='sent_unlink', ctx=Load()),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertSentEmail',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='author', ctx=Load()),
                                                                    List(
                                                                        elts=[Name(id='partner', ctx=Load())],
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
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertMailMail',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='partner', ctx=Load()),
                                                                    Subscript(
                                                                        value=Name(id='state_mapping', ctx=Load()),
                                                                        slice=Name(id='status', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='author',
                                                                        value=Name(id='author', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='content',
                                                                        value=Name(id='content', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='fields_values',
                                                                        value=Name(id='fields_values', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='email', ctx=Load()),
                                                            ),
                                                            Compare(
                                                                left=Name(id='status', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='cancel', kind=None),
                                                                            Constant(value='bounce', kind=None),
                                                                        ],
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
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertMailMailWId',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='recipient_trace', ctx=Load()),
                                                                        attr='mail_mail_id_int',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Name(id='state_mapping', ctx=Load()),
                                                                        slice=Name(id='status', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='content',
                                                                        value=Name(id='content', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='fields_values',
                                                                        value=Name(id='fields_values', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertMailMailWEmails',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[Name(id='email', ctx=Load())],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Name(id='state_mapping', ctx=Load()),
                                                                        slice=Name(id='status', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='author',
                                                                        value=Name(id='author', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='content',
                                                                        value=Name(id='content', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='fields_values',
                                                                        value=Name(id='fields_values', ctx=Load()),
                                                                    ),
                                                                ],
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
                                    test=Name(id='link_info', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='trace_mail', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_find_mail_mail_wrecord',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='record', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='anchor_id', ctx=Store()),
                                                    Name(id='url', ctx=Store()),
                                                    Name(id='is_shortened', ctx=Store()),
                                                    Name(id='add_link_params', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Name(id='link_info', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='link_params', ctx=Store())],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='utm_medium', kind=None),
                                                            Constant(value='utm_source', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='Email', kind=None),
                                                            Attribute(
                                                                value=Name(id='mailing', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='add_link_params', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='link_params', ctx=Load()),
                                                                    attr='update',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg=None,
                                                                        value=Name(id='add_link_params', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertLinkShortenedHtml',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='trace_mail', ctx=Load()),
                                                                attr='body_html',
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='anchor_id', ctx=Load()),
                                                                    Name(id='url', ctx=Load()),
                                                                    Name(id='is_shortened', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='link_params',
                                                                value=Name(id='link_params', ctx=Load()),
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
                    name='gateway_mail_bounce',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='mailing', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='bounce_base_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Generate a bounce at mailgateway level.\n\n        :param mailing: a ``mailing.mailing`` record on which we find a trace\n          to bounce;\n        :param record: record which should bounce;\n        :param bounce_base_values: optional values given to routing;\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='trace', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='mailing', ctx=Load()),
                                        attr='mailing_trace_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='t', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='t', ctx=Load()),
                                                        attr='model',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='_name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='t', ctx=Load()),
                                                        attr='res_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='parsed_bounce_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='email_from', kind=None),
                                    Constant(value='to', kind=None),
                                    Constant(value='message_id', kind=None),
                                    Constant(value='bounced_partner', kind=None),
                                    Constant(value='bounced_message', kind=None),
                                ],
                                values=[
                                    Constant(value='some.email@external.example.com', kind=None),
                                    Constant(value='bounce@test.example.com', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='generate_tracking_message_id',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='MailTest', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mail.message', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='bounce_base_values', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='parsed_bounce_values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='bounce_base_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parsed_bounce_values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='bounced_email', kind=None),
                                            Constant(value='bounced_msg_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='trace', ctx=Load()),
                                                attr='email',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='trace', ctx=Load()),
                                                        attr='message_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
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
                                    attr='_routing_handle_bounce',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=False, kind=None),
                                    Name(id='parsed_bounce_values', ctx=Load()),
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
                    name='gateway_mail_click',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='mailing', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='click_label', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Simulate a click on a sent email. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='trace', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='mailing', ctx=Load()),
                                        attr='mailing_trace_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='t', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='t', ctx=Load()),
                                                        attr='model',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='_name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='t', ctx=Load()),
                                                        attr='res_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='email', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_find_sent_mail_wemail',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='trace', ctx=Load()),
                                        attr='email',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[Name(id='email', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='_url_href', ctx=Store()),
                                    Name(id='link_url', ctx=Store()),
                                    Name(id='_dummy', ctx=Store()),
                                    Name(id='label', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='findall',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='tools', ctx=Load()),
                                        attr='HTML_TAG_URL_REGEX',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='email', ctx=Load()),
                                        slice=Constant(value='body', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='label', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Name(id='click_label', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='/r/', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='link_url', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
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
                                                args=[Name(id='link_url', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='path_items', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='parsed_url', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='code', ctx=Store()),
                                                        Name(id='trace_id', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Name(id='path_items', ctx=Load()),
                                                        slice=Constant(value=2, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='path_items', ctx=Load()),
                                                                slice=Constant(value=4, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='trace', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='trace_id', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
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
                                                                slice=Constant(value='link.tracker.click', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='add_click',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='code', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='ip',
                                                        value=BinOp(
                                                            left=Constant(value='100.200.300.%3f', kind=None),
                                                            op=Mod(),
                                                            right=Call(
                                                                func=Attribute(
                                                                    value=Name(id='random', ctx=Load()),
                                                                    attr='random',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='country_code',
                                                        value=Constant(value='BE', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='mailing_trace_id',
                                                        value=Attribute(
                                                            value=Name(id='trace', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Break(),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AssertionError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='url %s not found in mailing %s for record %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='click_label', ctx=Load()),
                                                        Name(id='mailing', ctx=Load()),
                                                        Name(id='record', ctx=Load()),
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_bounce_trace',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='mailing', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='dt', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='email_normalized', kind=None),
                                ops=[In()],
                                comparators=[Name(id='record', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='trace_email', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='email_normalized',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Constant(value='email_from', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='record', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='trace_email', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='email_from',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='trace_email', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='email',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='dt', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='dt', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='datetime',
                                                    ctx=Load(),
                                                ),
                                                attr='now',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='datetime', ctx=Load()),
                                                attr='timedelta',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Constant(value=1, kind=None),
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
                            targets=[Name(id='randomized', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='random', ctx=Load()),
                                    attr='random',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='Cursor', ctx=Load()),
                                            Constant(value='now', kind=None),
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[],
                                                    vararg=arg(arg='args', annotation=None, type_comment=None),
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                                    defaults=[],
                                                ),
                                                body=Name(id='dt', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='trace', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='mailing.trace', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='mass_mailing_id', kind=None),
                                                    Constant(value='model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='trace_status', kind=None),
                                                    Constant(value='email', kind=None),
                                                    Constant(value='message_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='mailing', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='_name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='bounce', kind=None),
                                                    Name(id='trace_email', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='<%5f@gilbert.boitempomils>', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='randomized', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='trace', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='MassMailCommon',
            bases=[
                Name(id='MailCommon', ctx=Load()),
                Name(id='MassMailCase', ctx=Load()),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                            Name(id='MassMailCommon', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_marketing',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='mail_new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='user_marketing', kind=None),
                                    ),
                                    keyword(
                                        arg='groups',
                                        value=Constant(value='base.group_user,base.group_partner_manager,mass_mailing.group_mass_mailing_user', kind=None),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='Martial Marketing', kind=None),
                                    ),
                                    keyword(
                                        arg='signature',
                                        value=Constant(value='--\nMartial', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='email_reply_to',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='MyCompany SomehowAlias <test.alias@test.mycompany.com>', kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_mailing_list',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Shortcut to create mailing lists. Currently hardcoded, maybe evolve\n        in a near future. ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='mailing_list_1',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mailing.list', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='_test_context',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='contact_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='List1', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='email', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Déboulonneur', kind=None),
                                                                    Constant(value='fleurus@example.com', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='email', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Gorramts', kind=None),
                                                                    Constant(value='gorramts@example.com', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='email', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Ybrant', kind=None),
                                                                    Constant(value='ybrant@example.com', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
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
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='mailing_list_2',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mailing.list', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='_test_context',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='contact_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='List2', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='email', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Gilberte', kind=None),
                                                                    Constant(value='gilberte@example.com', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='email', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Gilberte En Mieux', kind=None),
                                                                    Constant(value='gilberte@example.com', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='email', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Norbert', kind=None),
                                                                    Constant(value='norbert@example.com', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='email', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Ybrant', kind=None),
                                                                    Constant(value='ybrant@example.com', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_mailing_list_of_x_contacts',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='contacts_nbr', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Shortcut to create a mailing list that contains a defined number\n        of contacts. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mailing.list', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='_test_context',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='contact_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test List', kind=None),
                                            ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='name', kind=None),
                                                                Constant(value='email', kind=None),
                                                            ],
                                                            values=[
                                                                BinOp(
                                                                    left=Constant(value='Contact %s', kind=None),
                                                                    op=Mod(),
                                                                    right=Name(id='i', ctx=Load()),
                                                                ),
                                                                BinOp(
                                                                    left=Constant(value='contact%s@example.com', kind=None),
                                                                    op=Mod(),
                                                                    right=Name(id='i', ctx=Load()),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='i', ctx=Store()),
                                                        iter=Call(
                                                            func=Name(id='range', ctx=Load()),
                                                            args=[Name(id='contacts_nbr', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
