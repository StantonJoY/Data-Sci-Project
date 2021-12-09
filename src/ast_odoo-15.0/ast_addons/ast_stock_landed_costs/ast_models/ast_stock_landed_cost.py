Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.float_utils',
            names=[alias(name='float_is_zero', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='SPLIT_METHOD', ctx=Store())],
            value=List(
                elts=[
                    Tuple(
                        elts=[
                            Constant(value='equal', kind=None),
                            Constant(value='Equal', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='by_quantity', kind=None),
                            Constant(value='By Quantity', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='by_current_cost_price', kind=None),
                            Constant(value='By Current Cost', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='by_weight', kind=None),
                            Constant(value='By Weight', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='by_volume', kind=None),
                            Constant(value='By Volume', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='StockLandedCost',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='stock.landed.cost', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Stock Landed Cost', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='mail.thread', kind=None),
                            Constant(value='mail.activity.mixin', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_account_journal_id',
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
                            value=Constant(value='Take the journal configured in the company, else fallback on the stock journal.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='lc_journal', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.journal', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='company',
                                    ctx=Load(),
                                ),
                                attr='lc_journal_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='lc_journal', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='lc_journal_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='lc_journal', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.property', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='property_stock_journal', kind=None),
                                            Constant(value='product.category', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='lc_journal', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='New', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='tracking',
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
                        args=[Constant(value='Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='context_today',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[Constant(value='done', kind=None)],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=True, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='target_model', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='picking', kind=None),
                                            Constant(value='Transfers', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Apply On', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='picking', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[Constant(value='done', kind=None)],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=True, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='picking_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='stock.picking', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Transfers', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[Constant(value='done', kind=None)],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=True, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cost_lines', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.landed.cost.lines', kind=None),
                            Constant(value='cost_id', kind=None),
                            Constant(value='Cost Lines', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[Constant(value='done', kind=None)],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=True, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='valuation_adjustment_lines', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.valuation.adjustment.lines', kind=None),
                            Constant(value='cost_id', kind=None),
                            Constant(value='Valuation Adjustments', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[Constant(value='done', kind=None)],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=True, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='description', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Item Description', kind=None)],
                        keywords=[
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[Constant(value='done', kind=None)],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=True, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='amount_total', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Total', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_total_amount', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='state', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='draft', kind=None),
                                            Constant(value='Draft', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='done', kind=None),
                                            Constant(value='Posted', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='cancel', kind=None),
                                            Constant(value='Cancelled', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            Constant(value='State', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='draft', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='account_move_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.move', kind=None),
                            Constant(value='Journal Entry', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
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
                            Constant(value='Account Journal', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[Constant(value='done', kind=None)],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=True, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_default_account_journal_id',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ),
                        ],
                    ),
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
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='account_journal_id.company_id', kind=None),
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
                            Constant(value='stock_landed_cost_id', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='vendor_bill_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.move', kind=None),
                            Constant(value='Vendor Bill', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='move_type', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value='in_invoice', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
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
                                arg='related',
                                value=Constant(value='company_id.currency_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_total_amount',
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
                            target=Name(id='cost', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='cost', ctx=Load()),
                                            attr='amount_total',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='line', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='cost', ctx=Load()),
                                                            attr='cost_lines',
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
                            args=[Constant(value='cost_lines.price_unit', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_target_model',
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='target_model',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='picking', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='picking_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='target_model', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='vals', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='name', kind=None),
                                        Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='New', kind=None)],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='New', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
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
                                                slice=Constant(value='ir.sequence', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='next_by_code',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='stock.landed.cost', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
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
                    name='unlink',
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
                                    attr='button_cancel',
                                    ctx=Load(),
                                ),
                                args=[],
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
                    name='_track_subtype',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='init_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='state', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='init_values', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='done', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
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
                                        args=[Constant(value='stock_landed_costs.mt_stock_landed_cost_open', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_track_subtype',
                                    ctx=Load(),
                                ),
                                args=[Name(id='init_values', ctx=Load())],
                                keywords=[],
                            ),
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
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Attribute(
                                                value=Name(id='cost', ctx=Load()),
                                                attr='state',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='done', kind=None)],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='cost', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
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
                                                args=[Constant(value='Validated landed costs cannot be cancelled, but you could create negative landed costs to reverse them', kind=None)],
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='cancel', kind=None)],
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
                    name='button_validate',
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
                                    attr='_check_can_validate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='cost_without_adjusment_lines', ctx=Store())],
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
                                            args=[arg(arg='c', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='c', ctx=Load()),
                                                attr='valuation_adjustment_lines',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='cost_without_adjusment_lines', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cost_without_adjusment_lines', ctx=Load()),
                                            attr='compute_landed_cost',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_check_sum',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Cost and adjustments lines do not match. You should maybe recompute the landed costs.', kind=None)],
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
                        For(
                            target=Name(id='cost', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='cost', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cost', ctx=Load()),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='cost', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='move', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='move_vals', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='ref', kind=None),
                                            Constant(value='line_ids', kind=None),
                                            Constant(value='move_type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cost', ctx=Load()),
                                                    attr='account_journal_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='cost', ctx=Load()),
                                                attr='date',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='cost', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='entry', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='valuation_layer_ids', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='cost_to_add_byproduct', ctx=Store())],
                                    value=Call(
                                        func=Name(id='defaultdict', ctx=Load()),
                                        args=[
                                            Lambda(
                                                args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                                body=Constant(value=0.0, kind=None),
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
                                                value=Name(id='cost', ctx=Load()),
                                                attr='valuation_adjustment_lines',
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
                                                body=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='move_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='remaining_qty', ctx=Store())],
                                            value=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='move_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='stock_valuation_layer_ids',
                                                                ctx=Load(),
                                                            ),
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
                                            targets=[Name(id='linked_layer', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='move_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='stock_valuation_layer_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=1, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='cost_to_add', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Name(id='remaining_qty', ctx=Load()),
                                                    op=Div(),
                                                    right=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='move_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='product_qty',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='additional_landed_cost',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='cost', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='currency_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='is_zero',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='cost_to_add', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='valuation_layer', ctx=Store())],
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
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='value', kind=None),
                                                                    Constant(value='unit_cost', kind=None),
                                                                    Constant(value='quantity', kind=None),
                                                                    Constant(value='remaining_qty', kind=None),
                                                                    Constant(value='stock_valuation_layer_id', kind=None),
                                                                    Constant(value='description', kind=None),
                                                                    Constant(value='stock_move_id', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='stock_landed_cost_id', kind=None),
                                                                    Constant(value='company_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='cost_to_add', ctx=Load()),
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Attribute(
                                                                        value=Name(id='linked_layer', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='cost', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='move_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='move_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='cost', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cost', ctx=Load()),
                                                                            attr='company_id',
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
                                                AugAssign(
                                                    target=Attribute(
                                                        value=Name(id='linked_layer', ctx=Load()),
                                                        attr='remaining_value',
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Name(id='cost_to_add', ctx=Load()),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='valuation_layer_ids', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='valuation_layer', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='product', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='cost_method',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='average', kind=None)],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='cost_to_add_byproduct', ctx=Load()),
                                                        slice=Name(id='product', ctx=Load()),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Name(id='cost_to_add', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='qty_out', ctx=Store())],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='move_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_is_in',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='qty_out', ctx=Store())],
                                                    value=BinOp(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_qty',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Name(id='remaining_qty', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_is_out',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='qty_out', ctx=Store())],
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='move_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='product_qty',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='move_vals', ctx=Load()),
                                                slice=Constant(value='line_ids', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='_create_accounting_entries',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='move', ctx=Load()),
                                                    Name(id='qty_out', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='products', ctx=Store())],
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
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='p', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='cost_to_add_byproduct', ctx=Load()),
                                                                attr='keys',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
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
                                For(
                                    target=Name(id='product', ctx=Store()),
                                    iter=Name(id='products', ctx=Load()),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='float_is_zero', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='quantity_svl',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='precision_rounding',
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='product', ctx=Load()),
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
                                                AugAssign(
                                                    target=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='product', ctx=Load()),
                                                                                attr='with_company',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='cost', ctx=Load()),
                                                                                    attr='company_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='sudo',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
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
                                                        left=Subscript(
                                                            value=Name(id='cost_to_add_byproduct', ctx=Load()),
                                                            slice=Name(id='product', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        op=Div(),
                                                        right=Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='quantity_svl',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='move_vals', ctx=Load()),
                                            slice=Constant(value='stock_valuation_layer_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=6, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Name(id='valuation_layer_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='move', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='move', ctx=Load()),
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
                                            value=Name(id='cost', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='account_move_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='done', kind=None),
                                                    Attribute(
                                                        value=Name(id='move', ctx=Load()),
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
                                            value=Name(id='move', ctx=Load()),
                                            attr='_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='cost', ctx=Load()),
                                                attr='vendor_bill_id',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='cost', ctx=Load()),
                                                        attr='vendor_bill_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='posted', kind=None)],
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cost', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='anglo_saxon_accounting',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='all_amls', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='cost', ctx=Load()),
                                                        attr='vendor_bill_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='line_ids',
                                                    ctx=Load(),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='cost', ctx=Load()),
                                                        attr='account_move_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='line_ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='product', ctx=Store()),
                                            iter=Attribute(
                                                value=Attribute(
                                                    value=Name(id='cost', ctx=Load()),
                                                    attr='cost_lines',
                                                    ctx=Load(),
                                                ),
                                                attr='product_id',
                                                ctx=Load(),
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
                                                    targets=[Name(id='input_account', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='accounts', ctx=Load()),
                                                        slice=Constant(value='stock_input', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='all_amls', ctx=Load()),
                                                                    attr='filtered',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Lambda(
                                                                        args=arguments(
                                                                            posonlyargs=[],
                                                                            args=[arg(arg='aml', annotation=None, type_comment=None)],
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
                                                                                        value=Name(id='aml', ctx=Load()),
                                                                                        attr='account_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[Name(id='input_account', ctx=Load())],
                                                                                ),
                                                                                UnaryOp(
                                                                                    op=Not(),
                                                                                    operand=Attribute(
                                                                                        value=Name(id='aml', ctx=Load()),
                                                                                        attr='full_reconcile_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='reconcile',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
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
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_valuation_lines',
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
                            targets=[Name(id='lines', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='move', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_targeted_move_ids',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='valuation',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='real_time', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='cost_method',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='fifo', kind=None),
                                                            Constant(value='average', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='cancel', kind=None)],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='product_qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='vals', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='product_id', kind=None),
                                            Constant(value='move_id', kind=None),
                                            Constant(value='quantity', kind=None),
                                            Constant(value='former_cost', kind=None),
                                            Constant(value='weight', kind=None),
                                            Constant(value='volume', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='product_qty',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='stock_valuation_layer_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='value', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='weight',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='product_qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='volume',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='product_qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lines', ctx=Load()),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='lines', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='target_model_descriptions', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_fields',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='target_model', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_description_selection',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='You cannot apply landed costs on the chosen %s(s). Landed costs can only be applied for products with automated inventory valuation and FIFO or average costing method.', kind=None),
                                                    Subscript(
                                                        value=Name(id='target_model_descriptions', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='target_model',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                        Return(
                            value=Name(id='lines', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='compute_landed_cost',
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
                            targets=[Name(id='AdjustementLines', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.valuation.adjustment.lines', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='AdjustementLines', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='cost_id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
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
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='towrite_dict', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='cost', ctx=Store()),
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
                                            args=[arg(arg='cost', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='cost', ctx=Load()),
                                                attr='_get_targeted_move_ids',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='rounding', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='cost', ctx=Load()),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='rounding',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='total_qty', ctx=Store())],
                                    value=Constant(value=0.0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='total_cost', ctx=Store())],
                                    value=Constant(value=0.0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='total_weight', ctx=Store())],
                                    value=Constant(value=0.0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='total_volume', ctx=Store())],
                                    value=Constant(value=0.0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='total_line', ctx=Store())],
                                    value=Constant(value=0.0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='all_val_line_values', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cost', ctx=Load()),
                                            attr='get_valuation_lines',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='val_line_values', ctx=Store()),
                                    iter=Name(id='all_val_line_values', ctx=Load()),
                                    body=[
                                        For(
                                            target=Name(id='cost_line', ctx=Store()),
                                            iter=Attribute(
                                                value=Name(id='cost', ctx=Load()),
                                                attr='cost_lines',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='val_line_values', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='cost_id', kind=None),
                                                                    Constant(value='cost_line_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='cost', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='cost_line', ctx=Load()),
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
                                                                slice=Constant(value='stock.valuation.adjustment.lines', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='val_line_values', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='total_qty', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='val_line_values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        AugAssign(
                                            target=Name(id='total_weight', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='val_line_values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='weight', kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        AugAssign(
                                            target=Name(id='total_volume', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='val_line_values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='volume', kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='former_cost', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='val_line_values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='former_cost', kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='total_cost', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='cost', ctx=Load()),
                                                        attr='currency_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='round',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='former_cost', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        AugAssign(
                                            target=Name(id='total_line', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='line', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='cost', ctx=Load()),
                                        attr='cost_lines',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='value_split', ctx=Store())],
                                            value=Constant(value=0.0, kind=None),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='valuation', ctx=Store()),
                                            iter=Attribute(
                                                value=Name(id='cost', ctx=Load()),
                                                attr='valuation_adjustment_lines',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='value', ctx=Store())],
                                                    value=Constant(value=0.0, kind=None),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='valuation', ctx=Load()),
                                                                attr='cost_line_id',
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='valuation', ctx=Load()),
                                                                        attr='cost_line_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='split_method',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='by_quantity', kind=None)],
                                                                    ),
                                                                    Name(id='total_qty', ctx=Load()),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='per_unit', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='price_unit',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Div(),
                                                                        right=Name(id='total_qty', ctx=Load()),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='value', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Attribute(
                                                                            value=Name(id='valuation', ctx=Load()),
                                                                            attr='quantity',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Mult(),
                                                                        right=Name(id='per_unit', ctx=Load()),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='split_method',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='by_weight', kind=None)],
                                                                            ),
                                                                            Name(id='total_weight', ctx=Load()),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='per_unit', ctx=Store())],
                                                                            value=BinOp(
                                                                                left=Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='price_unit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Div(),
                                                                                right=Name(id='total_weight', ctx=Load()),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='value', ctx=Store())],
                                                                            value=BinOp(
                                                                                left=Attribute(
                                                                                    value=Name(id='valuation', ctx=Load()),
                                                                                    attr='weight',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Mult(),
                                                                                right=Name(id='per_unit', ctx=Load()),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='line', ctx=Load()),
                                                                                            attr='split_method',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='by_volume', kind=None)],
                                                                                    ),
                                                                                    Name(id='total_volume', ctx=Load()),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='per_unit', ctx=Store())],
                                                                                    value=BinOp(
                                                                                        left=Attribute(
                                                                                            value=Name(id='line', ctx=Load()),
                                                                                            attr='price_unit',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        op=Div(),
                                                                                        right=Name(id='total_volume', ctx=Load()),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='value', ctx=Store())],
                                                                                    value=BinOp(
                                                                                        left=Attribute(
                                                                                            value=Name(id='valuation', ctx=Load()),
                                                                                            attr='volume',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        op=Mult(),
                                                                                        right=Name(id='per_unit', ctx=Load()),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='line', ctx=Load()),
                                                                                            attr='split_method',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='equal', kind=None)],
                                                                                    ),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='value', ctx=Store())],
                                                                                            value=BinOp(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='line', ctx=Load()),
                                                                                                    attr='price_unit',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                op=Div(),
                                                                                                right=Name(id='total_line', ctx=Load()),
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[
                                                                                        If(
                                                                                            test=BoolOp(
                                                                                                op=And(),
                                                                                                values=[
                                                                                                    Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Name(id='line', ctx=Load()),
                                                                                                            attr='split_method',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[Constant(value='by_current_cost_price', kind=None)],
                                                                                                    ),
                                                                                                    Name(id='total_cost', ctx=Load()),
                                                                                                ],
                                                                                            ),
                                                                                            body=[
                                                                                                Assign(
                                                                                                    targets=[Name(id='per_unit', ctx=Store())],
                                                                                                    value=BinOp(
                                                                                                        left=Attribute(
                                                                                                            value=Name(id='line', ctx=Load()),
                                                                                                            attr='price_unit',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        op=Div(),
                                                                                                        right=Name(id='total_cost', ctx=Load()),
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                                Assign(
                                                                                                    targets=[Name(id='value', ctx=Store())],
                                                                                                    value=BinOp(
                                                                                                        left=Attribute(
                                                                                                            value=Name(id='valuation', ctx=Load()),
                                                                                                            attr='former_cost',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        op=Mult(),
                                                                                                        right=Name(id='per_unit', ctx=Load()),
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[
                                                                                                Assign(
                                                                                                    targets=[Name(id='value', ctx=Store())],
                                                                                                    value=BinOp(
                                                                                                        left=Attribute(
                                                                                                            value=Name(id='line', ctx=Load()),
                                                                                                            attr='price_unit',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        op=Div(),
                                                                                                        right=Name(id='total_line', ctx=Load()),
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        If(
                                                            test=Name(id='rounding', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='value', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='tools', ctx=Load()),
                                                                            attr='float_round',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='value', ctx=Load())],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='precision_rounding',
                                                                                value=Name(id='rounding', ctx=Load()),
                                                                            ),
                                                                            keyword(
                                                                                arg='rounding_method',
                                                                                value=Constant(value='UP', kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='fnc', ctx=Store())],
                                                                    value=IfExp(
                                                                        test=Compare(
                                                                            left=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='price_unit',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Gt()],
                                                                            comparators=[Constant(value=0, kind=None)],
                                                                        ),
                                                                        body=Name(id='min', ctx=Load()),
                                                                        orelse=Name(id='max', ctx=Load()),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='value', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='fnc', ctx=Load()),
                                                                        args=[
                                                                            Name(id='value', ctx=Load()),
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='price_unit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Sub(),
                                                                                right=Name(id='value_split', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                AugAssign(
                                                                    target=Name(id='value_split', ctx=Store()),
                                                                    op=Add(),
                                                                    value=Name(id='value', ctx=Load()),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='valuation', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotIn()],
                                                                comparators=[Name(id='towrite_dict', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='towrite_dict', ctx=Load()),
                                                                            slice=Attribute(
                                                                                value=Name(id='valuation', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Name(id='value', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                AugAssign(
                                                                    target=Subscript(
                                                                        value=Name(id='towrite_dict', ctx=Load()),
                                                                        slice=Attribute(
                                                                            value=Name(id='valuation', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ctx=Store(),
                                                                    ),
                                                                    op=Add(),
                                                                    value=Name(id='value', ctx=Load()),
                                                                ),
                                                            ],
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
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='towrite_dict', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='AdjustementLines', ctx=Load()),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='key', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='additional_landed_cost', kind=None)],
                                                values=[Name(id='value', ctx=Load())],
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
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_view_stock_valuation_layers',
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
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='stock_valuation_layer_ids',
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='stock_account.stock_valuation_layer_action', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[Name(id='action', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=Name(id='domain', ctx=Load()),
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
                    name='_get_targeted_move_ids',
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
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='picking_ids',
                                    ctx=Load(),
                                ),
                                attr='move_lines',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_can_validate',
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
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Attribute(
                                                value=Name(id='cost', ctx=Load()),
                                                attr='state',
                                                ctx=Load(),
                                            ),
                                            ops=[NotEq()],
                                            comparators=[Constant(value='draft', kind=None)],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='cost', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
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
                                                args=[Constant(value='Only draft landed costs can be validated', kind=None)],
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
                        For(
                            target=Name(id='cost', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='cost', ctx=Load()),
                                                attr='_get_targeted_move_ids',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='target_model_descriptions', ctx=Store())],
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_fields',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='target_model', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_description_selection',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='Please define %s on which those additional costs should apply.', kind=None),
                                                            Subscript(
                                                                value=Name(id='target_model_descriptions', ctx=Load()),
                                                                slice=Attribute(
                                                                    value=Name(id='cost', ctx=Load()),
                                                                    attr='target_model',
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                    name='_check_sum',
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
                            value=Constant(value=' Check if each cost line its valuation lines sum to the correct amount\n        and if the overall total amount is correct also ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='prec_digits', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    attr='currency_id',
                                    ctx=Load(),
                                ),
                                attr='decimal_places',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='landed_cost', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='total_amount', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='landed_cost', ctx=Load()),
                                                        attr='valuation_adjustment_lines',
                                                        ctx=Load(),
                                                    ),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='additional_landed_cost', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='float_is_zero',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                BinOp(
                                                    left=Name(id='total_amount', ctx=Load()),
                                                    op=Sub(),
                                                    right=Attribute(
                                                        value=Name(id='landed_cost', ctx=Load()),
                                                        attr='amount_total',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='precision_digits',
                                                    value=Name(id='prec_digits', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='val_to_cost_lines', ctx=Store())],
                                    value=Call(
                                        func=Name(id='defaultdict', ctx=Load()),
                                        args=[
                                            Lambda(
                                                args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                                body=Constant(value=0.0, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='val_line', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='landed_cost', ctx=Load()),
                                        attr='valuation_adjustment_lines',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='val_to_cost_lines', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='val_line', ctx=Load()),
                                                    attr='cost_line_id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Attribute(
                                                value=Name(id='val_line', ctx=Load()),
                                                attr='additional_landed_cost',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=UnaryOp(
                                                    op=Not(),
                                                    operand=Call(
                                                        func=Attribute(
                                                            value=Name(id='tools', ctx=Load()),
                                                            attr='float_is_zero',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='cost_line', ctx=Load()),
                                                                    attr='price_unit',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Sub(),
                                                                right=Name(id='val_amount', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_digits',
                                                                value=Name(id='prec_digits', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='cost_line', ctx=Store()),
                                                                Name(id='val_amount', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='val_to_cost_lines', ctx=Load()),
                                                                attr='items',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
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
        ClassDef(
            name='StockLandedCostLine',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='stock.landed.cost.lines', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Stock Landed Cost Line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Description', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cost_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.landed.cost', kind=None),
                            Constant(value='Landed Cost', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
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
                            Constant(value='Product', kind=None),
                        ],
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
                    targets=[Name(id='price_unit', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Cost', kind=None)],
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
                    targets=[Name(id='split_method', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[Name(id='SPLIT_METHOD', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Split Method', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Equal : Cost will be equally divided.\nBy Quantity : Cost will be divided according to product's quantity.\nBy Current cost : Cost will be divided according to product's current cost.\nBy Weight : Cost will be divided depending on its weight.\nBy Volume : Cost will be divided depending on its volume.", kind=None),
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
                            Constant(value='Account', kind=None),
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
                                arg='related',
                                value=Constant(value='cost_id.currency_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='onchange_product_id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='split_method',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='product_tmpl_id',
                                            ctx=Load(),
                                        ),
                                        attr='split_method_landed_cost',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='split_method',
                                        ctx=Load(),
                                    ),
                                    Constant(value='equal', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='price_unit',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='standard_price',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.0, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='accounts_data', ctx=Store())],
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='account_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='accounts_data', ctx=Load()),
                                slice=Constant(value='stock_input', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='product_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='AdjustmentLines',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='stock.valuation.adjustment.lines', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Valuation Adjustment Lines', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Description', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_name', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cost_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.landed.cost', kind=None),
                            Constant(value='Landed Cost', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
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
                    targets=[Name(id='cost_line_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.landed.cost.lines', kind=None),
                            Constant(value='Cost Line', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='move_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.move', kind=None),
                            Constant(value='Stock Move', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='readonly',
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
                            Constant(value='Product', kind=None),
                        ],
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
                    targets=[Name(id='quantity', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Quantity', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=1.0, kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value=0, kind=None),
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
                    targets=[Name(id='weight', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Weight', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=1.0, kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value='Stock Weight', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='volume', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Volume', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=1.0, kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value='Volume', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='former_cost', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Original Value', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='additional_landed_cost', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Additional Landed Cost', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='final_cost', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='New Value', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_final_cost', kind=None),
                            ),
                            keyword(
                                arg='store',
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
                        args=[Constant(value='res.currency', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='cost_id.company_id.currency_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_name',
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
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s - ', kind=None),
                                        op=Mod(),
                                        right=IfExp(
                                            test=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='cost_line_id',
                                                ctx=Load(),
                                            ),
                                            body=Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='cost_line_id',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            orelse=Constant(value='', kind=None),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='name',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Name(id='name', ctx=Load()),
                                        op=Add(),
                                        right=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='code',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='', kind=None),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
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
                                Constant(value='cost_line_id.name', kind=None),
                                Constant(value='product_id.code', kind=None),
                                Constant(value='product_id.name', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_final_cost',
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
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='final_cost',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='former_cost',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='additional_landed_cost',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
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
                                Constant(value='former_cost', kind=None),
                                Constant(value='additional_landed_cost', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_accounting_entries',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='move', annotation=None, type_comment=None),
                            arg(arg='qty_out', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='cost_product', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='cost_line_id',
                                    ctx=Load(),
                                ),
                                attr='product_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='cost_product', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='debit_account_id', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
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
                                    Constant(value=False, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    attr='_is_dropshipped',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='debit_account_id', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='accounts', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='expense', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='accounts', ctx=Load()),
                                                            slice=Constant(value='expense', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='already_out_account_id', ctx=Store())],
                            value=Attribute(
                                value=Subscript(
                                    value=Name(id='accounts', ctx=Load()),
                                    slice=Constant(value='stock_output', kind=None),
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
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cost_line_id',
                                                ctx=Load(),
                                            ),
                                            attr='account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cost_product', ctx=Load()),
                                                attr='categ_id',
                                                ctx=Load(),
                                            ),
                                            attr='property_stock_account_input_categ_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='credit_account_id', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Please configure Stock Expense Account for product: %s.', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='cost_product', ctx=Load()),
                                                    attr='name',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_account_move_line',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='move', ctx=Load()),
                                    Name(id='credit_account_id', ctx=Load()),
                                    Name(id='debit_account_id', ctx=Load()),
                                    Name(id='qty_out', ctx=Load()),
                                    Name(id='already_out_account_id', ctx=Load()),
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
                    name='_create_account_move_line',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='move', annotation=None, type_comment=None),
                            arg(arg='credit_account_id', annotation=None, type_comment=None),
                            arg(arg='debit_account_id', annotation=None, type_comment=None),
                            arg(arg='qty_out', annotation=None, type_comment=None),
                            arg(arg='already_out_account_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Generate the account.move.line values to track the landed cost.\n        Afterwards, for the goods that are already out of stock, we should create the out moves\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='AccountMoveLine', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_line', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='quantity', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='debit_line', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[Name(id='base_line', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='account_id',
                                        value=Name(id='debit_account_id', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='credit_line', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[Name(id='base_line', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='account_id',
                                        value=Name(id='credit_account_id', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='diff', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='additional_landed_cost',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='diff', ctx=Load()),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='debit_line', ctx=Load()),
                                            slice=Constant(value='debit', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='diff', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='credit_line', ctx=Load()),
                                            slice=Constant(value='credit', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='diff', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='debit_line', ctx=Load()),
                                            slice=Constant(value='credit', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=UnaryOp(
                                        op=USub(),
                                        operand=Name(id='diff', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='credit_line', ctx=Load()),
                                            slice=Constant(value='debit', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=UnaryOp(
                                        op=USub(),
                                        operand=Name(id='diff', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='AccountMoveLine', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Name(id='debit_line', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='AccountMoveLine', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Name(id='credit_line', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='qty_out', ctx=Load()),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='debit_line', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='base_line', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Constant(value=': ', kind=None),
                                                        ),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[Name(id='qty_out', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value=' already out', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ),
                                            keyword(
                                                arg='quantity',
                                                value=Constant(value=0, kind=None),
                                            ),
                                            keyword(
                                                arg='account_id',
                                                value=Name(id='already_out_account_id', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='credit_line', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='base_line', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Constant(value=': ', kind=None),
                                                        ),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[Name(id='qty_out', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value=' already out', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ),
                                            keyword(
                                                arg='quantity',
                                                value=Constant(value=0, kind=None),
                                            ),
                                            keyword(
                                                arg='account_id',
                                                value=Name(id='debit_account_id', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='diff', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Name(id='diff', ctx=Load()),
                                            op=Mult(),
                                            right=Name(id='qty_out', ctx=Load()),
                                        ),
                                        op=Div(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='quantity',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='diff', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='debit_line', ctx=Load()),
                                                    slice=Constant(value='debit', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='diff', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='credit_line', ctx=Load()),
                                                    slice=Constant(value='credit', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='diff', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='debit_line', ctx=Load()),
                                                    slice=Constant(value='credit', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=UnaryOp(
                                                op=USub(),
                                                operand=Name(id='diff', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='credit_line', ctx=Load()),
                                                    slice=Constant(value='debit', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=UnaryOp(
                                                op=USub(),
                                                operand=Name(id='diff', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='AccountMoveLine', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Name(id='debit_line', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='AccountMoveLine', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Name(id='credit_line', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='anglo_saxon_accounting',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='expense_account_id', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
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
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value='expense', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='debit_line', ctx=Store())],
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[Name(id='base_line', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=BinOp(
                                                            left=BinOp(
                                                                left=BinOp(
                                                                    left=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Constant(value=': ', kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[Name(id='qty_out', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            op=Add(),
                                                            right=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value=' already out', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='quantity',
                                                        value=Constant(value=0, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='account_id',
                                                        value=Name(id='expense_account_id', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='credit_line', ctx=Store())],
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[Name(id='base_line', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=BinOp(
                                                            left=BinOp(
                                                                left=BinOp(
                                                                    left=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Constant(value=': ', kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[Name(id='qty_out', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            op=Add(),
                                                            right=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value=' already out', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='quantity',
                                                        value=Constant(value=0, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='account_id',
                                                        value=Name(id='already_out_account_id', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='diff', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='debit_line', ctx=Load()),
                                                            slice=Constant(value='debit', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='diff', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='credit_line', ctx=Load()),
                                                            slice=Constant(value='credit', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='diff', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='debit_line', ctx=Load()),
                                                            slice=Constant(value='credit', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=UnaryOp(
                                                        op=USub(),
                                                        operand=Name(id='diff', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='credit_line', ctx=Load()),
                                                            slice=Constant(value='debit', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=UnaryOp(
                                                        op=USub(),
                                                        operand=Name(id='diff', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='AccountMoveLine', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Name(id='debit_line', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='AccountMoveLine', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Name(id='credit_line', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='AccountMoveLine', ctx=Load()),
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
