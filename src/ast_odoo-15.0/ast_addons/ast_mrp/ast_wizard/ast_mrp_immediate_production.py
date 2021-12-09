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
            names=[alias(name='float_compare', asname=None)],
            level=0,
        ),
        ClassDef(
            name='MrpImmediateProductionLine',
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
                    value=Constant(value='mrp.immediate.production.line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Immediate Production Line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='immediate_production_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mrp.immediate.production', kind=None),
                            Constant(value='Immediate Production', kind=None),
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
                    targets=[Name(id='production_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mrp.production', kind=None),
                            Constant(value='Production', kind=None),
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
                    targets=[Name(id='to_immediate', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='To Process', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='MrpImmediateProduction',
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
                    value=Constant(value='mrp.immediate.production', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Immediate Production', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
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
                                args=[Name(id='fields', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='immediate_production_line_ids', kind=None),
                                ops=[In()],
                                comparators=[Name(id='fields', ctx=Load())],
                            ),
                            body=[
                                If(
                                    test=Call(
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
                                        args=[Constant(value='default_mo_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='mo_ids', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='default_mo_ids', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='immediate_production_line_ids', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='to_immediate', kind=None),
                                                                Constant(value='production_id', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=True, kind=None),
                                                                Subscript(
                                                                    value=Name(id='mo_id', ctx=Load()),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='mo_id', ctx=Store()),
                                                        iter=Subscript(
                                                            value=Name(id='res', ctx=Load()),
                                                            slice=Constant(value='mo_ids', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
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
                    targets=[Name(id='mo_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mrp.production', kind=None),
                            Constant(value='mrp_production_production_rel', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='show_productions', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_show_production', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='immediate_production_line_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mrp.immediate.production.line', kind=None),
                            Constant(value='immediate_production_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Immediate Production Lines', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_show_production',
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
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='show_productions',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='wizard', ctx=Load()),
                                                        attr='immediate_production_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='production_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
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
                            args=[Constant(value='immediate_production_line_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='process',
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
                            targets=[Name(id='productions_to_do', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='mrp.production', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='productions_not_to_do', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='mrp.production', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='immediate_production_line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='to_immediate',
                                            ctx=Load(),
                                        ),
                                        ops=[Is()],
                                        comparators=[Constant(value=True, kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='productions_to_do', ctx=Store()),
                                            op=BitOr(),
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='production_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        AugAssign(
                                            target=Name(id='productions_not_to_do', ctx=Store()),
                                            op=BitOr(),
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='production_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='production', ctx=Store()),
                            iter=Name(id='productions_to_do', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='error_msg', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='production', ctx=Load()),
                                                    attr='product_tracking',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='lot', kind=None),
                                                            Constant(value='serial', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='production', ctx=Load()),
                                                    attr='lot_producing_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='production', ctx=Load()),
                                                    attr='action_generate_serial',
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
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='production', ctx=Load()),
                                                    attr='product_tracking',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='serial', kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='float_compare', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='production', ctx=Load()),
                                                            attr='qty_producing',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value=1, kind=None),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='precision_rounding',
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='production', ctx=Load()),
                                                                    attr='product_uom_id',
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
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='production', ctx=Load()),
                                                    attr='qty_producing',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=1, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='production', ctx=Load()),
                                                    attr='qty_producing',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='production', ctx=Load()),
                                                    attr='product_qty',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Attribute(
                                                    value=Name(id='production', ctx=Load()),
                                                    attr='qty_produced',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='production', ctx=Load()),
                                            attr='_set_qty_producing',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='move', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='production', ctx=Load()),
                                                attr='move_raw_ids',
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
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='m', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotIn()],
                                                    comparators=[
                                                        List(
                                                            elts=[
                                                                Constant(value='done', kind=None),
                                                                Constant(value='cancel', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
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
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='product_uom',
                                                    ctx=Load(),
                                                ),
                                                attr='rounding',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='move_line', ctx=Store()),
                                            iter=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='move_line_ids',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                If(
                                                    test=Attribute(
                                                        value=Name(id='move_line', ctx=Load()),
                                                        attr='product_uom_qty',
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
                                                            value=Call(
                                                                func=Name(id='min', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='move_line', ctx=Load()),
                                                                        attr='product_uom_qty',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='move_line', ctx=Load()),
                                                                            attr='move_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='should_consume_qty',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Name(id='float_compare', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='quantity_done',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='should_consume_qty',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[
                                                                keyword(
                                                                    arg='precision_rounding',
                                                                    value=Name(id='rounding', ctx=Load()),
                                                                ),
                                                            ],
                                                        ),
                                                        ops=[GtE()],
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
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='has_tracking',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='serial', kind=None),
                                                                    Constant(value='lot', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='error_msg', ctx=Store()),
                                                            op=Add(),
                                                            value=BinOp(
                                                                left=Constant(value='\n  - %s', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='move', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='display_name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
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
                                    test=Name(id='error_msg', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='error_msg', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='You need to supply Lot/Serial Number for products:', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Name(id='error_msg', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[Name(id='error_msg', ctx=Load())],
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
                        Assign(
                            targets=[Name(id='productions_to_validate', ctx=Store())],
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
                                args=[Constant(value='button_mark_done_production_ids', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='productions_to_validate', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='productions_to_validate', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mrp.production', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='productions_to_validate', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='productions_to_validate', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='productions_to_validate', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='productions_not_to_do', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='productions_to_validate', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='skip_immediate',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='button_mark_done',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
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
