Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='float_is_zero', asname=None)],
            level=0,
        ),
        ClassDef(
            name='StockValuationLayerRevaluation',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='stock.valuation.layer.revaluation', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Wizard model to reavaluate a stock inventory for a product', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_check_company_auto', ctx=Store())],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='default_fields', annotation=None, type_comment=None),
                        ],
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='default_fields', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_id', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='product.product', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Constant(value='product_id', kind=None),
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
                                            value=Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='categ_id',
                                                ctx=Load(),
                                            ),
                                            attr='property_cost_method',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='standard', kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='You cannot revalue a product with a standard cost method.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='quantity_svl',
                                            ctx=Load(),
                                        ),
                                        ops=[LtE()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='You cannot revalue a product with an empty or negative stock.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='account_journal_id', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='res', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='account_journal_id', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='default_fields', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='categ_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='property_valuation',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='real_time', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='accounts', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='product_tmpl_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get_product_accounts',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='account_journal_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Name(id='accounts', ctx=Load()),
                                                    slice=Constant(value='stock_journal', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.company', kind=None),
                            Constant(value='Company', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='currency_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.currency', kind=None),
                            Constant(value='Currency', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.currency_id', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='product.product', kind=None),
                            Constant(value='Related product', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_valuation', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.categ_id.property_valuation', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_uom_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Unit of Measure', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.uom_id.name', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='current_value_svl', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Current Value', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.value_svl', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='current_quantity_svl', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Current Quantity', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.quantity_svl', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='added_value', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Added value', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='new_value', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='New value', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_new_value', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='new_value_by_qty', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='New value by quantity', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_new_value', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reason', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Reason', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Reason of the revaluation', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='account_journal_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.journal', kind=None),
                            Constant(value='Journal', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='account_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.account', kind=None),
                            Constant(value='Counterpart Account', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='deprecated', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Accounting Date', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_new_value',
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
                        For(
                            target=Name(id='reval', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='reval', ctx=Load()),
                                            attr='new_value',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='reval', ctx=Load()),
                                            attr='current_value_svl',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='reval', ctx=Load()),
                                            attr='added_value',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='float_is_zero', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='reval', ctx=Load()),
                                                    attr='current_quantity_svl',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='precision_rounding',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='rounding',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='reval', ctx=Load()),
                                                    attr='new_value_by_qty',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='reval', ctx=Load()),
                                                    attr='new_value',
                                                    ctx=Load(),
                                                ),
                                                op=Div(),
                                                right=Attribute(
                                                    value=Name(id='reval', ctx=Load()),
                                                    attr='current_quantity_svl',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='reval', ctx=Load()),
                                                    attr='new_value_by_qty',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=0.0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='current_value_svl', kind=None),
                                Constant(value='current_quantity_svl', kind=None),
                                Constant(value='added_value', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_validate_revaluation',
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
                            value=Constant(value=' Revaluate the stock for `self.product_id` in `self.company_id`.\n\n        - Change the stardard price with the new valuation by product unit.\n        - Create a manual stock valuation layer with the `added_value` of `self`.\n        - Distribute the `added_value` on the remaining_value of layers still in stock (with a remaining quantity)\n        - If the Inventory Valuation of the product category is automated, create\n        related account move.\n        ', kind=None),
                        ),
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
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    attr='is_zero',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='added_value',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="The added value doesn't have any impact on the stock valuation", kind=None)],
                                                keywords=[],
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
                            targets=[Name(id='product_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    attr='with_company',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='remaining_svls', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.valuation.layer', kind=None),
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
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='product_id', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='remaining_qty', kind=None),
                                                    Constant(value='>', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='company_id',
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
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='reason',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='description', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='Manual Stock Valuation: %s.', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='reason',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='description', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Manual Stock Valuation: No Reason Given.', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='product_id', ctx=Load()),
                                        attr='categ_id',
                                        ctx=Load(),
                                    ),
                                    attr='property_cost_method',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='average', kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='description', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value=' Product cost updated from %(previous)s to %(new_cost)s.', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='previous',
                                                value=Attribute(
                                                    value=Name(id='product_id', ctx=Load()),
                                                    attr='standard_price',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='new_cost',
                                                value=BinOp(
                                                    left=Attribute(
                                                        value=Name(id='product_id', ctx=Load()),
                                                        attr='standard_price',
                                                        ctx=Load(),
                                                    ),
                                                    op=Add(),
                                                    right=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='added_value',
                                                            ctx=Load(),
                                                        ),
                                                        op=Div(),
                                                        right=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='current_quantity_svl',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='revaluation_svl_vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='company_id', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='value', kind=None),
                                    Constant(value='quantity', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='product_id', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='description', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='added_value',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='remaining_qty', ctx=Store())],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='remaining_svls', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='remaining_qty', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='remaining_value', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='added_value',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='remaining_value_unit_cost', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    attr='round',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='remaining_value', ctx=Load()),
                                        op=Div(),
                                        right=Name(id='remaining_qty', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='svl', ctx=Store()),
                            iter=Name(id='remaining_svls', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='svl', ctx=Load()),
                                                    attr='remaining_qty',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Name(id='remaining_qty', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='rounding',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='svl', ctx=Load()),
                                                attr='remaining_value',
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Name(id='remaining_value', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='taken_remaining_value', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='remaining_value_unit_cost', ctx=Load()),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Name(id='svl', ctx=Load()),
                                                    attr='remaining_qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='svl', ctx=Load()),
                                                attr='remaining_value',
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Name(id='taken_remaining_value', ctx=Load()),
                                        ),
                                        AugAssign(
                                            target=Name(id='remaining_value', ctx=Store()),
                                            op=Sub(),
                                            value=Name(id='taken_remaining_value', ctx=Load()),
                                        ),
                                        AugAssign(
                                            target=Name(id='remaining_qty', ctx=Store()),
                                            op=Sub(),
                                            value=Attribute(
                                                value=Name(id='svl', ctx=Load()),
                                                attr='remaining_qty',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='revaluation_svl', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.valuation.layer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='revaluation_svl_vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='product_id', ctx=Load()),
                                        attr='categ_id',
                                        ctx=Load(),
                                    ),
                                    attr='property_cost_method',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='average', kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='product_id', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='disable_auto_svl',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='standard_price',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='added_value',
                                            ctx=Load(),
                                        ),
                                        op=Div(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='current_quantity_svl',
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='property_valuation',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='real_time', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='accounts', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='product_id', ctx=Load()),
                                        attr='product_tmpl_id',
                                        ctx=Load(),
                                    ),
                                    attr='get_product_accounts',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='added_value',
                                    ctx=Load(),
                                ),
                                ops=[Lt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='debit_account_id', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='credit_account_id', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='accounts', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='stock_valuation', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='accounts', ctx=Load()),
                                                    slice=Constant(value='stock_valuation', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='debit_account_id', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='accounts', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='stock_valuation', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='accounts', ctx=Load()),
                                                    slice=Constant(value='stock_valuation', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='credit_account_id', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='move_vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='journal_id', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='ref', kind=None),
                                    Constant(value='stock_valuation_layer_ids', kind=None),
                                    Constant(value='date', kind=None),
                                    Constant(value='move_type', kind=None),
                                    Constant(value='line_ids', kind=None),
                                ],
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='account_journal_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='accounts', ctx=Load()),
                                                    slice=Constant(value='stock_journal', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='Revaluation of %s', kind=None),
                                            Attribute(
                                                value=Name(id='product_id', ctx=Load()),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=6, kind=None),
                                                    Constant(value=None, kind=None),
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='revaluation_svl', ctx=Load()),
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
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='date',
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
                                    ),
                                    Constant(value='entry', kind=None),
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
                                                            Constant(value='credit', kind=None),
                                                            Constant(value='product_id', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='%(user)s changed stock valuation from  %(previous)s to %(new_value)s - %(product)s', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='user',
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='user',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='previous',
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='current_value_svl',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='new_value',
                                                                        value=BinOp(
                                                                            left=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='current_value_svl',
                                                                                ctx=Load(),
                                                                            ),
                                                                            op=Add(),
                                                                            right=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='added_value',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='product',
                                                                        value=Attribute(
                                                                            value=Name(id='product_id', ctx=Load()),
                                                                            attr='display_name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            Name(id='debit_account_id', ctx=Load()),
                                                            Call(
                                                                func=Name(id='abs', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='added_value',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Name(id='product_id', ctx=Load()),
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
                                                            Constant(value='credit', kind=None),
                                                            Constant(value='product_id', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='%(user)s changed stock valuation from  %(previous)s to %(new_value)s - %(product)s', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='user',
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='user',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='previous',
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='current_value_svl',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='new_value',
                                                                        value=BinOp(
                                                                            left=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='current_value_svl',
                                                                                ctx=Load(),
                                                                            ),
                                                                            op=Add(),
                                                                            right=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='added_value',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='product',
                                                                        value=Attribute(
                                                                            value=Name(id='product_id', ctx=Load()),
                                                                            attr='display_name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            Name(id='credit_account_id', ctx=Load()),
                                                            Constant(value=0, kind=None),
                                                            Call(
                                                                func=Name(id='abs', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='added_value',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='product_id', ctx=Load()),
                                                                attr='id',
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='account_move', ctx=Store())],
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
                                args=[Name(id='move_vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='account_move', ctx=Load()),
                                    attr='_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
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
