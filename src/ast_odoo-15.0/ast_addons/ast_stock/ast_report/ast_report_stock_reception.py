Module(
    body=[
        ImportFrom(
            module='collections',
            names=[
                alias(name='defaultdict', asname=None),
                alias(name='OrderedDict', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_compare', asname=None),
                alias(name='float_is_zero', asname=None),
                alias(name='format_date', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ReceptionReport',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='report.stock.report_reception', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Stock Reception Report', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_report_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='docids', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' This report is flexibly designed to work with both individual and batch pickings.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='docids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='default_picking_ids', kind=None),
                                    Name(id='docids', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pickings', ctx=Store())],
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='docids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='picking_type_code', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value='outgoing', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value='cancel', kind=None),
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
                        Assign(
                            targets=[Name(id='picking_states', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pickings', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='state', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='pickings', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='msg', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='No transfers selected or a delivery order selected', kind=None)],
                                        keywords=[],
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
                                                left=Constant(value='done', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='picking_states', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Name(id='set', ctx=Load()),
                                                            args=[Name(id='picking_states', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='pickings', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='This report cannot be used for done and not done transfers at the same time', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='pickings', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='pickings', kind=None),
                                            Constant(value='reason', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Name(id='msg', ctx=Load()),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='product_to_qty_draft', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='float', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_to_qty_to_assign', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_to_total_assigned', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=List(
                                            elts=[
                                                Constant(value=0.0, kind=None),
                                                List(elts=[], ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='pickings', ctx=Load()),
                                        attr='move_lines',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='m', annotation=None, type_comment=None)],
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
                                                            value=Name(id='m', ctx=Load()),
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
                                                        value=Name(id='m', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[Constant(value='cancel', kind=None)],
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
                            targets=[Name(id='assigned_moves', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_lines', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='move_dest_ids', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_to_assigned_qty', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='float', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='assigned', ctx=Store()),
                            iter=Name(id='assigned_moves', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='product_to_assigned_qty', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='assigned', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Attribute(
                                        value=Name(id='assigned', ctx=Load()),
                                        attr='product_qty',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='move_lines', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='qty_already_assigned', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='move_dest_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='qty_already_assigned', ctx=Store())],
                                            value=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='product_to_assigned_qty', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='product_qty',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='product_to_assigned_qty', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Store(),
                                            ),
                                            op=Sub(),
                                            value=Name(id='qty_already_assigned', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='qty_already_assigned', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Subscript(
                                                    value=Name(id='product_to_total_assigned', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Name(id='qty_already_assigned', ctx=Load()),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='product_to_total_assigned', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='move', ctx=Load()),
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
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='qty_already_assigned', ctx=Load())],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='draft', kind=None)],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='product_to_qty_draft', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='product_qty',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Name(id='qty_already_assigned', ctx=Load()),
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='quantity_to_assign', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='product_qty',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='picking_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='immediate_transfer',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='quantity_to_assign', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='move', ctx=Load()),
                                                                        attr='product_uom',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='_compute_quantity',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='move', ctx=Load()),
                                                                        attr='quantity_done',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='move', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='uom_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='rounding_method',
                                                                        value=Constant(value='HALF-UP', kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='product_to_qty_to_assign', ctx=Load()),
                                                                slice=Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    BinOp(
                                                                        left=Name(id='quantity_to_assign', ctx=Load()),
                                                                        op=Sub(),
                                                                        right=Name(id='qty_already_assigned', ctx=Load()),
                                                                    ),
                                                                    Name(id='move', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                        Assign(
                            targets=[Name(id='warehouse', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Subscript(
                                        value=Name(id='pickings', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='picking_type_id',
                                    ctx=Load(),
                                ),
                                attr='warehouse_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='wh_location_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.location', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='child_of', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='warehouse', ctx=Load()),
                                                            attr='view_location_id',
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
                                                    Constant(value='usage', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value='supplier', kind=None),
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
                        Assign(
                            targets=[Name(id='allowed_states', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='confirmed', kind=None),
                                    Constant(value='partially_available', kind=None),
                                    Constant(value='waiting', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='done', kind=None),
                                ops=[In()],
                                comparators=[Name(id='picking_states', ctx=Load())],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='allowed_states', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[Constant(value='assigned', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='outs', ctx=Store())],
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
                                                    Constant(value='state', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='allowed_states', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='product_qty', kind=None),
                                                    Constant(value='>', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='location_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='wh_location_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='move_orig_ids', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='picking_id', kind=None),
                                                    Constant(value='not in', kind=None),
                                                    Attribute(
                                                        value=Name(id='pickings', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    ListComp(
                                                        elt=Attribute(
                                                            value=Name(id='p', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='p', ctx=Store()),
                                                                iter=BinOp(
                                                                    left=Call(
                                                                        func=Name(id='list', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='product_to_qty_to_assign', ctx=Load()),
                                                                                    attr='keys',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    op=Add(),
                                                                    right=Call(
                                                                        func=Name(id='list', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='product_to_qty_draft', ctx=Load()),
                                                                                    attr='keys',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
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
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='reservation_date, priority desc, date, id', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='products_to_outs', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='out', ctx=Store()),
                            iter=Name(id='outs', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='products_to_outs', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='out', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='out', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sources_to_lines', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='product_id', ctx=Store()),
                                    Name(id='outs', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='products_to_outs', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='out', ctx=Store()),
                                    iter=Name(id='outs', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='source', ctx=Store())],
                                            value=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='out', ctx=Load()),
                                                            attr='_get_source_document',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='source', ctx=Load()),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='out', ctx=Load()),
                                                        attr='picking_id',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='source', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='out', ctx=Load()),
                                                                attr='picking_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='source', ctx=Store())],
                                                    value=Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='out', ctx=Load()),
                                                                attr='picking_id',
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='source', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='qty_to_reserve', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='out', ctx=Load()),
                                                attr='product_qty',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='product_uom', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='out', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='uom_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Constant(value='done', kind=None),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='picking_states', ctx=Load())],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='out', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='partially_available', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='qty_to_reserve', ctx=Store()),
                                                    op=Sub(),
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='out', ctx=Load()),
                                                                attr='product_uom',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_compute_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='out', ctx=Load()),
                                                                attr='reserved_availability',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='product_uom', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='moves_in_ids', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='qty_done', ctx=Store())],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='move_in_qty', ctx=Store()),
                                                    Name(id='move_in', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Subscript(
                                                value=Name(id='product_to_qty_to_assign', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='out', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='moves_in_ids', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='move_in', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Name(id='float_compare', ctx=Load()),
                                                            args=[
                                                                BinOp(
                                                                    left=Name(id='qty_done', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Name(id='move_in_qty', ctx=Load()),
                                                                ),
                                                                Name(id='qty_to_reserve', ctx=Load()),
                                                            ],
                                                            keywords=[
                                                                keyword(
                                                                    arg='precision_rounding',
                                                                    value=Attribute(
                                                                        value=Name(id='product_uom', ctx=Load()),
                                                                        attr='rounding',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        ops=[LtE()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='qty_to_add', ctx=Store())],
                                                            value=Name(id='move_in_qty', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='move_in_qty', ctx=Store())],
                                                            value=Constant(value=0, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='qty_to_add', ctx=Store())],
                                                            value=BinOp(
                                                                left=Name(id='qty_to_reserve', ctx=Load()),
                                                                op=Sub(),
                                                                right=Name(id='qty_done', ctx=Load()),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='move_in_qty', ctx=Store()),
                                                            op=Sub(),
                                                            value=Name(id='qty_to_add', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                                AugAssign(
                                                    target=Name(id='qty_done', ctx=Store()),
                                                    op=Add(),
                                                    value=Name(id='qty_to_add', ctx=Load()),
                                                ),
                                                If(
                                                    test=Name(id='move_in_qty', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='product_to_qty_to_assign', ctx=Load()),
                                                                        slice=Attribute(
                                                                            value=Name(id='out', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Tuple(
                                                                elts=[
                                                                    Name(id='move_in_qty', ctx=Load()),
                                                                    Name(id='move_in', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='product_to_qty_to_assign', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='out', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='product_to_qty_to_assign', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='out', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Slice(
                                                                    lower=Constant(value=1, kind=None),
                                                                    upper=None,
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Name(id='float_compare', ctx=Load()),
                                                            args=[
                                                                Name(id='qty_to_reserve', ctx=Load()),
                                                                Name(id='qty_done', ctx=Load()),
                                                            ],
                                                            keywords=[
                                                                keyword(
                                                                    arg='precision_rounding',
                                                                    value=Attribute(
                                                                        value=Name(id='product_uom', ctx=Load()),
                                                                        attr='rounding',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    body=[Break()],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='float_is_zero', ctx=Load()),
                                                    args=[Name(id='qty_done', ctx=Load())],
                                                    keywords=[
                                                        keyword(
                                                            arg='precision_rounding',
                                                            value=Attribute(
                                                                value=Name(id='product_uom', ctx=Load()),
                                                                attr='rounding',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='sources_to_lines', ctx=Load()),
                                                                slice=Name(id='source', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_prepare_report_line',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='qty_done', ctx=Load()),
                                                                    Name(id='product_id', ctx=Load()),
                                                                    Name(id='out', ctx=Load()),
                                                                    Subscript(
                                                                        value=Name(id='source', ctx=Load()),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='move_ins',
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
                                                                                attr='browse',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='moves_in_ids', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='qty_expected', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='product_to_qty_draft', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='product_id', ctx=Load()),
                                                    Constant(value=0, kind=None),
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
                                                        left=Call(
                                                            func=Name(id='float_compare', ctx=Load()),
                                                            args=[
                                                                Name(id='qty_to_reserve', ctx=Load()),
                                                                Name(id='qty_done', ctx=Load()),
                                                            ],
                                                            keywords=[
                                                                keyword(
                                                                    arg='precision_rounding',
                                                                    value=Attribute(
                                                                        value=Name(id='product_uom', ctx=Load()),
                                                                        attr='rounding',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Name(id='float_is_zero', ctx=Load()),
                                                            args=[Name(id='qty_expected', ctx=Load())],
                                                            keywords=[
                                                                keyword(
                                                                    arg='precision_rounding',
                                                                    value=Attribute(
                                                                        value=Name(id='product_uom', ctx=Load()),
                                                                        attr='rounding',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='to_expect', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='min', ctx=Load()),
                                                        args=[
                                                            Name(id='qty_expected', ctx=Load()),
                                                            BinOp(
                                                                left=Name(id='qty_to_reserve', ctx=Load()),
                                                                op=Sub(),
                                                                right=Name(id='qty_done', ctx=Load()),
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
                                                                value=Name(id='sources_to_lines', ctx=Load()),
                                                                slice=Name(id='source', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_prepare_report_line',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='to_expect', ctx=Load()),
                                                                    Name(id='product_id', ctx=Load()),
                                                                    Name(id='out', ctx=Load()),
                                                                    Subscript(
                                                                        value=Name(id='source', ctx=Load()),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='is_qty_assignable',
                                                                        value=Constant(value=False, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='product_to_qty_draft', ctx=Load()),
                                                        slice=Name(id='product_id', ctx=Load()),
                                                        ctx=Store(),
                                                    ),
                                                    op=Sub(),
                                                    value=Name(id='to_expect', ctx=Load()),
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
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='product_id', ctx=Store()),
                                    Name(id='qty_and_ins', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='product_to_total_assigned', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='total_assigned', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='qty_and_ins', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='moves_in', ctx=Store())],
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
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='qty_and_ins', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='out_moves', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='moves_in', ctx=Load()),
                                        attr='move_dest_ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='out_move', ctx=Store()),
                                    iter=Name(id='out_moves', ctx=Load()),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='float_is_zero', ctx=Load()),
                                                args=[Name(id='total_assigned', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_rounding',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='out_move', ctx=Load()),
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
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='source', ctx=Store())],
                                            value=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='out_move', ctx=Load()),
                                                            attr='_get_source_document',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='source', ctx=Load()),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='out_move', ctx=Load()),
                                                        attr='picking_id',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='source', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='out_move', ctx=Load()),
                                                                attr='picking_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='source', ctx=Store())],
                                                    value=Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='out_move', ctx=Load()),
                                                                attr='picking_id',
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='source', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='qty_assigned', ctx=Store())],
                                            value=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    Name(id='total_assigned', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='out_move', ctx=Load()),
                                                        attr='product_qty',
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
                                                    value=Subscript(
                                                        value=Name(id='sources_to_lines', ctx=Load()),
                                                        slice=Name(id='source', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_prepare_report_line',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='qty_assigned', ctx=Load()),
                                                            Name(id='product_id', ctx=Load()),
                                                            Name(id='out_move', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='source', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='is_assigned',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='move_ins',
                                                                value=Name(id='moves_in', ctx=Load()),
                                                            ),
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
                        Assign(
                            targets=[Name(id='sources_to_formatted_scheduled_date', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='source', ctx=Store()),
                                    Name(id='dummy', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='sources_to_lines', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='sources_to_formatted_scheduled_date', ctx=Load()),
                                            slice=Name(id='source', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_formatted_scheduled_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='source', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
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
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='data', kind=None),
                                    Constant(value='doc_ids', kind=None),
                                    Constant(value='doc_model', kind=None),
                                    Constant(value='sources_to_lines', kind=None),
                                    Constant(value='precision', kind=None),
                                    Constant(value='pickings', kind=None),
                                    Constant(value='sources_to_formatted_scheduled_date', kind=None),
                                ],
                                values=[
                                    Name(id='data', ctx=Load()),
                                    Name(id='docids', ctx=Load()),
                                    Constant(value='stock.picking', kind=None),
                                    Name(id='sources_to_lines', ctx=Load()),
                                    Call(
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
                                    Name(id='pickings', ctx=Load()),
                                    Name(id='sources_to_formatted_scheduled_date', ctx=Load()),
                                ],
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
                    name='_prepare_report_line',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='quantity', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
                            arg(arg='move_out', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                            arg(arg='is_assigned', annotation=None, type_comment=None),
                            arg(arg='is_qty_assignable', annotation=None, type_comment=None),
                            arg(arg='move_ins', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='source', kind=None),
                                    Constant(value='product', kind=None),
                                    Constant(value='uom', kind=None),
                                    Constant(value='quantity', kind=None),
                                    Constant(value='is_qty_assignable', kind=None),
                                    Constant(value='move_out', kind=None),
                                    Constant(value='is_assigned', kind=None),
                                    Constant(value='move_ins', kind=None),
                                ],
                                values=[
                                    Name(id='source', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='id', kind=None),
                                            Constant(value='display_name', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='uom_id',
                                            ctx=Load(),
                                        ),
                                        attr='display_name',
                                        ctx=Load(),
                                    ),
                                    Name(id='quantity', ctx=Load()),
                                    Name(id='is_qty_assignable', ctx=Load()),
                                    Name(id='move_out', ctx=Load()),
                                    Name(id='is_assigned', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='move_ins', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='move_ins', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=False, kind=None),
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
                    name='_get_formatted_scheduled_date',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Unfortunately different source record types have different field names for their "Scheduled Date"\n        Therefore an extendable method is needed.\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='source', ctx=Load()),
                                    attr='_name',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='stock.picking', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='format_date', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='source', ctx=Load()),
                                                attr='scheduled_date',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_assign',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='move_ids', annotation=None, type_comment=None),
                            arg(arg='qtys', annotation=None, type_comment=None),
                            arg(arg='in_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Assign picking move(s) [i.e. link] to other moves (i.e. make them MTO)\n        :param move_id ids: the ids of the moves to make MTO\n        :param qtys list: the quantities that are being assigned to the move_ids (in same order as move_ids)\n        :param in_ids ids: the ids of the moves that are to be assigned to move_ids\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='outs', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='move_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='out_to_new_out', ctx=Store())],
                            value=Call(
                                func=Name(id='OrderedDict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_move_vals', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='out', ctx=Store()),
                                    Name(id='qty_to_link', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='outs', ctx=Load()),
                                    Name(id='qtys', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='float_compare', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='out', ctx=Load()),
                                                    attr='product_qty',
                                                    ctx=Load(),
                                                ),
                                                Name(id='qty_to_link', ctx=Load()),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='precision_rounding',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='out', ctx=Load()),
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
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='new_move_vals', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='out', ctx=Load()),
                                                    attr='_split',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='out', ctx=Load()),
                                                            attr='product_qty',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Name(id='qty_to_link', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='out_to_new_out', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='out', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.move', kind=None),
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
                        Assign(
                            targets=[Name(id='new_outs', ctx=Store())],
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
                                args=[Name(id='new_move_vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='new_outs', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='confirmed', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='i', ctx=Store()),
                                    Name(id='k', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='out_to_new_out', ctx=Load()),
                                            attr='keys',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='out_to_new_out', ctx=Load()),
                                            slice=Name(id='k', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='new_outs', ctx=Load()),
                                        slice=Name(id='i', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='out', ctx=Store()),
                                    Name(id='qty_to_link', ctx=Store()),
                                    Name(id='ins', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='outs', ctx=Load()),
                                    Name(id='qtys', ctx=Load()),
                                    Name(id='in_ids', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='potential_ins', ctx=Store())],
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
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ins', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='out', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='out_to_new_out', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='new_out', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='out_to_new_out', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='out', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='potential_ins', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='done', kind=None)],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='out', ctx=Load()),
                                                        attr='reserved_availability',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='out', ctx=Load()),
                                                                attr='move_line_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='move_id',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='new_out', ctx=Load()),
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
                                                                    value=Subscript(
                                                                        value=Name(id='potential_ins', ctx=Load()),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='state',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='done', kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='out', ctx=Load()),
                                                                    attr='reserved_availability',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Name(id='qty_to_link', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='out', ctx=Load()),
                                                                        attr='move_line_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='move_id',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='new_out', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='assigned_amount', ctx=Store())],
                                                            value=Constant(value=0, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        For(
                                                            target=Name(id='move_line_id', ctx=Store()),
                                                            iter=Attribute(
                                                                value=Name(id='new_out', ctx=Load()),
                                                                attr='move_line_ids',
                                                                ctx=Load(),
                                                            ),
                                                            body=[
                                                                If(
                                                                    test=Compare(
                                                                        left=BinOp(
                                                                            left=Name(id='assigned_amount', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Attribute(
                                                                                value=Name(id='move_line_id', ctx=Load()),
                                                                                attr='product_qty',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                        ops=[Gt()],
                                                                        comparators=[Name(id='qty_to_link', ctx=Load())],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='new_move_line', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='move_line_id', ctx=Load()),
                                                                                    attr='copy',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='product_uom_qty', kind=None),
                                                                                            Constant(value='qty_done', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=0, kind=None),
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
                                                                                    value=Name(id='new_move_line', ctx=Load()),
                                                                                    attr='product_uom_qty',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Attribute(
                                                                                value=Name(id='move_line_id', ctx=Load()),
                                                                                attr='product_uom_qty',
                                                                                ctx=Load(),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='move_line_id', ctx=Load()),
                                                                                    attr='product_uom_qty',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='out', ctx=Load()),
                                                                                            attr='product_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='uom_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='_compute_quantity',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Name(id='qty_to_link', ctx=Load()),
                                                                                        op=Sub(),
                                                                                        right=Name(id='assigned_amount', ctx=Load()),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='out', ctx=Load()),
                                                                                        attr='product_uom',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='rounding_method',
                                                                                        value=Constant(value='HALF-UP', kind=None),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        AugAssign(
                                                                            target=Attribute(
                                                                                value=Name(id='new_move_line', ctx=Load()),
                                                                                attr='product_uom_qty',
                                                                                ctx=Store(),
                                                                            ),
                                                                            op=Sub(),
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='out', ctx=Load()),
                                                                                            attr='product_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='uom_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='_compute_quantity',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='move_line_id', ctx=Load()),
                                                                                        attr='product_qty',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='out', ctx=Load()),
                                                                                        attr='product_uom',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='rounding_method',
                                                                                        value=Constant(value='HALF-UP', kind=None),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='move_line_id', ctx=Load()),
                                                                            attr='move_id',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Name(id='out', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                                AugAssign(
                                                                    target=Name(id='assigned_amount', ctx=Store()),
                                                                    op=Add(),
                                                                    value=Attribute(
                                                                        value=Name(id='move_line_id', ctx=Load()),
                                                                        attr='product_qty',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                If(
                                                                    test=Compare(
                                                                        left=Call(
                                                                            func=Name(id='float_compare', ctx=Load()),
                                                                            args=[
                                                                                Name(id='assigned_amount', ctx=Load()),
                                                                                Name(id='qty_to_link', ctx=Load()),
                                                                            ],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='precision_rounding',
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='out', ctx=Load()),
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
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value=0, kind=None)],
                                                                    ),
                                                                    body=[Break()],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='in_move', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='reversed', ctx=Load()),
                                        args=[Name(id='potential_ins', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='quantity_remaining', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='in_move', ctx=Load()),
                                                    attr='product_qty',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Call(
                                                    func=Name(id='sum', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='in_move', ctx=Load()),
                                                                    attr='move_dest_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='mapped',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='product_qty', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='in_move', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='out', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='float_compare', ctx=Load()),
                                                            args=[
                                                                Constant(value=0, kind=None),
                                                                Name(id='quantity_remaining', ctx=Load()),
                                                            ],
                                                            keywords=[
                                                                keyword(
                                                                    arg='precision_rounding',
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='in_move', ctx=Load()),
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
                                                        ops=[GtE()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='potential_ins', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='potential_ins', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Constant(value=1, kind=None),
                                                            upper=None,
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='linked_qty', ctx=Store())],
                                            value=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='in_move', ctx=Load()),
                                                        attr='product_qty',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='qty_to_link', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='in_move', ctx=Load()),
                                                attr='move_dest_ids',
                                                ctx=Store(),
                                            ),
                                            op=BitOr(),
                                            value=Name(id='out', ctx=Load()),
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='out', ctx=Load()),
                                                    attr='procure_method',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='make_to_order', kind=None),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='quantity_remaining', ctx=Store()),
                                            op=Sub(),
                                            value=Name(id='linked_qty', ctx=Load()),
                                        ),
                                        AugAssign(
                                            target=Name(id='qty_to_link', ctx=Store()),
                                            op=Sub(),
                                            value=Name(id='linked_qty', ctx=Load()),
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='float_is_zero', ctx=Load()),
                                                args=[Name(id='qty_to_link', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_rounding',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='out', ctx=Load()),
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
                                            body=[Break()],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=BinOp(
                                        left=Name(id='outs', ctx=Load()),
                                        op=BitOr(),
                                        right=Name(id='new_outs', ctx=Load()),
                                    ),
                                    attr='_recompute_state',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
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
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='move_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='_action_assign',
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
                    name='action_unassign',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='move_id', annotation=None, type_comment=None),
                            arg(arg='qty', annotation=None, type_comment=None),
                            arg(arg='in_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Unassign moves [i.e. unlink] from a move (i.e. make non-MTO)\n        :param move_id id: the id of the move to make non-MTO\n        :param qty float: the total quantity that is being unassigned from move_id\n        :param in_ids ids: the ids of the moves that are to be unassigned from move_id\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='out', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='move_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ins', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='in_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='amount_unassigned', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='in_move', ctx=Store()),
                            iter=Name(id='ins', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='out', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='in_move', ctx=Load()),
                                                    attr='move_dest_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='in_move', ctx=Load()),
                                        attr='move_dest_ids',
                                        ctx=Store(),
                                    ),
                                    op=Sub(),
                                    value=Name(id='out', ctx=Load()),
                                ),
                                AugAssign(
                                    target=Name(id='amount_unassigned', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Name(id='min', ctx=Load()),
                                        args=[
                                            Name(id='qty', ctx=Load()),
                                            Attribute(
                                                value=Name(id='in_move', ctx=Load()),
                                                attr='product_qty',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='float_compare', ctx=Load()),
                                            args=[
                                                Name(id='qty', ctx=Load()),
                                                Name(id='amount_unassigned', ctx=Load()),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='precision_rounding',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='out', ctx=Load()),
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
                                        ops=[LtE()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='out', ctx=Load()),
                                attr='move_orig_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='new_move_vals', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='out', ctx=Load()),
                                            attr='_split',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='amount_unassigned', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='new_move_vals', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='new_move_vals', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='procure_method', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='make_to_order', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='new_out', ctx=Store())],
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
                                                args=[Name(id='new_move_vals', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='new_out', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='state', kind=None)],
                                                        values=[Constant(value='confirmed', kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='out', ctx=Load()),
                                                        attr='move_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='move_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='new_out', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=BinOp(
                                                        left=Name(id='out', ctx=Load()),
                                                        op=BitOr(),
                                                        right=Name(id='new_out', ctx=Load()),
                                                    ),
                                                    attr='_compute_reserved_availability',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='new_out', ctx=Load()),
                                                    attr='reserved_availability',
                                                    ctx=Load(),
                                                ),
                                                ops=[Gt()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='new_out', ctx=Load()),
                                                        attr='product_qty',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='reserved_amount_to_remain', ctx=Store())],
                                                    value=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='new_out', ctx=Load()),
                                                            attr='reserved_availability',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Attribute(
                                                            value=Name(id='new_out', ctx=Load()),
                                                            attr='product_qty',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='move_line_id', ctx=Store()),
                                                    iter=Attribute(
                                                        value=Name(id='new_out', ctx=Load()),
                                                        attr='move_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='reserved_amount_to_remain', ctx=Load()),
                                                                ops=[LtE()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                            body=[Break()],
                                                            orelse=[],
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='move_line_id', ctx=Load()),
                                                                    attr='product_qty',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Name(id='reserved_amount_to_remain', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='new_move_line', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='move_line_id', ctx=Load()),
                                                                            attr='copy',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='product_uom_qty', kind=None),
                                                                                    Constant(value='qty_done', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=0, kind=None),
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
                                                                            value=Name(id='new_move_line', ctx=Load()),
                                                                            attr='product_uom_qty',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='out', ctx=Load()),
                                                                                    attr='product_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='uom_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='_compute_quantity',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Name(id='move_line_id', ctx=Load()),
                                                                                    attr='product_qty',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Sub(),
                                                                                right=Name(id='reserved_amount_to_remain', ctx=Load()),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='move_line_id', ctx=Load()),
                                                                                attr='product_uom_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='rounding_method',
                                                                                value=Constant(value='HALF-UP', kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                AugAssign(
                                                                    target=Attribute(
                                                                        value=Name(id='move_line_id', ctx=Load()),
                                                                        attr='product_uom_qty',
                                                                        ctx=Store(),
                                                                    ),
                                                                    op=Sub(),
                                                                    value=Attribute(
                                                                        value=Name(id='new_move_line', ctx=Load()),
                                                                        attr='product_uom_qty',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='new_move_line', ctx=Load()),
                                                                            attr='move_id',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Name(id='out', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                                Break(),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='move_line_id', ctx=Load()),
                                                                            attr='move_id',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Name(id='out', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                                AugAssign(
                                                                    target=Name(id='reserved_amount_to_remain', ctx=Store()),
                                                                    op=Sub(),
                                                                    value=Attribute(
                                                                        value=Name(id='move_line_id', ctx=Load()),
                                                                        attr='product_qty',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=BinOp(
                                                                left=Name(id='out', ctx=Load()),
                                                                op=BitOr(),
                                                                right=Name(id='new_out', ctx=Load()),
                                                            ),
                                                            attr='_compute_reserved_availability',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='out', ctx=Load()),
                                                    attr='move_orig_ids',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='new_out', ctx=Load()),
                                                    attr='_recompute_state',
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
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='out', ctx=Load()),
                                    attr='procure_method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='make_to_stock', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='out', ctx=Load()),
                                    attr='_recompute_state',
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
    ],
    type_ignores=[],
)
