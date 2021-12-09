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
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_is_zero', asname=None),
                alias(name='float_compare', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='itertools',
            names=[alias(name='groupby', asname=None)],
            level=0,
        ),
        ClassDef(
            name='StockPicking',
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
                    value=Constant(value='stock.picking', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='pos_session_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='pos.session', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='pos_order_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='pos.order', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_picking_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                            arg(arg='picking_type', annotation=None, type_comment=None),
                            arg(arg='location_id', annotation=None, type_comment=None),
                            arg(arg='location_dest_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='user_id', kind=None),
                                    Constant(value='picking_type_id', kind=None),
                                    Constant(value='move_type', kind=None),
                                    Constant(value='location_id', kind=None),
                                    Constant(value='location_dest_id', kind=None),
                                ],
                                values=[
                                    IfExp(
                                        test=Name(id='partner', ctx=Load()),
                                        body=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    Constant(value=False, kind=None),
                                    Attribute(
                                        value=Name(id='picking_type', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='direct', kind=None),
                                    Name(id='location_id', ctx=Load()),
                                    Name(id='location_dest_id', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_picking_from_pos_order_lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='location_dest_id', annotation=None, type_comment=None),
                            arg(arg='lines', annotation=None, type_comment=None),
                            arg(arg='picking_type', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="We'll create some picking based on order_lines", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='pickings', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.picking', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stockable_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='lines', ctx=Load()),
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
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='l', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        List(
                                                            elts=[
                                                                Constant(value='product', kind=None),
                                                                Constant(value='consu', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Call(
                                                        func=Name(id='float_is_zero', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='l', ctx=Load()),
                                                                attr='qty',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_rounding',
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='l', ctx=Load()),
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
                                operand=Name(id='stockable_lines', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='pickings', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='positive_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stockable_lines', ctx=Load()),
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
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='l', ctx=Load()),
                                                attr='qty',
                                                ctx=Load(),
                                            ),
                                            ops=[Gt()],
                                            comparators=[Constant(value=0, kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='negative_lines', ctx=Store())],
                            value=BinOp(
                                left=Name(id='stockable_lines', ctx=Load()),
                                op=Sub(),
                                right=Name(id='positive_lines', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='positive_lines', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='location_id', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='picking_type', ctx=Load()),
                                            attr='default_location_src_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='positive_picking', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.picking', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_prepare_picking_vals',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='partner', ctx=Load()),
                                                    Name(id='picking_type', ctx=Load()),
                                                    Name(id='location_id', ctx=Load()),
                                                    Name(id='location_dest_id', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='positive_picking', ctx=Load()),
                                            attr='_create_move_from_pos_order_lines',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='positive_lines', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Try(
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
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
                                                            value=Name(id='positive_picking', ctx=Load()),
                                                            attr='_action_done',
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
                                    handlers=[
                                        ExceptHandler(
                                            type=Tuple(
                                                elts=[
                                                    Name(id='UserError', ctx=Load()),
                                                    Name(id='ValidationError', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                AugAssign(
                                    target=Name(id='pickings', ctx=Store()),
                                    op=BitOr(),
                                    value=Name(id='positive_picking', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='negative_lines', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='picking_type', ctx=Load()),
                                        attr='return_picking_type_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='return_picking_type', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='picking_type', ctx=Load()),
                                                attr='return_picking_type_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='return_location_id', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='return_picking_type', ctx=Load()),
                                                    attr='default_location_dest_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='return_picking_type', ctx=Store())],
                                            value=Name(id='picking_type', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='return_location_id', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='picking_type', ctx=Load()),
                                                    attr='default_location_src_id',
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
                                    targets=[Name(id='negative_picking', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.picking', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_prepare_picking_vals',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='partner', ctx=Load()),
                                                    Name(id='return_picking_type', ctx=Load()),
                                                    Name(id='location_dest_id', ctx=Load()),
                                                    Name(id='return_location_id', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='negative_picking', ctx=Load()),
                                            attr='_create_move_from_pos_order_lines',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='negative_lines', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Try(
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
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
                                                            value=Name(id='negative_picking', ctx=Load()),
                                                            attr='_action_done',
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
                                    handlers=[
                                        ExceptHandler(
                                            type=Tuple(
                                                elts=[
                                                    Name(id='UserError', ctx=Load()),
                                                    Name(id='ValidationError', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                AugAssign(
                                    target=Name(id='pickings', ctx=Store()),
                                    op=BitOr(),
                                    value=Name(id='negative_picking', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='pickings', ctx=Load()),
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
                    name='_prepare_stock_move_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='first_line', annotation=None, type_comment=None),
                            arg(arg='order_lines', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='product_uom', kind=None),
                                    Constant(value='picking_id', kind=None),
                                    Constant(value='picking_type_id', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='product_uom_qty', kind=None),
                                    Constant(value='state', kind=None),
                                    Constant(value='location_id', kind=None),
                                    Constant(value='location_dest_id', kind=None),
                                    Constant(value='company_id', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='first_line', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='first_line', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='uom_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='picking_type_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='first_line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='abs', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='order_lines', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='qty', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='draft', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='location_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='location_dest_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
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
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_move_from_pos_order_lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='lines', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='lines_by_product', ctx=Store())],
                            value=Call(
                                func=Name(id='groupby', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[Name(id='lines', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Lambda(
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
                                                        value=Attribute(
                                                            value=Name(id='l', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
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
                                                value=Attribute(
                                                    value=Name(id='l', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='product', ctx=Store()),
                                    Name(id='lines', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='lines_by_product', ctx=Load()),
                            body=[
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
                                            attr='concat',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Name(id='lines', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='first_line', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='order_lines', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='current_move', ctx=Store())],
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
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_prepare_stock_move_vals',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='first_line', ctx=Load()),
                                                    Name(id='order_lines', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='confirmed_moves', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='current_move', ctx=Load()),
                                            attr='_action_confirm',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='move', ctx=Store()),
                                    iter=Name(id='confirmed_moves', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='first_line', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='first_line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tracking',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='none', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='picking_type_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='use_existing_lots',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='picking_type_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='use_create_lots',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        For(
                                                            target=Name(id='line', ctx=Store()),
                                                            iter=Name(id='order_lines', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='sum_of_lots', ctx=Store())],
                                                                    value=Constant(value=0, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                For(
                                                                    target=Name(id='lot', ctx=Store()),
                                                                    iter=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='pack_lot_ids',
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
                                                                                body=Attribute(
                                                                                    value=Name(id='l', ctx=Load()),
                                                                                    attr='lot_name',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    body=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='line', ctx=Load()),
                                                                                        attr='product_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='tracking',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='serial', kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='qty', ctx=Store())],
                                                                                    value=Constant(value=1, kind=None),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Assign(
                                                                                    targets=[Name(id='qty', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Name(id='abs', ctx=Load()),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Name(id='line', ctx=Load()),
                                                                                                attr='qty',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='ml_vals', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='move', ctx=Load()),
                                                                                    attr='_prepare_move_line_vals',
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
                                                                                    value=Name(id='ml_vals', ctx=Load()),
                                                                                    attr='update',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='qty_done', kind=None)],
                                                                                        values=[Name(id='qty', ctx=Load())],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        If(
                                                                            test=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='picking_type_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='use_existing_lots',
                                                                                ctx=Load(),
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='existing_lot', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Subscript(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='env',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                slice=Constant(value='stock.production.lot', kind=None),
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
                                                                                                    Tuple(
                                                                                                        elts=[
                                                                                                            Constant(value='product_id', kind=None),
                                                                                                            Constant(value='=', kind=None),
                                                                                                            Attribute(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='line', ctx=Load()),
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
                                                                                                            Constant(value='name', kind=None),
                                                                                                            Constant(value='=', kind=None),
                                                                                                            Attribute(
                                                                                                                value=Name(id='lot', ctx=Load()),
                                                                                                                attr='lot_name',
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
                                                                                    test=BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            UnaryOp(
                                                                                                op=Not(),
                                                                                                operand=Name(id='existing_lot', ctx=Load()),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='picking_type_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='use_create_lots',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='existing_lot', ctx=Store())],
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Subscript(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='env',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        slice=Constant(value='stock.production.lot', kind=None),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='create',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    Dict(
                                                                                                        keys=[
                                                                                                            Constant(value='company_id', kind=None),
                                                                                                            Constant(value='product_id', kind=None),
                                                                                                            Constant(value='name', kind=None),
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
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='line', ctx=Load()),
                                                                                                                    attr='product_id',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                attr='id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            Attribute(
                                                                                                                value=Name(id='lot', ctx=Load()),
                                                                                                                attr='lot_name',
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
                                                                                    orelse=[],
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='quant', ctx=Store())],
                                                                                    value=Subscript(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='existing_lot', ctx=Load()),
                                                                                                    attr='quant_ids',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='filtered',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Lambda(
                                                                                                    args=arguments(
                                                                                                        posonlyargs=[],
                                                                                                        args=[arg(arg='q', annotation=None, type_comment=None)],
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
                                                                                                                    value=Name(id='q', ctx=Load()),
                                                                                                                    attr='quantity',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                ops=[Gt()],
                                                                                                                comparators=[Constant(value=0.0, kind=None)],
                                                                                                            ),
                                                                                                            Call(
                                                                                                                func=Attribute(
                                                                                                                    value=Attribute(
                                                                                                                        value=Attribute(
                                                                                                                            value=Name(id='q', ctx=Load()),
                                                                                                                            attr='location_id',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        attr='parent_path',
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    attr='startswith',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                args=[
                                                                                                                    Attribute(
                                                                                                                        value=Attribute(
                                                                                                                            value=Name(id='move', ctx=Load()),
                                                                                                                            attr='location_id',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        attr='parent_path',
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                ],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        slice=Slice(
                                                                                            lower=UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=1, kind=None),
                                                                                            ),
                                                                                            upper=None,
                                                                                            step=None,
                                                                                        ),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='ml_vals', ctx=Load()),
                                                                                            attr='update',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='lot_id', kind=None),
                                                                                                    Constant(value='location_id', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='existing_lot', ctx=Load()),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    BoolOp(
                                                                                                        op=Or(),
                                                                                                        values=[
                                                                                                            Attribute(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='quant', ctx=Load()),
                                                                                                                    attr='location_id',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                attr='id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            Attribute(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='move', ctx=Load()),
                                                                                                                    attr='location_id',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                attr='id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='ml_vals', ctx=Load()),
                                                                                            attr='update',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='lot_name', kind=None)],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='lot', ctx=Load()),
                                                                                                        attr='lot_name',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
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
                                                                                        slice=Constant(value='stock.move.line', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='create',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='ml_vals', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        AugAssign(
                                                                            target=Name(id='sum_of_lots', ctx=Store()),
                                                                            op=Add(),
                                                                            value=Name(id='qty', ctx=Load()),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Compare(
                                                                        left=Call(
                                                                            func=Name(id='abs', ctx=Load()),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='qty',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        ops=[NotEq()],
                                                                        comparators=[Name(id='sum_of_lots', ctx=Load())],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='difference_qty', ctx=Store())],
                                                                            value=BinOp(
                                                                                left=Call(
                                                                                    func=Name(id='abs', ctx=Load()),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Name(id='line', ctx=Load()),
                                                                                            attr='qty',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                op=Sub(),
                                                                                right=Name(id='sum_of_lots', ctx=Load()),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='ml_vals', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='current_move', ctx=Load()),
                                                                                    attr='_prepare_move_line_vals',
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
                                                                                    value=Attribute(
                                                                                        value=Name(id='line', ctx=Load()),
                                                                                        attr='product_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='tracking',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='serial', kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='ml_vals', ctx=Load()),
                                                                                            attr='update',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='qty_done', kind=None)],
                                                                                                values=[Constant(value=1, kind=None)],
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                                For(
                                                                                    target=Name(id='i', ctx=Store()),
                                                                                    iter=Call(
                                                                                        func=Name(id='range', ctx=Load()),
                                                                                        args=[
                                                                                            Call(
                                                                                                func=Name(id='int', ctx=Load()),
                                                                                                args=[Name(id='difference_qty', ctx=Load())],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    body=[
                                                                                        Expr(
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Subscript(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='env',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        slice=Constant(value='stock.move.line', kind=None),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='create',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[Name(id='ml_vals', ctx=Load())],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='ml_vals', ctx=Load()),
                                                                                            attr='update',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='qty_done', kind=None)],
                                                                                                values=[Name(id='difference_qty', ctx=Load())],
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
                                                                                                slice=Constant(value='stock.move.line', kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='create',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Name(id='ml_vals', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
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
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='_action_assign',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        For(
                                                            target=Name(id='move_line', ctx=Store()),
                                                            iter=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='move_line_ids',
                                                                ctx=Load(),
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='move_line', ctx=Load()),
                                                                            attr='qty_done',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Attribute(
                                                                        value=Name(id='move_line', ctx=Load()),
                                                                        attr='product_uom_qty',
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Name(id='float_compare', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='product_uom_qty',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='quantity_done',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='precision_rounding',
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='move', ctx=Load()),
                                                                                    attr='product_uom',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='rounding',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='remaining_qty', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='product_uom_qty',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Sub(),
                                                                        right=Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='quantity_done',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='ml_vals', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='_prepare_move_line_vals',
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
                                                                            value=Name(id='ml_vals', ctx=Load()),
                                                                            attr='update',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Dict(
                                                                                keys=[Constant(value='qty_done', kind=None)],
                                                                                values=[Name(id='remaining_qty', ctx=Load())],
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
                                                                                slice=Constant(value='stock.move.line', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='create',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='ml_vals', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='_action_assign',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                For(
                                                    target=Name(id='move_line', ctx=Store()),
                                                    iter=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='move_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='move_line', ctx=Load()),
                                                                    attr='qty_done',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Attribute(
                                                                value=Name(id='move_line', ctx=Load()),
                                                                attr='product_uom_qty',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Name(id='float_compare', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='product_uom_qty',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='quantity_done',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[
                                                                keyword(
                                                                    arg='precision_rounding',
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='product_uom',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='rounding',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='remaining_qty', ctx=Store())],
                                                            value=BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='product_uom_qty',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Sub(),
                                                                right=Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='quantity_done',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='ml_vals', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='_prepare_move_line_vals',
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
                                                                    value=Name(id='ml_vals', ctx=Load()),
                                                                    attr='update',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[Constant(value='qty_done', kind=None)],
                                                                        values=[Name(id='remaining_qty', ctx=Load())],
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
                                                                        slice=Constant(value='stock.move.line', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='ml_vals', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='quantity_done',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='product_uom_qty',
                                                        ctx=Load(),
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
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_send_confirmation_email',
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
                            targets=[Name(id='pickings', ctx=Store())],
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
                                            args=[arg(arg='p', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='p', ctx=Load()),
                                                attr='picking_type_id',
                                                ctx=Load(),
                                            ),
                                            ops=[NotEq()],
                                            comparators=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='p', ctx=Load()),
                                                            attr='picking_type_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='warehouse_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pos_type_id',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockPicking', ctx=Load()),
                                            Name(id='pickings', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_send_confirmation_email',
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ProcurementGroup',
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
                    value=Constant(value='procurement.group', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='pos_order_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='pos.order', kind=None),
                            Constant(value='POS Order', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='StockMove',
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
                    value=Constant(value='stock.move', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_new_picking_values',
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
                            targets=[Name(id='vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockMove', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_new_picking_values',
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
                                    value=Name(id='vals', ctx=Load()),
                                    slice=Constant(value='pos_session_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mapped',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='group_id.pos_order_id.session_id', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='vals', ctx=Load()),
                                    slice=Constant(value='pos_order_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mapped',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='group_id.pos_order_id', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='vals', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_key_assign_picking',
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
                            targets=[Name(id='keys', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockMove', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_key_assign_picking',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Name(id='keys', ctx=Load()),
                                op=Add(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='group_id',
                                                ctx=Load(),
                                            ),
                                            attr='pos_order_id',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
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
