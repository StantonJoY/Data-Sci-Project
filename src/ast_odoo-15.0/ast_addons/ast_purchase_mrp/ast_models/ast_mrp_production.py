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
        ClassDef(
            name='MrpProduction',
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
                    value=Constant(value='mrp.production', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='purchase_order_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Count of generated PO', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_purchase_order_count', kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='purchase.group_purchase_user', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_purchase_order_count',
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
                            target=Name(id='production', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='production', ctx=Load()),
                                            attr='purchase_order_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='production', ctx=Load()),
                                                                attr='procurement_group_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='stock_move_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='created_purchase_line_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='order_id',
                                                    ctx=Load(),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='production', ctx=Load()),
                                                                    attr='procurement_group_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='stock_move_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='move_orig_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='purchase_line_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='order_id',
                                                    ctx=Load(),
                                                ),
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
                            args=[
                                Constant(value='procurement_group_id.stock_move_ids.created_purchase_line_id.order_id', kind=None),
                                Constant(value='procurement_group_id.stock_move_ids.move_orig_ids.purchase_line_id.order_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_view_purchase_orders',
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
                            targets=[Name(id='purchase_order_ids', ctx=Store())],
                            value=Attribute(
                                value=BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='procurement_group_id',
                                                    ctx=Load(),
                                                ),
                                                attr='stock_move_ids',
                                                ctx=Load(),
                                            ),
                                            attr='created_purchase_line_id',
                                            ctx=Load(),
                                        ),
                                        attr='order_id',
                                        ctx=Load(),
                                    ),
                                    op=BitOr(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='procurement_group_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='stock_move_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='move_orig_ids',
                                                ctx=Load(),
                                            ),
                                            attr='purchase_line_id',
                                            ctx=Load(),
                                        ),
                                        attr='order_id',
                                        ctx=Load(),
                                    ),
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='res_model', kind=None),
                                    Constant(value='type', kind=None),
                                ],
                                values=[
                                    Constant(value='purchase.order', kind=None),
                                    Constant(value='ir.actions.act_window', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='purchase_order_ids', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='action', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='view_mode', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='form', kind=None),
                                                    Subscript(
                                                        value=Name(id='purchase_order_ids', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
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
                                            value=Name(id='action', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='domain', kind=None),
                                                    Constant(value='view_mode', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='Purchase Order generated from %s', kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Name(id='purchase_order_ids', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='tree,form', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_document_iterate_key',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='move_raw_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='iterate_key', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MrpProduction', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_document_iterate_key',
                                    ctx=Load(),
                                ),
                                args=[Name(id='move_raw_id', ctx=Load())],
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
                                        operand=Name(id='iterate_key', ctx=Load()),
                                    ),
                                    Attribute(
                                        value=Name(id='move_raw_id', ctx=Load()),
                                        attr='created_purchase_line_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='iterate_key', ctx=Store())],
                                    value=Constant(value='created_purchase_line_id', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='iterate_key', ctx=Load()),
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
