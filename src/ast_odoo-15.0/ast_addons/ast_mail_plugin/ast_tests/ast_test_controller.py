Module(
    body=[
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='Mock', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.iap.tools',
            names=[alias(name='iap_tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mail_plugin.tests.common',
            names=[alias(name='TestMailPluginControllerCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestMailPluginController',
            bases=[Name(id='TestMailPluginControllerCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_enrich_and_create_company',
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
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='is_company', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test partner', kind=None),
                                            Constant(value='test@test_domain.xyz', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mock_enrich_and_create_company',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[
                                                arg(arg='_', annotation=None, type_comment=None),
                                                arg(arg='domain', annotation=None, type_comment=None),
                                            ],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Dict(
                                            keys=[Constant(value='return', kind=None)],
                                            values=[Name(id='domain', ctx=Load())],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='enrichment_info', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='type', kind=None)],
                                        values=[Constant(value='company_created', kind=None)],
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
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='additionalInfo', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='return', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='test_domain.xyz', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='company_id', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=Constant(value='company', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
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
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='company_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='partner', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='parent_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='company', ctx=Load()),
                                    Constant(value='Should change the company of the partner', kind=None),
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
                    name='test_get_partner_blacklisted_domain',
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
                            value=Constant(value='Test enrichment on a blacklisted domain.\n\n        Even is the domain is blacklisted, we should not duplicate the company each\n        time a request is made.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Name(id='list', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='iap_tools', ctx=Load()),
                                            attr='_MAIL_DOMAIN_BLACKLIST',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mock_plugin_partner_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Test', kind=None),
                                    BinOp(
                                        left=Constant(value='qsd@', kind=None),
                                        op=Add(),
                                        right=Name(id='domain', ctx=Load()),
                                    ),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[
                                                arg(arg='_', annotation=None, type_comment=None),
                                                arg(arg='__', annotation=None, type_comment=None),
                                            ],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='email', kind=None),
                                                Constant(value='iap_information', kind=None),
                                            ],
                                            values=[
                                                Constant(value='Name', kind=None),
                                                List(
                                                    elts=[
                                                        BinOp(
                                                            left=Constant(value='contact@', kind=None),
                                                            op=Add(),
                                                            right=Name(id='domain', ctx=Load()),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Constant(value='test', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='first_company_id', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='company', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='id', kind=None),
                                ctx=Load(),
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
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='first_company_id', ctx=Load()),
                                            Compare(
                                                left=Name(id='first_company_id', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Constant(value=0, kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Constant(value='partner', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='additionalInfo', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='iap_information', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='test', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='first_company', ctx=Store())],
                            value=Call(
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='first_company_id', ctx=Load())],
                                keywords=[],
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
                                        value=Name(id='first_company', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Name', kind=None),
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
                                    Attribute(
                                        value=Name(id='first_company', ctx=Load()),
                                        attr='email',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='contact@', kind=None),
                                        op=Add(),
                                        right=Name(id='domain', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mock_iap_enrich', ctx=Store())],
                            value=Call(
                                func=Name(id='Mock', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mock_plugin_partner_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Test', kind=None),
                                    BinOp(
                                        left=Constant(value='qsd@', kind=None),
                                        op=Add(),
                                        right=Name(id='domain', ctx=Load()),
                                    ),
                                    Name(id='mock_iap_enrich', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='mock_iap_enrich', ctx=Load()),
                                        attr='called',
                                        ctx=Load(),
                                    ),
                                    Constant(value='We already enriched this company, should not call IAP a second time', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='second_company_id', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='company', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='id', kind=None),
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
                                    Name(id='first_company_id', ctx=Load()),
                                    Name(id='second_company_id', ctx=Load()),
                                    Constant(value='Should not create a new company', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mock_plugin_partner_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Test', kind=None),
                                    BinOp(
                                        left=Constant(value='asbl@', kind=None),
                                        op=Add(),
                                        right=Name(id='domain', ctx=Load()),
                                    ),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[
                                                arg(arg='_', annotation=None, type_comment=None),
                                                arg(arg='domain', annotation=None, type_comment=None),
                                            ],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='email', kind=None),
                                            ],
                                            values=[
                                                Constant(value='Name', kind=None),
                                                List(
                                                    elts=[
                                                        BinOp(
                                                            left=Constant(value='asbl@', kind=None),
                                                            op=Add(),
                                                            right=Name(id='domain', ctx=Load()),
                                                        ),
                                                    ],
                                                    ctx=Load(),
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
                            targets=[Name(id='second_company_id', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='company', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='first_company_id', ctx=Load()),
                                    Name(id='second_company_id', ctx=Load()),
                                    Constant(value='Should create a new company', kind=None),
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
                    name='test_get_partner_company_found',
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
                            targets=[Name(id='company', ctx=Store())],
                            value=Call(
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='is_company', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test partner', kind=None),
                                            Constant(value='test@test_domain.xyz', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mock_iap_enrich', ctx=Store())],
                            value=Call(
                                func=Name(id='Mock', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mock_plugin_partner_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Test', kind=None),
                                    Constant(value='qsd@test_domain.xyz', kind=None),
                                    Name(id='mock_iap_enrich', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='mock_iap_enrich', ctx=Load()),
                                        attr='called',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='partner', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='partner', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='email', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='qsd@test_domain.xyz', kind=None),
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
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='company', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='id',
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='company', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='additionalInfo', kind=None),
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
                    name='test_get_partner_company_not_found',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='is_company', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test partner', kind=None),
                                            Constant(value='test@test_domain.xyz', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mock_plugin_partner_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Test', kind=None),
                                    Constant(value='qsd@test_domain.xyz', kind=None),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[
                                                arg(arg='_', annotation=None, type_comment=None),
                                                arg(arg='domain', annotation=None, type_comment=None),
                                            ],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Dict(
                                            keys=[Constant(value='enrichment_info', kind=None)],
                                            values=[Constant(value='missing_data', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='partner', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='partner', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='email', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='qsd@test_domain.xyz', kind=None),
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
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='company', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
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
                    name='test_get_partner_iap_return_different_domain',
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
                            value=Constant(value='\n        Test the case where the domain of the email returned by IAP is not the same as\n        the domain requested.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mock_plugin_partner_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Test', kind=None),
                                    Constant(value='qsd@test_domain.xyz', kind=None),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[
                                                arg(arg='_', annotation=None, type_comment=None),
                                                arg(arg='domain', annotation=None, type_comment=None),
                                            ],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='email', kind=None),
                                                Constant(value='iap_information', kind=None),
                                            ],
                                            values=[
                                                Constant(value='Name', kind=None),
                                                List(
                                                    elts=[Constant(value='contact@gmail.com', kind=None)],
                                                    ctx=Load(),
                                                ),
                                                Constant(value='test', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='first_company_id', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='company', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='first_company', ctx=Store())],
                            value=Call(
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='first_company_id', ctx=Load())],
                                keywords=[],
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='partner', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='partner', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='email', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='qsd@test_domain.xyz', kind=None),
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
                                    Name(id='first_company_id', ctx=Load()),
                                    Constant(value='Should have created the company', kind=None),
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
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Constant(value='partner', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='additionalInfo', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='iap_information', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='test', kind=None),
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
                                    Attribute(
                                        value=Name(id='first_company', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Name', kind=None),
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
                                    Attribute(
                                        value=Name(id='first_company', ctx=Load()),
                                        attr='email',
                                        ctx=Load(),
                                    ),
                                    Constant(value='contact@gmail.com', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mock_iap_enrich', ctx=Store())],
                            value=Call(
                                func=Name(id='Mock', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mock_plugin_partner_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Test', kind=None),
                                    Constant(value='qsd@test_domain.xyz', kind=None),
                                    Name(id='mock_iap_enrich', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='mock_iap_enrich', ctx=Load()),
                                        attr='called',
                                        ctx=Load(),
                                    ),
                                    Constant(value='We already enriched this company, should not call IAP a second time', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='second_company_id', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='company', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='id', kind=None),
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
                                    Name(id='first_company_id', ctx=Load()),
                                    Name(id='second_company_id', ctx=Load()),
                                    Constant(value='Should not create a new company', kind=None),
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
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Constant(value='partner', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='additionalInfo', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='iap_information', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='test', kind=None),
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
                    name='test_get_partner_no_email_returned_by_iap',
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
                            value=Constant(value='Test the case where IAP do not return an email address.\n\n        We should not duplicate the previously enriched company and we should be able to\n        retrieve the first one.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mock_plugin_partner_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Test', kind=None),
                                    Constant(value='qsd@domain.com', kind=None),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[
                                                arg(arg='_', annotation=None, type_comment=None),
                                                arg(arg='domain', annotation=None, type_comment=None),
                                            ],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='email', kind=None),
                                            ],
                                            values=[
                                                Constant(value='Name', kind=None),
                                                List(elts=[], ctx=Load()),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='first_company_id', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='company', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='id', kind=None),
                                ctx=Load(),
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
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='first_company_id', ctx=Load()),
                                            Compare(
                                                left=Name(id='first_company_id', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='first_company', ctx=Store())],
                            value=Call(
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='first_company_id', ctx=Load())],
                                keywords=[],
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
                                        value=Name(id='first_company', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Name', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='first_company', ctx=Load()),
                                        attr='email',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mock_plugin_partner_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Test', kind=None),
                                    Constant(value='qsd@domain.com', kind=None),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[
                                                arg(arg='_', annotation=None, type_comment=None),
                                                arg(arg='domain', annotation=None, type_comment=None),
                                            ],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='email', kind=None),
                                            ],
                                            values=[
                                                Constant(value='Name', kind=None),
                                                List(
                                                    elts=[
                                                        BinOp(
                                                            left=Constant(value='contact@', kind=None),
                                                            op=Add(),
                                                            right=Name(id='domain', ctx=Load()),
                                                        ),
                                                    ],
                                                    ctx=Load(),
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
                            targets=[Name(id='second_company_id', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='company', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='id', kind=None),
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
                                    Name(id='first_company_id', ctx=Load()),
                                    Name(id='second_company_id', ctx=Load()),
                                    Constant(value='Should not create a new company', kind=None),
                                ],
                                keywords=[],
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
