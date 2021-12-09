Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mass_mailing.tests.common',
            names=[alias(name='MassMailCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.sms.tests.common',
            names=[
                alias(name='SMSCase', asname=None),
                alias(name='SMSCommon', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='MassSMSCase',
            bases=[Name(id='SMSCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='assertSMSStatistics',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='recipients_info', annotation=None, type_comment=None),
                            arg(arg='mailing', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='check_sms', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Deprecated, remove in 14.4 ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMSTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='recipients_info', ctx=Load()),
                                    Name(id='mailing', ctx=Load()),
                                    Name(id='records', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='check_sms',
                                        value=Name(id='check_sms', ctx=Load()),
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
                    name='assertSMSTraces',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='recipients_info', annotation=None, type_comment=None),
                            arg(arg='mailing', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='check_sms', annotation=None, type_comment=None),
                            arg(arg='sent_unlink', annotation=None, type_comment=None),
                            arg(arg='sms_links_info', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Check content of traces. Traces are fetched based on a given mailing\n        and records. Their content is compared to recipients_info structure that\n        holds expected information. Links content may be checked, notably to\n        assert shortening or unsubscribe links. Sms.sms records may optionally\n        be checked.\n\n        :param recipients_info: list[{\n          # TRACE\n          'partner': res.partner record (may be empty),\n          'number': number used for notification (may be empty, computed based on partner),\n          'trace_status': outgoing / sent / cancel / bounce / error / opened (sent by default),\n          'record: linked record,\n          # SMS.SMS\n          'content': optional: if set, check content of sent SMS;\n          'failure_type': error code linked to sms failure (see ``error_code``\n            field on ``sms.sms`` model);\n          },\n          { ... }];\n        :param mailing: a mailing.mailing record from which traces have been\n          generated;\n        :param records: records given to mailing that generated traces. It is\n          used notably to find traces using their IDs;\n        :param check_sms: if set, check sms.sms records that should be linked to traces;\n        :param sent_unlink: it True, sent sms.sms are deleted and we check gateway\n          output result instead of actual sms.sms records;\n        :param sms_links_info: if given, should follow order of ``recipients_info``\n          and give details about links. See ``assertLinkShortenedHtml`` helper for\n          more details about content to give;\n        ]\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='state_mapping', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='sent', kind=None),
                                    Constant(value='outgoing', kind=None),
                                    Constant(value='error', kind=None),
                                    Constant(value='cancel', kind=None),
                                    Constant(value='bounce', kind=None),
                                ],
                                values=[
                                    Constant(value='sent', kind=None),
                                    Constant(value='outgoing', kind=None),
                                    Constant(value='error', kind=None),
                                    Constant(value='canceled', kind=None),
                                    Constant(value='error', kind=None),
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
                                operand=Name(id='sms_links_info', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sms_links_info', ctx=Store())],
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
                                    Name(id='sms_links_info', ctx=Load()),
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
                                    targets=[Name(id='number', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='recipient_info', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='number', kind=None)],
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
                                            Constant(value='outgoing', kind=None),
                                        ],
                                        keywords=[],
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
                                        args=[
                                            Constant(value='content', kind=None),
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
                                            Compare(
                                                left=Name(id='number', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Name(id='partner', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='number', ctx=Store())],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='_sms_get_recipients_info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    slice=Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='sanitized', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='trace', ctx=Store())],
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
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='t', ctx=Load()),
                                                                attr='sms_number',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Name(id='number', ctx=Load())],
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
                                                    args=[Name(id='trace', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            BinOp(
                                                left=Constant(value='SMS: found %s notification for number %s, (status: %s) (1 expected)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='trace', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        Name(id='number', ctx=Load()),
                                                        Name(id='status', ctx=Load()),
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
                                                        value=Name(id='trace', ctx=Load()),
                                                        attr='sms_sms_id_int',
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
                                    test=Name(id='check_sms', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='status', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='sent', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=Name(id='sent_unlink', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertSMSIapSent',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[Name(id='number', ctx=Load())],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='content',
                                                                        value=Name(id='content', ctx=Load()),
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
                                                                    attr='assertSMS',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='partner', ctx=Load()),
                                                                    Name(id='number', ctx=Load()),
                                                                    Constant(value='sent', kind=None),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='content',
                                                                        value=Name(id='content', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='status', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='state_mapping', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='sms_state', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='state_mapping', ctx=Load()),
                                                                slice=Name(id='status', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='failure_type', ctx=Store())],
                                                            value=IfExp(
                                                                test=Compare(
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
                                                                body=Subscript(
                                                                    value=Name(id='recipient_info', ctx=Load()),
                                                                    slice=Constant(value='failure_type', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                orelse=Constant(value=None, kind=None),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertSMS',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='partner', ctx=Load()),
                                                                    Name(id='number', ctx=Load()),
                                                                    Name(id='sms_state', ctx=Load()),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='failure_type',
                                                                        value=Name(id='failure_type', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='content',
                                                                        value=Name(id='content', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='NotImplementedError', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            cause=None,
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
                                            targets=[Name(id='sms_sent', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_find_sms_sent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='partner', ctx=Load()),
                                                    Name(id='number', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='sms_sms', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_find_sms_sms',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='partner', ctx=Load()),
                                                    Name(id='number', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='state_mapping', ctx=Load()),
                                                        slice=Name(id='status', ctx=Load()),
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
                                                    Name(id='url', ctx=Store()),
                                                    Name(id='is_shortened', ctx=Store()),
                                                    Name(id='add_link_params', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Name(id='link_info', ctx=Load()),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='url', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='unsubscribe', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='url', ctx=Store())],
                                                            value=BinOp(
                                                                left=Constant(value='%s/sms/%d/%s', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='mailing', ctx=Load()),
                                                                                attr='get_base_url',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='mailing', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='trace', ctx=Load()),
                                                                            attr='sms_code',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='link_params', ctx=Store())],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='utm_medium', kind=None),
                                                            Constant(value='utm_source', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='SMS', kind=None),
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
                                                            attr='assertLinkShortenedText',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='sms_sms', ctx=Load()),
                                                                attr='body',
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
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
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertLinkShortenedText',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='sms_sent', ctx=Load()),
                                                                slice=Constant(value='body', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
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
                    name='gateway_sms_click',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='mailing', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Simulate a click on a sent SMS. Usage: giving a partner and/or\n        a number, find an SMS sent to him, find shortened links in its body\n        and call add_click to simulate a click. ', kind=None),
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
                            targets=[Name(id='sms_sent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_find_sms_sent',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='trace', ctx=Load()),
                                        attr='sms_number',
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
                                        args=[Name(id='sms_sent', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='gateway_sms_sent_click',
                                    ctx=Load(),
                                ),
                                args=[Name(id='sms_sent', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='gateway_sms_sent_click',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sms_sent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" When clicking on a link in a SMS we actually don't have any\n        easy information in body, only body. We currently click on all found\n        shortened links. ", kind=None),
                        ),
                        For(
                            target=Name(id='url', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='findall',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='tools', ctx=Load()),
                                        attr='TEXT_URL_REGEX',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='sms_sent', ctx=Load()),
                                        slice=Constant(value='body', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='/r/', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='url', ctx=Load())],
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
                                                args=[Name(id='url', ctx=Load())],
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
                                                        Name(id='sms_sms_id', ctx=Store()),
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
                                        Assign(
                                            targets=[Name(id='trace_id', ctx=Store())],
                                            value=Attribute(
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
                                                                    slice=Constant(value='mailing.trace', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='sudo',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        attr='search',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='sms_sms_id_int', kind=None),
                                                                        Constant(value='=', kind=None),
                                                                        Name(id='sms_sms_id', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
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
                                                        value=Constant(value='100.200.300.400', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='country_code',
                                                        value=Constant(value='BE', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='mailing_trace_id',
                                                        value=Name(id='trace_id', ctx=Load()),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='MassSMSCommon',
            bases=[
                Name(id='MassMailCommon', ctx=Load()),
                Name(id='SMSCommon', ctx=Load()),
                Name(id='MassSMSCase', ctx=Load()),
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
                                            Name(id='MassSMSCommon', ctx=Load()),
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
