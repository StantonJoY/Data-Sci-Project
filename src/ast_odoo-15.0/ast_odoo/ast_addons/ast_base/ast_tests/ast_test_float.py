Module(
    body=[
        ImportFrom(
            module='math',
            names=[alias(name='log10', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_compare', asname=None),
                alias(name='float_is_zero', asname=None),
                alias(name='float_repr', asname=None),
                alias(name='float_round', asname=None),
                alias(name='float_split', asname=None),
                alias(name='float_split_str', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestFloatPrecision',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Tests on float precision. ', kind=None),
                ),
                FunctionDef(
                    name='test_rounding_02',
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
                            value=Constant(value=' Test rounding methods with 2 digits. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='currency', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.EUR', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='try_round',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='amount', annotation=None, type_comment=None),
                                    arg(arg='expected', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='digits', ctx=Store())],
                                    value=Call(
                                        func=Name(id='max', ctx=Load()),
                                        args=[
                                            Constant(value=0, kind=None),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Name(id='log10', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='currency', ctx=Load()),
                                                                    attr='rounding',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float_repr', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='currency', ctx=Load()),
                                                    attr='round',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='amount', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Name(id='digits', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='result', ctx=Load()),
                                            Name(id='expected', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Rounding error: got %s, expected %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='result', ctx=Load()),
                                                        Name(id='expected', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=2.674, kind=None),
                                    Constant(value='2.67', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=2.675, kind=None),
                                    Constant(value='2.68', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.675, kind=None),
                                    ),
                                    Constant(value='-2.68', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=0.001, kind=None),
                                    Constant(value='0.00', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.001, kind=None),
                                    ),
                                    Constant(value='-0.00', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=0.0049, kind=None),
                                    Constant(value='0.00', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=0.005, kind=None),
                                    Constant(value='0.01', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.005, kind=None),
                                    ),
                                    Constant(value='-0.01', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value=6.6, kind=None),
                                        op=Mult(),
                                        right=Constant(value=0.175, kind=None),
                                    ),
                                    Constant(value='1.16', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=6.6, kind=None),
                                        ),
                                        op=Mult(),
                                        right=Constant(value=0.175, kind=None),
                                    ),
                                    Constant(value='-1.16', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        FunctionDef(
                            name='try_zero',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='amount', annotation=None, type_comment=None),
                                    arg(arg='expected', annotation=None, type_comment=None),
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
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='currency', ctx=Load()),
                                                    attr='is_zero',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='amount', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Name(id='expected', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Rounding error: %s should be zero!', kind=None),
                                                op=Mod(),
                                                right=Name(id='amount', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    Constant(value=0.01, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.01, kind=None),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    Constant(value=0.001, kind=None),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.001, kind=None),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    Constant(value=0.0046, kind=None),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.0046, kind=None),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value=2.68, kind=None),
                                        op=Sub(),
                                        right=Constant(value=2.675, kind=None),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value=2.68, kind=None),
                                        op=Sub(),
                                        right=Constant(value=2.676, kind=None),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value=2.676, kind=None),
                                        op=Sub(),
                                        right=Constant(value=2.68, kind=None),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value=2.675, kind=None),
                                        op=Sub(),
                                        right=Constant(value=2.68, kind=None),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        FunctionDef(
                            name='try_compare',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='amount1', annotation=None, type_comment=None),
                                    arg(arg='amount2', annotation=None, type_comment=None),
                                    arg(arg='expected', annotation=None, type_comment=None),
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
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='currency', ctx=Load()),
                                                    attr='compare_amounts',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='amount1', ctx=Load()),
                                                    Name(id='amount2', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='expected', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Rounding error, compare_amounts(%s,%s) should be %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='amount1', ctx=Load()),
                                                        Name(id='amount2', ctx=Load()),
                                                        Name(id='expected', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    Constant(value=0.001, kind=None),
                                    Constant(value=0.001, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.001, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.001, kind=None),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    Constant(value=0.001, kind=None),
                                    Constant(value=0.002, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.001, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.002, kind=None),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    Constant(value=2.675, kind=None),
                                    Constant(value=2.68, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    Constant(value=2.676, kind=None),
                                    Constant(value=2.68, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.676, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.68, kind=None),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    Constant(value=2.674, kind=None),
                                    Constant(value=2.68, kind=None),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.674, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.68, kind=None),
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    Constant(value=3, kind=None),
                                    Constant(value=2.68, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=3, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.68, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    Constant(value=0.01, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.01, kind=None),
                                    ),
                                    Constant(value=0, kind=None),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_rounding_03',
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
                            value=Constant(value=' Test rounding methods with 3 digits. ', kind=None),
                        ),
                        FunctionDef(
                            name='try_round',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='amount', annotation=None, type_comment=None),
                                    arg(arg='expected', annotation=None, type_comment=None),
                                    arg(arg='digits', annotation=None, type_comment=None),
                                    arg(arg='method', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[
                                    Constant(value=3, kind=None),
                                    Constant(value='HALF-UP', kind=None),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[Name(id='amount', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Name(id='digits', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='rounding_method',
                                                value=Name(id='method', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float_repr', ctx=Load()),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Name(id='digits', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='result', ctx=Load()),
                                            Name(id='expected', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Rounding error: got %s, expected %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='result', ctx=Load()),
                                                        Name(id='expected', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=2.6745, kind=None),
                                    Constant(value='2.675', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.6745, kind=None),
                                    ),
                                    Constant(value='-2.675', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=2.6744, kind=None),
                                    Constant(value='2.674', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.6744, kind=None),
                                    ),
                                    Constant(value='-2.674', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=0.0004, kind=None),
                                    Constant(value='0.000', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.0004, kind=None),
                                    ),
                                    Constant(value='-0.000', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=357.4555, kind=None),
                                    Constant(value='357.456', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=357.4555, kind=None),
                                    ),
                                    Constant(value='-357.456', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=457.4554, kind=None),
                                    Constant(value='457.455', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=457.4554, kind=None),
                                    ),
                                    Constant(value='-457.455', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=8.175, kind=None),
                                    Constant(value='8.175', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='UP', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=8.1751, kind=None),
                                    Constant(value='8.176', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='UP', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=8.175, kind=None),
                                    ),
                                    Constant(value='-8.175', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='UP', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=8.1751, kind=None),
                                    ),
                                    Constant(value='-8.176', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='UP', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=6.0, kind=None),
                                    ),
                                    Constant(value='-6.000', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='UP', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=1.8, kind=None),
                                    Constant(value='2', kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='UP', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1.8, kind=None),
                                    ),
                                    Constant(value='-2', kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='UP', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=2.425, kind=None),
                                    Constant(value='2.425', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='DOWN', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=2.4249, kind=None),
                                    Constant(value='2.424', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='DOWN', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.425, kind=None),
                                    ),
                                    Constant(value='-2.425', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='DOWN', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.4249, kind=None),
                                    ),
                                    Constant(value='-2.424', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='DOWN', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.5, kind=None),
                                    ),
                                    Constant(value='-2.500', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='DOWN', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=1.8, kind=None),
                                    Constant(value='1', kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='DOWN', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1.8, kind=None),
                                    ),
                                    Constant(value='-1', kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='DOWN', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='fractions', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value=0.0, kind=None),
                                    Constant(value=0.015, kind=None),
                                    Constant(value=0.01499, kind=None),
                                    Constant(value=0.675, kind=None),
                                    Constant(value=0.67499, kind=None),
                                    Constant(value=0.4555, kind=None),
                                    Constant(value=0.4555, kind=None),
                                    Constant(value=0.45555, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expecteds', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='.00', kind=None),
                                    Constant(value='.02', kind=None),
                                    Constant(value='.01', kind=None),
                                    Constant(value='.68', kind=None),
                                    Constant(value='.67', kind=None),
                                    Constant(value='.46', kind=None),
                                    Constant(value='.456', kind=None),
                                    Constant(value='.4556', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='precisions', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value=2, kind=None),
                                    Constant(value=2, kind=None),
                                    Constant(value=2, kind=None),
                                    Constant(value=2, kind=None),
                                    Constant(value=2, kind=None),
                                    Constant(value=2, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=4, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='magnitude', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Constant(value=7, kind=None)],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='frac', ctx=Store()),
                                            Name(id='exp', ctx=Store()),
                                            Name(id='prec', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='zip', ctx=Load()),
                                        args=[
                                            Name(id='fractions', ctx=Load()),
                                            Name(id='expecteds', ctx=Load()),
                                            Name(id='precisions', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='sign', ctx=Store()),
                                            iter=List(
                                                elts=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                    Constant(value=1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            body=[
                                                For(
                                                    target=Name(id='x', ctx=Store()),
                                                    iter=Call(
                                                        func=Name(id='range', ctx=Load()),
                                                        args=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=10000, kind=None),
                                                            Constant(value=97, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='n', ctx=Store())],
                                                            value=BinOp(
                                                                left=Name(id='x', ctx=Load()),
                                                                op=Mult(),
                                                                right=BinOp(
                                                                    left=Constant(value=10, kind=None),
                                                                    op=Pow(),
                                                                    right=Name(id='magnitude', ctx=Load()),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='f', ctx=Store())],
                                                            value=BinOp(
                                                                left=Name(id='sign', ctx=Load()),
                                                                op=Mult(),
                                                                right=BinOp(
                                                                    left=Name(id='n', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Name(id='frac', ctx=Load()),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='f_exp', ctx=Store())],
                                                            value=BinOp(
                                                                left=BinOp(
                                                                    left=IfExp(
                                                                        test=BoolOp(
                                                                            op=And(),
                                                                            values=[
                                                                                Compare(
                                                                                    left=Name(id='f', ctx=Load()),
                                                                                    ops=[NotEq()],
                                                                                    comparators=[Constant(value=0, kind=None)],
                                                                                ),
                                                                                Compare(
                                                                                    left=Name(id='sign', ctx=Load()),
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
                                                                        body=Constant(value='-', kind=None),
                                                                        orelse=Constant(value='', kind=None),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Call(
                                                                        func=Name(id='str', ctx=Load()),
                                                                        args=[Name(id='n', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                op=Add(),
                                                                right=Name(id='exp', ctx=Load()),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='try_round', ctx=Load()),
                                                                args=[
                                                                    Name(id='f', ctx=Load()),
                                                                    Name(id='f_exp', ctx=Load()),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='digits',
                                                                        value=Name(id='prec', ctx=Load()),
                                                                    ),
                                                                ],
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
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='try_zero',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='amount', annotation=None, type_comment=None),
                                    arg(arg='expected', annotation=None, type_comment=None),
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
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='float_is_zero', ctx=Load()),
                                                args=[Name(id='amount', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_digits',
                                                        value=Constant(value=3, kind=None),
                                                    ),
                                                ],
                                            ),
                                            Name(id='expected', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Rounding error: %s should be zero!', kind=None),
                                                op=Mod(),
                                                right=Name(id='amount', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    Constant(value=0.0002, kind=None),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.0002, kind=None),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    Constant(value=0.00034, kind=None),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    Constant(value=0.0005, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.0005, kind=None),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    Constant(value=0.0008, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_zero', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.0008, kind=None),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        FunctionDef(
                            name='try_compare',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='amount1', annotation=None, type_comment=None),
                                    arg(arg='amount2', annotation=None, type_comment=None),
                                    arg(arg='expected', annotation=None, type_comment=None),
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
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='float_compare', ctx=Load()),
                                                args=[
                                                    Name(id='amount1', ctx=Load()),
                                                    Name(id='amount2', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_digits',
                                                        value=Constant(value=3, kind=None),
                                                    ),
                                                ],
                                            ),
                                            Name(id='expected', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Rounding error, compare_amounts(%s,%s) should be %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='amount1', ctx=Load()),
                                                        Name(id='amount2', ctx=Load()),
                                                        Name(id='expected', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    Constant(value=0.0003, kind=None),
                                    Constant(value=0.0004, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.0003, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.0004, kind=None),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    Constant(value=0.0002, kind=None),
                                    Constant(value=0.0005, kind=None),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.0002, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.0005, kind=None),
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    Constant(value=0.0009, kind=None),
                                    Constant(value=0.0004, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.0009, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.0004, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    Constant(value=557.4555, kind=None),
                                    Constant(value=557.4556, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=557.4555, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=557.4556, kind=None),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    Constant(value=657.4444, kind=None),
                                    Constant(value=657.445, kind=None),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_compare', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=657.4444, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=657.445, kind=None),
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        FunctionDef(
                            name='try_round',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='amount', annotation=None, type_comment=None),
                                    arg(arg='expected', annotation=None, type_comment=None),
                                    arg(arg='precision_rounding', annotation=None, type_comment=None),
                                    arg(arg='method', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[
                                    Constant(value=None, kind=None),
                                    Constant(value='HALF-UP', kind=None),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[Name(id='amount', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Name(id='precision_rounding', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='rounding_method',
                                                value=Name(id='method', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float_repr', ctx=Load()),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='result', ctx=Load()),
                                            Name(id='expected', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Rounding error: got %s, expected %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='result', ctx=Load()),
                                                        Name(id='expected', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=457.4554, kind=None),
                                    ),
                                    Constant(value='-457.45', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='precision_rounding',
                                        value=Constant(value=0.05, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=457.444, kind=None),
                                    Constant(value='457.50', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='precision_rounding',
                                        value=Constant(value=0.5, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=457.3, kind=None),
                                    Constant(value='455.00', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='precision_rounding',
                                        value=Constant(value=5, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=457.5, kind=None),
                                    Constant(value='460.00', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='precision_rounding',
                                        value=Constant(value=5, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=457.1, kind=None),
                                    Constant(value='456.00', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='precision_rounding',
                                        value=Constant(value=3, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    Constant(value=2.5, kind=None),
                                    Constant(value='2.50', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='precision_rounding',
                                        value=Constant(value=0.05, kind=None),
                                    ),
                                    keyword(
                                        arg='method',
                                        value=Constant(value='DOWN', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_round', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.5, kind=None),
                                    ),
                                    Constant(value='-2.50', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='precision_rounding',
                                        value=Constant(value=0.05, kind=None),
                                    ),
                                    keyword(
                                        arg='method',
                                        value=Constant(value='DOWN', kind=None),
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
                    name='test_rounding_04',
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
                            value=Constant(value=' check that proper rounding is performed for float persistence ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='currency', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.EUR', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currency_rate', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.currency.rate', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='try_roundtrip',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='value', annotation=None, type_comment=None),
                                    arg(arg='expected', annotation=None, type_comment=None),
                                    arg(arg='date', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='rate', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='currency_rate', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='rate', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='date', ctx=Load()),
                                                    Name(id='value', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='currency', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='rate', ctx=Load()),
                                                attr='rate',
                                                ctx=Load(),
                                            ),
                                            Name(id='expected', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Roundtrip error: got %s back from db, expected %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='rate', ctx=Load()),
                                                        Name(id='expected', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_roundtrip', ctx=Load()),
                                args=[
                                    Constant(value=10000.999999, kind=None),
                                    Constant(value=10000.999999, kind=None),
                                    Constant(value='2000-01-03', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_float_split_05',
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
                            value=Constant(value=' Test split method with 2 digits. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='currency', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.EUR', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='try_split',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='value', annotation=None, type_comment=None),
                                    arg(arg='expected', annotation=None, type_comment=None),
                                    arg(arg='split_fun', annotation=None, type_comment=None),
                                    arg(arg='rounding', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='digits', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='rounding', ctx=Load()),
                                            ops=[Is()],
                                            comparators=[Constant(value=None, kind=None)],
                                        ),
                                        body=Call(
                                            func=Name(id='max', ctx=Load()),
                                            args=[
                                                Constant(value=0, kind=None),
                                                UnaryOp(
                                                    op=USub(),
                                                    operand=Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='log10', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='currency', ctx=Load()),
                                                                        attr='rounding',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        orelse=Name(id='rounding', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Name(id='split_fun', ctx=Load()),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Name(id='digits', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='result', ctx=Load()),
                                            Name(id='expected', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Split error: got %s, expected %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='result', ctx=Load()),
                                                        Name(id='expected', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    Constant(value=2.674, kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='2', kind=None),
                                            Constant(value='67', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split_str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    Constant(value=2.675, kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='2', kind=None),
                                            Constant(value='68', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split_str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.675, kind=None),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='-2', kind=None),
                                            Constant(value='68', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split_str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    Constant(value=0.001, kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='0', kind=None),
                                            Constant(value='00', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split_str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.001, kind=None),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='-0', kind=None),
                                            Constant(value='00', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split_str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    Constant(value=42, kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='42', kind=None),
                                            Constant(value='00', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split_str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    Constant(value=0.1, kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='0', kind=None),
                                            Constant(value='10', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split_str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    Constant(value=13.0, kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='13', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split_str', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='rounding',
                                        value=Constant(value=0, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    Constant(value=2.674, kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value=2, kind=None),
                                            Constant(value=67, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    Constant(value=2.675, kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value=2, kind=None),
                                            Constant(value=68, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.675, kind=None),
                                    ),
                                    Tuple(
                                        elts=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=2, kind=None),
                                            ),
                                            Constant(value=68, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    Constant(value=0.001, kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=0.001, kind=None),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    Constant(value=42, kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value=42, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    Constant(value=0.1, kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value=0, kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='try_split', ctx=Load()),
                                args=[
                                    Constant(value=13.0, kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value=13, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='float_split', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='rounding',
                                        value=Constant(value=0, kind=None),
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
                    name='test_rounding_invalid',
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
                            value=Constant(value=' verify that invalid parameters are forbidden ', kind=None),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AssertionError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[Constant(value=0.01, kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=3, kind=None),
                                            ),
                                            keyword(
                                                arg='precision_rounding',
                                                value=Constant(value=0.01, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AssertionError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[Constant(value=0.0, kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Constant(value=0.0, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AssertionError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='float_is_zero', ctx=Load()),
                                        args=[Constant(value=0.0, kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=0.1, kind=None),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AssertionError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Constant(value=0.01, kind=None),
                                            Constant(value=0.02, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=3, kind=None),
                                            ),
                                            keyword(
                                                arg='precision_rounding',
                                                value=Constant(value=0.01, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AssertionError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Constant(value=1.0, kind=None),
                                            Constant(value=1.0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Constant(value=0.0, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AssertionError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Constant(value=1.0, kind=None),
                                            Constant(value=1.0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=0.1, kind=None),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AssertionError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[Constant(value=0.01, kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=3, kind=None),
                                            ),
                                            keyword(
                                                arg='precision_rounding',
                                                value=Constant(value=0.01, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AssertionError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[Constant(value=1.25, kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Constant(value=0.0, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AssertionError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[Constant(value=1.25, kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=0.1, kind=None),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_amount_to_text_10',
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
                            value=Constant(value=' verify that amount_to_text works as expected ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='currency', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.EUR', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='amount_target', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='currency', ctx=Load()),
                                    attr='amount_to_text',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=0.29, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='amount_test', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='currency', ctx=Load()),
                                    attr='amount_to_text',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=0.28, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='amount_test', ctx=Load()),
                                    Name(id='amount_target', ctx=Load()),
                                    Constant(value='Amount in text should not depend on float representation', kind=None),
                                ],
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
