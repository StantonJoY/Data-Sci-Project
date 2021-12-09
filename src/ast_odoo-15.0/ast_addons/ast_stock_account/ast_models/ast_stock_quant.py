Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.float_utils',
            names=[alias(name='float_is_zero', asname=None)],
            level=0,
        ),
        ClassDef(
            name='StockQuant',
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
                    value=Constant(value='stock.quant', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='value', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Value', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_value', kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='stock.group_stock_manager', kind=None),
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
                        args=[Constant(value='res.currency', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_value', kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='stock.group_stock_manager', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='accounting_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Accounting Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Date at which the accounting entries will be created in case of automated inventory valuation. If empty, the inventory date will be used.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_value',
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
                            value=Constant(value=' For standard and AVCO valuation, compute the current accounting\n        valuation of the quants by multiplying the quantity by\n        the standard price. Instead for FIFO, use the quantity times the\n        average cost (valuation layers are not manage by location so the\n        average cost is the same for all location and the valuation field is\n        a estimation more than a real value).\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='quant', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='currency_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='location_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='quant', ctx=Load()),
                                                    attr='value',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                        Return(value=None),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='location_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='_should_be_valued',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='quant', ctx=Load()),
                                                        attr='owner_id',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='owner_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='quant', ctx=Load()),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='quant', ctx=Load()),
                                                    attr='value',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='quant', ctx=Load()),
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
                                            targets=[Name(id='quantity', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='quant', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='quantity_svl',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='float_is_zero', ctx=Load()),
                                                args=[Name(id='quantity', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_rounding',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='quant', ctx=Load()),
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
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='value',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=0.0, kind=None),
                                                    type_comment=None,
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='average_cost', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='quant', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='with_company',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='quant', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='value_svl',
                                                    ctx=Load(),
                                                ),
                                                op=Div(),
                                                right=Name(id='quantity', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='quant', ctx=Load()),
                                                    attr='value',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='quant', ctx=Load()),
                                                    attr='quantity',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Name(id='average_cost', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='quant', ctx=Load()),
                                                    attr='value',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='quant', ctx=Load()),
                                                    attr='quantity',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='quant', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='with_company',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='quant', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='standard_price',
                                                    ctx=Load(),
                                                ),
                                            ),
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
                                Constant(value='company_id', kind=None),
                                Constant(value='location_id', kind=None),
                                Constant(value='owner_id', kind=None),
                                Constant(value='product_id', kind=None),
                                Constant(value='quantity', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='read_group',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='groupby', annotation=None, type_comment=None),
                            arg(arg='offset', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='orderby', annotation=None, type_comment=None),
                            arg(arg='lazy', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" This override is done in order for the grouped list view to display the total value of\n        the quants inside a location. This doesn't work out of the box because `value` is a computed\n        field.\n        ", kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='value', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='fields', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='StockQuant', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='read_group',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='domain', ctx=Load()),
                                            Name(id='fields', ctx=Load()),
                                            Name(id='groupby', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='offset',
                                                value=Name(id='offset', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='limit',
                                                value=Name(id='limit', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='orderby',
                                                value=Name(id='orderby', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='lazy',
                                                value=Name(id='lazy', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockQuant', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    Name(id='fields', ctx=Load()),
                                    Name(id='groupby', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='offset',
                                        value=Name(id='offset', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='orderby',
                                        value=Name(id='orderby', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='lazy',
                                        value=Name(id='lazy', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='group', ctx=Store()),
                            iter=Name(id='res', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='group', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='__domain', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='quants', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='group', ctx=Load()),
                                                        slice=Constant(value='__domain', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='group', ctx=Load()),
                                                    slice=Constant(value='value', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='value',
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='quant', ctx=Store()),
                                                                iter=Name(id='quants', ctx=Load()),
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
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
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
                FunctionDef(
                    name='_apply_inventory',
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
                            targets=[Name(id='acc_inventories', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='quant', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='accounting_date',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='inventory', ctx=Store()),
                            iter=Name(id='acc_inventories', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='StockQuant', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='force_period_date',
                                                                value=Attribute(
                                                                    value=Name(id='inventory', ctx=Load()),
                                                                    attr='accounting_date',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_apply_inventory',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='inventory', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='accounting_date', kind=None)],
                                                values=[Constant(value=False, kind=None)],
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
                            targets=[Name(id='other_inventories', ctx=Store())],
                            value=BinOp(
                                left=Name(id='self', ctx=Load()),
                                op=Sub(),
                                right=Name(id='acc_inventories', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='other_inventories', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='StockQuant', ctx=Load()),
                                                    Name(id='other_inventories', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_apply_inventory',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_inventory_fields_write',
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
                            value=Constant(value=' Returns a list of fields user can edit when editing a quant in `inventory_mode`.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_inventory_fields_write',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='res', ctx=Store()),
                            op=Add(),
                            value=List(
                                elts=[Constant(value='accounting_date', kind=None)],
                                ctx=Load(),
                            ),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
