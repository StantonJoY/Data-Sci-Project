Module(
    body=[
        ImportFrom(
            module='math',
            names=[
                alias(name='floor', asname=None),
                alias(name='log10', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='CRMHelpers',
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
                    value=Constant(value='crm.iap.lead.helpers', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Helper methods for crm_iap_mine modules', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='notify_no_more_credit',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='service_name', annotation=None, type_comment=None),
                            arg(arg='model_name', annotation=None, type_comment=None),
                            arg(arg='notification_parameter', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Notify about the number of credit.\n        In order to avoid to spam people each hour, an ir.config_parameter is set\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='already_notified', ctx=Store())],
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
                                args=[
                                    Name(id='notification_parameter', ctx=Load()),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='already_notified', ctx=Load()),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='mail_template', ctx=Store())],
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
                                args=[Constant(value='crm_iap_mine.lead_generation_no_credits', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='iap_account', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='iap.account', kind=None),
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
                                                    Constant(value='service_name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='service_name', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model_name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(elts=[], ctx=Load()),
                                    List(
                                        elts=[Constant(value='create_uid', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uids', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Subscript(
                                                value=Name(id='r', ctx=Load()),
                                                slice=Constant(value='create_uid', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='r', ctx=Store()),
                                                iter=Name(id='res', ctx=Load()),
                                                ifs=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='create_uid', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
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
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[Name(id='uids', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='email', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='emails', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Name(id='r', ctx=Load()),
                                            slice=Constant(value='email', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='r', ctx=Store()),
                                                iter=Name(id='res', ctx=Load()),
                                                ifs=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='email', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='email_values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='email_to', kind=None)],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=',', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='emails', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mail_template', ctx=Load()),
                                    attr='send_mail',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='iap_account', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='force_send',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='email_values',
                                        value=Name(id='email_values', ctx=Load()),
                                    ),
                                ],
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
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='notification_parameter', ctx=Load()),
                                    Constant(value=True, kind=None),
                                ],
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
                    name='lead_vals_from_response',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='lead_type', annotation=None, type_comment=None),
                            arg(arg='team_id', annotation=None, type_comment=None),
                            arg(arg='tag_ids', annotation=None, type_comment=None),
                            arg(arg='user_id', annotation=None, type_comment=None),
                            arg(arg='company_data', annotation=None, type_comment=None),
                            arg(arg='people_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='country_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.country', kind=None),
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
                                                        Constant(value='code', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Subscript(
                                                            value=Name(id='company_data', ctx=Load()),
                                                            slice=Constant(value='country_code', kind=None),
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
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='website_url', ctx=Store())],
                            value=IfExp(
                                test=Subscript(
                                    value=Name(id='company_data', ctx=Load()),
                                    slice=Constant(value='domain', kind=None),
                                    ctx=Load(),
                                ),
                                body=BinOp(
                                    left=Constant(value='https://www.%s', kind=None),
                                    op=Mod(),
                                    right=Subscript(
                                        value=Name(id='company_data', ctx=Load()),
                                        slice=Constant(value='domain', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Constant(value=False, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lead_vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='team_id', kind=None),
                                    Constant(value='tag_ids', kind=None),
                                    Constant(value='user_id', kind=None),
                                    Constant(value='reveal_id', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='partner_name', kind=None),
                                    Constant(value='email_from', kind=None),
                                    Constant(value='phone', kind=None),
                                    Constant(value='website', kind=None),
                                    Constant(value='street', kind=None),
                                    Constant(value='city', kind=None),
                                    Constant(value='zip', kind=None),
                                    Constant(value='country_id', kind=None),
                                    Constant(value='state_id', kind=None),
                                ],
                                values=[
                                    Name(id='lead_type', ctx=Load()),
                                    Name(id='team_id', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=6, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Name(id='tag_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='user_id', ctx=Load()),
                                    Subscript(
                                        value=Name(id='company_data', ctx=Load()),
                                        slice=Constant(value='clearbit_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Name(id='company_data', ctx=Load()),
                                                slice=Constant(value='name', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='company_data', ctx=Load()),
                                                slice=Constant(value='domain', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Name(id='company_data', ctx=Load()),
                                                slice=Constant(value='legal_name', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='company_data', ctx=Load()),
                                                slice=Constant(value='name', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='iter', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='company_data', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='email', kind=None),
                                                            List(elts=[], ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Name(id='company_data', ctx=Load()),
                                                slice=Constant(value='phone', kind=None),
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='company_data', ctx=Load()),
                                                        slice=Constant(value='phone_numbers', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='company_data', ctx=Load()),
                                                            slice=Constant(value='phone_numbers', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    Name(id='website_url', ctx=Load()),
                                    Subscript(
                                        value=Name(id='company_data', ctx=Load()),
                                        slice=Constant(value='location', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='company_data', ctx=Load()),
                                        slice=Constant(value='city', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='company_data', ctx=Load()),
                                        slice=Constant(value='postal_code', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='country_id', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_find_state_id',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='company_data', ctx=Load()),
                                                slice=Constant(value='state_code', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='country_id', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='people_data', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lead_vals', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='contact_name', kind=None),
                                                    Constant(value='email_from', kind=None),
                                                    Constant(value='function', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='people_data', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='full_name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='people_data', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='email', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='people_data', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='title', kind=None),
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
                            value=Name(id='lead_vals', ctx=Load()),
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
                    name='_find_state_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='state_code', annotation=None, type_comment=None),
                            arg(arg='country_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='state_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.country.state', kind=None),
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
                                                    Constant(value='code', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='state_code', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='country_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='country_id', ctx=Load()),
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
                            test=Name(id='state_id', ctx=Load()),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Name(id='state_id', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
