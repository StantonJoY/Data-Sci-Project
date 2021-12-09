Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='UoM',
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
                    value=Constant(value='uom.uom', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_rounding',
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
                            targets=[Name(id='precision', ctx=Store())],
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
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rounding',
                                    ctx=Load(),
                                ),
                                ops=[Lt()],
                                comparators=[
                                    BinOp(
                                        left=Constant(value=1.0, kind=None),
                                        op=Div(),
                                        right=BinOp(
                                            left=Constant(value=10.0, kind=None),
                                            op=Pow(),
                                            right=Name(id='precision', ctx=Load()),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='warning', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='title', kind=None),
                                                    Constant(value='message', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Warning!', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='This rounding precision is higher than the Decimal Accuracy (%s digits).\nThis may cause inconsistencies in computations.\nPlease set a precision between %s and 1.', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='precision', ctx=Load()),
                                                                BinOp(
                                                                    left=Constant(value=1.0, kind=None),
                                                                    op=Div(),
                                                                    right=BinOp(
                                                                        left=Constant(value=10.0, kind=None),
                                                                        op=Pow(),
                                                                        right=Name(id='precision', ctx=Load()),
                                                                    ),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
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
                            args=[Constant(value='rounding', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
