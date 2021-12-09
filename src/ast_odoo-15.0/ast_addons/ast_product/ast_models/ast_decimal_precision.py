Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='DecimalPrecision',
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
                    value=Constant(value='decimal.precision', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_main_currency_rounding',
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
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='precision', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='Account', kind=None)],
                                                ),
                                                Compare(
                                                    left=Call(
                                                        func=Attribute(
                                                            value=Name(id='tools', ctx=Load()),
                                                            attr='float_compare',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='company',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='currency_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='rounding',
                                                                ctx=Load(),
                                                            ),
                                                            BinOp(
                                                                left=Constant(value=10, kind=None),
                                                                op=Pow(),
                                                                right=UnaryOp(
                                                                    op=USub(),
                                                                    operand=Attribute(
                                                                        value=Name(id='precision', ctx=Load()),
                                                                        attr='digits',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_digits',
                                                                value=Constant(value=6, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='precision', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="You cannot define the decimal precision of 'Account' as greater than the rounding factor of the company's main currency", kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='digits', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_digits',
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='Product Unit of Measure', kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='rounding', ctx=Store())],
                            value=BinOp(
                                left=Constant(value=1.0, kind=None),
                                op=Div(),
                                right=BinOp(
                                    left=Constant(value=10.0, kind=None),
                                    op=Pow(),
                                    right=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='digits',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dangerous_uom', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='uom.uom', kind=None),
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
                                                    Constant(value='rounding', kind=None),
                                                    Constant(value='<', kind=None),
                                                    Name(id='rounding', ctx=Load()),
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
                            test=Name(id='dangerous_uom', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='uom_descriptions', ctx=Store())],
                                    value=ListComp(
                                        elt=BinOp(
                                            left=Constant(value=' - %s (id=%s, precision=%s)', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='uom', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='uom', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='uom', ctx=Load()),
                                                        attr='rounding',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='uom', ctx=Store()),
                                                iter=Name(id='dangerous_uom', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                                            args=[Constant(value='You are setting a Decimal Accuracy less precise than the UOMs:\n%s\nThis may cause inconsistencies in computations.\nPlease increase the rounding of those units of measure, or the digits of this Decimal Accuracy.', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Constant(value='\n', kind=None),
                                                                attr='join',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='uom_descriptions', ctx=Load())],
                                                            keywords=[],
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
                            args=[Constant(value='digits', kind=None)],
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
