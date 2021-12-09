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
                FunctionDef(
                    name='_get_account_move_line_group_data_type_key',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data_type', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Dict(keys=[], values=[])],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
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
                                    attr='_get_account_move_line_group_data_type_key',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='data_type', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                    Name(id='options', ctx=Load()),
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
                                        left=Name(id='data_type', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='tax', kind=None)],
                                    ),
                                    Name(id='res', ctx=Load()),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='account.tax', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='values', ctx=Load()),
                                                                slice=Constant(value='tax_line_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='account_fiscal_country_id',
                                                ctx=Load(),
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='IN', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Name(id='res', ctx=Load()),
                                                op=Add(),
                                                right=Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='product_uom_id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='product_id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
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
                    name='_prepare_account_move_line',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='line', annotation=None, type_comment=None),
                            arg(arg='partner_id', annotation=None, type_comment=None),
                            arg(arg='current_company', annotation=None, type_comment=None),
                            arg(arg='currency_id', annotation=None, type_comment=None),
                            arg(arg='rounding_method', annotation=None, type_comment=None),
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
                                        args=[
                                            Name(id='PosOrder', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_prepare_account_move_line',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='line', ctx=Load()),
                                    Name(id='partner_id', ctx=Load()),
                                    Name(id='current_company', ctx=Load()),
                                    Name(id='currency_id', ctx=Load()),
                                    Name(id='rounding_method', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line_values', ctx=Store()),
                            iter=Name(id='res', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='line_values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='data_type', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='tax', kind=None),
                                                    Constant(value='product', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='line_values', ctx=Load()),
                                                        slice=Constant(value='values', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='product_uom_id', kind=None),
                                                        ],
                                                        values=[
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
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='uom_id',
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
