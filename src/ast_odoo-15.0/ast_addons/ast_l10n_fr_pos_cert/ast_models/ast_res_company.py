Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='api', asname=None),
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
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.fields',
            names=[
                alias(name='Datetime', asname=None),
                alias(name='Date', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='format_date', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        FunctionDef(
            name='ctx_tz',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='record', annotation=None, type_comment=None),
                    arg(arg='field', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='res_lang', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ctx', ctx=Store())],
                    value=Attribute(
                        value=Name(id='record', ctx=Load()),
                        attr='_context',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tz_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='pytz', ctx=Load()),
                            attr='timezone',
                            ctx=Load(),
                        ),
                        args=[
                            BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='ctx', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='tz', kind=None)],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='tz',
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
                    targets=[Name(id='timestamp', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='Datetime', ctx=Load()),
                            attr='from_string',
                            ctx=Load(),
                        ),
                        args=[
                            Subscript(
                                value=Name(id='record', ctx=Load()),
                                slice=Name(id='field', ctx=Load()),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=Name(id='ctx', ctx=Load()),
                            attr='get',
                            ctx=Load(),
                        ),
                        args=[Constant(value='lang', kind=None)],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res_lang', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_lang_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='ctx', ctx=Load()),
                                        slice=Constant(value='lang', kind=None),
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
                    test=Name(id='res_lang', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='timestamp', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='pytz', ctx=Load()),
                                        attr='utc',
                                        ctx=Load(),
                                    ),
                                    attr='localize',
                                    ctx=Load(),
                                ),
                                args=[Name(id='timestamp', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='is_dst',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='strftime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='timestamp', ctx=Load()),
                                            attr='astimezone',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='tz_name', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Name(id='res_lang', ctx=Load()),
                                                attr='date_format',
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Constant(value=' ', kind=None),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='res_lang', ctx=Load()),
                                            attr='time_format',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='Datetime', ctx=Load()),
                            attr='context_timestamp',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='record', ctx=Load()),
                            Name(id='timestamp', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='ResCompany',
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
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.company', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_fr_pos_cert_sequence_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.sequence', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='companies', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='company', ctx=Store()),
                            iter=Name(id='companies', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='company', ctx=Load()),
                                            attr='_is_accounting_unalterable',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='sequence_fields', ctx=Store())],
                                            value=List(
                                                elts=[Constant(value='l10n_fr_pos_cert_sequence_id', kind=None)],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='company', ctx=Load()),
                                                    attr='_create_secure_sequence',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='sequence_fields', ctx=Load())],
                                                keywords=[],
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
                            value=Name(id='companies', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResCompany', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='company', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='company', ctx=Load()),
                                            attr='_is_accounting_unalterable',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='sequence_fields', ctx=Store())],
                                            value=List(
                                                elts=[Constant(value='l10n_fr_pos_cert_sequence_id', kind=None)],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='company', ctx=Load()),
                                                    attr='_create_secure_sequence',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='sequence_fields', ctx=Load())],
                                                keywords=[],
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
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_action_check_pos_hash_integrity',
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
                        Return(
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
                                        args=[Constant(value='l10n_fr_pos_cert.action_report_pos_hash_integrity', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='report_action',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
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
                    name='_check_pos_hash_integrity',
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
                            value=Constant(value='Checks that all posted or invoiced pos orders have still the same data as when they were posted\n        and raises an error with the result.\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='build_order_info',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='order', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='entry_reference', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='(Receipt ref.: %s)', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='order_reference_string', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='pos_reference',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Name(id='entry_reference', ctx=Load()),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='pos_reference',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=List(
                                        elts=[
                                            Call(
                                                func=Name(id='ctx_tz', ctx=Load()),
                                                args=[
                                                    Name(id='order', ctx=Load()),
                                                    Constant(value='date_order', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='l10n_fr_hash',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Name(id='order_reference_string', ctx=Load()),
                                            Call(
                                                func=Name(id='ctx_tz', ctx=Load()),
                                                args=[
                                                    Name(id='order', ctx=Load()),
                                                    Constant(value='write_date', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='hash_verified', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg_alert', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='report_dict', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_accounting_unalterable',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='orders', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='pos.order', kind=None),
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
                                                            Constant(value='state', kind=None),
                                                            Constant(value='in', kind=None),
                                                            List(
                                                                elts=[
                                                                    Constant(value='paid', kind=None),
                                                                    Constant(value='done', kind=None),
                                                                    Constant(value='invoiced', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='l10n_fr_secure_sequence_number', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='order',
                                                value=Constant(value='l10n_fr_secure_sequence_number ASC', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='orders', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='msg_alert', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value="There isn't any order flagged for data inalterability yet for the company %s. This mechanism only runs for point of sale orders generated after the installation of the module France - Certification CGI 286 I-3 bis. - POS", kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='hash_verified', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='previous_hash', ctx=Store())],
                                    value=Constant(value='', kind='u'),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='start_order_info', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='order', ctx=Store()),
                                    iter=Name(id='orders', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='l10n_fr_hash',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='_compute_hash',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='previous_hash',
                                                                value=Name(id='previous_hash', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='msg_alert', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='Corrupted data on point of sale order with id %s.', kind=None),
                                                            Attribute(
                                                                value=Name(id='order', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='hash_verified', ctx=Store())],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                                Break(),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='previous_hash', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='l10n_fr_hash',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='hash_verified', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='orders_sorted_date', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='orders', ctx=Load()),
                                                    attr='sorted',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='o', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Attribute(
                                                            value=Name(id='o', ctx=Load()),
                                                            attr='date_order',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='start_order_info', ctx=Store())],
                                            value=Call(
                                                func=Name(id='build_order_info', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='orders_sorted_date', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='end_order_info', ctx=Store())],
                                            value=Call(
                                                func=Name(id='build_order_info', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='orders_sorted_date', ctx=Load()),
                                                        slice=UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=1, kind=None),
                                                        ),
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
                                                    value=Name(id='report_dict', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='first_order_name', kind=None),
                                                            Constant(value='first_order_hash', kind=None),
                                                            Constant(value='first_order_date', kind=None),
                                                            Constant(value='last_order_name', kind=None),
                                                            Constant(value='last_order_hash', kind=None),
                                                            Constant(value='last_order_date', kind=None),
                                                        ],
                                                        values=[
                                                            Subscript(
                                                                value=Name(id='start_order_info', ctx=Load()),
                                                                slice=Constant(value=2, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='start_order_info', ctx=Load()),
                                                                slice=Constant(value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='start_order_info', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='end_order_info', ctx=Load()),
                                                                slice=Constant(value=2, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='end_order_info', ctx=Load()),
                                                                slice=Constant(value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='end_order_info', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
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
                                ),
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='result', kind=None),
                                            Constant(value='msg_alert', kind=None),
                                            Constant(value='printing_date', kind=None),
                                        ],
                                        values=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='hash_verified', ctx=Load()),
                                                            Name(id='report_dict', ctx=Load()),
                                                        ],
                                                    ),
                                                    Constant(value='None', kind=None),
                                                ],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='msg_alert', ctx=Load()),
                                                    Constant(value='None', kind=None),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='format_date', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Date', ctx=Load()),
                                                            attr='to_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Date', ctx=Load()),
                                                                    attr='today',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
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
