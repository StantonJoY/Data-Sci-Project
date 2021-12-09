Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
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
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='stock.landed.cost', kind=None),
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
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection_add',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='manufacturing', kind=None),
                                                Constant(value='Manufacturing Orders', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Dict(
                                    keys=[Constant(value='manufacturing', kind=None)],
                                    values=[Constant(value='set default', kind=None)],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mrp_production_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='mrp.production', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Manufacturing order', kind=None),
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
                            keyword(
                                arg='groups',
                                value=Constant(value='mrp.group_mrp_user', kind=None),
                            ),
                        ],
                    ),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_onchange_target_model',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='target_model',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='manufacturing', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mrp_production_ids',
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
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='_get_targeted_move_ids',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=BitOr(),
                                right=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mrp_production_ids',
                                        ctx=Load(),
                                    ),
                                    attr='move_finished_ids',
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
