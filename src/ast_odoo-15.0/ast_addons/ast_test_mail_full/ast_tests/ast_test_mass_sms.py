Module(
    body=[
        ImportFrom(
            module='ast',
            names=[alias(name='literal_eval', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.phone_validation.tools',
            names=[alias(name='phone_validation', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.test_mail_full.tests.common',
            names=[alias(name='TestMailFullCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='exceptions', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='users', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestMassSMSCommon',
            bases=[Name(id='TestMailFullCommon', ctx=Load())],
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
                                            Name(id='TestMassSMSCommon', ctx=Load()),
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
                                    attr='_test_body',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Mass SMS in your face', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='mail.test.sms', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partners', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='country_be_id', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Attribute(
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
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='country_us_id', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Attribute(
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
                                            args=[Constant(value='base.us', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='x', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Constant(value=10, kind=None)],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='partners', ctx=Store()),
                                    op=Add(),
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
                                                        slice=Constant(value='res.partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg=None,
                                                        value=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='_test_context',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='email', kind=None),
                                                    Constant(value='country_id', kind=None),
                                                    Constant(value='mobile', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='Partner_%s', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='x', ctx=Load()),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='_test_partner_%s@example.com', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='x', ctx=Load()),
                                                    ),
                                                    Name(id='country_be_id', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='045600%s%s99', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='x', ctx=Load()),
                                                                Name(id='x', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='records', ctx=Store()),
                                    op=Add(),
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
                                                        slice=Constant(value='mail.test.sms', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg=None,
                                                        value=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='_test_context',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='customer_id', kind=None),
                                                    Constant(value='phone_nbr', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='MassSMSTest_%s', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='x', ctx=Load()),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='partners', ctx=Load()),
                                                            slice=Name(id='x', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='045600%s%s44', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='x', ctx=Load()),
                                                                Name(id='x', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='records',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_reset_mail_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='records', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='records_numbers',
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='phone_validation', ctx=Load()),
                                        attr='phone_format',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='phone_nbr',
                                            ctx=Load(),
                                        ),
                                        Constant(value='BE', kind=None),
                                        Constant(value='32', kind=None),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='force_format',
                                            value=Constant(value='E164', kind=None),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='r', ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='records',
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='partners',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='partners', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='sms_template',
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
                                        slice=Constant(value='sms.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model_id', kind=None),
                                            Constant(value='body', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Template', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='cls', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='mail.test.sms', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Dear {{ object.display_name }} this is a mass SMS.', kind=None),
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
                                    attr='partner_numbers',
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='phone_validation', ctx=Load()),
                                        attr='phone_format',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='mobile',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='country_id',
                                                ctx=Load(),
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='country_id',
                                                ctx=Load(),
                                            ),
                                            attr='phone_code',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='force_format',
                                            value=Constant(value='E164', kind=None),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='partner', ctx=Store()),
                                        iter=Name(id='partners', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='mailing',
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
                                                slice=Constant(value='mailing.mailing', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='user_marketing',
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
                                            Constant(value='subject', kind=None),
                                            Constant(value='mailing_model_id', kind=None),
                                            Constant(value='mailing_type', kind=None),
                                            Constant(value='mailing_domain', kind=None),
                                            Constant(value='sms_template_id', kind=None),
                                            Constant(value='sms_allow_unsubscribe', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Xmas Spam', kind=None),
                                            Constant(value='Xmas Spam', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='cls', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='mail.test.sms', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='sms', kind=None),
                                            BinOp(
                                                left=Constant(value='%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='repr', ctx=Load()),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='name', kind=None),
                                                                        Constant(value='ilike', kind=None),
                                                                        Constant(value='MassSMSTest', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='sms_template',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
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
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='mass_mailing', kind=None)],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestMassSMSInternals',
            bases=[Name(id='TestMassSMSCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_mass_sms_domain',
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
                            targets=[Name(id='mailing', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.mailing', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='mailing_model_id', kind=None),
                                            Constant(value='mailing_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Xmas Spam', kind=None),
                                            Constant(value='Xmas Spam', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='mail.test.sms', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='sms', kind=None),
                                        ],
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
                                    Call(
                                        func=Name(id='literal_eval', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='mailing', ctx=Load()),
                                                attr='mailing_domain',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mailing', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.mailing', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='mailing_model_id', kind=None),
                                            Constant(value='mailing_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Xmas Spam', kind=None),
                                            Constant(value='Xmas Spam', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='mail.test.sms.bl', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='sms', kind=None),
                                        ],
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
                                    Call(
                                        func=Name(id='literal_eval', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='mailing', ctx=Load()),
                                                attr='mailing_domain',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='phone_sanitized_blacklisted', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='user_marketing', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mass_sms_internals',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='user_marketing', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='mailing', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mailing.mailing', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='subject', kind=None),
                                                    Constant(value='mailing_model_id', kind=None),
                                                    Constant(value='mailing_type', kind=None),
                                                    Constant(value='mailing_domain', kind=None),
                                                    Constant(value='sms_template_id', kind=None),
                                                    Constant(value='sms_allow_unsubscribe', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Xmas Spam', kind=None),
                                                    Constant(value='Xmas Spam', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='ir.model', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='mail.test.sms', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='sms', kind=None),
                                                    BinOp(
                                                        left=Constant(value='%s', kind=None),
                                                        op=Mod(),
                                                        right=Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value='name', kind=None),
                                                                                Constant(value='ilike', kind=None),
                                                                                Constant(value='MassSMSTest', kind=None),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='sms_template',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
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
                                            Attribute(
                                                value=Name(id='mailing', ctx=Load()),
                                                attr='mailing_model_real',
                                                ctx=Load(),
                                            ),
                                            Constant(value='mail.test.sms', kind=None),
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
                                                value=Name(id='mailing', ctx=Load()),
                                                attr='medium_id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mass_mailing_sms.utm_medium_sms', kind=None)],
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
                                            Attribute(
                                                value=Name(id='mailing', ctx=Load()),
                                                attr='body_plaintext',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sms_template',
                                                    ctx=Load(),
                                                ),
                                                attr='body',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='remaining_res_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mailing', ctx=Load()),
                                            attr='_get_remaining_recipients',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                                            Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[Name(id='remaining_res_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='records',
                                                            ctx=Load(),
                                                        ),
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
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mockSMSGateway',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='mailing', ctx=Load()),
                                                    attr='action_send_sms',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMSTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='partner', kind=None),
                                                Constant(value='number', kind=None),
                                                Constant(value='content', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='customer_id',
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='records_numbers',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='i', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                BinOp(
                                                    left=Constant(value='Dear %s this is a mass SMS.', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='i', ctx=Store()),
                                                        Name(id='record', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Name(id='enumerate', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='records',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Name(id='mailing', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='records',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='user_marketing', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mass_sms_internals_errors',
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
                            targets=[Name(id='new_record_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.sms', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='phone_nbr', kind=None),
                                        ],
                                        values=[
                                            Constant(value='MassSMSTest_nr1', kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partners',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='0456999999', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='void_record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.sms', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='phone_nbr', kind=None),
                                        ],
                                        values=[
                                            Constant(value='MassSMSTest_void', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='falsy_record_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.sms', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='phone_nbr', kind=None),
                                        ],
                                        values=[
                                            Constant(value='MassSMSTest_falsy_1', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='abcd', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='falsy_record_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.sms', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='phone_nbr', kind=None),
                                        ],
                                        values=[
                                            Constant(value='MassSMSTest_falsy_2', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='04561122', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bl_record_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.sms', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='phone_nbr', kind=None),
                                        ],
                                        values=[
                                            Constant(value='MassSMSTest_bl_1', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='0456110011', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
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
                                        slice=Constant(value='phone.blacklist', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='number', kind=None)],
                                        values=[Constant(value='0456110011', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='country_be_id', ctx=Store())],
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
                                    args=[Constant(value='base.be', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='nr2_partner', ctx=Store())],
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
                                            Constant(value='country_id', kind=None),
                                            Constant(value='mobile', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Partner_nr2', kind=None),
                                            Name(id='country_be_id', ctx=Load()),
                                            Constant(value='0456449999', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_record_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.sms', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='phone_nbr', kind=None),
                                        ],
                                        values=[
                                            Constant(value='MassSMSTest_nr2', kind=None),
                                            Attribute(
                                                value=Name(id='nr2_partner', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='records',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='phone_nbr',
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
                            targets=[Name(id='records_numbers', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='records_numbers',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=List(
                                    elts=[Constant(value='+32456999999', kind=None)],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='user_marketing', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mockSMSGateway',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='mailing',
                                                        ctx=Load(),
                                                    ),
                                                    attr='action_send_sms',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMSTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='partner', kind=None),
                                                Constant(value='number', kind=None),
                                                Constant(value='content', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='customer_id',
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='records_numbers', ctx=Load()),
                                                    slice=Name(id='i', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                BinOp(
                                                    left=Constant(value='Dear %s this is a mass SMS.', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='i', ctx=Store()),
                                                        Name(id='record', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Name(id='enumerate', ctx=Load()),
                                                    args=[
                                                        BinOp(
                                                            left=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='records',
                                                                ctx=Load(),
                                                            ),
                                                            op=BitOr(),
                                                            right=Name(id='new_record_1', ctx=Load()),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mailing',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='records',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Name(id='new_record_1', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMSTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='partner', kind=None),
                                                    Constant(value='number', kind=None),
                                                    Constant(value='content', kind=None),
                                                    Constant(value='trace_status', kind=None),
                                                    Constant(value='failure_type', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='new_record_2', ctx=Load()),
                                                        attr='customer_id',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='records_numbers',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='Dear %s this is a mass SMS.', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='new_record_2', ctx=Load()),
                                                            attr='display_name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Constant(value='cancel', kind=None),
                                                    Constant(value='sms_duplicate', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mailing',
                                        ctx=Load(),
                                    ),
                                    Name(id='new_record_2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMSTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='partner', kind=None),
                                                    Constant(value='number', kind=None),
                                                    Constant(value='content', kind=None),
                                                    Constant(value='trace_status', kind=None),
                                                    Constant(value='failure_type', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='phone_validation', ctx=Load()),
                                                            attr='phone_format',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='bl_record_1', ctx=Load()),
                                                                attr='phone_nbr',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='BE', kind=None),
                                                            Constant(value='32', kind=None),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='force_format',
                                                                value=Constant(value='E164', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='Dear %s this is a mass SMS.', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='bl_record_1', ctx=Load()),
                                                            attr='display_name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Constant(value='cancel', kind=None),
                                                    Constant(value='sms_blacklist', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mailing',
                                        ctx=Load(),
                                    ),
                                    Name(id='bl_record_1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMSTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='partner', kind=None),
                                                    Constant(value='number', kind=None),
                                                    Constant(value='content', kind=None),
                                                    Constant(value='trace_status', kind=None),
                                                    Constant(value='failure_type', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    BinOp(
                                                        left=Constant(value='Dear %s this is a mass SMS.', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='void_record', ctx=Load()),
                                                            attr='display_name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Constant(value='cancel', kind=None),
                                                    Constant(value='sms_number_missing', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mailing',
                                        ctx=Load(),
                                    ),
                                    Name(id='void_record', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMSTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='partner', kind=None),
                                                Constant(value='number', kind=None),
                                                Constant(value='content', kind=None),
                                                Constant(value='trace_status', kind=None),
                                                Constant(value='failure_type', kind=None),
                                            ],
                                            values=[
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
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='phone_nbr',
                                                    ctx=Load(),
                                                ),
                                                BinOp(
                                                    left=Constant(value='Dear %s this is a mass SMS.', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Constant(value='cancel', kind=None),
                                                Constant(value='sms_number_format', kind=None),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='record', ctx=Store()),
                                                iter=BinOp(
                                                    left=Name(id='falsy_record_1', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='falsy_record_2', ctx=Load()),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mailing',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='falsy_record_1', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='falsy_record_2', ctx=Load()),
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
                    name='test_mass_sms_internals_done_ids',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='user_marketing', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mockSMSGateway',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='mailing',
                                                        ctx=Load(),
                                                    ),
                                                    attr='action_send_sms',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='res_ids',
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='records',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Slice(
                                                                    lower=None,
                                                                    upper=Constant(value=5, kind=None),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
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
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='mailing',
                                                            ctx=Load(),
                                                        ),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='traces', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=5, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMSTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='partner', kind=None),
                                                Constant(value='number', kind=None),
                                                Constant(value='content', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='customer_id',
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='records_numbers',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='i', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                BinOp(
                                                    left=Constant(value='Dear %s this is a mass SMS.', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='i', ctx=Store()),
                                                        Name(id='record', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Name(id='enumerate', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='records',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Slice(
                                                                lower=None,
                                                                upper=Constant(value=5, kind=None),
                                                                step=None,
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mailing',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='records',
                                            ctx=Load(),
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=5, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='user_marketing', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mockSMSGateway',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='mailing',
                                                        ctx=Load(),
                                                    ),
                                                    attr='action_send_sms',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='res_ids',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='records',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='traces', ctx=Load()),
                                    attr='unlink',
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
                                    attr='assertSMSTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='partner', kind=None),
                                                Constant(value='number', kind=None),
                                                Constant(value='content', kind=None),
                                                Constant(value='trace_status', kind=None),
                                                Constant(value='failure_type', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='customer_id',
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='records_numbers',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='i', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                BinOp(
                                                    left=Constant(value='Dear %s this is a mass SMS.', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Constant(value='cancel', kind=None),
                                                Constant(value='sms_duplicate', kind=None),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='i', ctx=Store()),
                                                        Name(id='record', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Name(id='enumerate', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='records',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Slice(
                                                                lower=None,
                                                                upper=Constant(value=5, kind=None),
                                                                step=None,
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mailing',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='records',
                                            ctx=Load(),
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=5, kind=None),
                                            step=None,
                                        ),
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
                                    attr='assertSMSTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='partner', kind=None),
                                                Constant(value='number', kind=None),
                                                Constant(value='content', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='customer_id',
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='records_numbers',
                                                        ctx=Load(),
                                                    ),
                                                    slice=BinOp(
                                                        left=Name(id='i', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=5, kind=None),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                BinOp(
                                                    left=Constant(value='Dear %s this is a mass SMS.', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='i', ctx=Store()),
                                                        Name(id='record', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Name(id='enumerate', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='records',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Slice(
                                                                lower=Constant(value=5, kind=None),
                                                                upper=None,
                                                                step=None,
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mailing',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='records',
                                            ctx=Load(),
                                        ),
                                        slice=Slice(
                                            lower=Constant(value=5, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
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
                    name='test_mass_sms_test_button',
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
                            targets=[Name(id='mailing', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.mailing', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='preview', kind=None),
                                            Constant(value='state', kind=None),
                                            Constant(value='mailing_type', kind=None),
                                            Constant(value='body_plaintext', kind=None),
                                            Constant(value='mailing_model_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='TestButton', kind=None),
                                            Constant(value='Subject {{ object.name }}', kind=None),
                                            Constant(value='Preview {{ object.name }}', kind=None),
                                            Constant(value='draft', kind=None),
                                            Constant(value='sms', kind=None),
                                            Constant(value='Hello {{ object.name }}', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='res.partner', kind=None)],
                                                    keywords=[],
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
                            targets=[Name(id='mailing_test', ctx=Store())],
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
                                                slice=Constant(value='mailing.sms.test', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_marketing',
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
                                            Constant(value='numbers', kind=None),
                                            Constant(value='mailing_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='+32456001122', kind=None),
                                            Attribute(
                                                value=Name(id='mailing', ctx=Load()),
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='user_marketing', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mockSMSGateway',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='mailing_test', ctx=Load()),
                                                    attr='action_send_sms',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mailing', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='body_plaintext', kind=None)],
                                        values=[Constant(value='Hello {{ object.name_id.id }}', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='user_marketing', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mock_mail_gateway',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertRaises',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='Exception', ctx=Load())],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='mailing_test', ctx=Load()),
                                                    attr='action_send_sms',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.addons.mail.models.mail_render_mixin', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='mass_mailing', kind=None)],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestMassSMS',
            bases=[Name(id='TestMassSMSCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_mass_sms_links',
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
                            targets=[Name(id='mailing', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.mailing', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mailing',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
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
                                    value=Name(id='mailing', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='body_plaintext', kind=None),
                                            Constant(value='sms_template_id', kind=None),
                                            Constant(value='sms_force_send', kind=None),
                                            Constant(value='sms_allow_unsubscribe', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Dear {{ object.display_name }} this is a mass SMS with two links http://www.odoo.com/smstest and http://www.odoo.com/smstest/{{ object.name }}', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mockSMSGateway',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mailing', ctx=Load()),
                                            attr='action_send_sms',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMSTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='partner', kind=None),
                                                Constant(value='number', kind=None),
                                                Constant(value='trace_status', kind=None),
                                                Constant(value='content', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='customer_id',
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='records_numbers',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='i', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                Constant(value='sent', kind=None),
                                                BinOp(
                                                    left=Constant(value='Dear %s this is a mass SMS with two links', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='i', ctx=Store()),
                                                        Name(id='record', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Name(id='enumerate', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='records',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Name(id='mailing', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='records',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='sms_links_info',
                                        value=ListComp(
                                            elt=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='http://www.odoo.com/smstest', kind=None),
                                                            Constant(value=True, kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            BinOp(
                                                                left=Constant(value='http://www.odoo.com/smstest/%s', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='unsubscribe', kind=None),
                                                            Constant(value=False, kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='record', ctx=Store()),
                                                    iter=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='records',
                                                        ctx=Load(),
                                                    ),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='user_marketing', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mass_sms_partner_only',
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
                            value=Constant(value=' Check sending SMS marketing on models having only a partner_id fields\n        set is working. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='mailing', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.mailing', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mailing_sms',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
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
                                    value=Name(id='mailing', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='mailing_model_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='mail.test.sms.partner', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.sms.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='customer_id', kind=None),
                                            ],
                                            values=[
                                                BinOp(
                                                    left=Constant(value='SMSTest on %s', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='partner', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partners',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mockSMSGateway',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mailing', ctx=Load()),
                                            attr='action_send_sms',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
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
                                    Call(
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
                                    Constant(value=10, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMSTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='partner', kind=None),
                                                Constant(value='number', kind=None),
                                                Constant(value='trace_status', kind=None),
                                                Constant(value='content', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='customer_id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='customer_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='phone_sanitized',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='sent', kind=None),
                                                BinOp(
                                                    left=Constant(value='Dear %s this is a mass SMS with two links', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='record', ctx=Store()),
                                                iter=Name(id='records', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Name(id='mailing', ctx=Load()),
                                    Name(id='records', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='sms_links_info',
                                        value=ListComp(
                                            elt=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='http://www.odoo.com/smstest', kind=None),
                                                            Constant(value=True, kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            BinOp(
                                                                left=Constant(value='http://www.odoo.com/smstest/%s', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='unsubscribe', kind=None),
                                                            Constant(value=False, kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='record', ctx=Store()),
                                                    iter=Name(id='records', ctx=Load()),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='new_record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.sms.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='customer_id', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='Duplicate SMS on %s', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='partners',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partners',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mockSMSGateway',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mailing', ctx=Load()),
                                            attr='action_send_sms',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
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
                                    Call(
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
                                    Constant(value=11, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMSTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='partner', kind=None),
                                                    Constant(value='number', kind=None),
                                                    Constant(value='trace_status', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='new_record', ctx=Load()),
                                                        attr='customer_id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='new_record', ctx=Load()),
                                                            attr='customer_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='phone_sanitized',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='sent', kind=None),
                                                    BinOp(
                                                        left=Constant(value='Dear %s this is a mass SMS with two links', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='new_record', ctx=Load()),
                                                            attr='display_name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='mailing', ctx=Load()),
                                    Name(id='new_record', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='sms_links_info',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='http://www.odoo.com/smstest', kind=None),
                                                                Constant(value=True, kind=None),
                                                                Dict(keys=[], values=[]),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                BinOp(
                                                                    left=Constant(value='http://www.odoo.com/smstest/%s', kind=None),
                                                                    op=Mod(),
                                                                    right=Attribute(
                                                                        value=Name(id='new_record', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                Constant(value=True, kind=None),
                                                                Dict(keys=[], values=[]),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='unsubscribe', kind=None),
                                                                Constant(value=False, kind=None),
                                                                Dict(keys=[], values=[]),
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
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='user_marketing', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.addons.mail.models.mail_mail', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mass_sms_partner_only_m2m',
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
                            value=Constant(value=' Check sending SMS marketing on models having only a m2m to partners\n        is currently not suppored. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='mailing', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.mailing', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mailing_sms',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
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
                                    value=Name(id='mailing', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='mailing_model_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='mail.test.sms.partner.2many', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
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
                                        slice=Constant(value='mail.test.sms.partner.2many', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='customer_ids', kind=None),
                                            ],
                                            values=[
                                                BinOp(
                                                    left=Constant(value='SMSTest on %s', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=4, kind=None),
                                                                Attribute(
                                                                    value=Name(id='partner', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='partner', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partners',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='exceptions', ctx=Load()),
                                                attr='UserError',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mockSMSGateway',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mailing', ctx=Load()),
                                            attr='action_send_sms',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='user_marketing', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.addons.mail.models.mail_mail', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mass_sms_w_opt_out',
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
                            targets=[Name(id='mailing', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.mailing', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mailing_sms',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recipients', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_mailing_sms_test_records',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='mail.test.sms.bl.optout', kind=None),
                                    ),
                                    keyword(
                                        arg='count',
                                        value=Constant(value=5, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=BinOp(
                                        left=Subscript(
                                            value=Name(id='recipients', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Subscript(
                                            value=Name(id='recipients', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='opt_out', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
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
                                                slice=Constant(value='phone.blacklist', kind=None),
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
                                        keys=[Constant(value='number', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='recipients', ctx=Load()),
                                                    slice=Constant(value=4, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='phone_nbr',
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
                                    value=Name(id='mailing', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='mailing_model_id', kind=None),
                                            Constant(value='mailing_domain', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.model', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mail.test.sms.bl.optout', kind=None)],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Name(id='recipients', ctx=Load()),
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mockSMSGateway',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mailing', ctx=Load()),
                                            attr='action_send_sms',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertSMSTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='number', kind=None),
                                                    Constant(value='trace_status', kind=None),
                                                    Constant(value='failure_type', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='+32456000000', kind=None),
                                                    Constant(value='cancel', kind=None),
                                                    Constant(value='sms_optout', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='number', kind=None),
                                                    Constant(value='trace_status', kind=None),
                                                    Constant(value='failure_type', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='+32456000101', kind=None),
                                                    Constant(value='cancel', kind=None),
                                                    Constant(value='sms_optout', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='number', kind=None),
                                                    Constant(value='trace_status', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='+32456000202', kind=None),
                                                    Constant(value='sent', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='number', kind=None),
                                                    Constant(value='trace_status', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='+32456000303', kind=None),
                                                    Constant(value='sent', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='number', kind=None),
                                                    Constant(value='trace_status', kind=None),
                                                    Constant(value='failure_type', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='+32456000404', kind=None),
                                                    Constant(value='cancel', kind=None),
                                                    Constant(value='sms_blacklist', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='mailing', ctx=Load()),
                                    Name(id='recipients', ctx=Load()),
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
                                        value=Name(id='mailing', ctx=Load()),
                                        attr='canceled',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='user_marketing', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.addons.mail.models.mail_mail', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='mass_mailing', kind=None),
                        Constant(value='mass_mailing_sms', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
