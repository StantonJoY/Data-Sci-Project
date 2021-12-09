Module(
    body=[
        ImportFrom(
            module='odoo.addons.phone_validation.tools',
            names=[alias(name='phone_validation', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mass_mailing_sms.tests.common',
            names=[alias(name='MassSMSCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.test_mail.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.test_mass_mailing.tests.common',
            names=[alias(name='TestMassMailCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestMailFullCommon',
            bases=[
                Name(id='TestMassMailCommon', ctx=Load()),
                Name(id='MassSMSCommon', ctx=Load()),
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
                                            Name(id='TestMailFullCommon', ctx=Load()),
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
                                    attr='mailing_sms',
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
                                            Constant(value='body_plaintext', kind=None),
                                            Constant(value='sms_force_send', kind=None),
                                            Constant(value='sms_allow_unsubscribe', kind=None),
                                        ],
                                        values=[
                                            Constant(value='XMas SMS', kind=None),
                                            Constant(value='Xmas SMS for {object.name}', kind=None),
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
                                                                        Constant(value='SMSTest', kind=None),
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
                                            Constant(value='Dear {{ object.display_name }} this is a mass SMS with two links http://www.odoo.com/smstest and http://www.odoo.com/smstest/{{ object.id }}', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
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
                    name='_create_mailing_sms_test_records',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='partners', annotation=None, type_comment=None),
                            arg(arg='count', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='mail.test.sms', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=1, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Helper to create data. Currently simple, to be improved. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='Model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Name(id='model', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='phone_field', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Constant(value='phone_nbr', kind=None),
                                    ops=[In()],
                                    comparators=[Name(id='Model', ctx=Load())],
                                ),
                                body=Constant(value='phone_nbr', kind=None),
                                orelse=Constant(value='phone', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner_field', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Constant(value='customer_id', kind=None),
                                    ops=[In()],
                                    comparators=[Name(id='Model', ctx=Load())],
                                ),
                                body=Constant(value='customer_id', kind=None),
                                orelse=Constant(value='partner_id', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='idx', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Name(id='count', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='vals', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Name(id='phone_field', ctx=Load()),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Constant(value='SMSTestRecord_%02d', kind=None),
                                                op=Mod(),
                                                right=Name(id='idx', ctx=Load()),
                                            ),
                                            BinOp(
                                                left=Constant(value='045600%02d%02d', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='idx', ctx=Load()),
                                                        Name(id='idx', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='partners', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Name(id='partner_field', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='partners', ctx=Load()),
                                                slice=BinOp(
                                                    left=Name(id='idx', ctx=Load()),
                                                    op=Mod(),
                                                    right=Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='partners', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='vals_list', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
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
        ClassDef(
            name='TestMailFullRecipients',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TestRecipients',
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
                                            Name(id='TestMailFullRecipients', ctx=Load()),
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
                                        iter=BinOp(
                                            left=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='partner_1',
                                                ctx=Load(),
                                            ),
                                            op=BitOr(),
                                            right=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='partner_2',
                                                ctx=Load(),
                                            ),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
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
