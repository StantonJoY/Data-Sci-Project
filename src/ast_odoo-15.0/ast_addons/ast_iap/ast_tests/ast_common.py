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
            module='odoo.addons.iap.tools',
            names=[alias(name='iap_tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.iap.models.iap_enrich_api',
            names=[alias(name='IapEnrichAPI', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ClassDef(
            name='MockIAPEnrich',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
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
                                            Name(id='MockIAPEnrich', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_init_iap_mock',
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
                FunctionDef(
                    name='mockIAPEnrichGateway',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='default_data', annotation=None, type_comment=None),
                            arg(arg='email_data', annotation=None, type_comment=None),
                            arg(arg='sim_error', annotation=None, type_comment=None),
                            arg(arg='failing_emails', annotation=None, type_comment=None),
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
                        ],
                    ),
                    body=[
                        FunctionDef(
                            name='_contact_iap',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='local_endpoint', annotation=None, type_comment=None),
                                    arg(arg='params', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sim_result', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='city', kind=None),
                                            Constant(value='postal_code', kind=None),
                                            Constant(value='country_code', kind=None),
                                            Constant(value='clearbit_id', kind=None),
                                            Constant(value='phone_numbers', kind=None),
                                            Constant(value='twitter', kind=None),
                                            Constant(value='facebook', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Simulator INC', kind=None),
                                            Constant(value='Simulator Street', kind=None),
                                            Constant(value='SimCity', kind=None),
                                            Constant(value='9876', kind=None),
                                            Constant(value='BE', kind=None),
                                            Constant(value='idontknow', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='+3269001122', kind=None),
                                                    Constant(value='+32456001122', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='testtwitter', kind=None),
                                            Constant(value='testfacebook', kind=None),
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
                                                    value=Name(id='sim_result', ctx=Load()),
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
                                If(
                                    test=Compare(
                                        left=Name(id='local_endpoint', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='/iap/clearbit/1/lead_enrichment_email', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='result', ctx=Store())],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='lead_id', ctx=Store()),
                                                    Name(id='email', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='params', ctx=Load()),
                                                        slice=Constant(value='domains', kind=None),
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
                                                            Name(id='sim_error', ctx=Load()),
                                                            Compare(
                                                                left=Name(id='sim_error', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='credit', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Attribute(
                                                                    value=Name(id='iap_tools', ctx=Load()),
                                                                    attr='InsufficientCreditError',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='InsufficientCreditError', kind=None)],
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
                                                                        args=[
                                                                            BinOp(
                                                                                left=Constant(value='The url that this service requested returned an error. Please contact the author of the app. The url it tried to contact was ', kind=None),
                                                                                op=Add(),
                                                                                right=Name(id='local_endpoint', ctx=Load()),
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
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='result', ctx=Load()),
                                                            slice=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='lead_id', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[Name(id='sim_result', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='email_data', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='email_data', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='email', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='result', ctx=Load()),
                                                                        slice=Call(
                                                                            func=Name(id='str', ctx=Load()),
                                                                            args=[Name(id='lead_id', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='update',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='email_data', ctx=Load()),
                                                                        slice=Name(id='email', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                                            value=Name(id='result', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Try(
                            body=[
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
                                                    Name(id='IapEnrichAPI', ctx=Load()),
                                                    Constant(value='_contact_iap', kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='side_effect',
                                                        value=Name(id='_contact_iap', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=Name(id='contact_iap_mock', ctx=Store()),
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
                            handlers=[],
                            orelse=[],
                            finalbody=[Pass()],
                        ),
                    ],
                    decorator_list=[Name(id='contextmanager', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_init_iap_mock',
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='base_de',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.de', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='de_state_st',
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
                                        slice=Constant(value='res.country.state', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='code', kind=None),
                                            Constant(value='country_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='DE ST State', kind=None),
                                            Constant(value='st', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='base_de',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                                    attr='base_be',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.be', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='be_state_bw',
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
                                        slice=Constant(value='res.country.state', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='code', kind=None),
                                            Constant(value='country_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Béwééé dis', kind=None),
                                            Constant(value='bw', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='base_be',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='domain', kind=None),
                                    Constant(value='clearbit_id', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='legal_name', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='founded_year', kind=None),
                                    Constant(value='logo', kind=None),
                                    Constant(value='company_type', kind=None),
                                    Constant(value='phone_numbers', kind=None),
                                    Constant(value='email', kind=None),
                                    Constant(value='timezone', kind=None),
                                    Constant(value='timezone_url', kind=None),
                                    Constant(value='facebook', kind=None),
                                    Constant(value='linkedin', kind=None),
                                    Constant(value='crunchbase', kind=None),
                                    Constant(value='twitter', kind=None),
                                    Constant(value='twitter_bio', kind=None),
                                    Constant(value='twitter_followers', kind=None),
                                    Constant(value='twitter_location', kind=None),
                                    Constant(value='estimated_annual_revenue', kind=None),
                                    Constant(value='employees', kind=None),
                                    Constant(value='market_cap', kind=None),
                                    Constant(value='raised', kind=None),
                                    Constant(value='annual_revenue', kind=None),
                                    Constant(value='sector', kind=None),
                                    Constant(value='sector_primary', kind=None),
                                    Constant(value='industry', kind=None),
                                    Constant(value='industry_group', kind=None),
                                    Constant(value='sub_industry', kind=None),
                                    Constant(value='tag', kind=None),
                                    Constant(value='tech', kind=None),
                                    Constant(value='website_title', kind=None),
                                    Constant(value='location', kind=None),
                                    Constant(value='street_number', kind=None),
                                    Constant(value='street_name', kind=None),
                                    Constant(value='sub_premise', kind=None),
                                    Constant(value='postal_code', kind=None),
                                    Constant(value='city', kind=None),
                                    Constant(value='state_code', kind=None),
                                    Constant(value='state_name', kind=None),
                                    Constant(value='country_code', kind=None),
                                    Constant(value='country_name', kind=None),
                                ],
                                values=[
                                    BinOp(
                                        left=Constant(value='%s.de', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='123_ClearbitID_%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s GmbH', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s GmbH legal_name', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s GmbH description', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    Constant(value='1930', kind=None),
                                    BinOp(
                                        left=Constant(value='https://logo.clearbit.com/%slogo.com', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    Constant(value='private', kind=None),
                                    List(
                                        elts=[
                                            Constant(value='+4930499193937', kind=None),
                                            Constant(value='+4930653376208', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='info@%s.example.com', kind=None),
                                                op=Mod(),
                                                right=Name(id='base_name', ctx=Load()),
                                            ),
                                            BinOp(
                                                left=Constant(value='info2@%s.example.com', kind=None),
                                                op=Mod(),
                                                right=Name(id='base_name', ctx=Load()),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='Europe/Berlin', kind=None),
                                    Constant(value='https://time.is/Berlin', kind=None),
                                    BinOp(
                                        left=Constant(value='%s Facebook Handle', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s Linkedin Handle', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='organization/%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s Twitter Handle', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s Twitter Bio', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    Constant(value=1250, kind=None),
                                    Constant(value='Berlin', kind=None),
                                    Constant(value='1000000', kind=None),
                                    Constant(value=3.14, kind=None),
                                    Constant(value=6.28, kind=None),
                                    Constant(value=15000, kind=None),
                                    Constant(value=1000000, kind=None),
                                    BinOp(
                                        left=Constant(value='%s sector', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s sector_primary', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s industry', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s industry_group', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s sub_industry', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='Automation', kind=None),
                                            Constant(value='Construction', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='3d_cart', kind=None),
                                            Constant(value='nginx', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s Website Title', kind=None),
                                        op=Mod(),
                                        right=Name(id='base_name', ctx=Load()),
                                    ),
                                    Constant(value='Mennrather Str. 123456', kind=None),
                                    Constant(value='123456', kind=None),
                                    Constant(value='Mennrather Str.', kind=None),
                                    Constant(value='sub premise', kind=None),
                                    Constant(value='41179', kind=None),
                                    Constant(value='Mönchengladbach', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='de_state_st',
                                            ctx=Load(),
                                        ),
                                        attr='code',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='de_state_st',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='base_de',
                                            ctx=Load(),
                                        ),
                                        attr='code',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='base_de',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
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
                    name='_get_iap_contact_data',
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
                            targets=[Name(id='people_data', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='index', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Constant(value=2, kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='payload', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='full_name', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='phone', kind=None),
                                            Constant(value='seniority', kind=None),
                                            Constant(value='title', kind=None),
                                            Constant(value='role', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Constant(value='Contact %s %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='base_name', ctx=Load()),
                                                        Name(id='index', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            BinOp(
                                                left=Constant(value='test.contact.%s@%s.example.com', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='index', ctx=Load()),
                                                        Name(id='base_name', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Constant(value='+49 30 548406496', kind=None),
                                            Constant(value='manager', kind=None),
                                            Constant(value='Doing stuff', kind=None),
                                            Constant(value='health_professional', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='people_data', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='payload', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='people_data', ctx=Load()),
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
