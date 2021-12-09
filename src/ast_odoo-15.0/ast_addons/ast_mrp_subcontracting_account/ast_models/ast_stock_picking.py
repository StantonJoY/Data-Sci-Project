Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv.expression',
            names=[alias(name='OR', asname=None)],
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
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockPicking', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='action_view_stock_valuation_layers',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='subcontracted_productions', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_subcontract_production',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='subcontracted_productions', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='action', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Subscript(
                                value=Name(id='action', ctx=Load()),
                                slice=Constant(value='domain', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain_subcontracting', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='subcontracted_productions', ctx=Load()),
                                                            attr='move_raw_ids',
                                                            ctx=Load(),
                                                        ),
                                                        op=BitOr(),
                                                        right=Attribute(
                                                            value=Name(id='subcontracted_productions', ctx=Load()),
                                                            attr='move_finished_ids',
                                                            ctx=Load(),
                                                        ),
                                                    ),
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
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Name(id='OR', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Name(id='domain', ctx=Load()),
                                            Name(id='domain_subcontracting', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
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
                    name='_prepare_subcontract_mo_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='subcontract_move', annotation=None, type_comment=None),
                            arg(arg='bom', annotation=None, type_comment=None),
                        ],
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
                                            Name(id='StockPicking', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_prepare_subcontract_mo_vals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='subcontract_move', ctx=Load()),
                                    Name(id='bom', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='bom', ctx=Load()),
                                        attr='product_tmpl_id',
                                        ctx=Load(),
                                    ),
                                    attr='cost_method',
                                    ctx=Load(),
                                ),
                                ops=[In()],
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
                            body=[
                                Assign(
                                    targets=[Name(id='vals', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='vals', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='extra_cost',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='subcontract_move', ctx=Load()),
                                                        attr='_get_price_unit',
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
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='vals', ctx=Load()),
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
