Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.float_utils',
            names=[
                alias(name='float_compare', asname=None),
                alias(name='float_is_zero', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
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
                FunctionDef(
                    name='_stock_account_prepare_anglo_saxon_in_lines_vals',
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
                            value=Constant(value=" Prepare values used to create the journal items (account.move.line) corresponding to the price difference\n         lines for vendor bills.\n\n        Example:\n\n        Buy a product having a cost of 9 and a supplier price of 10 and being a storable product and having a perpetual\n        valuation in FIFO. The vendor bill's journal entries looks like:\n\n        Account                                     | Debit | Credit\n        ---------------------------------------------------------------\n        101120 Stock Interim Account (Received)     | 10.0  |\n        ---------------------------------------------------------------\n        101100 Account Payable                      |       | 10.0\n        ---------------------------------------------------------------\n\n        This method computes values used to make two additional journal items:\n\n        ---------------------------------------------------------------\n        101120 Stock Interim Account (Received)     |       | 1.0\n        ---------------------------------------------------------------\n        xxxxxx Price Difference Account             | 1.0   |\n        ---------------------------------------------------------------\n\n        :return: A list of Python dictionary to be passed to env['account.move.line'].create.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='lines_vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='price_unit_prec', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='decimal.precision', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='precision_get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Product Price', kind=None)],
                                keywords=[],
                            ),
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
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='move_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='in_invoice', kind=None),
                                                            Constant(value='in_refund', kind=None),
                                                            Constant(value='in_receipt', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                                Assign(
                                    targets=[Name(id='move', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='line', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='invoice_line_ids',
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
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
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
                                                                    value=Name(id='line', ctx=Load()),
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
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='product', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='valuation',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='real_time', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='debit_pdiff_account', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='property_account_creditor_price_difference',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='categ_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='property_account_creditor_price_difference_categ',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='debit_pdiff_account', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='fiscal_position_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='map_account',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='debit_pdiff_account', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='debit_pdiff_account', ctx=Load()),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='cost_method',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='standard', kind=None)],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='purchase_line_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='po_currency', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='purchase_line_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='currency_id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='po_company', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='purchase_line_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='valuation_stock_moves', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='stock.move', kind=None),
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
                                                                            Constant(value='purchase_line_id', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='purchase_line_id',
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
                                                                            Constant(value='state', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Constant(value='done', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='product_qty', kind=None),
                                                                            Constant(value='!=', kind=None),
                                                                            Constant(value=0.0, kind=None),
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
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='move_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='in_refund', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='valuation_stock_moves', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='valuation_stock_moves', ctx=Load()),
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
                                                                        body=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='stock_move', ctx=Load()),
                                                                                attr='_is_out',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='valuation_stock_moves', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='valuation_stock_moves', ctx=Load()),
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
                                                                        body=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='stock_move', ctx=Load()),
                                                                                attr='_is_in',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                                If(
                                                    test=Name(id='valuation_stock_moves', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='valuation_price_unit_total', ctx=Store())],
                                                            value=Constant(value=0, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='valuation_total_qty', ctx=Store())],
                                                            value=Constant(value=0, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        For(
                                                            target=Name(id='val_stock_move', ctx=Store()),
                                                            iter=Name(id='valuation_stock_moves', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='valuation_date', ctx=Store())],
                                                                    value=BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='val_stock_move', ctx=Load()),
                                                                                    attr='origin_returned_move_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='date',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='val_stock_move', ctx=Load()),
                                                                                attr='date',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='svl', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='val_stock_move', ctx=Load()),
                                                                                            attr='with_context',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[
                                                                                            keyword(
                                                                                                arg='active_test',
                                                                                                value=Constant(value=False, kind=None),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    attr='mapped',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='stock_valuation_layer_ids', kind=None)],
                                                                                keywords=[],
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
                                                                                body=Attribute(
                                                                                    value=Name(id='l', ctx=Load()),
                                                                                    attr='quantity',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='layers_qty', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='sum', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='svl', ctx=Load()),
                                                                                    attr='mapped',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='quantity', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='layers_values', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='sum', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='svl', ctx=Load()),
                                                                                    attr='mapped',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='value', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                AugAssign(
                                                                    target=Name(id='valuation_price_unit_total', ctx=Store()),
                                                                    op=Add(),
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='company_currency_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='_convert',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='layers_values', ctx=Load()),
                                                                            Attribute(
                                                                                value=Name(id='move', ctx=Load()),
                                                                                attr='currency_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='move', ctx=Load()),
                                                                                attr='company_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='valuation_date', ctx=Load()),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='round',
                                                                                value=Constant(value=False, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                                AugAssign(
                                                                    target=Name(id='valuation_total_qty', ctx=Store()),
                                                                    op=Add(),
                                                                    value=Name(id='layers_qty', ctx=Load()),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Call(
                                                                func=Name(id='float_is_zero', ctx=Load()),
                                                                args=[Name(id='valuation_total_qty', ctx=Load())],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='precision_rounding',
                                                                        value=BoolOp(
                                                                            op=Or(),
                                                                            values=[
                                                                                Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='line', ctx=Load()),
                                                                                        attr='product_uom_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='rounding',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Attribute(
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='line', ctx=Load()),
                                                                                            attr='product_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='uom_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='rounding',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Raise(
                                                                    exc=Call(
                                                                        func=Name(id='UserError', ctx=Load()),
                                                                        args=[
                                                                            BinOp(
                                                                                left=Call(
                                                                                    func=Name(id='_', ctx=Load()),
                                                                                    args=[Constant(value='Odoo is not able to generate the anglo saxon entries. The total valuation of %s is zero.', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                op=Mod(),
                                                                                right=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='line', ctx=Load()),
                                                                                        attr='product_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='display_name',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    cause=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='valuation_price_unit', ctx=Store())],
                                                            value=BinOp(
                                                                left=Name(id='valuation_price_unit_total', ctx=Load()),
                                                                op=Div(),
                                                                right=Name(id='valuation_total_qty', ctx=Load()),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='valuation_price_unit', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='uom_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='_compute_price',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='valuation_price_unit', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='product_uom_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='cost_method',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='fifo', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='valuation_price_unit', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='po_currency', ctx=Load()),
                                                                            attr='_convert',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='purchase_line_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='price_unit',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='move', ctx=Load()),
                                                                                attr='currency_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='po_company', ctx=Load()),
                                                                            Attribute(
                                                                                value=Name(id='move', ctx=Load()),
                                                                                attr='date',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='round',
                                                                                value=Constant(value=False, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='price_unit', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='purchase_line_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='product_uom',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='_compute_price',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='purchase_line_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='price_unit',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='product_uom_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='valuation_price_unit', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='po_currency', ctx=Load()),
                                                                            attr='_convert',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='price_unit', ctx=Load()),
                                                                            Attribute(
                                                                                value=Name(id='move', ctx=Load()),
                                                                                attr='currency_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='po_company', ctx=Load()),
                                                                            Attribute(
                                                                                value=Name(id='move', ctx=Load()),
                                                                                attr='date',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='round',
                                                                                value=Constant(value=False, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='price_unit', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='uom_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_compute_price',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='standard_price',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_uom_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='valuation_price_unit', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='company_currency_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_convert',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='price_unit', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='currency_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        attr='Date',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='today',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='round',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='price_unit', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=BinOp(
                                                    left=Constant(value=1, kind=None),
                                                    op=Sub(),
                                                    right=BinOp(
                                                        left=BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='discount',
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value=0.0, kind=None),
                                                            ],
                                                        ),
                                                        op=Div(),
                                                        right=Constant(value=100.0, kind=None),
                                                    ),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='tax_ids',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='quantity',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='price_unit', ctx=Store()),
                                                    op=Mult(),
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='quantity',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='price_unit', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='tax_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='with_context',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='round',
                                                                            value=Constant(value=False, kind=None),
                                                                        ),
                                                                        keyword(
                                                                            arg='force_sign',
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='move', ctx=Load()),
                                                                                    attr='_get_tax_force_sign',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                attr='compute_all',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='price_unit', ctx=Load())],
                                                            keywords=[
                                                                keyword(
                                                                    arg='currency',
                                                                    value=Attribute(
                                                                        value=Name(id='move', ctx=Load()),
                                                                        attr='currency_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                keyword(
                                                                    arg='quantity',
                                                                    value=Constant(value=1.0, kind=None),
                                                                ),
                                                                keyword(
                                                                    arg='is_refund',
                                                                    value=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='move_type',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='in_refund', kind=None)],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        slice=Constant(value='total_excluded', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='price_unit', ctx=Store()),
                                                    op=Div(),
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='quantity',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='price_unit_val_dif', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='price_unit', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='valuation_price_unit', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='price_subtotal', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='quantity',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Name(id='price_unit_val_dif', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='currency_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='is_zero',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='price_subtotal', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='float_compare', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    slice=Constant(value='price_unit', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='price_unit',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[
                                                                keyword(
                                                                    arg='precision_digits',
                                                                    value=Name(id='price_unit_prec', ctx=Load()),
                                                                ),
                                                            ],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='vals', ctx=Store())],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='move_id', kind=None),
                                                            Constant(value='currency_id', kind=None),
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='product_uom_id', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='price_subtotal', kind=None),
                                                            Constant(value='account_id', kind=None),
                                                            Constant(value='analytic_account_id', kind=None),
                                                            Constant(value='analytic_tag_ids', kind=None),
                                                            Constant(value='exclude_from_invoice_tab', kind=None),
                                                            Constant(value='is_anglo_saxon_line', kind=None),
                                                            Constant(value='partner_id', kind=None),
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
                                                                    attr='currency_id',
                                                                    ctx=Load(),
                                                                ),
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
                                                            Name(id='price_unit_val_dif', ctx=Load()),
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='quantity',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Mult(),
                                                                right=Name(id='price_unit_val_dif', ctx=Load()),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='debit_pdiff_account', ctx=Load()),
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='vals', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='_get_fields_onchange_subtotal',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='price_subtotal',
                                                                        value=Subscript(
                                                                            value=Name(id='vals', ctx=Load()),
                                                                            slice=Constant(value='price_subtotal', kind=None),
                                                                            ctx=Load(),
                                                                        ),
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
                                                            value=Name(id='lines_vals_list', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='vals', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='vals', ctx=Store())],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='move_id', kind=None),
                                                            Constant(value='currency_id', kind=None),
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='product_uom_id', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='price_subtotal', kind=None),
                                                            Constant(value='account_id', kind=None),
                                                            Constant(value='analytic_account_id', kind=None),
                                                            Constant(value='analytic_tag_ids', kind=None),
                                                            Constant(value='exclude_from_invoice_tab', kind=None),
                                                            Constant(value='is_anglo_saxon_line', kind=None),
                                                            Constant(value='partner_id', kind=None),
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
                                                                    attr='currency_id',
                                                                    ctx=Load(),
                                                                ),
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
                                                                operand=Name(id='price_unit_val_dif', ctx=Load()),
                                                            ),
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='quantity',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Mult(),
                                                                right=UnaryOp(
                                                                    op=USub(),
                                                                    operand=Name(id='price_unit_val_dif', ctx=Load()),
                                                                ),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='account_id',
                                                                    ctx=Load(),
                                                                ),
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='vals', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='_get_fields_onchange_subtotal',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='price_subtotal',
                                                                        value=Subscript(
                                                                            value=Name(id='vals', ctx=Load()),
                                                                            slice=Constant(value='price_subtotal', kind=None),
                                                                            ctx=Load(),
                                                                        ),
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
                                                            value=Name(id='lines_vals_list', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='vals', ctx=Load())],
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
                        Return(
                            value=Name(id='lines_vals_list', ctx=Load()),
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
                                            attr='_stock_account_prepare_anglo_saxon_in_lines_vals',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
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
                            value=Constant(value=' Overridden from stock_account.\n        Returns the stock moves associated to this invoice.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='rslt', ctx=Store())],
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
                                    attr='_stock_account_get_last_step_stock_moves',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='invoice', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
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
                                                attr='move_type',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='in_invoice', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='rslt', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='invoice_line_ids.purchase_line_id.move_ids', kind=None)],
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
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='done', kind=None)],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='location_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='usage',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='supplier', kind=None)],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='invoice', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
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
                                                attr='move_type',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='in_refund', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='rslt', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='invoice_line_ids.purchase_line_id.move_ids', kind=None)],
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
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='done', kind=None)],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='location_dest_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='usage',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='supplier', kind=None)],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='rslt', ctx=Load()),
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
