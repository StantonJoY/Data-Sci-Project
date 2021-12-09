Module(
    body=[
        FunctionDef(
            name='convert_field',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='model', annotation=None, type_comment=None),
                    arg(arg='field', annotation=None, type_comment=None),
                    arg(arg='target_model', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='table', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='model', ctx=Load()),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='.', kind=None),
                            Constant(value='_', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='SELECT 1\n                    FROM information_schema.columns\n                   WHERE table_name = %s\n                     AND column_name = %s\n               ', kind=None),
                            Tuple(
                                elts=[
                                    Name(id='table', ctx=Load()),
                                    Name(id='field', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Attribute(
                                value=Name(id='cr', ctx=Load()),
                                attr='fetchone',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                    ),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='SELECT id FROM ir_model_fields WHERE model=%s AND name=%s', kind=None),
                            Tuple(
                                elts=[
                                    Name(id='model', ctx=Load()),
                                    Name(id='field', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[
                        List(
                            elts=[Name(id='fields_id', ctx=Store())],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='fetchone',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Constant(value="\n        INSERT INTO ir_property(name, type, fields_id, company_id, res_id, value_reference)\n        SELECT %(field)s, 'many2one', %(fields_id)s, company_id, CONCAT('{model},', id),\n               CONCAT('{target_model},', {field})\n          FROM {table} t\n         WHERE {field} IS NOT NULL\n           AND NOT EXISTS(SELECT 1\n                            FROM ir_property\n                           WHERE fields_id=%(fields_id)s\n                             AND company_id=t.company_id\n                             AND res_id=CONCAT('{model},', t.id))\n    ", kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Call(
                                            func=Name(id='locals', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            Call(
                                func=Name(id='locals', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Constant(value='ALTER TABLE "{0}" DROP COLUMN "{1}" CASCADE', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='table', ctx=Load()),
                                    Name(id='field', ctx=Load()),
                                ],
                                keywords=[],
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
            name='migrate',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='version', annotation=None, type_comment=None),
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
                        func=Name(id='convert_field', ctx=Load()),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Constant(value='res.partner', kind=None),
                            Constant(value='property_purchase_currency_id', kind=None),
                            Constant(value='res.currency', kind=None),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='convert_field', ctx=Load()),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Constant(value='product.template', kind=None),
                            Constant(value='property_account_creditor_price_difference', kind=None),
                            Constant(value='account.account', kind=None),
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
    type_ignores=[],
)
