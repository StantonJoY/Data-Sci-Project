Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.safe_eval',
            names=[alias(name='safe_eval', asname=None)],
            level=0,
        ),
        ClassDef(
            name='AccountTaxPython',
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
                    value=Constant(value='account.tax', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='amount_type', ctx=Store())],
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
                                                Constant(value='code', kind=None),
                                                Constant(value='Python Code', kind=None),
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
                                    keys=[Constant(value='code', kind=None)],
                                    values=[
                                        Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='recs', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Call(
                                                func=Attribute(
                                                    value=Name(id='recs', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='amount_type', kind=None),
                                                            Constant(value='active', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='percent', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='python_compute', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Python Code', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='result = price_unit * 0.10', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Compute the amount of the tax by setting the variable 'result'.\n\n:param base_amount: float, actual amount on which the tax is applied\n:param price_unit: float\n:param quantity: float\n:param company: res.company recordset singleton\n:param product: product.product recordset singleton or None\n:param partner: res.partner recordset singleton or None", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='python_applicable', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Applicable Code', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='result = True', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Determine if the tax will be applied by setting the variable 'result' to True or False.\n\n:param price_unit: float\n:param quantity: float\n:param company: res.company recordset singleton\n:param product: product.product recordset singleton or None\n:param partner: res.partner recordset singleton or None", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_amount',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='base_amount', annotation=None, type_comment=None),
                            arg(arg='price_unit', annotation=None, type_comment=None),
                            arg(arg='quantity', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=1.0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='product', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='product.template', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='product', ctx=Load()),
                                        attr='product_variant_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='amount_type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='code', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='localdict', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='base_amount', kind=None),
                                            Constant(value='price_unit', kind=None),
                                            Constant(value='quantity', kind=None),
                                            Constant(value='product', kind=None),
                                            Constant(value='partner', kind=None),
                                            Constant(value='company', kind=None),
                                        ],
                                        values=[
                                            Name(id='base_amount', ctx=Load()),
                                            Name(id='price_unit', ctx=Load()),
                                            Name(id='quantity', ctx=Load()),
                                            Name(id='product', ctx=Load()),
                                            Name(id='partner', ctx=Load()),
                                            Name(id='company', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='safe_eval', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='python_compute',
                                                ctx=Load(),
                                            ),
                                            Name(id='localdict', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='mode',
                                                value=Constant(value='exec', kind=None),
                                            ),
                                            keyword(
                                                arg='nocopy',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Return(
                                    value=Subscript(
                                        value=Name(id='localdict', ctx=Load()),
                                        slice=Constant(value='result', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='AccountTaxPython', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_compute_amount',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='base_amount', ctx=Load()),
                                    Name(id='price_unit', ctx=Load()),
                                    Name(id='quantity', ctx=Load()),
                                    Name(id='product', ctx=Load()),
                                    Name(id='partner', ctx=Load()),
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
                    name='compute_all',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='price_unit', annotation=None, type_comment=None),
                            arg(arg='currency', annotation=None, type_comment=None),
                            arg(arg='quantity', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                            arg(arg='is_refund', annotation=None, type_comment=None),
                            arg(arg='handle_price_include', annotation=None, type_comment=None),
                            arg(arg='include_caba_tags', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=1.0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='taxes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='r', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='r', ctx=Load()),
                                                attr='amount_type',
                                                ctx=Load(),
                                            ),
                                            ops=[NotEq()],
                                            comparators=[Constant(value='code', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='company',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='product', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='product.template', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='product', ctx=Load()),
                                        attr='product_variant_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='tax', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='r', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='r', ctx=Load()),
                                                attr='amount_type',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='code', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='localdict', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='tax_computation_context', kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='localdict', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='price_unit', kind=None),
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='product', kind=None),
                                                    Constant(value='partner', kind=None),
                                                    Constant(value='company', kind=None),
                                                ],
                                                values=[
                                                    Name(id='price_unit', ctx=Load()),
                                                    Name(id='quantity', ctx=Load()),
                                                    Name(id='product', ctx=Load()),
                                                    Name(id='partner', ctx=Load()),
                                                    Name(id='company', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='safe_eval', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='tax', ctx=Load()),
                                                attr='python_applicable',
                                                ctx=Load(),
                                            ),
                                            Name(id='localdict', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='mode',
                                                value=Constant(value='exec', kind=None),
                                            ),
                                            keyword(
                                                arg='nocopy',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='localdict', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='result', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='taxes', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='tax', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='AccountTaxPython', ctx=Load()),
                                            Name(id='taxes', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='compute_all',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='price_unit', ctx=Load()),
                                    Name(id='currency', ctx=Load()),
                                    Name(id='quantity', ctx=Load()),
                                    Name(id='product', ctx=Load()),
                                    Name(id='partner', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='is_refund',
                                        value=Name(id='is_refund', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='handle_price_include',
                                        value=Name(id='handle_price_include', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='include_caba_tags',
                                        value=Name(id='include_caba_tags', ctx=Load()),
                                    ),
                                ],
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
        ClassDef(
            name='AccountTaxTemplatePython',
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
                    value=Constant(value='account.tax.template', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='amount_type', ctx=Store())],
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
                                                Constant(value='code', kind=None),
                                                Constant(value='Python Code', kind=None),
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
                                    keys=[Constant(value='code', kind=None)],
                                    values=[Constant(value='cascade', kind=None)],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='python_compute', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Python Code', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='result = price_unit * 0.10', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Compute the amount of the tax by setting the variable 'result'.\n\n:param base_amount: float, actual amount on which the tax is applied\n:param price_unit: float\n:param quantity: float\n:param product: product.product recordset singleton or None\n:param partner: res.partner recordset singleton or None", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='python_applicable', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Applicable Code', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='result = True', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Determine if the tax will be applied by setting the variable 'result' to True or False.\n\n:param price_unit: float\n:param quantity: float\n:param product: product.product recordset singleton or None\n:param partner: res.partner recordset singleton or None", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_tax_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                            arg(arg='tax_template_to_tax', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' This method generates a dictionnary of all the values for the tax that will be created.\n        ', kind=None),
                        ),
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='AccountTaxTemplatePython', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_tax_vals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='company', ctx=Load()),
                                    Name(id='tax_template_to_tax', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='python_compute', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='python_compute',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='python_applicable', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='python_applicable',
                                ctx=Load(),
                            ),
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
