Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='date', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='markupsafe',
            names=[alias(name='Markup', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.urls',
            names=[alias(name='url_join', asname=None)],
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
            module='odoo.addons.base.models.ir_mail_server',
            names=[alias(name='MailDeliveryException', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.float_utils',
            names=[alias(name='float_round', asname=None)],
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
            name='Digest',
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
                    value=Constant(value='digest.digest', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Digest', kind=None),
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
                                value=Constant(value='Name', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.users', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Recipients', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('share', '=', False)]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='periodicity', ctx=Store())],
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
                                            Constant(value='daily', kind=None),
                                            Constant(value='Daily', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='weekly', kind=None),
                                            Constant(value='Weekly', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='monthly', kind=None),
                                            Constant(value='Monthly', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='quarterly', kind=None),
                                            Constant(value='Quarterly', kind=None),
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
                                value=Constant(value='Periodicity', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='daily', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='next_run_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Next Send Date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='currency_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.currency_id', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Currency', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
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
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='available_fields', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_available_fields', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_subscribed', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Is user subscribed', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_is_subscribed', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='state', ctx=Store())],
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
                                            Constant(value='activated', kind=None),
                                            Constant(value='Activated', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='deactivated', kind=None),
                                            Constant(value='Deactivated', kind=None),
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
                                value=Constant(value='Status', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='activated', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='kpi_res_users_connected', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Connected Users', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='kpi_res_users_connected_value', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_kpi_res_users_connected_value', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='kpi_mail_message_total', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Messages', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='kpi_mail_message_total_value', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_kpi_mail_message_total_value', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_is_subscribed',
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
                            target=Name(id='digest', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='digest', ctx=Load()),
                                            attr='is_subscribed',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='digest', ctx=Load()),
                                                attr='user_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
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
                    name='_compute_available_fields',
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
                            target=Name(id='digest', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='kpis_values_fields', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='field_name', ctx=Store()),
                                            Name(id='field', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='digest', ctx=Load()),
                                                attr='_fields',
                                                ctx=Load(),
                                            ),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='field', ctx=Load()),
                                                            attr='type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='boolean', kind=None)],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='field_name', ctx=Load()),
                                                            attr='startswith',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='kpi_', kind=None),
                                                                    Constant(value='x_kpi_', kind=None),
                                                                    Constant(value='x_studio_kpi_', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Subscript(
                                                        value=Name(id='digest', ctx=Load()),
                                                        slice=Name(id='field_name', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='kpis_values_fields', ctx=Store()),
                                                    op=Add(),
                                                    value=List(
                                                        elts=[
                                                            BinOp(
                                                                left=Name(id='field_name', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value='_value', kind=None),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='digest', ctx=Load()),
                                            attr='available_fields',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value=', ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='kpis_values_fields', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
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
                    name='_get_kpi_compute_parameters',
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
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='to_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='start_datetime', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='to_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='end_datetime', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
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
                FunctionDef(
                    name='_compute_kpi_res_users_connected_value',
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
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='start', ctx=Store()),
                                                Name(id='end', ctx=Store()),
                                                Name(id='company', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='_get_kpi_compute_parameters',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='user_connected', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search_count',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='company', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='login_date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Name(id='start', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='login_date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Name(id='end', ctx=Load()),
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
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='kpi_res_users_connected_value',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='user_connected', ctx=Load()),
                                    type_comment=None,
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
                    name='_compute_kpi_mail_message_total_value',
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
                            targets=[Name(id='discussion_subtype_id', ctx=Store())],
                            value=Attribute(
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
                                    args=[Constant(value='mail.mt_comment', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='start', ctx=Store()),
                                                Name(id='end', ctx=Store()),
                                                Name(id='company', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='_get_kpi_compute_parameters',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='total_messages', ctx=Store())],
                                    value=Call(
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
                                            attr='search_count',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='create_date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Name(id='start', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='create_date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Name(id='end', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='subtype_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='discussion_subtype_id', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='message_type', kind=None),
                                                            Constant(value='in', kind=None),
                                                            List(
                                                                elts=[
                                                                    Constant(value='comment', kind=None),
                                                                    Constant(value='email', kind=None),
                                                                ],
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
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='kpi_mail_message_total_value',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='total_messages', ctx=Load()),
                                    type_comment=None,
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
                    name='_onchange_periodicity',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='next_run_date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_next_run_date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='periodicity', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
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
                            targets=[Name(id='digests', ctx=Store())],
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
                            target=Name(id='digest', ctx=Store()),
                            iter=Name(id='digests', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='digest', ctx=Load()),
                                            attr='next_run_date',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='digest', ctx=Load()),
                                                    attr='next_run_date',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='digest', ctx=Load()),
                                                    attr='_get_next_run_date',
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='digests', ctx=Load()),
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
                    name='action_subscribe',
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
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='has_group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.group_user', kind=None)],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                AugAssign(
                                    target=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='user_ids',
                                        ctx=Store(),
                                    ),
                                    op=BitOr(),
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
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
                FunctionDef(
                    name='action_unsubcribe',
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
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='has_group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.group_user', kind=None)],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                AugAssign(
                                    target=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='user_ids',
                                        ctx=Store(),
                                    ),
                                    op=Sub(),
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
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
                FunctionDef(
                    name='action_activate',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='activated', kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_deactivate',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='deactivated', kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_set_periodicity',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='periodicity', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='periodicity',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='periodicity', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_send',
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
                            targets=[Name(id='to_slowdown', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_daily_logs',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='digest', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='user', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='digest', ctx=Load()),
                                        attr='user_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='digest', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='digest_slowdown',
                                                                value=Compare(
                                                                    left=Name(id='digest', ctx=Load()),
                                                                    ops=[In()],
                                                                    comparators=[Name(id='to_slowdown', ctx=Load())],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='lang',
                                                                value=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='lang',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    attr='_action_send_to_user',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='user', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='tips_count',
                                                        value=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='digest', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='to_slowdown', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='digest', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='periodicity', kind=None)],
                                                        values=[Constant(value='weekly', kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='digest', ctx=Load()),
                                            attr='next_run_date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='digest', ctx=Load()),
                                            attr='_get_next_run_date',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
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
                    name='_action_send_to_user',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                            arg(arg='tips_count', annotation=None, type_comment=None),
                            arg(arg='consum_tips', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=1, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='rendered_body', ctx=Store())],
                            value=Subscript(
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
                                        attr='_render_template',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='digest.digest_mail_main', kind=None),
                                        Constant(value='digest.digest', kind=None),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='engine',
                                            value=Constant(value='qweb_view', kind=None),
                                        ),
                                        keyword(
                                            arg='add_context',
                                            value=Dict(
                                                keys=[
                                                    Constant(value='title', kind=None),
                                                    Constant(value='top_button_label', kind=None),
                                                    Constant(value='top_button_url', kind=None),
                                                    Constant(value='company', kind=None),
                                                    Constant(value='user', kind=None),
                                                    Constant(value='tips_count', kind=None),
                                                    Constant(value='formatted_date', kind=None),
                                                    Constant(value='display_mobile_banner', kind=None),
                                                    Constant(value='kpi_data', kind=None),
                                                    Constant(value='tips', kind=None),
                                                    Constant(value='preferences', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Connect', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='get_base_url',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='user', ctx=Load()),
                                                    Name(id='tips_count', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='datetime', ctx=Load()),
                                                                    attr='today',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='%B %d, %Y', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=True, kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_compute_kpis',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='user', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='user', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_compute_tips',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='user', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='user', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='tips_count',
                                                                value=Name(id='tips_count', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='consumed',
                                                                value=Name(id='consum_tips', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_compute_preferences',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='user', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='user', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ),
                                        keyword(
                                            arg='post_process',
                                            value=Constant(value=True, kind=None),
                                        ),
                                    ],
                                ),
                                slice=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='full_mail', ctx=Store())],
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
                                    attr='_render_encapsulate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='digest.digest_mail_layout', kind=None),
                                    Name(id='rendered_body', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='add_context',
                                        value=Dict(
                                            keys=[
                                                Constant(value='company', kind=None),
                                                Constant(value='user', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                Name(id='user', ctx=Load()),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mail_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='subject', kind=None),
                                    Constant(value='email_from', kind=None),
                                    Constant(value='email_to', kind=None),
                                    Constant(value='body_html', kind=None),
                                    Constant(value='auto_delete', kind=None),
                                ],
                                values=[
                                    BinOp(
                                        left=Constant(value='%s: %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    IfExp(
                                        test=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        body=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='email_formatted',
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
                                            attr='email_formatted',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='email_formatted',
                                        ctx=Load(),
                                    ),
                                    Name(id='full_mail', ctx=Load()),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mail', ctx=Store())],
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
                                                slice=Constant(value='mail.mail', kind=None),
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
                                args=[Name(id='mail_values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mail', ctx=Load()),
                                    attr='send',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='raise_exception',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_cron_send_digest_email',
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
                            targets=[Name(id='digests', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='next_run_date', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='today',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='activated', kind=None),
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
                        For(
                            target=Name(id='digest', ctx=Store()),
                            iter=Name(id='digests', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='digest', ctx=Load()),
                                                    attr='action_send',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='MailDeliveryException', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='MailDeliveryException while sending digest %d. Digest is now scheduled for next cron update.', kind=None),
                                                            Attribute(
                                                                value=Name(id='digest', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                            orelse=[],
                            type_comment=None,
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
                    name='_compute_kpis',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Compute KPIs to display in the digest template. It is expected to be\n        a list of KPIs, each containing values for 3 columns display.\n\n        :return list: result [{\n            'kpi_name': 'kpi_mail_message',\n            'kpi_fullname': 'Messages',  # translated\n            'kpi_action': 'crm.crm_lead_action_pipeline',  # xml id of an action to execute\n            'kpi_col1': {\n                'value': '12.0',\n                'margin': 32.36,\n                'col_subtitle': 'Yesterday',  # translated\n            },\n            'kpi_col2': { ... },\n            'kpi_col3':  { ... },\n        }, { ... }] ", kind=None),
                        ),
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
                            targets=[Name(id='digest_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_kpi_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invalid_fields', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='kpis', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='dict', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='kpi_name',
                                            value=Name(id='field_name', ctx=Load()),
                                        ),
                                        keyword(
                                            arg='kpi_fullname',
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.model.fields', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_name',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='field_name', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='field_description',
                                                ctx=Load(),
                                            ),
                                        ),
                                        keyword(
                                            arg='kpi_action',
                                            value=Constant(value=False, kind=None),
                                        ),
                                        keyword(
                                            arg='kpi_col1',
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        keyword(
                                            arg='kpi_col2',
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        keyword(
                                            arg='kpi_col3',
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='field_name', ctx=Store()),
                                        iter=Name(id='digest_fields', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='kpis_actions', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compute_kpis_actions',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='company', ctx=Load()),
                                    Name(id='user', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='col_index', ctx=Store()),
                                    Tuple(
                                        elts=[
                                            Name(id='tf_name', ctx=Store()),
                                            Name(id='tf', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compute_timeframes',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='company', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='digest', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='start_datetime',
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='tf', ctx=Load()),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='end_datetime',
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='tf', ctx=Load()),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    attr='with_user',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='user', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='company', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='previous_digest', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='start_datetime',
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='tf', ctx=Load()),
                                                                        slice=Constant(value=1, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='end_datetime',
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='tf', ctx=Load()),
                                                                        slice=Constant(value=1, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    attr='with_user',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='user', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='company', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='index', ctx=Store()),
                                            Name(id='field_name', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='enumerate', ctx=Load()),
                                        args=[Name(id='digest_fields', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='kpi_values', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='kpis', ctx=Load()),
                                                slice=Name(id='index', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='kpi_values', ctx=Load()),
                                                    slice=Constant(value='kpi_action', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='kpis_actions', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='field_name', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='compute_value', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='digest', ctx=Load()),
                                                        slice=BinOp(
                                                            left=Name(id='field_name', ctx=Load()),
                                                            op=Add(),
                                                            right=Constant(value='_value', kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='digest', ctx=Load()),
                                                            attr='invalidate_cache',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    BinOp(
                                                                        left=Name(id='field_name', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value='_value', kind=None),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='previous_value', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='previous_digest', ctx=Load()),
                                                        slice=BinOp(
                                                            left=Name(id='field_name', ctx=Load()),
                                                            op=Add(),
                                                            right=Constant(value='_value', kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='previous_digest', ctx=Load()),
                                                            attr='invalidate_cache',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    BinOp(
                                                                        left=Name(id='field_name', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value='_value', kind=None),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='AccessError', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='invalid_fields', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='field_name', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Continue(),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='margin', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_margin_value',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='compute_value', ctx=Load()),
                                                    Name(id='previous_value', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_fields',
                                                            ctx=Load(),
                                                        ),
                                                        slice=BinOp(
                                                            left=Constant(value='%s_value', kind=None),
                                                            op=Mod(),
                                                            right=Name(id='field_name', ctx=Load()),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='monetary', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='converted_amount', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='tools', ctx=Load()),
                                                            attr='format_decimalized_amount',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='compute_value', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='compute_value', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_format_currency_amount',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='converted_amount', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='company', ctx=Load()),
                                                                attr='currency_id',
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='kpi_values', ctx=Load()),
                                                        slice=BinOp(
                                                            left=Constant(value='kpi_col%s', kind=None),
                                                            op=Mod(),
                                                            right=BinOp(
                                                                left=Name(id='col_index', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='value', kind=None),
                                                            Constant(value='margin', kind=None),
                                                            Constant(value='col_subtitle', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='compute_value', ctx=Load()),
                                                            Name(id='margin', ctx=Load()),
                                                            Name(id='tf_name', ctx=Load()),
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
                            type_comment=None,
                        ),
                        Return(
                            value=ListComp(
                                elt=Name(id='kpi', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='kpi', ctx=Store()),
                                        iter=Name(id='kpis', ctx=Load()),
                                        ifs=[
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='kpi', ctx=Load()),
                                                    slice=Constant(value='kpi_name', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[Name(id='invalid_fields', ctx=Load())],
                                            ),
                                        ],
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
                FunctionDef(
                    name='_compute_tips',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                            arg(arg='tips_count', annotation=None, type_comment=None),
                            arg(arg='consumed', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=1, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='tips', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='digest.tip', kind=None),
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
                                                    Constant(value='user_ids', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='user', ctx=Load()),
                                                            attr='groups_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
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
                                        value=Name(id='tips_count', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tip_descriptions', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
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
                                            attr='_render_template',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='html_sanitize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='tip', ctx=Load()),
                                                        attr='tip_description',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='digest.tip', kind=None),
                                            Attribute(
                                                value=Name(id='tip', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='post_process',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='engine',
                                                value=Constant(value='qweb', kind=None),
                                            ),
                                        ],
                                    ),
                                    slice=Attribute(
                                        value=Name(id='tip', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='tip', ctx=Store()),
                                        iter=Name(id='tips', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='consumed', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='tips', ctx=Load()),
                                        attr='user_ids',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Name(id='user', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='tip_descriptions', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_kpis_actions',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Give an optional action to display in digest email linked to some KPIs.\n\n        :return dict: key: kpi name (field name), value: an action that will be\n          concatenated with /web#action={action}\n        ', kind=None),
                        ),
                        Return(
                            value=Dict(keys=[], values=[]),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_preferences',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Give an optional text for preferences, like a shortcut for configuration.\n\n        :return string: html to put in template\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='preferences', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='digest_slowdown', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='preferences', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="We have noticed you did not connect these last few days so we've automatically switched your preference to weekly Digests.", kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='periodicity',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='daily', kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='has_group',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='base.group_erp_manager', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='preferences', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='Markup', ctx=Load()),
                                                            args=[Constant(value='<p>%s<br /><a href="%s" target="_blank" style="color:#875A7B; font-weight: bold;">%s</a></p>', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='Prefer a broader overview ?', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                JoinedStr(
                                                                    values=[
                                                                        Constant(value='/digest/', kind=None),
                                                                        FormattedValue(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            conversion=-1,
                                                                            format_spec=JoinedStr(
                                                                                values=[Constant(value='d', kind=None)],
                                                                            ),
                                                                        ),
                                                                        Constant(value='/set_periodicity?periodicity=weekly', kind=None),
                                                                    ],
                                                                ),
                                                                Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='Switch to weekly Digests', kind=None)],
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
                                ),
                            ],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='user', ctx=Load()),
                                    attr='has_group',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.group_erp_manager', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='preferences', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='Markup', ctx=Load()),
                                                    args=[Constant(value='<p>%s<br /><a href="%s" target="_blank" style="color:#875A7B; font-weight: bold;">%s</a></p>', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Want to customize this email?', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        JoinedStr(
                                                            values=[
                                                                Constant(value='/web#view_type=form&amp;model=', kind=None),
                                                                FormattedValue(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    conversion=-1,
                                                                    format_spec=None,
                                                                ),
                                                                Constant(value='&amp;id=', kind=None),
                                                                FormattedValue(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    conversion=-1,
                                                                    format_spec=JoinedStr(
                                                                        values=[Constant(value='d', kind=None)],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Choose the metrics you care about', kind=None)],
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
                        ),
                        Return(
                            value=Name(id='preferences', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_next_run_date',
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='periodicity',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='daily', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='delta', ctx=Store())],
                                    value=Call(
                                        func=Name(id='relativedelta', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='days',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='periodicity',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='weekly', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='delta', ctx=Store())],
                                    value=Call(
                                        func=Name(id='relativedelta', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='weeks',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='periodicity',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='monthly', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='delta', ctx=Store())],
                                            value=Call(
                                                func=Name(id='relativedelta', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='months',
                                                        value=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='periodicity',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='quarterly', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='delta', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='relativedelta', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='months',
                                                                value=Constant(value=3, kind=None),
                                                            ),
                                                        ],
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
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='date', ctx=Load()),
                                        attr='today',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Name(id='delta', ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_timeframes',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='start_datetime', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='utcnow',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tz_name', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='company', ctx=Load()),
                                    attr='resource_calendar_id',
                                    ctx=Load(),
                                ),
                                attr='tz',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='tz_name', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='start_datetime', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='pytz', ctx=Load()),
                                                    attr='timezone',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='tz_name', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='localize',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='start_datetime', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Last 24 hours', kind=None)],
                                                keywords=[],
                                            ),
                                            Tuple(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            BinOp(
                                                                left=Name(id='start_datetime', ctx=Load()),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='days',
                                                                            value=UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=1, kind=None),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            Name(id='start_datetime', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            BinOp(
                                                                left=Name(id='start_datetime', ctx=Load()),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='days',
                                                                            value=UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=2, kind=None),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            BinOp(
                                                                left=Name(id='start_datetime', ctx=Load()),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='days',
                                                                            value=UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=1, kind=None),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Last 7 Days', kind=None)],
                                                keywords=[],
                                            ),
                                            Tuple(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            BinOp(
                                                                left=Name(id='start_datetime', ctx=Load()),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='weeks',
                                                                            value=UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=1, kind=None),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            Name(id='start_datetime', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            BinOp(
                                                                left=Name(id='start_datetime', ctx=Load()),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='weeks',
                                                                            value=UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=2, kind=None),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            BinOp(
                                                                left=Name(id='start_datetime', ctx=Load()),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='weeks',
                                                                            value=UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=1, kind=None),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Last 30 Days', kind=None)],
                                                keywords=[],
                                            ),
                                            Tuple(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            BinOp(
                                                                left=Name(id='start_datetime', ctx=Load()),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='months',
                                                                            value=UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=1, kind=None),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            Name(id='start_datetime', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            BinOp(
                                                                left=Name(id='start_datetime', ctx=Load()),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='months',
                                                                            value=UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=2, kind=None),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            BinOp(
                                                                left=Name(id='start_datetime', ctx=Load()),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='months',
                                                                            value=UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=1, kind=None),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
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
                FunctionDef(
                    name='_get_kpi_fields',
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
                            value=ListComp(
                                elt=Name(id='field_name', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='field_name', ctx=Store()),
                                                Name(id='field', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_fields',
                                                    ctx=Load(),
                                                ),
                                                attr='items',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='field', ctx=Load()),
                                                            attr='type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='boolean', kind=None)],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='field_name', ctx=Load()),
                                                            attr='startswith',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='kpi_', kind=None),
                                                                    Constant(value='x_kpi_', kind=None),
                                                                    Constant(value='x_studio_kpi_', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Subscript(
                                                        value=Name(id='self', ctx=Load()),
                                                        slice=Name(id='field_name', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
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
                FunctionDef(
                    name='_get_margin_value',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='previous_value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=0.0, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='margin', ctx=Store())],
                            value=Constant(value=0.0, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='value', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Name(id='previous_value', ctx=Load())],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='value', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=0.0, kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='previous_value', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=0.0, kind=None)],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='margin', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        BinOp(
                                                            left=Call(
                                                                func=Name(id='float', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Name(id='value', ctx=Load()),
                                                                        op=Sub(),
                                                                        right=Name(id='previous_value', ctx=Load()),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            op=Div(),
                                                            right=Name(id='previous_value', ctx=Load()),
                                                        ),
                                                        Constant(value=1, kind=None),
                                                    ],
                                                ),
                                                op=Mult(),
                                                right=Constant(value=100, kind=None),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='margin', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_daily_logs',
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
                            targets=[Name(id='three_days_ago', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='datetime', ctx=Load()),
                                                attr='now',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='replace',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='hour',
                                            value=Constant(value=0, kind=None),
                                        ),
                                        keyword(
                                            arg='minute',
                                            value=Constant(value=0, kind=None),
                                        ),
                                        keyword(
                                            arg='second',
                                            value=Constant(value=0, kind=None),
                                        ),
                                        keyword(
                                            arg='microsecond',
                                            value=Constant(value=0, kind=None),
                                        ),
                                    ],
                                ),
                                op=Sub(),
                                right=Call(
                                    func=Name(id='relativedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='days',
                                            value=Constant(value=3, kind=None),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='to_slowdown', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='digest.digest', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='digest', ctx=Store()),
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
                                            args=[arg(arg='digest', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='digest', ctx=Load()),
                                                attr='periodicity',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='daily', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='users_logs', ctx=Store())],
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
                                                        slice=Constant(value='res.users.log', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search_count',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='create_uid', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='digest', ctx=Load()),
                                                                    attr='user_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='create_date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Name(id='three_days_ago', ctx=Load()),
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
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='users_logs', ctx=Load()),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='to_slowdown', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='digest', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='to_slowdown', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_format_currency_amount',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='currency_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='pre', ctx=Store())],
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='currency_id', ctx=Load()),
                                    attr='position',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='before', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='symbol', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='{symbol}', kind='u'),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='symbol',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='currency_id', ctx=Load()),
                                                    attr='symbol',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='{pre}{0}{post}', kind='u'),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[Name(id='amount', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='pre',
                                        value=IfExp(
                                            test=Name(id='pre', ctx=Load()),
                                            body=Name(id='symbol', ctx=Load()),
                                            orelse=Constant(value='', kind=None),
                                        ),
                                    ),
                                    keyword(
                                        arg='post',
                                        value=IfExp(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='pre', ctx=Load()),
                                            ),
                                            body=Name(id='symbol', ctx=Load()),
                                            orelse=Constant(value='', kind=None),
                                        ),
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
