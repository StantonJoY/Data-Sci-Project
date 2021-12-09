Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='AccountMove',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='account.move', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='stock_move_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='stock.move', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Stock Move', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='stock_valuation_layer_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.valuation.layer', kind=None),
                            Constant(value='account_move_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Stock Valuation Layer', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_lines_onchange_currency',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
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
                                            args=[arg(arg='l', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='l', ctx=Load()),
                                                attr='is_anglo_saxon_line',
                                                ctx=Load(),
                                            ),
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
                    name='_reverse_move_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='default_values', annotation=None, type_comment=None),
                            arg(arg='cancel', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='move_vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='AccountMove', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_reverse_move_vals',
                                    ctx=Load(),
                                ),
                                args=[Name(id='default_values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='cancel',
                                        value=Name(id='cancel', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='cancel', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='move_vals', ctx=Load()),
                                            slice=Constant(value='line_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=ListComp(
                                        elt=Name(id='vals', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='vals', ctx=Store()),
                                                iter=Subscript(
                                                    value=Name(id='move_vals', ctx=Load()),
                                                    slice=Constant(value='line_ids', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ifs=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='vals', ctx=Load()),
                                                                slice=Constant(value=2, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='is_anglo_saxon_line', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='move_vals', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='copy_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='copy_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Name(id='default', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_context',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='move_reverse_cancel', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                For(
                                    target=Name(id='copy_vals', ctx=Store()),
                                    iter=Name(id='res', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Constant(value='line_ids', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='copy_vals', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='copy_vals', ctx=Load()),
                                                            slice=Constant(value='line_ids', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=ListComp(
                                                        elt=Name(id='line_vals', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='line_vals', ctx=Store()),
                                                                iter=Subscript(
                                                                    value=Name(id='copy_vals', ctx=Load()),
                                                                    slice=Constant(value='line_ids', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[
                                                                    BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Compare(
                                                                                left=Subscript(
                                                                                    value=Name(id='line_vals', ctx=Load()),
                                                                                    slice=Constant(value=0, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[NotEq()],
                                                                                comparators=[Constant(value=0, kind=None)],
                                                                            ),
                                                                            UnaryOp(
                                                                                op=Not(),
                                                                                operand=Call(
                                                                                    func=Attribute(
                                                                                        value=Subscript(
                                                                                            value=Name(id='line_vals', ctx=Load()),
                                                                                            slice=Constant(value=2, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='get',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='is_anglo_saxon_line', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                    name='_post',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='soft', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='move_reverse_cancel', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_post',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='soft', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
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
                                        slice=Constant(value='account.move.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_stock_account_prepare_anglo_saxon_out_lines_vals',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='posted', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_post',
                                    ctx=Load(),
                                ),
                                args=[Name(id='soft', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='posted', ctx=Load()),
                                    attr='_stock_account_anglo_saxon_reconcile_valuation',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='posted', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='button_draft',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='AccountMove', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='button_draft',
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
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
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
                                                    args=[arg(arg='line', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='is_anglo_saxon_line',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
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
                    name='button_cancel',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='AccountMove', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='button_cancel',
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
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
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
                                                    args=[arg(arg='line', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='is_anglo_saxon_line',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
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
                    name='_stock_account_prepare_anglo_saxon_out_lines_vals',
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
                            value=Constant(value=" Prepare values used to create the journal items (account.move.line) corresponding to the Cost of Good Sold\n        lines (COGS) for customer invoices.\n\n        Example:\n\n        Buy a product having a cost of 9 being a storable product and having a perpetual valuation in FIFO.\n        Sell this product at a price of 10. The customer invoice's journal entries looks like:\n\n        Account                                     | Debit | Credit\n        ---------------------------------------------------------------\n        200000 Product Sales                        |       | 10.0\n        ---------------------------------------------------------------\n        101200 Account Receivable                   | 10.0  |\n        ---------------------------------------------------------------\n\n        This method computes values used to make two additional journal items:\n\n        ---------------------------------------------------------------\n        220000 Expenses                             | 9.0   |\n        ---------------------------------------------------------------\n        101130 Stock Interim Account (Delivered)    |       | 9.0\n        ---------------------------------------------------------------\n\n        Note: COGS are only generated for customer invoices except refund made to cancel an invoice.\n\n        :return: A list of Python dictionary to be passed to env['account.move.line'].create.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='lines_vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='is_sale_document',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='include_receipts',
                                                            value=Constant(value=True, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='anglo_saxon_accounting',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='line', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='invoice_line_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='_eligible_for_cogs',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='accounts', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='product_tmpl_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='with_company',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='get_product_accounts',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='fiscal_pos',
                                                        value=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='fiscal_position_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='debit_interim_account', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='accounts', ctx=Load()),
                                                slice=Constant(value='stock_output', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='credit_expense_account', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='accounts', ctx=Load()),
                                                        slice=Constant(value='expense', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='journal_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='default_account_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='debit_interim_account', ctx=Load()),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='credit_expense_account', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='sign', ctx=Store())],
                                            value=IfExp(
                                                test=Compare(
                                                    left=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='move_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='out_refund', kind=None)],
                                                ),
                                                body=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                                orelse=Constant(value=1, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='price_unit', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='_stock_account_get_anglo_saxon_price_unit',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='balance', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Name(id='sign', ctx=Load()),
                                                    op=Mult(),
                                                    right=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='quantity',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Mult(),
                                                right=Name(id='price_unit', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='lines_vals_list', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='move_id', kind=None),
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='product_uom_id', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='debit', kind=None),
                                                            Constant(value='credit', kind=None),
                                                            Constant(value='account_id', kind=None),
                                                            Constant(value='exclude_from_invoice_tab', kind=None),
                                                            Constant(value='is_anglo_saxon_line', kind=None),
                                                        ],
                                                        values=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Slice(
                                                                    lower=None,
                                                                    upper=Constant(value=64, kind=None),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='product_uom_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='quantity',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='price_unit', ctx=Load()),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Compare(
                                                                                left=Name(id='balance', ctx=Load()),
                                                                                ops=[Lt()],
                                                                                comparators=[Constant(value=0.0, kind=None)],
                                                                            ),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Name(id='balance', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Constant(value=0.0, kind=None),
                                                                ],
                                                            ),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Compare(
                                                                                left=Name(id='balance', ctx=Load()),
                                                                                ops=[Gt()],
                                                                                comparators=[Constant(value=0.0, kind=None)],
                                                                            ),
                                                                            Name(id='balance', ctx=Load()),
                                                                        ],
                                                                    ),
                                                                    Constant(value=0.0, kind=None),
                                                                ],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='debit_interim_account', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='lines_vals_list', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='move_id', kind=None),
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='product_uom_id', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='debit', kind=None),
                                                            Constant(value='credit', kind=None),
                                                            Constant(value='account_id', kind=None),
                                                            Constant(value='analytic_account_id', kind=None),
                                                            Constant(value='analytic_tag_ids', kind=None),
                                                            Constant(value='exclude_from_invoice_tab', kind=None),
                                                            Constant(value='is_anglo_saxon_line', kind=None),
                                                        ],
                                                        values=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Slice(
                                                                    lower=None,
                                                                    upper=Constant(value=64, kind=None),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='product_uom_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='quantity',
                                                                ctx=Load(),
                                                            ),
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Name(id='price_unit', ctx=Load()),
                                                            ),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Compare(
                                                                                left=Name(id='balance', ctx=Load()),
                                                                                ops=[Gt()],
                                                                                comparators=[Constant(value=0.0, kind=None)],
                                                                            ),
                                                                            Name(id='balance', ctx=Load()),
                                                                        ],
                                                                    ),
                                                                    Constant(value=0.0, kind=None),
                                                                ],
                                                            ),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Compare(
                                                                                left=Name(id='balance', ctx=Load()),
                                                                                ops=[Lt()],
                                                                                comparators=[Constant(value=0.0, kind=None)],
                                                                            ),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Name(id='balance', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Constant(value=0.0, kind=None),
                                                                ],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='credit_expense_account', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='analytic_account_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value=6, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='analytic_tag_ids',
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
                                                            Constant(value=True, kind=None),
                                                            Constant(value=True, kind=None),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='lines_vals_list', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_stock_account_get_last_step_stock_moves',
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
                            value=Constant(value=' To be overridden for customer invoices and vendor bills in order to\n        return the stock moves related to the invoices in self.\n        ', kind=None),
                        ),
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.move', kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_stock_account_anglo_saxon_reconcile_valuation',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Reconciles the entries made in the interim accounts in anglosaxon accounting,\n        reconciling stock valuation move lines with the invoice's.\n        ", kind=None),
                        ),
                        For(
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='is_invoice',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='anglo_saxon_accounting',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='stock_moves', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='_stock_account_get_last_step_stock_moves',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='stock_moves', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='products', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='product', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='invoice_line_ids.product_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='prod', ctx=Store()),
                                    iter=Name(id='products', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='prod', ctx=Load()),
                                                    attr='valuation',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='real_time', kind=None)],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='product_accounts', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='prod', ctx=Load()),
                                                        attr='product_tmpl_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_product_accounts',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='is_sale_document',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='product_interim_account', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='product_accounts', ctx=Load()),
                                                        slice=Constant(value='stock_output', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='product_interim_account', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='product_accounts', ctx=Load()),
                                                        slice=Constant(value='stock_input', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='product_interim_account', ctx=Load()),
                                                attr='reconcile',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='product_account_moves', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='move', ctx=Load()),
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
                                                                    args=[arg(arg='line', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Compare(
                                                                            left=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Name(id='prod', ctx=Load())],
                                                                        ),
                                                                        Compare(
                                                                            left=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='account_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Name(id='product_interim_account', ctx=Load())],
                                                                        ),
                                                                        UnaryOp(
                                                                            op=Not(),
                                                                            operand=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='reconciled',
                                                                                ctx=Load(),
                                                                            ),
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
                                                    targets=[Name(id='product_stock_moves', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='stock_moves', ctx=Load()),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='stock_move', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='stock_move', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Name(id='prod', ctx=Load())],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='product_account_moves', ctx=Store()),
                                                    op=Add(),
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='product_stock_moves', ctx=Load()),
                                                                    attr='mapped',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='account_move_ids.line_ids', kind=None)],
                                                                keywords=[],
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
                                                                body=BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Compare(
                                                                            left=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='account_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Name(id='product_interim_account', ctx=Load())],
                                                                        ),
                                                                        UnaryOp(
                                                                            op=Not(),
                                                                            operand=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='reconciled',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='product_account_moves', ctx=Load()),
                                                            attr='reconcile',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_invoiced_lot_values',
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
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='AccountMoveLine',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='account.move.line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_anglo_saxon_line', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Technical field used to retrieve the anglo-saxon lines.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_computed_account',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='self', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='with_company',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_id',
                                                ctx=Load(),
                                            ),
                                            attr='journal_id',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='product', kind=None)],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_id',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='anglo_saxon_accounting',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_id',
                                                ctx=Load(),
                                            ),
                                            attr='is_purchase_document',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fiscal_position', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='move_id',
                                            ctx=Load(),
                                        ),
                                        attr='fiscal_position_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='accounts', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='product_tmpl_id',
                                                ctx=Load(),
                                            ),
                                            attr='get_product_accounts',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='fiscal_pos',
                                                value=Name(id='fiscal_position', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Subscript(
                                        value=Name(id='accounts', ctx=Load()),
                                        slice=Constant(value='stock_input', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Return(
                                            value=Subscript(
                                                value=Name(id='accounts', ctx=Load()),
                                                slice=Constant(value='stock_input', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='AccountMoveLine', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_computed_account',
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
                    name='_eligible_for_cogs',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='product', kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='valuation',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='real_time', kind=None)],
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
                    name='_stock_account_get_anglo_saxon_price_unit',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='product_id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='price_unit',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    attr='_stock_account_get_anglo_saxon_price_unit',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='uom',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
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
