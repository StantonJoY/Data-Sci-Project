Module(
    body=[
        ImportFrom(
            module='odoo.addons.account.tests.common',
            names=[alias(name='AccountTestInvoicingCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ClassDef(
            name='TestAccountIncomingSupplierInvoice',
            bases=[Name(id='AccountTestInvoicingCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='chart_template_ref', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='chart_template_ref',
                                        value=Name(id='chart_template_ref', ctx=Load()),
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
                                                    value=Name(id='cls', ctx=Load()),
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
                                    Constant(value='mail.catchall.domain', kind=None),
                                    Constant(value='test-company.odoo.com', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='internal_user',
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
                                        slice=Constant(value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Internal User', kind=None),
                                            Constant(value='internal.user@test.odoo.com', kind=None),
                                            Constant(value='internal.user@test.odoo.com', kind=None),
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
                                    attr='supplier_partner',
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
                                            Constant(value='supplier_rank', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Your Supplier', kind=None),
                                            Constant(value='supplier@other.company.com', kind=None),
                                            Constant(value=10, kind=None),
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
                                    attr='journal',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='default_journal_purchase', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='journal_alias', ctx=Store())],
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
                                            Constant(value='alias_model_id', kind=None),
                                            Constant(value='alias_defaults', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test-bill', kind=None),
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
                                                    args=[Constant(value='account.model_account_move', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='json', ctx=Load()),
                                                    attr='dumps',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='move_type', kind=None),
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='journal_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='in_invoice', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='user',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='journal',
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
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='journal',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='alias_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='journal_alias', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_supplier_invoice_mailed_from_supplier',
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
                            targets=[Name(id='message_parsed', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='message_id', kind=None),
                                    Constant(value='subject', kind=None),
                                    Constant(value='from', kind=None),
                                    Constant(value='to', kind=None),
                                    Constant(value='body', kind=None),
                                    Constant(value='attachments', kind=None),
                                ],
                                values=[
                                    Constant(value='message-id-dead-beef', kind=None),
                                    Constant(value='Incoming bill', kind=None),
                                    BinOp(
                                        left=Constant(value='%s <%s>', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='supplier_partner',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='supplier_partner',
                                                        ctx=Load(),
                                                    ),
                                                    attr='email',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s@%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='journal',
                                                            ctx=Load(),
                                                        ),
                                                        attr='alias_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='alias_name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='journal',
                                                            ctx=Load(),
                                                        ),
                                                        attr='alias_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='alias_domain',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='You know, that thing that you bought.', kind=None),
                                    List(
                                        elts=[Constant(value=b'Hello, invoice', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='message_new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='message_parsed', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='move_type', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='in_invoice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='journal',
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
                            targets=[Name(id='message_ids', ctx=Store())],
                            value=Attribute(
                                value=Name(id='invoice', ctx=Load()),
                                attr='message_ids',
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='message_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='Only one message should be posted in the chatter', kind=None),
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
                                        value=Name(id='message_ids', ctx=Load()),
                                        attr='body',
                                        ctx=Load(),
                                    ),
                                    Constant(value='<p>Vendor Bill Created</p>', kind=None),
                                    Constant(value='Only the invoice creation should be posted', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='following_partners', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='message_follower_ids',
                                        ctx=Load(),
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='partner_id', kind=None)],
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
                                    Name(id='following_partners', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
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
                                    attr='assertRegex',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='BILL/\\d{4}/\\d{2}/0001', kind=None),
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
                    name='test_supplier_invoice_forwarded_by_internal_user_without_supplier',
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
                            value=Constant(value=' In this test, the bill was forwarded by an employee,\n            but no partner email address is found in the body.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='message_parsed', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='message_id', kind=None),
                                    Constant(value='subject', kind=None),
                                    Constant(value='from', kind=None),
                                    Constant(value='to', kind=None),
                                    Constant(value='body', kind=None),
                                    Constant(value='attachments', kind=None),
                                ],
                                values=[
                                    Constant(value='message-id-dead-beef', kind=None),
                                    Constant(value='Incoming bill', kind=None),
                                    BinOp(
                                        left=Constant(value='%s <%s>', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='internal_user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='internal_user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='email',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s@%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='journal',
                                                            ctx=Load(),
                                                        ),
                                                        attr='alias_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='alias_name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='journal',
                                                            ctx=Load(),
                                                        ),
                                                        attr='alias_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='alias_domain',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='You know, that thing that you bought.', kind=None),
                                    List(
                                        elts=[Constant(value=b'Hello, invoice', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='message_new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='message_parsed', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='move_type', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='in_invoice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='journal',
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
                            targets=[Name(id='message_ids', ctx=Store())],
                            value=Attribute(
                                value=Name(id='invoice', ctx=Load()),
                                attr='message_ids',
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='message_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='Only one message should be posted in the chatter', kind=None),
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
                                        value=Name(id='message_ids', ctx=Load()),
                                        attr='body',
                                        ctx=Load(),
                                    ),
                                    Constant(value='<p>Vendor Bill Created</p>', kind=None),
                                    Constant(value='Only the invoice creation should be posted', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='following_partners', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='message_follower_ids',
                                        ctx=Load(),
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='partner_id', kind=None)],
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
                                    Name(id='following_partners', ctx=Load()),
                                    BinOp(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='internal_user',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
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
                    name='test_supplier_invoice_forwarded_by_internal_with_supplier_in_body',
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
                            value=Constant(value=' In this test, the bill was forwarded by an employee,\n            and the partner email address is found in the body.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='message_parsed', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='message_id', kind=None),
                                    Constant(value='subject', kind=None),
                                    Constant(value='from', kind=None),
                                    Constant(value='to', kind=None),
                                    Constant(value='body', kind=None),
                                    Constant(value='attachments', kind=None),
                                ],
                                values=[
                                    Constant(value='message-id-dead-beef', kind=None),
                                    Constant(value='Incoming bill', kind=None),
                                    BinOp(
                                        left=Constant(value='%s <%s>', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='internal_user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='internal_user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='email',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s@%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='journal',
                                                            ctx=Load(),
                                                        ),
                                                        attr='alias_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='alias_name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='journal',
                                                            ctx=Load(),
                                                        ),
                                                        attr='alias_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='alias_domain',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    BinOp(
                                        left=Constant(value='Mail sent by %s <%s>:\nYou know, that thing that you bought.', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='supplier_partner',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='supplier_partner',
                                                        ctx=Load(),
                                                    ),
                                                    attr='email',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    List(
                                        elts=[Constant(value=b'Hello, invoice', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='message_new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='message_parsed', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='move_type', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='in_invoice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='journal',
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
                            targets=[Name(id='message_ids', ctx=Store())],
                            value=Attribute(
                                value=Name(id='invoice', ctx=Load()),
                                attr='message_ids',
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='message_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='Only one message should be posted in the chatter', kind=None),
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
                                        value=Name(id='message_ids', ctx=Load()),
                                        attr='body',
                                        ctx=Load(),
                                    ),
                                    Constant(value='<p>Vendor Bill Created</p>', kind=None),
                                    Constant(value='Only the invoice creation should be posted', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='following_partners', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='message_follower_ids',
                                        ctx=Load(),
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='partner_id', kind=None)],
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
                                    Name(id='following_partners', ctx=Load()),
                                    BinOp(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='internal_user',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
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
                    name='test_supplier_invoice_forwarded_by_internal_with_internal_in_body',
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
                            value=Constant(value=' In this test, the bill was forwarded by an employee,\n            and the internal user email address is found in the body.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='message_parsed', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='message_id', kind=None),
                                    Constant(value='subject', kind=None),
                                    Constant(value='from', kind=None),
                                    Constant(value='to', kind=None),
                                    Constant(value='body', kind=None),
                                    Constant(value='attachments', kind=None),
                                ],
                                values=[
                                    Constant(value='message-id-dead-beef', kind=None),
                                    Constant(value='Incoming bill', kind=None),
                                    BinOp(
                                        left=Constant(value='%s <%s>', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='internal_user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='internal_user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='email',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s@%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='journal',
                                                            ctx=Load(),
                                                        ),
                                                        attr='alias_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='alias_name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='journal',
                                                            ctx=Load(),
                                                        ),
                                                        attr='alias_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='alias_domain',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    BinOp(
                                        left=Constant(value='Mail sent by %s <%s>:\nYou know, that thing that you bought.', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='internal_user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='internal_user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='email',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    List(
                                        elts=[Constant(value=b'Hello, invoice', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='message_new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='message_parsed', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='move_type', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='in_invoice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='journal',
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
                            targets=[Name(id='message_ids', ctx=Store())],
                            value=Attribute(
                                value=Name(id='invoice', ctx=Load()),
                                attr='message_ids',
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='message_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='Only one message should be posted in the chatter', kind=None),
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
                                        value=Name(id='message_ids', ctx=Load()),
                                        attr='body',
                                        ctx=Load(),
                                    ),
                                    Constant(value='<p>Vendor Bill Created</p>', kind=None),
                                    Constant(value='Only the invoice creation should be posted', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='following_partners', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='message_follower_ids',
                                        ctx=Load(),
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='partner_id', kind=None)],
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
                                    Name(id='following_partners', ctx=Load()),
                                    BinOp(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='internal_user',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
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
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
