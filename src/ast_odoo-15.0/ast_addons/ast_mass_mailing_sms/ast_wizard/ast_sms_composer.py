Module(
    body=[
        Import(
            names=[alias(name='werkzeug.urls', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='SMSComposer',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='sms.composer', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mass_sms_allow_unsubscribe', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Include opt-out link', kind=None)],
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
                    targets=[Name(id='mailing_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='mailing.mailing', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Mailing', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='utm_campaign_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='utm.campaign', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Campaign', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_unsubscribe_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='trace_code', annotation=None, type_comment=None),
                            arg(arg='number', annotation=None, type_comment=None),
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
                                    value=Attribute(
                                        value=Name(id='werkzeug', ctx=Load()),
                                        attr='urls',
                                        ctx=Load(),
                                    ),
                                    attr='url_join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_base_url',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=Constant(value='/sms/%s/%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='mailing_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Name(id='trace_code', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
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
                    name='_prepare_mass_sms_trace_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='sms_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='trace_code', ctx=Store())],
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
                                    attr='_get_random_code',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='trace_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='model', kind=None),
                                    Constant(value='res_id', kind=None),
                                    Constant(value='trace_type', kind=None),
                                    Constant(value='mass_mailing_id', kind=None),
                                    Constant(value='sms_number', kind=None),
                                    Constant(value='sms_code', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='res_model',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='sms', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mailing_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='sms_values', ctx=Load()),
                                        slice=Constant(value='number', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='trace_code', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='sms_values', ctx=Load()),
                                    slice=Constant(value='state', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='error', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='trace_values', ctx=Load()),
                                            slice=Constant(value='failure_type', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='sms_values', ctx=Load()),
                                        slice=Constant(value='failure_type', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='trace_values', ctx=Load()),
                                            slice=Constant(value='trace_status', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='error', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='sms_values', ctx=Load()),
                                            slice=Constant(value='state', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='canceled', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='trace_values', ctx=Load()),
                                                    slice=Constant(value='failure_type', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='sms_values', ctx=Load()),
                                                slice=Constant(value='failure_type', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='trace_values', ctx=Load()),
                                                    slice=Constant(value='trace_status', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='cancel', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='mass_sms_allow_unsubscribe',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='sms_values', ctx=Load()),
                                                            slice=Constant(value='body', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=BinOp(
                                                        left=Constant(value='%s\n%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Subscript(
                                                                            value=Name(id='sms_values', ctx=Load()),
                                                                            slice=Constant(value='body', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        Constant(value='', kind=None),
                                                                    ],
                                                                ),
                                                                Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[
                                                                        Constant(value='STOP SMS : %s', kind=None),
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='_get_unsubscribe_url',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='record', ctx=Load()),
                                                                                    attr='id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Name(id='trace_code', ctx=Load()),
                                                                                Subscript(
                                                                                    value=Name(id='sms_values', ctx=Load()),
                                                                                    slice=Constant(value='number', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
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
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='trace_values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_optout_record_ids',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='recipients_info', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Fetch opt-out records based on mailing. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SMSComposer', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_optout_record_ids',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='records', ctx=Load()),
                                    Name(id='recipients_info', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='mailing_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='optout_res_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='mailing_id',
                                                ctx=Load(),
                                            ),
                                            attr='_get_opt_out_list_sms',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='res', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='optout_res_ids', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_done_record_ids',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='recipients_info', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' A/B testing could lead to records having been already mailed. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SMSComposer', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_done_record_ids',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='records', ctx=Load()),
                                    Name(id='recipients_info', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='mailing_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='seen_ids', ctx=Store()),
                                                Name(id='seen_list', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='mailing_id',
                                                ctx=Load(),
                                            ),
                                            attr='_get_seen_list_sms',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='res', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='seen_ids', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_body_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='all_bodies', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SMSComposer', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_prepare_body_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='records', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='mailing_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='tracker_values', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='mailing_id',
                                                ctx=Load(),
                                            ),
                                            attr='_get_link_tracker_values',
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
                                            Name(id='sms_id', ctx=Store()),
                                            Name(id='body', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='all_bodies', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='body', ctx=Store())],
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
                                                                slice=Constant(value='mail.render.mixin', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='_shorten_links_text',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='body', ctx=Load()),
                                                    Name(id='tracker_values', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='all_bodies', ctx=Load()),
                                                    slice=Name(id='sms_id', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='body', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='all_bodies', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_mass_sms_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SMSComposer', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_prepare_mass_sms_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='records', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='composition_mode',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='mass', kind=None)],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mailing_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='records', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='sms_values', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='trace_values', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_prepare_mass_sms_trace_values',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='record', ctx=Load()),
                                                    Name(id='sms_values', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sms_values', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='mailing_id', kind=None),
                                                            Constant(value='mailing_trace_ids', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='mailing_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Name(id='trace_values', ctx=Load()),
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
                                        ),
                                    ],
                                    orelse=[],
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
                FunctionDef(
                    name='_prepare_mass_sms',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='sms_record_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='sms_all', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SMSComposer', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_prepare_mass_sms',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='records', ctx=Load()),
                                    Name(id='sms_record_values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='mailing_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='updated_bodies', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sms_all', ctx=Load()),
                                            attr='_update_body_short_links',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='sms', ctx=Store()),
                                    iter=Name(id='sms_all', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='sms', ctx=Load()),
                                                    attr='body',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='updated_bodies', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='sms', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='sms_all', ctx=Load()),
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
