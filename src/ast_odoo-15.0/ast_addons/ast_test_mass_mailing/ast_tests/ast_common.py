Module(
    body=[
        ImportFrom(
            module='odoo.addons.mass_mailing.tests.common',
            names=[alias(name='MassMailCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.test_mail.tests.common',
            names=[alias(name='TestMailCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestMassMailCommon',
            bases=[
                Name(id='MassMailCommon', ctx=Load()),
                Name(id='TestMailCommon', ctx=Load()),
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
                                            Name(id='TestMassMailCommon', ctx=Load()),
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
                                    attr='test_alias',
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
                                        slice=Constant(value='mail.alias', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='alias_name', kind=None),
                                            Constant(value='alias_user_id', kind=None),
                                            Constant(value='alias_model_id', kind=None),
                                            Constant(value='alias_contact', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test.alias', kind=None),
                                            Constant(value=False, kind=None),
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
                                                    args=[Constant(value='mailing.test.simple', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='everyone', kind=None),
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
                                    attr='mailing_bl',
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
                                            Constant(value='preview', kind=None),
                                            Constant(value='body_html', kind=None),
                                            Constant(value='mailing_type', kind=None),
                                            Constant(value='mailing_model_id', kind=None),
                                            Constant(value='reply_to_mode', kind=None),
                                        ],
                                        values=[
                                            Constant(value='SourceName', kind=None),
                                            Constant(value='MailingSubject', kind=None),
                                            Constant(value='Hi {{ object.name + "" }} :)', kind=None),
                                            Constant(value='<div><p>Hello <t t-out="object.name"/></p>,\n<t t-set="url" t-value="\'www.odoo.com\'"/>\n<t t-set="httpurl" t-value="\'https://www.odoo.eu\'"/>f\n<span>Website0: <a id="url0" t-attf-href="https://www.odoo.tz/my/{{object.name}}">https://www.odoo.tz/my/<t t-out="object.name"/></a></span>\n<span>Website1: <a id="url1" href="https://www.odoo.be">https://www.odoo.be</a></span>\n<span>Website2: <a id="url2" t-attf-href="https://{{url}}">https://<t t-out="url"/></a></span>\n<span>Website3: <a id="url3" t-att-href="httpurl"><t t-out="httpurl"/></a></span>\n<span>External1: <a id="url4" href="https://www.example.com/foo/bar?baz=qux">Youpie</a></span>\n<span>Internal1: <a id="url5" href="/event/dummy-event-0">Internal link</a></span>\n<span>Internal2: <a id="url6" href="/view"/>View link</a></span>\n<span>Email: <a id="url7" href="mailto:test@odoo.com">test@odoo.com</a></span>\n<p>Stop spam ? <a id="url8" role="button" href="/unsubscribe_from_list">Ok</a></p>\n</div>', kind=None),
                                            Constant(value='mail', kind=None),
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
                                                    args=[Constant(value='mailing.test.blacklist', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='update', kind=None),
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
                    name='_create_test_blacklist_records',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='count', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='mailing.test.blacklist', kind=None),
                            Constant(value=1, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Deprecated, remove in 14.4 ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='__create_mailing_test_records',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Name(id='model', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='count',
                                        value=Name(id='count', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_mailing_test_records',
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
                            Constant(value='mailing.test.blacklist', kind=None),
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
                            targets=[Name(id='email_field', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Constant(value='email', kind=None),
                                    ops=[In()],
                                    comparators=[Name(id='Model', ctx=Load())],
                                ),
                                body=Constant(value='email', kind=None),
                                orelse=Constant(value='email_from', kind=None),
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
                            target=Name(id='x', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    Name(id='count', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='vals', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Name(id='email_field', ctx=Load()),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Constant(value='TestRecord_%02d', kind=None),
                                                op=Mod(),
                                                right=Name(id='x', ctx=Load()),
                                            ),
                                            BinOp(
                                                left=Constant(value='"TestCustomer %02d" <test.record.%02d@test.example.com>', kind=None),
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
                                                    left=Name(id='x', ctx=Load()),
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
    ],
    type_ignores=[],
)
