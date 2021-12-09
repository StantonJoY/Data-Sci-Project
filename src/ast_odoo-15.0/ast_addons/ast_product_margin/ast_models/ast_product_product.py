Module(
    body=[
        Import(
            names=[alias(name='time', asname=None)],
        ),
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
            name='ProductProduct',
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
                    value=Constant(value='product.product', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_from', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Margin Date From', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_to', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Margin Date To', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='invoice_state', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='paid', kind=None),
                                                Constant(value='Paid', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='open_paid', kind=None),
                                                Constant(value='Open and Paid', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='draft_open_paid', kind=None),
                                                Constant(value='Draft, Open and Paid', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Invoice State', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sale_avg_price', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Avg. Sale Unit Price', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Avg. Price in Customer Invoices.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='purchase_avg_price', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Avg. Purchase Unit Price', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Avg. Price in Vendor Bills ', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sale_num_invoiced', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='# Invoiced in Sale', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Sum of Quantity in Customer Invoices', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='purchase_num_invoiced', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='# Invoiced in Purchase', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Sum of Quantity in Vendor Bills', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sales_gap', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Sales Gap', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Expected Sale - Turn Over', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='purchase_gap', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Purchase Gap', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Normal Cost - Total Cost', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='turnover', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Turnover', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Sum of Multiplication of Invoice price and quantity of Customer Invoices', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='total_cost', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Total Cost', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Sum of Multiplication of Invoice price and quantity of Vendor Bills ', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sale_expected', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Expected Sale', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Sum of Multiplication of Sale Catalog price and quantity of Customer Invoices', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='normal_cost', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Normal Cost', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Sum of Multiplication of Cost price and quantity of Vendor Bills', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='total_margin', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Total Margin', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Turnover - Standard price', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='expected_margin', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Expected Margin', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Expected Sale - Normal Cost', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='total_margin_rate', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Total Margin Rate(%)', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Total margin * 100 / Turnover', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='expected_margin_rate', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_margin_fields_values', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Expected Margin (%)', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Expected margin * 100 / Expected Sale', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='read_group',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='groupby', annotation=None, type_comment=None),
                            arg(arg='offset', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='orderby', annotation=None, type_comment=None),
                            arg(arg='lazy', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n            Inherit read_group to calculate the sum of the non-stored fields, as it is not automatically done anymore through the XML.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ProductProduct', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    Name(id='fields', ctx=Load()),
                                    Name(id='groupby', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='offset',
                                        value=Name(id='offset', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='orderby',
                                        value=Name(id='orderby', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='lazy',
                                        value=Name(id='lazy', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fields_list', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='turnover', kind=None),
                                    Constant(value='sale_avg_price', kind=None),
                                    Constant(value='sale_purchase_price', kind=None),
                                    Constant(value='sale_num_invoiced', kind=None),
                                    Constant(value='purchase_num_invoiced', kind=None),
                                    Constant(value='sales_gap', kind=None),
                                    Constant(value='purchase_gap', kind=None),
                                    Constant(value='total_cost', kind=None),
                                    Constant(value='sale_expected', kind=None),
                                    Constant(value='normal_cost', kind=None),
                                    Constant(value='total_margin', kind=None),
                                    Constant(value='expected_margin', kind=None),
                                    Constant(value='total_margin_rate', kind=None),
                                    Constant(value='expected_margin_rate', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Name(id='x', ctx=Load()),
                                            ops=[In()],
                                            comparators=[Name(id='fields', ctx=Load())],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Name(id='fields_list', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='re_ind', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='prod_re', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='tot_products', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='re', ctx=Store()),
                                    iter=Name(id='res', ctx=Load()),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='__domain', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='products', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='re', ctx=Load()),
                                                                slice=Constant(value='__domain', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='tot_products', ctx=Store()),
                                                    op=BitOr(),
                                                    value=Name(id='products', ctx=Load()),
                                                ),
                                                For(
                                                    target=Name(id='prod', ctx=Store()),
                                                    iter=Name(id='products', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='prod_re', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='prod', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='re_ind', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        AugAssign(
                                            target=Name(id='re_ind', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='res_val', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tot_products', ctx=Load()),
                                            attr='_compute_product_margin_fields_values',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='field_names',
                                                value=ListComp(
                                                    elt=Name(id='x', ctx=Load()),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='x', ctx=Store()),
                                                            iter=Name(id='fields', ctx=Load()),
                                                            ifs=[
                                                                Compare(
                                                                    left=Name(id='fields', ctx=Load()),
                                                                    ops=[In()],
                                                                    comparators=[Name(id='fields_list', ctx=Load())],
                                                                ),
                                                            ],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='key', ctx=Store()),
                                    iter=Name(id='res_val', ctx=Load()),
                                    body=[
                                        For(
                                            target=Name(id='l', ctx=Store()),
                                            iter=Subscript(
                                                value=Name(id='res_val', ctx=Load()),
                                                slice=Name(id='key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='re', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Subscript(
                                                            value=Name(id='prod_re', ctx=Load()),
                                                            slice=Name(id='key', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(id='re', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='l', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Subscript(
                                                                value=Name(id='re', ctx=Load()),
                                                                slice=Name(id='l', ctx=Load()),
                                                                ctx=Store(),
                                                            ),
                                                            op=Add(),
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='res_val', ctx=Load()),
                                                                    slice=Name(id='key', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='l', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='re', ctx=Load()),
                                                                    slice=Name(id='l', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='res_val', ctx=Load()),
                                                                    slice=Name(id='key', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='l', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
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
                    name='_compute_product_margin_fields_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_names', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='field_names', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='field_names', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='date_from', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='date_from', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='strftime',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='%Y-01-01', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_to', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='date_to', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='strftime',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='%Y-12-31', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_state', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='invoice_state', kind=None),
                                    Constant(value='open_paid', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=DictComp(
                                key=Name(id='product_id', ctx=Load()),
                                value=Dict(
                                    keys=[
                                        Constant(value='date_from', kind=None),
                                        Constant(value='date_to', kind=None),
                                        Constant(value='invoice_state', kind=None),
                                        Constant(value='turnover', kind=None),
                                        Constant(value='sale_avg_price', kind=None),
                                        Constant(value='purchase_avg_price', kind=None),
                                        Constant(value='sale_num_invoiced', kind=None),
                                        Constant(value='purchase_num_invoiced', kind=None),
                                        Constant(value='sales_gap', kind=None),
                                        Constant(value='purchase_gap', kind=None),
                                        Constant(value='total_cost', kind=None),
                                        Constant(value='sale_expected', kind=None),
                                        Constant(value='normal_cost', kind=None),
                                        Constant(value='total_margin', kind=None),
                                        Constant(value='expected_margin', kind=None),
                                        Constant(value='total_margin_rate', kind=None),
                                        Constant(value='expected_margin_rate', kind=None),
                                    ],
                                    values=[
                                        Name(id='date_from', ctx=Load()),
                                        Name(id='date_to', ctx=Load()),
                                        Name(id='invoice_state', ctx=Load()),
                                        Constant(value=0.0, kind=None),
                                        Constant(value=0.0, kind=None),
                                        Constant(value=0.0, kind=None),
                                        Constant(value=0.0, kind=None),
                                        Constant(value=0.0, kind=None),
                                        Constant(value=0.0, kind=None),
                                        Constant(value=0.0, kind=None),
                                        Constant(value=0.0, kind=None),
                                        Constant(value=0.0, kind=None),
                                        Constant(value=0.0, kind=None),
                                        Constant(value=0.0, kind=None),
                                        Constant(value=0.0, kind=None),
                                        Constant(value=0.0, kind=None),
                                        Constant(value=0.0, kind=None),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='product_id', ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='states', ctx=Store())],
                            value=Tuple(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payment_states', ctx=Store())],
                            value=Tuple(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='invoice_state', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='paid', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='states', ctx=Store())],
                                    value=Tuple(
                                        elts=[Constant(value='posted', kind=None)],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='payment_states', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            Constant(value='in_payment', kind=None),
                                            Constant(value='paid', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='invoice_state', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='open_paid', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='states', ctx=Store())],
                                            value=Tuple(
                                                elts=[Constant(value='posted', kind=None)],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='payment_states', ctx=Store())],
                                            value=Tuple(
                                                elts=[
                                                    Constant(value='not_paid', kind=None),
                                                    Constant(value='in_payment', kind=None),
                                                    Constant(value='paid', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='invoice_state', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='draft_open_paid', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='states', ctx=Store())],
                                                    value=Tuple(
                                                        elts=[
                                                            Constant(value='posted', kind=None),
                                                            Constant(value='draft', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='payment_states', ctx=Store())],
                                                    value=Tuple(
                                                        elts=[
                                                            Constant(value='not_paid', kind=None),
                                                            Constant(value='in_payment', kind=None),
                                                            Constant(value='paid', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='force_company', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='company_id', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='context',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='force_company', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='company_id', ctx=Store())],
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
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='price_unit', kind=None),
                                            Constant(value='quantity', kind=None),
                                            Constant(value='balance', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='display_type', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='payment_state', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='invoice_date', kind=None),
                                            Constant(value='company_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='list_price', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='sqlstr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value="\n                WITH currency_rate AS ({})\n                SELECT\n                    l.product_id as product_id,\n                    SUM(\n                        l.price_unit / (CASE COALESCE(cr.rate, 0) WHEN 0 THEN 1.0 ELSE cr.rate END) *\n                        l.quantity * (CASE WHEN i.move_type IN ('out_invoice', 'in_invoice') THEN 1 ELSE -1 END) * ((100 - l.discount) * 0.01)\n                    ) / NULLIF(SUM(l.quantity * (CASE WHEN i.move_type IN ('out_invoice', 'in_invoice') THEN 1 ELSE -1 END)), 0) AS avg_unit_price,\n                    SUM(l.quantity * (CASE WHEN i.move_type IN ('out_invoice', 'in_invoice') THEN 1 ELSE -1 END)) AS num_qty,\n                    SUM(ABS(l.balance) * (CASE WHEN i.move_type IN ('out_invoice', 'in_invoice') THEN 1 ELSE -1 END)) AS total,\n                    SUM(l.quantity * pt.list_price * (CASE WHEN i.move_type IN ('out_invoice', 'in_invoice') THEN 1 ELSE -1 END)) AS sale_expected\n                FROM account_move_line l\n                LEFT JOIN account_move i ON (l.move_id = i.id)\n                LEFT JOIN product_product product ON (product.id=l.product_id)\n                LEFT JOIN product_template pt ON (pt.id = product.product_tmpl_id)\n                left join currency_rate cr on\n                (cr.currency_id = i.currency_id and\n                 cr.company_id = i.company_id and\n                 cr.date_start <= COALESCE(i.invoice_date, NOW()) and\n                 (cr.date_end IS NULL OR cr.date_end > COALESCE(i.invoice_date, NOW())))\n                WHERE l.product_id IN %s\n                AND i.state IN %s\n                AND i.payment_state IN %s\n                AND i.move_type IN %s\n                AND i.invoice_date BETWEEN %s AND  %s\n                AND i.company_id = %s\n                AND l.display_type IS NULL\n                AND l.exclude_from_invoice_tab = false\n                GROUP BY l.product_id\n                ", kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.currency', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_select_companies_rates',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_types', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value='out_invoice', kind=None),
                                    Constant(value='out_refund', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='sqlstr', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='states', ctx=Load()),
                                            Name(id='payment_states', ctx=Load()),
                                            Name(id='invoice_types', ctx=Load()),
                                            Name(id='date_from', ctx=Load()),
                                            Name(id='date_to', ctx=Load()),
                                            Name(id='company_id', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='product_id', ctx=Store()),
                                    Name(id='avg', ctx=Store()),
                                    Name(id='qty', ctx=Store()),
                                    Name(id='total', ctx=Store()),
                                    Name(id='sale', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='sale_avg_price', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='avg', ctx=Load()),
                                                    Name(id='avg', ctx=Load()),
                                                ],
                                            ),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='sale_num_invoiced', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='qty', ctx=Load()),
                                                    Name(id='qty', ctx=Load()),
                                                ],
                                            ),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='turnover', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='total', ctx=Load()),
                                                    Name(id='total', ctx=Load()),
                                                ],
                                            ),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='sale_expected', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='sale', ctx=Load()),
                                                    Name(id='sale', ctx=Load()),
                                                ],
                                            ),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='sales_gap', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='sale_expected', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='turnover', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='total_margin', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Name(id='product_id', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='turnover', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='expected_margin', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Name(id='product_id', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale_expected', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='total_margin_rate', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='res', ctx=Load()),
                                                            slice=Name(id='product_id', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='turnover', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    slice=Name(id='product_id', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='total_margin', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Mult(),
                                                            right=Constant(value=100, kind=None),
                                                        ),
                                                        op=Div(),
                                                        right=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='res', ctx=Load()),
                                                                slice=Name(id='product_id', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='turnover', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='expected_margin_rate', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='res', ctx=Load()),
                                                            slice=Name(id='product_id', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='sale_expected', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    slice=Name(id='product_id', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='expected_margin', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Mult(),
                                                            right=Constant(value=100, kind=None),
                                                        ),
                                                        op=Div(),
                                                        right=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='res', ctx=Load()),
                                                                slice=Name(id='product_id', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='sale_expected', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ctx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='ctx', ctx=Load()),
                                    slice=Constant(value='force_company', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='company_id', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_types', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value='in_invoice', kind=None),
                                    Constant(value='in_refund', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='sqlstr', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='states', ctx=Load()),
                                            Name(id='payment_states', ctx=Load()),
                                            Name(id='invoice_types', ctx=Load()),
                                            Name(id='date_from', ctx=Load()),
                                            Name(id='date_to', ctx=Load()),
                                            Name(id='company_id', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='product_id', ctx=Store()),
                                    Name(id='avg', ctx=Store()),
                                    Name(id='qty', ctx=Store()),
                                    Name(id='total', ctx=Store()),
                                    Name(id='dummy', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='purchase_avg_price', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='avg', ctx=Load()),
                                                    Name(id='avg', ctx=Load()),
                                                ],
                                            ),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='purchase_num_invoiced', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='qty', ctx=Load()),
                                                    Name(id='qty', ctx=Load()),
                                                ],
                                            ),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='total_cost', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='total', ctx=Load()),
                                                    Name(id='total', ctx=Load()),
                                                ],
                                            ),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='total_margin', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Name(id='product_id', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='turnover', kind=None),
                                                Constant(value=0.0, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='total_cost', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Name(id='product_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='total_margin_rate', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='res', ctx=Load()),
                                                                slice=Name(id='product_id', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='turnover', kind=None),
                                                            Constant(value=0.0, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    slice=Name(id='product_id', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='total_margin', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Mult(),
                                                            right=Constant(value=100, kind=None),
                                                        ),
                                                        op=Div(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    slice=Name(id='product_id', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='turnover', kind=None),
                                                                Constant(value=0.0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='product', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='normal_cost', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='standard_price',
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='purchase_num_invoiced', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='purchase_gap', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='normal_cost', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='total_cost', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='expected_margin', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='sale_expected', kind=None),
                                                Constant(value=0.0, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='normal_cost', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='expected_margin_rate', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='res', ctx=Load()),
                                                                slice=Attribute(
                                                                    value=Name(id='product', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='sale_expected', kind=None),
                                                            Constant(value=0.0, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='product', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='expected_margin', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Mult(),
                                                            right=Constant(value=100, kind=None),
                                                        ),
                                                        op=Div(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='product', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='sale_expected', kind=None),
                                                                Constant(value=0.0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
