Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
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
            module='odoo.tools',
            names=[
                alias(name='float_compare', asname=None),
                alias(name='float_is_zero', asname=None),
            ],
            level=0,
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
                    targets=[Name(id='sale_line_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='sale.order.line', kind=None),
                            Constant(value='sale_order_line_invoice_rel', kind=None),
                            Constant(value='invoice_line_id', kind=None),
                            Constant(value='order_line_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Sales Order Lines', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_copy_data_extend_business_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
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
                                            Name(id='AccountMoveLine', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_copy_data_extend_business_fields',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='sale_line_ids', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=6, kind=None),
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_line_ids',
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_analytic_line',
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
                            value=Constant(value=' Note: This method is called only on the move.line that having an analytic account, and\n            so that should create analytic entries.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='values_list', ctx=Store())],
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
                                    attr='_prepare_analytic_line',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move_to_reinvoice', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.move.line', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='index', ctx=Store()),
                                    Name(id='move_line', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='values_list', ctx=Load()),
                                        slice=Name(id='index', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='so_line', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='move_line', ctx=Load()),
                                                    attr='_sale_can_be_reinvoice',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='move_to_reinvoice', ctx=Store()),
                                                    op=BitOr(),
                                                    value=Name(id='move_line', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='move_to_reinvoice', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='map_sale_line_per_move', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='move_to_reinvoice', ctx=Load()),
                                            attr='_sale_create_reinvoice_sale_line',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='values', ctx=Store()),
                                    iter=Name(id='values_list', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='sale_line', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='map_sale_line_per_move', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='move_id', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='sale_line', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='so_line', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='sale_line', ctx=Load()),
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
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='values_list', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_sale_can_be_reinvoice',
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
                            value=Constant(value=" determine if the generated analytic line should be reinvoiced or not.\n            For Vendor Bill flow, if the product has a 'erinvoice policy' and is a cost, then we will find the SO on which reinvoice the AAL\n        ", kind=None),
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
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='sale_line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='uom_precision_digits', ctx=Store())],
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
                                args=[Constant(value='Product Unit of Measure', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='float_compare', ctx=Load()),
                                            args=[
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='credit',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value=0.0, kind=None),
                                                    ],
                                                ),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='debit',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value=0.0, kind=None),
                                                    ],
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='precision_digits',
                                                    value=Name(id='uom_precision_digits', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='expense_policy',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='no', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='_sale_create_reinvoice_sale_line',
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
                            targets=[Name(id='sale_order_map', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_sale_determine_order',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sale_line_values_to_create', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='existing_sale_line_cache', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='map_move_sale_line', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='move_line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='sale_order', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sale_order_map', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='move_line', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='sale_order', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='sale_order', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='sale', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='message_unconfirmed', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The Sales Order %s linked to the Analytic Account %s must be validated before registering expenses.', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='messages', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='draft', kind=None),
                                                    Constant(value='sent', kind=None),
                                                    Constant(value='done', kind=None),
                                                    Constant(value='cancel', kind=None),
                                                ],
                                                values=[
                                                    Name(id='message_unconfirmed', ctx=Load()),
                                                    Name(id='message_unconfirmed', ctx=Load()),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The Sales Order %s linked to the Analytic Account %s is currently locked. You cannot register an expense on a locked Sales Order. Please create a new SO linked to this Analytic Account.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The Sales Order %s linked to the Analytic Account %s is cancelled. You cannot register an expense on a cancelled Sales Order.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Subscript(
                                                            value=Name(id='messages', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='sale_order', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='sale_order', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='sale_order', ctx=Load()),
                                                                        attr='analytic_account_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
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
                                    targets=[Name(id='price', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='move_line', ctx=Load()),
                                            attr='_sale_get_invoice_price',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='sale_order', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='sale_line', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move_line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='expense_policy',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='sales_price', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move_line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='invoice_policy',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='delivery', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='map_entry_key', ctx=Store())],
                                            value=Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='sale_order', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='move_line', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='price', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='sale_line', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='existing_sale_line_cache', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='map_entry_key', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='sale_line', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='map_move_sale_line', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='move_line', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='sale_line', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='existing_sale_line_cache', ctx=Load()),
                                                            slice=Name(id='map_entry_key', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='sale_line', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='sale_line', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='sale.order.line', kind=None),
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
                                                                            Constant(value='order_id', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='sale_order', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='price_unit', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Name(id='price', ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='move_line', ctx=Load()),
                                                                                    attr='product_id',
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
                                                                            Constant(value='is_expense', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Constant(value=True, kind=None),
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
                                                                value=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='sale_line', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='map_move_sale_line', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='move_line', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='existing_sale_line_cache', ctx=Load()),
                                                                    slice=Name(id='map_entry_key', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='sale_line', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='sale_line_values_to_create', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='move_line', ctx=Load()),
                                                                            attr='_sale_prepare_sale_line_values',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='sale_order', ctx=Load()),
                                                                            Name(id='price', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='existing_sale_line_cache', ctx=Load()),
                                                                    slice=Name(id='map_entry_key', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=BinOp(
                                                                left=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[Name(id='sale_line_values_to_create', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                op=Sub(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='map_move_sale_line', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='move_line', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=BinOp(
                                                                left=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[Name(id='sale_line_values_to_create', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                op=Sub(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sale_line_values_to_create', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='move_line', ctx=Load()),
                                                            attr='_sale_prepare_sale_line_values',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='sale_order', ctx=Load()),
                                                            Name(id='price', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='map_move_sale_line', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='move_line', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='sale_line_values_to_create', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=Sub(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_sale_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='sale_line_values_to_create', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='sol', ctx=Store()),
                            iter=Name(id='new_sale_lines', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sol', ctx=Load()),
                                            attr='_onchange_discount',
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
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='move_line_id', ctx=Store()),
                                    Name(id='unknown_sale_line', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='map_move_sale_line', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='unknown_sale_line', ctx=Load()),
                                            Name(id='int', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Name(id='move_line_id', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='new_sale_lines', ctx=Load()),
                                                slice=Name(id='unknown_sale_line', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='unknown_sale_line', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='models', ctx=Load()),
                                                        attr='BaseModel',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='result', ctx=Load()),
                                                            slice=Name(id='move_line_id', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='unknown_sale_line', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_sale_determine_order',
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
                            value=Constant(value=' Get the mapping of move.line with the sale.order record on which its analytic entries should be reinvoiced\n            :return a dict where key is the move line id, and value is sale.order record (or None).\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='analytic_accounts', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='analytic_account_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapping', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='analytic_accounts', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='sale_orders', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='sale.order', kind=None),
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
                                                            Constant(value='analytic_account_id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Name(id='analytic_accounts', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='state', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='sale', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='order',
                                                value=Constant(value='create_date DESC', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='sale_order', ctx=Store()),
                                    iter=Name(id='sale_orders', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='mapping', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='sale_order', ctx=Load()),
                                                            attr='analytic_account_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='sale_order', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='analytic_accounts_without_open_order', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='analytic_accounts', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='account', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=UnaryOp(
                                                    op=Not(),
                                                    operand=Call(
                                                        func=Attribute(
                                                            value=Name(id='mapping', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='account', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='analytic_accounts_without_open_order', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='sale_orders', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='sale.order', kind=None),
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
                                                                    Constant(value='analytic_account_id', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='analytic_accounts_without_open_order', ctx=Load()),
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
                                                keywords=[
                                                    keyword(
                                                        arg='order',
                                                        value=Constant(value='create_date DESC', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='sale_order', ctx=Store()),
                                    iter=Name(id='sale_orders', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='mapping', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='sale_order', ctx=Load()),
                                                            attr='analytic_account_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='sale_order', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='move_line', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='mapping', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='move_line', ctx=Load()),
                                                attr='analytic_account_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='move_line', ctx=Store()),
                                        iter=Name(id='self', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
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
                    name='_sale_prepare_sale_line_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                            arg(arg='price', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Generate the sale.line creation value from the current move line ', kind=None),
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
                        Assign(
                            targets=[Name(id='last_so_line', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order.line', kind=None),
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
                                                    Constant(value='order_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='order', ctx=Load()),
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
                                        arg='order',
                                        value=Constant(value='sequence desc', kind=None),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_sequence', ctx=Store())],
                            value=IfExp(
                                test=Name(id='last_so_line', ctx=Load()),
                                body=BinOp(
                                    left=Attribute(
                                        value=Name(id='last_so_line', ctx=Load()),
                                        attr='sequence',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Constant(value=1, kind=None),
                                ),
                                orelse=Constant(value=100, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fpos', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='order', ctx=Load()),
                                        attr='fiscal_position_id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='fiscal_position_id',
                                                ctx=Load(),
                                            ),
                                            attr='get_fiscal_position',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='taxes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='fpos', ctx=Load()),
                                    attr='map_tax',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='taxes_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='order_id', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='sequence', kind=None),
                                    Constant(value='price_unit', kind=None),
                                    Constant(value='tax_id', kind=None),
                                    Constant(value='discount', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='product_uom', kind=None),
                                    Constant(value='product_uom_qty', kind=None),
                                    Constant(value='is_expense', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='order', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Name(id='last_sequence', ctx=Load()),
                                    Name(id='price', ctx=Load()),
                                    ListComp(
                                        elt=Attribute(
                                            value=Name(id='x', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Name(id='taxes', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Constant(value=0.0, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.0, kind=None),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_sale_get_invoice_price',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Based on the current move line, compute the price to reinvoice the analytic line that is going to be created (so the\n            price of the sale line).\n        ', kind=None),
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
                        Assign(
                            targets=[Name(id='unit_amount', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='quantity',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='amount', ctx=Store())],
                            value=BinOp(
                                left=BoolOp(
                                    op=Or(),
                                    values=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='credit',
                                            ctx=Load(),
                                        ),
                                        Constant(value=0.0, kind=None),
                                    ],
                                ),
                                op=Sub(),
                                right=BoolOp(
                                    op=Or(),
                                    values=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='debit',
                                            ctx=Load(),
                                        ),
                                        Constant(value=0.0, kind=None),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    attr='expense_policy',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='sales_price', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='partner',
                                                    value=Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='date_order',
                                                    value=Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='date_order',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='pricelist',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='pricelist_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='uom',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        attr='price',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='uom_precision_digits', ctx=Store())],
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
                                args=[Constant(value='Product Unit of Measure', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='float_is_zero', ctx=Load()),
                                args=[Name(id='unit_amount', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='precision_digits',
                                        value=Name(id='uom_precision_digits', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=0.0, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='amount', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='abs', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='amount', ctx=Load()),
                                                op=Div(),
                                                right=Name(id='unit_amount', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='price_unit', ctx=Store())],
                            value=Call(
                                func=Name(id='abs', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='amount', ctx=Load()),
                                        op=Div(),
                                        right=Name(id='unit_amount', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currency_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='company_id',
                                    ctx=Load(),
                                ),
                                attr='currency_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='currency_id', ctx=Load()),
                                    Compare(
                                        left=Name(id='currency_id', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='price_unit', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='currency_id', ctx=Load()),
                                            attr='_convert',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='price_unit', ctx=Load()),
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='date_order',
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
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='price_unit', ctx=Load()),
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
