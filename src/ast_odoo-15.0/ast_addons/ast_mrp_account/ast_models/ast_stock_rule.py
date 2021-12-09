Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            name='StockRule',
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
                    value=Constant(value='stock.rule', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_mo_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='product_qty', annotation=None, type_comment=None),
                            arg(arg='product_uom', annotation=None, type_comment=None),
                            arg(arg='location_id', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='origin', annotation=None, type_comment=None),
                            arg(arg='company_id', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_prepare_mo_vals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='product_id', ctx=Load()),
                                    Name(id='product_qty', ctx=Load()),
                                    Name(id='product_uom', ctx=Load()),
                                    Name(id='location_id', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Name(id='origin', ctx=Load()),
                                    Name(id='company_id', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                    Name(id='bom', ctx=Load()),
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
                                        operand=Attribute(
                                            value=Name(id='bom', ctx=Load()),
                                            attr='analytic_account_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='analytic_account_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='analytic_account_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='analytic_account_id', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
