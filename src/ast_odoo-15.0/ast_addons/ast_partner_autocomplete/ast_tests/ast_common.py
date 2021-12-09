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
            module='odoo.addons.partner_autocomplete.models.iap_autocomplete_api',
            names=[alias(name='IapAutocompleteEnrichAPI', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ClassDef(
            name='MockIAPPartnerAutocomplete',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='BaseCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Mock PartnerAutocomplete IAP calls for testing purpose.\n\n    Example of company_data {\n      \'partner_gid\': 51580, \'website\': \'mywebsite.be\',\n      \'additional_info\': {\n        "name": "Mywebsite",\n        "description": "Mywebsite is the largest of Belgium\'s custom companies and part of Mywebsite Group.",\n        "facebook": "mywebsitebe", "twitter": "mywebsite", "linkedin": "company/mywebsite",\n        "twitter_followers": 99999, "twitter_bio": "This is the official Twitter account of MyWebsite.",\n        "industry_group": "Technology Hardware & Equipment", "sub_industry": "Computer Networking",\n        "industry": "Communications Equipment",\n        "sector": ["Information Technology", "Technology Hardware & Equipment"],\n        "sector_primary": "Information Technology"\n        "tech": ["Tealium", "Hotjar", "Google Analytics", "Instagram", "Facebook Advertiser", "Facebook Connect", "Google Tag Manager", "Mandrill", "Bazaarvoice", "Mailgun", "Conversio"],\n        "email": [], "crunchbase": "organization/mywebsite-group",\n        "phone_numbers": ["+32 800 00 000", "+32 800 00 001", "+32 800 00 002"],\n        "timezone": "Europe/Brussels", "timezone_url": "https://time.is/Brussels",\n        "company_type": "private", "employees": 15000.0, "annual_revenue": 0.0, "estimated_annual_revenue": false, "founded_year": 0,\n        "logo": "https://logo.clearbit.com/mywebsite.be"},\n      \'child_ids\': [{\n        \'is_company\': False, \'type\': \'contact\', \'city\': False, \'email\': False,\n        \'name\': \'Client support - SMEs\', \'street\': \'False False\', \'phone\': \'0800 00 500\',\n        \'zip\': False, \'country_id\': False, \'state_id\': False}, {\n        \'is_company\': False, \'type\': \'contact\', \'city\': False, \'email\': False,\n        \'name\': \'Client Support - Large Business\', \'street\': \'False False\', \'phone\': \'0800 00 501\',\n        \'zip\': False, \'country_id\': False, \'state_id\': False}],\n      \'city\': \'Brussel\', \'vat\': \'BE0202239951\',\n      \'email\': False, \'logo\': \'https://logo.clearbit.com/mywebsite.be\',\n      \'name\': \'Proximus\', \'zip\': \'1000\', \'ignored\': False, \'phone\': \'+32 800 00 800\',\n      \'bank_ids\': [{\n        \'acc_number\': \'BE012012012\', \'acc_holder_name\': \'MyWebsite\'}, {\n        \'acc_number\': \'BE013013013\', \'acc_holder_name\': \'MyWebsite Online\'}],\n      \'street\': \'Rue Perdues 27\',\n      \'country_code\': \'de\', \'country_name\': \'Germany\',\n      \'state_id\': False\n    }\n    ', kind=None),
                ),
                FunctionDef(
                    name='_init_mock_partner_autocomplete',
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
                    name='mockPartnerAutocomplete',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
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
                        ],
                    ),
                    body=[
                        FunctionDef(
                            name='_contact_iap',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='local_endpoint', annotation=None, type_comment=None),
                                    arg(arg='action', annotation=None, type_comment=None),
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
                                Assign(
                                    targets=[Name(id='sim_result', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='partner_gid', kind=None),
                                            Constant(value='website', kind=None),
                                            Constant(value='additional_info', kind=None),
                                            Constant(value='city', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='logo', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='zip', kind=None),
                                            Constant(value='ignored', kind=None),
                                            Constant(value='phone', kind=None),
                                            Constant(value='street', kind=None),
                                            Constant(value='country_code', kind=None),
                                            Constant(value='country_name', kind=None),
                                            Constant(value='state_id', kind=None),
                                            Constant(value='child_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='9876', kind=None),
                                            Constant(value='https://www.heinrich.de', kind=None),
                                            Dict(keys=[], values=[]),
                                            Constant(value='Mönchengladbach', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='https://logo.clearbit.com/heinrichsroofing.com', kind=None),
                                            Constant(value='Heinrich', kind=None),
                                            Constant(value='41179', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='+49 0000 112233', kind=None),
                                            Constant(value='Mennrather Str. 123456', kind=None),
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
                                            Constant(value=False, kind=None),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='is_company', kind=None),
                                                            Constant(value='type', kind=None),
                                                            Constant(value='city', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='contact', kind=None),
                                                            Constant(value='Orcq', kind=None),
                                                            Constant(value='Heinrich Support', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='is_company', kind=None),
                                                            Constant(value='type', kind=None),
                                                            Constant(value='email', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='street', kind=None),
                                                            Constant(value='phone', kind=None),
                                                            Constant(value='zip', kind=None),
                                                            Constant(value='country_code', kind=None),
                                                            Constant(value='country_name', kind=None),
                                                            Constant(value='state_code', kind=None),
                                                            Constant(value='state_name', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='contact', kind=None),
                                                            Constant(value='heinrich.clien@test.example.com', kind=None),
                                                            Constant(value='Heinrich Client Support', kind=None),
                                                            Constant(value='Rue des Bourlottes, 9', kind=None),
                                                            Constant(value='0456 00 11 22', kind=None),
                                                            Constant(value='1367', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='base_be',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='code',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='base_be',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='be_state_bw',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='code',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='be_state_bw',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
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
                                        left=Name(id='action', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='enrich', kind=None)],
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
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='sim_error', ctx=Load()),
                                                                    Compare(
                                                                        left=Name(id='sim_error', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='token', kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Raise(
                                                                    exc=Call(
                                                                        func=Name(id='ValueError', ctx=Load()),
                                                                        args=[Constant(value='No account token', kind=None)],
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
                                        ),
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='company_data', kind=None)],
                                                values=[Name(id='sim_result', ctx=Load())],
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
                                                    Name(id='IapAutocompleteEnrichAPI', ctx=Load()),
                                                    Constant(value='_contact_iap', kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='side_effect',
                                                        value=Name(id='_contact_iap', ctx=Load()),
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
                            handlers=[],
                            orelse=[],
                            finalbody=[Pass()],
                        ),
                    ],
                    decorator_list=[Name(id='contextmanager', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
