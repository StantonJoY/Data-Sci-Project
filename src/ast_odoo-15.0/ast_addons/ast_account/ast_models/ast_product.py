Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='format_amount', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='ACCOUNT_DOMAIN', ctx=Store())],
            value=Constant(value="['&', '&', '&', ('deprecated', '=', False), ('internal_type','=','other'), ('company_id', '=', current_company_id), ('is_off_balance', '=', False)]", kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='ProductCategory',
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
                    value=Constant(value='product.category', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_account_income_categ_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.account', kind=None)],
                        keywords=[
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Income Account', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Name(id='ACCOUNT_DOMAIN', ctx=Load()),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This account will be used when validating a customer invoice.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_account_expense_categ_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.account', kind=None)],
                        keywords=[
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Expense Account', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Name(id='ACCOUNT_DOMAIN', ctx=Load()),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The expense is accounted for when a vendor bill is validated, except in anglo-saxon accounting with perpetual inventory valuation in which case the expense (Cost of Goods Sold account) is recognized at the customer invoice validation.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ProductTemplate',
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
                    value=Constant(value='product.template', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='taxes_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.tax', kind=None),
                            Constant(value='product_taxes_rel', kind=None),
                            Constant(value='prod_id', kind=None),
                            Constant(value='tax_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Default taxes used when selling the product.', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Customer Taxes', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='type_tax_use', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value='sale', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='account_sale_tax_id',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tax_string', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_tax_string', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='supplier_taxes_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.tax', kind=None),
                            Constant(value='product_supplier_taxes_rel', kind=None),
                            Constant(value='prod_id', kind=None),
                            Constant(value='tax_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Vendor Taxes', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Default taxes used when buying the product.', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='type_tax_use', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value='purchase', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='account_purchase_tax_id',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_account_income_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.account', kind=None)],
                        keywords=[
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Income Account', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Name(id='ACCOUNT_DOMAIN', ctx=Load()),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Keep this field empty to use the default value from the product category.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_account_expense_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.account', kind=None)],
                        keywords=[
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Expense Account', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Name(id='ACCOUNT_DOMAIN', ctx=Load()),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Keep this field empty to use the default value from the product category. If anglo-saxon accounting with automated valuation method is configured, the expense account on the product category will be used.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='account_tag_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Account Tags', kind=None),
                            ),
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='account.account.tag', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('applicability', '=', 'products')]", kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Tags to be set on the base and tax journal items created for this product.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_product_accounts',
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
                            value=Dict(
                                keys=[
                                    Constant(value='income', kind=None),
                                    Constant(value='expense', kind=None),
                                ],
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='property_account_income_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='categ_id',
                                                    ctx=Load(),
                                                ),
                                                attr='property_account_income_categ_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='property_account_expense_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='categ_id',
                                                    ctx=Load(),
                                                ),
                                                attr='property_account_expense_categ_id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='_get_asset_accounts',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='stock_input', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='stock_output', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
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
                FunctionDef(
                    name='get_product_accounts',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fiscal_pos', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='accounts', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_accounts',
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
                                operand=Name(id='fiscal_pos', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fiscal_pos', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.fiscal.position', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='fiscal_pos', ctx=Load()),
                                    attr='map_accounts',
                                    ctx=Load(),
                                ),
                                args=[Name(id='accounts', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_tax_string',
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
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='currency', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='taxes_id',
                                                ctx=Load(),
                                            ),
                                            attr='compute_all',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='joined', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='included', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='total_included', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='currency', ctx=Load()),
                                            attr='compare_amounts',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='included', ctx=Load()),
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='joined', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='%s Incl. Taxes', kind=None),
                                                            Call(
                                                                func=Name(id='format_amount', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='included', ctx=Load()),
                                                                    Name(id='currency', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='excluded', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='total_excluded', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='currency', ctx=Load()),
                                            attr='compare_amounts',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='excluded', ctx=Load()),
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='joined', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='%s Excl. Taxes', kind=None),
                                                            Call(
                                                                func=Name(id='format_amount', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='excluded', ctx=Load()),
                                                                    Name(id='currency', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='joined', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='tax_string',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=JoinedStr(
                                                values=[
                                                    Constant(value='(= ', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Constant(value=', ', kind=None),
                                                                attr='join',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='joined', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=')', kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='tax_string',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=' ', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='taxes_id', kind=None),
                                Constant(value='list_price', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
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
                FunctionDef(
                    name='_get_product_accounts',
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
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_tmpl_id',
                                        ctx=Load(),
                                    ),
                                    attr='_get_product_accounts',
                                    ctx=Load(),
                                ),
                                args=[],
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
