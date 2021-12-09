Module(
    body=[
        ImportFrom(
            module='odoo.addons.account.tests.common',
            names=[alias(name='AccountTestInvoicingCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='tagged', asname=None),
                alias(name='Form', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ClassDef(
            name='TestTransferWizard',
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='company', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='receivable_account',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='default_account_receivable', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='payable_account',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='default_account_payable', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='accounts',
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
                                        slice=Constant(value='account.account', kind=None),
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
                                                    Constant(value='reconcile', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='company',
                                                            ctx=Load(),
                                                        ),
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
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=5, kind=None),
                                    ),
                                ],
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
                                slice=Constant(value='default_journal_misc', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
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
                                                slice=Constant(value='res.currency.rate', kind=None),
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
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='company',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='currency_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='cls', ctx=Load()),
                                                                        attr='company',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='currency_id',
                                                                    ctx=Load(),
                                                                ),
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
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='rate', kind=None)],
                                        values=[Constant(value=1, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='test_currency_1',
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
                                        slice=Constant(value='res.currency', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='symbol', kind=None),
                                        ],
                                        values=[
                                            Constant(value='PMK', kind=None),
                                            Constant(value='P', kind=None),
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
                                    attr='test_currency_2',
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
                                        slice=Constant(value='res.currency', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='symbol', kind=None),
                                        ],
                                        values=[
                                            Constant(value='toto', kind=None),
                                            Constant(value='To', kind=None),
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
                                    attr='test_currency_3',
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
                                        slice=Constant(value='res.currency', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='symbol', kind=None),
                                        ],
                                        values=[
                                            Constant(value='titi', kind=None),
                                            Constant(value='Ti', kind=None),
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
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.currency.rate', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='rate', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='company_id', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='time', ctx=Load()),
                                                                attr='strftime',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='%Y', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value='-', kind=None),
                                                    ),
                                                    op=Add(),
                                                    right=Constant(value='01', kind=None),
                                                ),
                                                op=Add(),
                                                right=Constant(value='-01', kind=None),
                                            ),
                                            Constant(value=0.5, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='test_currency_1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company',
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.currency.rate', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='rate', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='company_id', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='time', ctx=Load()),
                                                                attr='strftime',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='%Y', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value='-', kind=None),
                                                    ),
                                                    op=Add(),
                                                    right=Constant(value='01', kind=None),
                                                ),
                                                op=Add(),
                                                right=Constant(value='-01', kind=None),
                                            ),
                                            Constant(value=2, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='test_currency_2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company',
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.currency.rate', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='rate', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='company_id', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='time', ctx=Load()),
                                                                attr='strftime',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='%Y', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value='-', kind=None),
                                                    ),
                                                    op=Add(),
                                                    right=Constant(value='01', kind=None),
                                                ),
                                                op=Add(),
                                                right=Constant(value='-01', kind=None),
                                            ),
                                            Constant(value=10, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='test_currency_3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company',
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
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='test_currency_account',
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
                                        slice=Constant(value='account.account', kind=None),
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
                                            Constant(value='user_type_id', kind=None),
                                            Constant(value='currency_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test destination account', kind=None),
                                            Constant(value='test_dest_acc', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.model.data', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_xmlid_to_res_id',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='account.data_account_type_current_assets', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='test_currency_3',
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
                                    attr='move_1',
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
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='line_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='journal',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test1_1', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='receivable_account',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=500, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test1_2', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=500, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='partner_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test1_3', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=800, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='partner_a',
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
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test1_4', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=1, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=500, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='partner_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test1_5', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=2, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=300, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='partner_a',
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
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='currency_id', kind=None),
                                                                    Constant(value='amount_currency', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test1_6', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=270, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='test_currency_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=540, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test1_7', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=1, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=140, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test1_8', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=2, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=160, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='currency_id', kind=None),
                                                                    Constant(value='amount_currency', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test1_9', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=2, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=30, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='test_currency_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=15, kind=None),
                                                                ],
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='move_1',
                                        ctx=Load(),
                                    ),
                                    attr='action_post',
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
                                    attr='move_2',
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
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='line_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='journal',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test2_1', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=1, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=400, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test2_2', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='payable_account',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=400, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='partner_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test2_3', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=3, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=250, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='partner_a',
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
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='partner_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test2_4', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=1, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=480, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='partner_b',
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
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='partner_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test2_5', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=2, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=730, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='partner_a',
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
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='partner_id', kind=None),
                                                                    Constant(value='currency_id', kind=None),
                                                                    Constant(value='amount_currency', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test2_6', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=2, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=412, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='partner_a',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='test_currency_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=633, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test2_7', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=1, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=572, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='partner_id', kind=None),
                                                                    Constant(value='currency_id', kind=None),
                                                                    Constant(value='amount_currency', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test2_8', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=2, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=100, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='partner_a',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='test_currency_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=123, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='partner_id', kind=None),
                                                                    Constant(value='currency_id', kind=None),
                                                                    Constant(value='amount_currency', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test2_9', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='accounts',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=2, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=60, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='partner_a',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='test_currency_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=10, kind=None),
                                                                    ),
                                                                ],
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='move_2',
                                        ctx=Load(),
                                    ),
                                    attr='action_post',
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
                    name='test_transfer_wizard_reconcile',
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
                            value=Constant(value=' Tests reconciliation when doing a transfer with the wizard\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='active_move_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='move_1',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='move_2',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='line_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='x', ctx=Load()),
                                                        attr='account_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user_type_id',
                                                    ctx=Load(),
                                                ),
                                                attr='type',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='receivable', kind=None),
                                                        Constant(value='payable', kind=None),
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
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='active_model', kind=None),
                                    Constant(value='active_ids', kind=None),
                                ],
                                values=[
                                    Constant(value='account.move.line', kind=None),
                                    Attribute(
                                        value=Name(id='active_move_lines', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.automatic.entry.wizard', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='context', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='wizard_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard_form', ctx=Load()),
                                            attr='action',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='change_account', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard_form', ctx=Load()),
                                            attr='destination_account_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='receivable_account',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard_form', ctx=Load()),
                                            attr='journal_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='journal',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='wizard_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='transfer_move_id', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='wizard', ctx=Load()),
                                        attr='do_action',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value='res_id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='transfer_move', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='transfer_move_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payable_transfer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='transfer_move', ctx=Load()),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='account_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='payable_account',
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
                            targets=[Name(id='receivable_transfer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='transfer_move', ctx=Load()),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='account_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='receivable_account',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='payable_transfer', ctx=Load()),
                                        attr='reconciled',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Payable line of the transfer move should be fully reconciled', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='move_1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='line_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='filtered',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='x', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Compare(
                                                        left=Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='account_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='receivable_account',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='amount_residual',
                                        ctx=Load(),
                                    ),
                                    Constant(value=100, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Receivable line of the original move should be partially reconciled, and still have a residual amount of 100 (500 - 400 from payable account)', kind=None),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='move_2',
                                                        ctx=Load(),
                                                    ),
                                                    attr='line_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='filtered',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='x', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Compare(
                                                        left=Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='account_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='payable_account',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='reconciled',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Payable line of the original move should be fully reconciled', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='receivable_transfer', ctx=Load()),
                                        attr='amount_residual',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Receivable line from the transfer move should have nothing left to reconcile', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='payable_transfer', ctx=Load()),
                                        attr='debit',
                                        ctx=Load(),
                                    ),
                                    Constant(value=400, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
                                        ctx=Load(),
                                    ),
                                    Constant(value='400 should have been debited from payable account to apply the transfer', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='receivable_transfer', ctx=Load()),
                                        attr='credit',
                                        ctx=Load(),
                                    ),
                                    Constant(value=400, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
                                        ctx=Load(),
                                    ),
                                    Constant(value='400 should have been credited to receivable account to apply the transfer', kind=None),
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
                    name='test_transfer_wizard_grouping',
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
                            value=Constant(value=' Tests grouping (by account and partner) when doing a transfer with the wizard\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='active_move_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='move_1',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='move_2',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='line_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='test1_3', kind=None),
                                                        Constant(value='test1_4', kind=None),
                                                        Constant(value='test1_5', kind=None),
                                                        Constant(value='test2_3', kind=None),
                                                        Constant(value='test2_4', kind=None),
                                                        Constant(value='test2_5', kind=None),
                                                        Constant(value='test2_6', kind=None),
                                                        Constant(value='test2_8', kind=None),
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
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='active_model', kind=None),
                                    Constant(value='active_ids', kind=None),
                                ],
                                values=[
                                    Constant(value='account.move.line', kind=None),
                                    Attribute(
                                        value=Name(id='active_move_lines', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.automatic.entry.wizard', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='context', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='wizard_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard_form', ctx=Load()),
                                            attr='action',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='change_account', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard_form', ctx=Load()),
                                            attr='destination_account_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='accounts',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=4, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard_form', ctx=Load()),
                                            attr='journal_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='journal',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='wizard_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='transfer_move_id', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='wizard', ctx=Load()),
                                        attr='do_action',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value='res_id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='transfer_move', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='transfer_move_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='transfer_move', ctx=Load()),
                                attr='line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='key', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='account_id',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=None, kind=None),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
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
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='groups', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='key', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value='There should be only one line per (account, partner, currency) group in the transfer move.', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='groups', ctx=Load()),
                                            slice=Name(id='key', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='line', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='groups', ctx=Load()),
                                            slice=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='accounts',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_a',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='company_data',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='currency', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        attr='balance',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=800, kind=None),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
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
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='groups', ctx=Load()),
                                            slice=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='accounts',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=None, kind=None),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='company_data',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='currency', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        attr='balance',
                                        ctx=Load(),
                                    ),
                                    Constant(value=500, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
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
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='groups', ctx=Load()),
                                            slice=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='accounts',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_b',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='company_data',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='currency', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        attr='balance',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=480, kind=None),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
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
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='groups', ctx=Load()),
                                            slice=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='accounts',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=2, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_a',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='company_data',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='currency', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        attr='balance',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1030, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
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
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='groups', ctx=Load()),
                                            slice=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='accounts',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=2, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_a',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='test_currency_2',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        attr='balance',
                                        ctx=Load(),
                                    ),
                                    Constant(value=512, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
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
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='groups', ctx=Load()),
                                            slice=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='accounts',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=3, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_a',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='company_data',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='currency', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        attr='balance',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=250, kind=None),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
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
                    name='test_transfer_wizard_currency_conversion',
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
                            value=Constant(value=' Tests multi currency use of the transfer wizard, checking the conversion\n        is propperly done when using a destination account with a currency_id set.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='active_move_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_1',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='line_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='test1_6', kind=None),
                                                        Constant(value='test1_9', kind=None),
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
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='active_model', kind=None),
                                    Constant(value='active_ids', kind=None),
                                ],
                                values=[
                                    Constant(value='account.move.line', kind=None),
                                    Attribute(
                                        value=Name(id='active_move_lines', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.automatic.entry.wizard', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='context', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='wizard_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard_form', ctx=Load()),
                                            attr='action',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='change_account', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard_form', ctx=Load()),
                                            attr='destination_account_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_currency_account',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard_form', ctx=Load()),
                                            attr='journal_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='journal',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='wizard_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='transfer_move_id', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='wizard', ctx=Load()),
                                        attr='do_action',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value='res_id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='transfer_move', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='transfer_move_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='destination_line', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='transfer_move', ctx=Load()),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='account_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='test_currency_account',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='destination_line', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_currency_3',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Transferring to an account with a currency set should keep this currency on the transfer line.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='destination_line', ctx=Load()),
                                        attr='amount_currency',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3000, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
                                        ctx=Load(),
                                    ),
                                    Constant(value="Transferring two lines with different currencies (and the same partner) on an account with a currency set should convert the balance of these lines into this account's currency (here (270 + 30) * 10 = 3000)", kind=None),
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
                    name='test_transfer_wizard_no_currency_conversion',
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
                            value=Constant(value=' Tests multi currency use of the transfer wizard, verifying that\n        currency amounts are kept on distinct lines when transferring to an\n        account without any currency specified.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='active_move_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_2',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='line_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='test2_9', kind=None),
                                                        Constant(value='test2_6', kind=None),
                                                        Constant(value='test2_8', kind=None),
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
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='active_model', kind=None),
                                    Constant(value='active_ids', kind=None),
                                ],
                                values=[
                                    Constant(value='account.move.line', kind=None),
                                    Attribute(
                                        value=Name(id='active_move_lines', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.automatic.entry.wizard', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='context', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='wizard_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard_form', ctx=Load()),
                                            attr='action',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='change_account', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard_form', ctx=Load()),
                                            attr='destination_account_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='receivable_account',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard_form', ctx=Load()),
                                            attr='journal_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='journal',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='wizard_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='transfer_move_id', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='wizard', ctx=Load()),
                                        attr='do_action',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value='res_id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='transfer_move', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='transfer_move_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='destination_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='transfer_move', ctx=Load()),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='account_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='receivable_account',
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
                                        args=[Name(id='destination_lines', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                    Constant(value='Two lines should have been created on destination account: one for each currency (the lines with same partner and currency should have been aggregated)', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='destination_lines', ctx=Load()),
                                                attr='filtered',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='x', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Compare(
                                                        left=Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='currency_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='test_currency_1',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='amount_currency',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=10, kind=None),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_currency_1',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
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
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='destination_lines', ctx=Load()),
                                                attr='filtered',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='x', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Compare(
                                                        left=Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='currency_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='test_currency_2',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='amount_currency',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=756, kind=None),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_currency_2',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
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
