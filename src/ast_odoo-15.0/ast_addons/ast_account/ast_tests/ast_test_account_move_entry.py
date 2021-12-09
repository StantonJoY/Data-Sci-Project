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
                alias(name='new_test_user', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='Form', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='api', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='ValidationError', asname=None),
                alias(name='UserError', asname=None),
                alias(name='RedirectWarning', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='functools',
            names=[alias(name='reduce', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='psycopg2', asname=None)],
        ),
        ClassDef(
            name='TestAccountMove',
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
                            targets=[Name(id='tax_repartition_line', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='default_tax_sale', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='refund_repartition_line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='line', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='repartition_type',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='tax', kind=None)],
                                        ),
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
                                    attr='test_move',
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
                                            Constant(value='move_type', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='entry', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2016-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=None, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='revenue line 1', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='company_data',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='default_account_revenue', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=500.0, kind=None),
                                                                    Constant(value=0.0, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=None, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='tax_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='revenue line 2', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='company_data',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='default_account_revenue', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=1000.0, kind=None),
                                                                    Constant(value=0.0, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=6, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Attribute(
                                                                                        value=Subscript(
                                                                                            value=Attribute(
                                                                                                value=Name(id='cls', ctx=Load()),
                                                                                                attr='company_data',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            slice=Constant(value='default_tax_sale', kind=None),
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
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=None, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                    Constant(value='tax_repartition_line_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='tax line', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='company_data',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='default_account_tax_sale', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=150.0, kind=None),
                                                                    Constant(value=0.0, kind=None),
                                                                    Attribute(
                                                                        value=Name(id='tax_repartition_line', ctx=Load()),
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
                                                            Constant(value=None, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='counterpart line', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='company_data',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='default_account_expense', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=0.0, kind=None),
                                                                    Constant(value=1650.0, kind=None),
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
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_custom_currency_on_account_1',
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
                            targets=[Name(id='custom_account', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='default_account_revenue', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='copy',
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
                                    value=Name(id='custom_account', ctx=Load()),
                                    attr='currency_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='currency_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='currency', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='test_move',
                                                        ctx=Load(),
                                                    ),
                                                    attr='line_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='account_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='custom_account', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='custom_account', ctx=Load()),
                                    attr='currency_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='currency', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='line_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='account_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='custom_account', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_misc_fiscalyear_lock_date_1',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_move',
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
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_move',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='fiscalyear_lock_date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='from_string',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='2017-01-01', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_move',
                                            ctx=Load(),
                                        ),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='sorted',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='debit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_move',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='whatever', kind=None),
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='line_ids', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='lines', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='credit', kind=None)],
                                                                        values=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='lines', ctx=Load()),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='credit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=100.0, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='lines', ctx=Load()),
                                                                            slice=Constant(value=2, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='debit', kind=None)],
                                                                        values=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='lines', ctx=Load()),
                                                                                        slice=Constant(value=2, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='debit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=100.0, kind=None),
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
                                ),
                            ],
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='test_move',
                                                        ctx=Load(),
                                                    ),
                                                    attr='line_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='account_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='test_move',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='line_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='account_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='copy',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
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
                            ],
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='line_ids', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='lines', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='credit', kind=None)],
                                                                        values=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='lines', ctx=Load()),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='credit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=100.0, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='lines', ctx=Load()),
                                                                            slice=Constant(value=3, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='debit', kind=None)],
                                                                        values=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='lines', ctx=Load()),
                                                                                        slice=Constant(value=3, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='debit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=100.0, kind=None),
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
                                ),
                            ],
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='line_ids', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='lines', ctx=Load()),
                                                                            slice=Constant(value=2, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='tax_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value=6, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Attribute(
                                                                                                value=Subscript(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='company_data',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    slice=Constant(value='default_tax_purchase', kind=None),
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
                            ],
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='line_ids', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='lines', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='credit', kind=None)],
                                                                        values=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='lines', ctx=Load()),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='credit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=100.0, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=None, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='revenue line 1', kind=None),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='company_data',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value='default_account_revenue', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=100.0, kind=None),
                                                                            Constant(value=0.0, kind=None),
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
                                ),
                            ],
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2018-01-01', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='button_draft',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='copy_move', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_move',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='date', kind=None)],
                                        values=[Constant(value='2017-01-01', kind=None)],
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
                                        value=Name(id='copy_move', ctx=Load()),
                                        attr='date',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='copy_move', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='fiscalyear_lock_date',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='relativedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
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
                    name='test_misc_fiscalyear_lock_date_2',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_move',
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
                            targets=[Name(id='statement', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.bank.statement', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='line_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='default_journal_bank', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='2016-01-01', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='payment_ref', kind=None),
                                                                    Constant(value='amount', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='test', kind=None),
                                                                    Constant(value=10.0, kind=None),
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
                                    value=Name(id='statement', ctx=Load()),
                                    attr='button_post',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        args=[Name(id='RedirectWarning', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='test_move',
                                                    ctx=Load(),
                                                ),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='fiscalyear_lock_date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2017-01-01', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_misc_tax_lock_date_1',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_move',
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
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_move',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='tax_lock_date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='from_string',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='2017-01-01', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_move',
                                            ctx=Load(),
                                        ),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='sorted',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='debit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_move',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='line_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='lines', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='credit', kind=None)],
                                                                values=[
                                                                    BinOp(
                                                                        left=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='lines', ctx=Load()),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='credit',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Constant(value=100.0, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='lines', ctx=Load()),
                                                                    slice=Constant(value=2, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='debit', kind=None)],
                                                                values=[
                                                                    BinOp(
                                                                        left=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='lines', ctx=Load()),
                                                                                slice=Constant(value=2, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='debit',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Constant(value=100.0, kind=None),
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='line_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='account_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='test_move',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='line_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='account_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='copy',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='line_ids', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='lines', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='credit', kind=None)],
                                                                        values=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='lines', ctx=Load()),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='credit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=100.0, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='lines', ctx=Load()),
                                                                            slice=Constant(value=3, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='debit', kind=None)],
                                                                        values=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='lines', ctx=Load()),
                                                                                        slice=Constant(value=3, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='debit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=100.0, kind=None),
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
                                ),
                            ],
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='line_ids', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='lines', ctx=Load()),
                                                                            slice=Constant(value=2, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='tax_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value=6, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Attribute(
                                                                                                value=Subscript(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='company_data',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    slice=Constant(value='default_tax_purchase', kind=None),
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
                            ],
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='line_ids', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='lines', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='credit', kind=None)],
                                                                        values=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='lines', ctx=Load()),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='credit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=100.0, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='lines', ctx=Load()),
                                                                            slice=Constant(value=1, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='debit', kind=None)],
                                                                        values=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='lines', ctx=Load()),
                                                                                        slice=Constant(value=1, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='debit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=100.0, kind=None),
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
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_move',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='line_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='lines', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='credit', kind=None)],
                                                                values=[
                                                                    BinOp(
                                                                        left=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='lines', ctx=Load()),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='credit',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Constant(value=100.0, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=None, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='account_id', kind=None),
                                                                    Constant(value='debit', kind=None),
                                                                    Constant(value='credit', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='revenue line 1', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='company_data',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='default_account_revenue', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=100.0, kind=None),
                                                                    Constant(value=0.0, kind=None),
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='line_ids', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='lines', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='credit', kind=None)],
                                                                        values=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='lines', ctx=Load()),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='credit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=100.0, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=None, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='tax_ids', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='revenue line 2', kind=None),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='company_data',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value='default_account_revenue', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1000.0, kind=None),
                                                                            Constant(value=0.0, kind=None),
                                                                            List(
                                                                                elts=[
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value=6, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Attribute(
                                                                                                value=Subscript(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='company_data',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    slice=Constant(value='default_tax_sale', kind=None),
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
                            ],
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2018-01-01', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                                attr='test_move',
                                                ctx=Load(),
                                            ),
                                            attr='button_draft',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='copy_move', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_move',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='date', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='test_move',
                                                    ctx=Load(),
                                                ),
                                                attr='date',
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
                                    value=Name(id='copy_move', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='copy_move', ctx=Load()),
                                            attr='date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2017-01-01', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_misc_draft_reconciled_entries_1',
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
                            targets=[Name(id='draft_moves', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='line_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='entry', kind=None),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=None, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='move 1 receivable line', kind=None),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='company_data',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value='default_account_receivable', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1000.0, kind=None),
                                                                            Constant(value=0.0, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=None, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='move 1 counterpart line', kind=None),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='company_data',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value='default_account_expense', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=0.0, kind=None),
                                                                            Constant(value=1000.0, kind=None),
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
                                            Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='line_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='entry', kind=None),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=None, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='move 2 receivable line', kind=None),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='company_data',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value='default_account_receivable', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=0.0, kind=None),
                                                                            Constant(value=2000.0, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=None, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='move 2 counterpart line', kind=None),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='company_data',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value='default_account_expense', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=2000.0, kind=None),
                                                                            Constant(value=0.0, kind=None),
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
                                    value=Name(id='draft_moves', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='draft_moves', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='line_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='sorted',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='balance', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=BinOp(
                                        left=Subscript(
                                            value=Name(id='lines', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Name(id='lines', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    attr='reconcile',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                            value=Subscript(
                                                value=Name(id='draft_moves', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='line_ids', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='lines', ctx=Load()),
                                                                            slice=Constant(value=1, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='credit', kind=None)],
                                                                        values=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='lines', ctx=Load()),
                                                                                        slice=Constant(value=1, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='credit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=100.0, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='lines', ctx=Load()),
                                                                            slice=Constant(value=2, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='debit', kind=None)],
                                                                        values=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='lines', ctx=Load()),
                                                                                        slice=Constant(value=2, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='debit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=100.0, kind=None),
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
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='draft_moves', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='line_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='lines', ctx=Load()),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='credit', kind=None)],
                                                                values=[
                                                                    BinOp(
                                                                        left=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='lines', ctx=Load()),
                                                                                slice=Constant(value=1, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='credit',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Constant(value=1e-07, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='lines', ctx=Load()),
                                                                    slice=Constant(value=2, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='debit', kind=None)],
                                                                values=[
                                                                    BinOp(
                                                                        left=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='lines', ctx=Load()),
                                                                                slice=Constant(value=2, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='debit',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Constant(value=1e-07, kind=None),
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                            value=Name(id='draft_moves', ctx=Load()),
                                            attr='unlink',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_misc_always_balanced_move',
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
                            value=Constant(value=' Ensure there is no way to make ', kind=None),
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='test_move',
                                                        ctx=Load(),
                                                    ),
                                                    attr='line_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='balance', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='test_move',
                                                        ctx=Load(),
                                                    ),
                                                    attr='line_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='balance',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Constant(value=5, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='test_move',
                                                        ctx=Load(),
                                                    ),
                                                    attr='line_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    IfExp(
                                                        test=Compare(
                                                            left=Name(id='balance', ctx=Load()),
                                                            ops=[Gt()],
                                                            comparators=[Constant(value=0.0, kind=None)],
                                                        ),
                                                        body=Name(id='balance', ctx=Load()),
                                                        orelse=Constant(value=0.0, kind=None),
                                                    ),
                                                    IfExp(
                                                        test=Compare(
                                                            left=Name(id='balance', ctx=Load()),
                                                            ops=[Lt()],
                                                            comparators=[Constant(value=0.0, kind=None)],
                                                        ),
                                                        body=UnaryOp(
                                                            op=USub(),
                                                            operand=Name(id='balance', ctx=Load()),
                                                        ),
                                                        orelse=Constant(value=0.0, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_move',
                                            ctx=Load(),
                                        ),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_add_followers_on_post',
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
                                        slice=Constant(value='res.company', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Oopo', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='company', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='existing_partners', ctx=Store())],
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
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='company_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Jean', kind=None),
                                                    Attribute(
                                                        value=Name(id='company', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Paulus', kind=None)],
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_move',
                                        ctx=Load(),
                                    ),
                                    attr='message_subscribe',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='existing_partners', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Name(id='new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='jag', kind=None),
                                    ),
                                    keyword(
                                        arg='groups',
                                        value=Constant(value='account.group_account_invoice', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_move',
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
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
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Belouga', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move', ctx=Load()),
                                    attr='partner_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='partner', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move', ctx=Load()),
                                    attr='action_post',
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
                                        value=Name(id='move', ctx=Load()),
                                        attr='message_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
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
                                            right=Name(id='existing_partners', ctx=Load()),
                                        ),
                                        op=BitOr(),
                                        right=Name(id='partner', ctx=Load()),
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
                    name='test_misc_move_onchange',
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
                            value=Constant(value=" Test the behavior on onchanges for account.move having 'entry' as type. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='from_string',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='2016-01-01', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='name',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='debit_line', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='account_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='default_account_revenue', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='currency_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='currency_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='currency', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='amount_currency',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=1200.0, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='name',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='credit_line', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='account_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='default_account_revenue', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='currency_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='currency_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='currency', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line_form', ctx=Load()),
                                            attr='amount_currency',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1200.0, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='debit', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1200.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=400.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1200.0, kind=None),
                                                    Constant(value=400.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                        ],
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
                                        func=Name(id='Form', ctx=Load()),
                                        args=[Name(id='move', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='move_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='move_form', ctx=Load()),
                                            attr='date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2017-01-01', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='debit', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1200.0, kind=None),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=600.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='amount_currency', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='currency_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1200.0, kind=None),
                                                    Constant(value=600.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                        ],
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
                    name='test_included_tax',
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
                            value=Constant(value="\n        Test an account.move.line is created automatically when adding a tax.\n        This test uses the following scenario:\n            - Create manually a debit line of 1000 having an included tax.\n            - Assume a line containing the tax amount is created automatically.\n            - Create manually a credit line to balance the two previous lines.\n            - Save the move.\n\n        included tax = 20%\n\n        Name                   | Debit     | Credit    | Tax_ids       | Tax_line_id's name\n        -----------------------|-----------|-----------|---------------|-------------------\n        debit_line_1           | 1000      |           | tax           |\n        included_tax_line      | 200       |           |               | included_tax_line\n        credit_line_1          |           | 1200      |               |\n        ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='included_percent_tax',
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
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='price_include', kind=None),
                                            Constant(value='include_base_amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='included_tax_line', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=20, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='account',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='default_account_revenue', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
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
                                                slice=Constant(value='account.move', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='default_move_type',
                                                value=Constant(value='entry', kind=None),
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
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='debit_line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='debit_line', ctx=Load()),
                                            attr='name',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='debit_line_1', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='debit_line', ctx=Load()),
                                            attr='account_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='account',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='debit_line', ctx=Load()),
                                            attr='debit',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=1000, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='debit_line', ctx=Load()),
                                                attr='tax_ids',
                                                ctx=Load(),
                                            ),
                                            attr='clear',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='debit_line', ctx=Load()),
                                                attr='tax_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='included_percent_tax',
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='debit_line', ctx=Load()),
                                                attr='recompute_tax_line',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_form', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='credit_line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='credit_line', ctx=Load()),
                                            attr='name',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='credit_line_1', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='credit_line', ctx=Load()),
                                            attr='account_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='account',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='credit_line', ctx=Load()),
                                            attr='credit',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=1200, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='save',
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='debit_line_1', kind=None),
                                                    Constant(value=1000.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='included_percent_tax',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='included_tax_line', kind=None),
                                                    Constant(value=200.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='included_percent_tax',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                    Constant(value='tax_ids', kind=None),
                                                    Constant(value='tax_line_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='credit_line_1', kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=1200.0, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                        ],
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
                    name='test_misc_prevent_unlink_posted_items',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_move',
                                        ctx=Load(),
                                    ),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='test_move',
                                                    ctx=Load(),
                                                ),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='unlink',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_move',
                                        ctx=Load(),
                                    ),
                                    attr='button_draft',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_move',
                                            ctx=Load(),
                                        ),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_account_move_inactive_currency_raise_error_on_post',
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
                            value=Constant(value=' Ensure a move cannot be posted when using an inactive currency ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='move', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='move_type', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_date', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='in_invoice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='from_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2019-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_terms_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Dict(keys=[], values=[])],
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
                                    value=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    attr='active',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
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
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
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
                                            value=Name(id='move', ctx=Load()),
                                            attr='action_post',
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
                                    value=Name(id='move', ctx=Load()),
                                    attr='action_activate_currency',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move', ctx=Load()),
                                    attr='action_post',
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
                                        value=Name(id='move', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='posted', kind=None),
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
