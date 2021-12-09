Module(
    body=[
        ImportFrom(
            module='itertools',
            names=[alias(name='groupby', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='re',
            names=[alias(name='search', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='functools',
            names=[alias(name='partial', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='PosOrderLine',
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
                    value=Constant(value='pos.order.line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='note', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Internal Note added by the waiter.', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mp_skip', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Skip line when sending ticket to kitchen printers.', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mp_dirty', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='PosOrder',
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
                    value=Constant(value='pos.order', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='table_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='restaurant.table', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Table', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The table where this order was served', kind=None),
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
                    targets=[Name(id='customer_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Guests', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The amount of customers that have been served by this order.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='multiprint_resume', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_pack_lot_lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order_lines', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Add pack_lot_lines to the order_lines.\n\n        The function doesn't return anything but adds the results directly to the order_lines.\n\n        :param order_lines: order_lines for which the pack_lot_lines are to be requested.\n        :type order_lines: pos.order.line.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='pack_lots', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='pos.pack.operation.lot', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='pos_order_line_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        ListComp(
                                                            elt=Subscript(
                                                                value=Name(id='order_line', ctx=Load()),
                                                                slice=Constant(value='id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='order_line', ctx=Store()),
                                                                    iter=Name(id='order_lines', ctx=Load()),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='id', kind=None),
                                                Constant(value='lot_name', kind=None),
                                                Constant(value='pos_order_line_id', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='pack_lot', ctx=Store()),
                            iter=Name(id='pack_lots', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='pack_lot', ctx=Load()),
                                            slice=Constant(value='order_line', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='pack_lot', ctx=Load()),
                                            slice=Constant(value='pos_order_line_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='pack_lot', ctx=Load()),
                                            slice=Constant(value='server_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='pack_lot', ctx=Load()),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='pack_lot', ctx=Load()),
                                            slice=Constant(value='pos_order_line_id', kind=None),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='pack_lot', ctx=Load()),
                                            slice=Constant(value='id', kind=None),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='order_line_id', ctx=Store()),
                                    Name(id='pack_lot_ids', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='groupby', ctx=Load()),
                                args=[Name(id='pack_lots', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='x', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Subscript(
                                                value=Name(id='x', ctx=Load()),
                                                slice=Constant(value='order_line', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Call(
                                                func=Name(id='next', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Name(id='order_line', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='order_line', ctx=Store()),
                                                                iter=Name(id='order_lines', ctx=Load()),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Subscript(
                                                                            value=Name(id='order_line', ctx=Load()),
                                                                            slice=Constant(value='id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='order_line_id', ctx=Load())],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            slice=Constant(value='pack_lot_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='pack_lots', ctx=Load())],
                                        keywords=[],
                                    ),
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
                    name='_get_fields_for_order_line',
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
                            value=List(
                                elts=[
                                    Constant(value='id', kind=None),
                                    Constant(value='discount', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='price_unit', kind=None),
                                    Constant(value='order_id', kind=None),
                                    Constant(value='qty', kind=None),
                                    Constant(value='note', kind=None),
                                    Constant(value='mp_skip', kind=None),
                                    Constant(value='mp_dirty', kind=None),
                                    Constant(value='full_product_name', kind=None),
                                    Constant(value='customer_note', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_order_lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='orders', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Add pos_order_lines to the orders.\n\n        The function doesn't return anything but adds the results directly to the orders.\n\n        :param orders: orders for which the order_lines are to be requested.\n        :type orders: pos.order.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='order_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='pos.order.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='order_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        ListComp(
                                                            elt=Subscript(
                                                                value=Name(id='to', ctx=Load()),
                                                                slice=Constant(value='id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='to', ctx=Store()),
                                                                    iter=Name(id='orders', ctx=Load()),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_fields_for_order_line',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='order_lines', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[List(elts=[], ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_pack_lot_lines',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='order_lines', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='extended_order_lines', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='order_line', ctx=Store()),
                            iter=Name(id='order_lines', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='order_line', ctx=Load()),
                                            slice=Constant(value='product_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='order_line', ctx=Load()),
                                            slice=Constant(value='product_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='order_line', ctx=Load()),
                                            slice=Constant(value='server_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='order_line', ctx=Load()),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='order_line', ctx=Load()),
                                            slice=Constant(value='id', kind=None),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Compare(
                                            left=Constant(value='pack_lot_ids', kind=None),
                                            ops=[In()],
                                            comparators=[Name(id='order_line', ctx=Load())],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='order_line', ctx=Load()),
                                                    slice=Constant(value='pack_lot_ids', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='extended_order_lines', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Name(id='order_line', ctx=Load()),
                                                ],
                                                ctx=Load(),
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
                            target=Tuple(
                                elts=[
                                    Name(id='order_id', ctx=Store()),
                                    Name(id='order_lines', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='groupby', ctx=Load()),
                                args=[Name(id='extended_order_lines', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='x', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Subscript(
                                                value=Subscript(
                                                    value=Name(id='x', ctx=Load()),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='order_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Call(
                                                func=Name(id='next', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Name(id='order', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='order', ctx=Store()),
                                                                iter=Name(id='orders', ctx=Load()),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Subscript(
                                                                            value=Name(id='order', ctx=Load()),
                                                                            slice=Constant(value='id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Subscript(
                                                                                value=Name(id='order_id', ctx=Load()),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            slice=Constant(value='lines', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='order_lines', ctx=Load())],
                                        keywords=[],
                                    ),
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
                    name='_get_fields_for_payment_lines',
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
                            value=List(
                                elts=[
                                    Constant(value='id', kind=None),
                                    Constant(value='amount', kind=None),
                                    Constant(value='pos_order_id', kind=None),
                                    Constant(value='payment_method_id', kind=None),
                                    Constant(value='card_type', kind=None),
                                    Constant(value='cardholder_name', kind=None),
                                    Constant(value='transaction_id', kind=None),
                                    Constant(value='payment_status', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_payment_lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='orders', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Add account_bank_statement_lines to the orders.\n\n        The function doesn't return anything but adds the results directly to the orders.\n\n        :param orders: orders for which the payment_lines are to be requested.\n        :type orders: pos.order.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='payment_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='pos.payment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='pos_order_id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        ListComp(
                                                            elt=Subscript(
                                                                value=Name(id='po', ctx=Load()),
                                                                slice=Constant(value='id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='po', ctx=Store()),
                                                                    iter=Name(id='orders', ctx=Load()),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_fields_for_payment_lines',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='extended_payment_lines', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='payment_line', ctx=Store()),
                            iter=Name(id='payment_lines', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='payment_line', ctx=Load()),
                                            slice=Constant(value='server_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='payment_line', ctx=Load()),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='payment_line', ctx=Load()),
                                            slice=Constant(value='payment_method_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='payment_line', ctx=Load()),
                                            slice=Constant(value='payment_method_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='payment_line', ctx=Load()),
                                            slice=Constant(value='id', kind=None),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='extended_payment_lines', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Name(id='payment_line', ctx=Load()),
                                                ],
                                                ctx=Load(),
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
                            target=Tuple(
                                elts=[
                                    Name(id='order_id', ctx=Store()),
                                    Name(id='payment_lines', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='groupby', ctx=Load()),
                                args=[Name(id='extended_payment_lines', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='x', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Subscript(
                                                value=Subscript(
                                                    value=Name(id='x', ctx=Load()),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='pos_order_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Call(
                                                func=Name(id='next', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Name(id='order', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='order', ctx=Store()),
                                                                iter=Name(id='orders', ctx=Load()),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Subscript(
                                                                            value=Name(id='order', ctx=Load()),
                                                                            slice=Constant(value='id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Subscript(
                                                                                value=Name(id='order_id', ctx=Load()),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            slice=Constant(value='statement_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='payment_lines', ctx=Load())],
                                        keywords=[],
                                    ),
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
                    name='_get_fields_for_draft_order',
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
                            value=List(
                                elts=[
                                    Constant(value='id', kind=None),
                                    Constant(value='pricelist_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='sequence_number', kind=None),
                                    Constant(value='session_id', kind=None),
                                    Constant(value='pos_reference', kind=None),
                                    Constant(value='create_uid', kind=None),
                                    Constant(value='create_date', kind=None),
                                    Constant(value='customer_count', kind=None),
                                    Constant(value='fiscal_position_id', kind=None),
                                    Constant(value='table_id', kind=None),
                                    Constant(value='to_invoice', kind=None),
                                    Constant(value='multiprint_resume', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_table_draft_orders',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='table_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Generate an object of all draft orders for the given table.\n\n        Generate and return an JSON object with all draft orders for the given table, to send to the\n        front end application.\n\n        :param table_id: Id of the selected table.\n        :type table_id: int.\n        :returns: list -- list of dict representing the table orders\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='table_orders', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='state', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Constant(value='draft', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        Constant(value='table_id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Name(id='table_id', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_fields_for_draft_order',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_order_lines',
                                    ctx=Load(),
                                ),
                                args=[Name(id='table_orders', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_payment_lines',
                                    ctx=Load(),
                                ),
                                args=[Name(id='table_orders', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='table_orders', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='order', ctx=Load()),
                                            slice=Constant(value='pos_session_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='order', ctx=Load()),
                                            slice=Constant(value='session_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='order', ctx=Load()),
                                            slice=Constant(value='uid', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='search', ctx=Load()),
                                                args=[
                                                    Constant(value='\\d{5,}-\\d{3,}-\\d{4,}', kind=None),
                                                    Subscript(
                                                        value=Name(id='order', ctx=Load()),
                                                        slice=Constant(value='pos_reference', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='order', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='order', ctx=Load()),
                                        slice=Constant(value='pos_reference', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='order', ctx=Load()),
                                            slice=Constant(value='creation_date', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='order', ctx=Load()),
                                        slice=Constant(value='create_date', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='order', ctx=Load()),
                                            slice=Constant(value='server_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='order', ctx=Load()),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Subscript(
                                        value=Name(id='order', ctx=Load()),
                                        slice=Constant(value='fiscal_position_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='order', ctx=Load()),
                                                    slice=Constant(value='fiscal_position_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='order', ctx=Load()),
                                                    slice=Constant(value='fiscal_position_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Subscript(
                                        value=Name(id='order', ctx=Load()),
                                        slice=Constant(value='pricelist_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='order', ctx=Load()),
                                                    slice=Constant(value='pricelist_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='order', ctx=Load()),
                                                    slice=Constant(value='pricelist_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Subscript(
                                        value=Name(id='order', ctx=Load()),
                                        slice=Constant(value='partner_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='order', ctx=Load()),
                                                    slice=Constant(value='partner_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='order', ctx=Load()),
                                                    slice=Constant(value='partner_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Subscript(
                                        value=Name(id='order', ctx=Load()),
                                        slice=Constant(value='table_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='order', ctx=Load()),
                                                    slice=Constant(value='table_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='order', ctx=Load()),
                                                    slice=Constant(value='table_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Compare(
                                            left=Constant(value='lines', kind=None),
                                            ops=[In()],
                                            comparators=[Name(id='order', ctx=Load())],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='order', ctx=Load()),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Compare(
                                            left=Constant(value='statement_ids', kind=None),
                                            ops=[In()],
                                            comparators=[Name(id='order', ctx=Load())],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='order', ctx=Load()),
                                                    slice=Constant(value='statement_ids', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='order', ctx=Load()),
                                            slice=Constant(value='id', kind=None),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='order', ctx=Load()),
                                            slice=Constant(value='session_id', kind=None),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='order', ctx=Load()),
                                            slice=Constant(value='pos_reference', kind=None),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='order', ctx=Load()),
                                            slice=Constant(value='create_date', kind=None),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='table_orders', ctx=Load()),
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
                    name='set_tip',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tip_line_vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Set tip to `self` based on values in `tip_line_vals`.', kind=None),
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
                            targets=[Name(id='PosOrderLine', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='pos.order.line', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='process_line', ctx=Store())],
                            value=Call(
                                func=Name(id='partial', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='PosOrderLine', ctx=Load()),
                                        attr='_order_line_fields',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='session_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='session_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='processed_tip_line_vals', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Name(id='process_line', ctx=Load()),
                                    args=[
                                        List(
                                            elts=[
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Name(id='tip_line_vals', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=2, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='processed_tip_line_vals', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='order_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
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
                            targets=[Name(id='tip_line', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='lines',
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
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='session_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='config_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tip_product_id',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='tip_line', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='tip_line', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='PosOrderLine', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='processed_tip_line_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tip_line', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='processed_tip_line_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='payment_line', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='payment_ids',
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
                                            body=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='is_change',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='payment_line', ctx=Load()),
                                    attr='_update_payment_line_for_tip',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='tip_line', ctx=Load()),
                                        attr='price_subtotal_incl',
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='is_tipped', kind=None),
                                            Constant(value='tip_amount', kind=None),
                                            Constant(value='amount_total', kind=None),
                                            Constant(value='amount_paid', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Attribute(
                                                value=Name(id='tip_line', ctx=Load()),
                                                attr='price_subtotal_incl',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='amount_total',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='tip_line', ctx=Load()),
                                                    attr='price_subtotal_incl',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='amount_paid',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='tip_line', ctx=Load()),
                                                    attr='price_subtotal_incl',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                    name='set_no_tip',
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
                            value=Constant(value='Override this method to introduce action when setting no tip.', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='is_tipped', kind=None),
                                            Constant(value='tip_amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
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
                    name='_order_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='ui_order', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='order_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PosOrder', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_order_fields',
                                    ctx=Load(),
                                ),
                                args=[Name(id='ui_order', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='order_fields', ctx=Load()),
                                    slice=Constant(value='table_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ui_order', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='table_id', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='order_fields', ctx=Load()),
                                    slice=Constant(value='customer_count', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ui_order', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='customer_count', kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='order_fields', ctx=Load()),
                                    slice=Constant(value='multiprint_resume', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ui_order', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='multiprint_resume', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='order_fields', ctx=Load()),
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
                    name='_export_for_ui',
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
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PosOrder', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_export_for_ui',
                                    ctx=Load(),
                                ),
                                args=[Name(id='order', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=Constant(value='table_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='order', ctx=Load()),
                                    attr='table_id',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
