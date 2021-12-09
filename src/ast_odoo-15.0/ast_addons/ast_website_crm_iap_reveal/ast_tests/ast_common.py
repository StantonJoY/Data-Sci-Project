Module(
    body=[
        ImportFrom(
            module='contextlib',
            names=[alias(name='contextmanager', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='exceptions', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.crm.models.crm_lead',
            names=[alias(name='Lead', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.iap.tests.common',
            names=[alias(name='MockIAPEnrich', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website_crm_iap_reveal.models.crm_reveal_rule',
            names=[alias(name='CRMRevealRule', asname=None)],
            level=0,
        ),
        ClassDef(
            name='MockIAPReveal',
            bases=[Name(id='MockIAPEnrich', ctx=Load())],
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
                                            Name(id='MockIAPReveal', ctx=Load()),
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
                                    attr='_new_leads',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='crm.lead', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='rules',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='views',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='mock_IAP_reveal',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='ip_to_rules', annotation=None, type_comment=None),
                            arg(arg='name_list', annotation=None, type_comment=None),
                            arg(arg='default_data', annotation=None, type_comment=None),
                            arg(arg='sim_error', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_new_leads',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='crm.lead', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='crm_lead_create_origin', ctx=Store())],
                            value=Attribute(
                                value=Name(id='Lead', ctx=Load()),
                                attr='create',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_crm_lead_create',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='model', annotation=None, type_comment=None)],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Name(id='crm_lead_create_origin', ctx=Load()),
                                        args=[
                                            Name(id='model', ctx=Load()),
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
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_new_leads',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
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
                            name='_iap_contact_reveal',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='params', annotation=None, type_comment=None),
                                    arg(arg='timeout', annotation=None, type_comment=None),
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
                                        op=And(),
                                        values=[
                                            Name(id='sim_error', ctx=Load()),
                                            Compare(
                                                left=Name(id='sim_error', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='credit', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[
                                                    Constant(value='credit_error', kind=None),
                                                    Constant(value='reveal_data', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='sim_error', ctx=Load()),
                                            Compare(
                                                left=Name(id='sim_error', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='jsonrpc_exception', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Name(id='exceptions', ctx=Load()),
                                                    attr='AccessError',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='The url that this service requested returned an error. Please contact the author of the app. The url it tried to contact was [STRIPPED]', kind=None)],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='sim_error', ctx=Load()),
                                            Compare(
                                                left=Name(id='sim_error', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='no_result', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[
                                                    Constant(value='credit_error', kind=None),
                                                    Constant(value='reveal_data', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='counter', ctx=Store()),
                                            Name(id='ip_values', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='enumerate', ctx=Load()),
                                        args=[Name(id='ip_to_rules', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='ip', ctx=Store()),
                                                        Name(id='rule', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Name(id='ip_values', ctx=Load()),
                                                        slice=Constant(value='ip', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='ip_values', ctx=Load()),
                                                        slice=Constant(value='rules', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='name_list', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='base_name', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='name_list', ctx=Load()),
                                                        slice=BinOp(
                                                            left=Name(id='counter', ctx=Load()),
                                                            op=Mod(),
                                                            right=Call(
                                                                func=Name(id='len', ctx=Load()),
                                                                args=[Name(id='name_list', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='base_name', ctx=Store())],
                                                    value=BinOp(
                                                        left=Constant(value='heinrich_%d', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='counter', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='iap_payload', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='ip', kind=None),
                                                    Constant(value='ip_time_zone', kind=None),
                                                    Constant(value='not_found', kind=None),
                                                    Constant(value='rule_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='ip', ctx=Load()),
                                                    Constant(value='Europe/Berlin', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Name(id='rule', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='company_data', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_iap_company_data',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='base_name', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='service',
                                                        value=Constant(value='reveal', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='add_values',
                                                        value=Dict(
                                                            keys=[
                                                                Constant(value='ip', kind=None),
                                                                Constant(value='rule', kind=None),
                                                            ],
                                                            values=[
                                                                Name(id='ip', ctx=Load()),
                                                                Name(id='rule', ctx=Load()),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='default_data', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='company_data', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='default_data', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='iap_payload', ctx=Load()),
                                                    slice=Constant(value='clearbit_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='company_data', ctx=Load()),
                                                slice=Constant(value='clearbit_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='iap_payload', ctx=Load()),
                                                    slice=Constant(value='reveal_data', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='company_data', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='rule', ctx=Load()),
                                                    attr='lead_for',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='people', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='people_data', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_iap_contact_data',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='base_name', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='service',
                                                                value=Constant(value='reveal', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='iap_payload', ctx=Load()),
                                                            slice=Constant(value='people_data', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='people_data', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='iap_payload', ctx=Load()),
                                                    slice=Constant(value='credit', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Constant(value=1, kind=None),
                                                op=Add(),
                                                right=IfExp(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='rule', ctx=Load()),
                                                            attr='lead_for',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='people', kind=None)],
                                                    ),
                                                    body=Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='people_data', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    orelse=Constant(value=0, kind=None),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='iap_payload', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='reveal_data', kind=None),
                                            Constant(value='credit_error', kind=None),
                                        ],
                                        values=[
                                            Name(id='response', ctx=Load()),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
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
                                            Name(id='CRMRevealRule', ctx=Load()),
                                            Constant(value='_iap_contact_reveal', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='side_effect',
                                                value=Name(id='_iap_contact_reveal', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='Lead', ctx=Load()),
                                            Constant(value='create', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='autospec',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='wraps',
                                                value=Name(id='Lead', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='side_effect',
                                                value=Name(id='_crm_lead_create', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Yield(value=None),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='contextmanager', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_iap_company_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='base_name', annotation=None, type_comment=None),
                            arg(arg='service', annotation=None, type_comment=None),
                            arg(arg='add_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='company_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MockIAPReveal', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_iap_company_data',
                                    ctx=Load(),
                                ),
                                args=[Name(id='base_name', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='service',
                                        value=Name(id='service', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='add_values',
                                        value=Name(id='add_values', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='service', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='reveal', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='company_data', ctx=Load()),
                                            slice=Constant(value='phone', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='company_data', ctx=Load()),
                                            slice=Constant(value='phone_numbers', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='company_data', ctx=Load()),
                                            slice=Constant(value='sector', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='Sector Info', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='company_data', ctx=Load()),
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
